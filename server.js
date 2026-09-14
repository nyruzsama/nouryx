const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const archiver = require('archiver');
const cors = require('cors');
const os = require('os');
const crypto = require('crypto');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Directories
const UPLOADS_DIR = path.join(__dirname, 'uploads');
const DATA_DIR = path.join(__dirname, 'data');
const PHOTOS_FILE = path.join(DATA_DIR, 'photos.json');
const CONFIG_FILE = path.join(DATA_DIR, 'config.json');

// Ensure directories exist
if (!fs.existsSync(UPLOADS_DIR)) fs.mkdirSync(UPLOADS_DIR, { recursive: true });
if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR, { recursive: true });

// Load or initialize config
function getConfig() {
  try {
    if (fs.existsSync(CONFIG_FILE)) {
      return JSON.parse(fs.readFileSync(CONFIG_FILE, 'utf8'));
    }
  } catch (e) {
    console.error('Error reading config:', e);
  }
  return {
    ssgPin: process.env.SSG_PIN || '2026',
    schoolName: 'Supreme Student Government (SSG) Photo Vault',
    maxFileSizeMb: parseInt(process.env.MAX_FILE_SIZE_MB || '25', 10)
  };
}

function saveConfig(cfg) {
  fs.writeFileSync(CONFIG_FILE, JSON.stringify(cfg, null, 2), 'utf8');
}

// Load or initialize photos database
function getPhotos() {
  try {
    if (fs.existsSync(PHOTOS_FILE)) {
      return JSON.parse(fs.readFileSync(PHOTOS_FILE, 'utf8'));
    }
  } catch (e) {
    console.error('Error reading photos DB:', e);
  }
  return [];
}

function savePhotos(photos) {
  fs.writeFileSync(PHOTOS_FILE, JSON.stringify(photos, null, 2), 'utf8');
}

// SSG Auth Session Tokens (in-memory with 24h validity)
const activeTokens = new Map();

function generateToken() {
  const token = crypto.randomBytes(32).toString('hex');
  const expiresAt = Date.now() + 24 * 60 * 60 * 1000;
  activeTokens.set(token, { expiresAt });
  return token;
}

function verifySsgAuth(req, res, next) {
  const authHeader = req.headers['authorization'] || '';
  const queryToken = req.query.token;
  const token = authHeader.replace(/^Bearer\s+/i, '') || queryToken;

  if (!token || !activeTokens.has(token)) {
    return res.status(401).json({ error: 'Unauthorized: SSG PIN authentication required.' });
  }

  const session = activeTokens.get(token);
  if (Date.now() > session.expiresAt) {
    activeTokens.delete(token);
    return res.status(401).json({ error: 'SSG session expired. Please re-enter your PIN.' });
  }

  next();
}

// Multer storage setup
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, UPLOADS_DIR);
  },
  filename: function (req, file, cb) {
    const ext = path.extname(file.originalname).toLowerCase();
    const cleanExt = ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.heic', '.bmp'].includes(ext) ? ext : '.jpg';
    const uniqueSuffix = Date.now() + '-' + crypto.randomBytes(6).toString('hex');
    cb(null, 'photo-' + uniqueSuffix + cleanExt);
  }
});

const upload = multer({
  storage: storage,
  limits: {
    fileSize: 25 * 1024 * 1024 // 25 MB per file
  },
  fileFilter: function (req, file, cb) {
    const allowedMime = /^image\/(jpeg|png|webp|gif|heic|bmp)/;
    if (allowedMime.test(file.mimetype) || /\.(jpe?g|png|webp|gif|heic|bmp)$/i.test(file.originalname)) {
      cb(null, true);
    } else {
      cb(new Error('Only image files (JPG, PNG, WEBP, GIF, HEIC) are accepted.'));
    }
  }
});

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Format bytes helper
function formatBytes(bytes, decimals = 2) {
  if (!+bytes) return '0 Bytes';
  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return `${parseFloat((bytes / Math.pow(k, i)).toFixed(dm))} ${sizes[i]}`;
}

// Default Channels list
const DEFAULT_CHANNELS = [
  "June 29 - Kean's Day",
  "June 25 - James's Day",
  "June 12 - Lucky's Day",
  "Sportsfest & Intramurals",
  "Foundation Day",
  "Classroom & Barkada Memories"
];

// -------------------------------------------------------------
// PUBLIC CHANNELS & TV VIEW ENDPOINTS
// -------------------------------------------------------------

// Get network info & school name
app.get('/api/info', (req, res) => {
  const config = getConfig();
  const networkInterfaces = os.networkInterfaces();
  const ipAddresses = [];

  for (const name of Object.keys(networkInterfaces)) {
    for (const net of networkInterfaces[name]) {
      if (net.family === 'IPv4' && !net.internal) {
        ipAddresses.push({ interface: name, address: net.address });
      }
    }
  }

  res.json({
    schoolName: config.schoolName,
    port: PORT,
    ipAddresses: ipAddresses,
    maxFileSizeMb: config.maxFileSizeMb,
    defaultChannels: DEFAULT_CHANNELS
  });
});

// List all channels with photo count and latest photo preview
app.get('/api/channels', (req, res) => {
  const photos = getPhotos();
  const channelMap = new Map();

  // Initialize with default channels
  DEFAULT_CHANNELS.forEach((name, idx) => {
    channelMap.set(name, {
      name,
      channelNumber: (idx + 1).toString().padStart(2, '0'),
      photoCount: 0,
      coverPhotoId: null,
      latestDate: null
    });
  });

  // Populate counts and latest covers from uploads
  photos.forEach(photo => {
    const channelName = photo.channel || photo.category || 'General';
    if (!channelMap.has(channelName)) {
      const chNum = (channelMap.size + 1).toString().padStart(2, '0');
      channelMap.set(channelName, {
        name: channelName,
        channelNumber: chNum,
        photoCount: 0,
        coverPhotoId: null,
        latestDate: null
      });
    }

    const item = channelMap.get(channelName);
    item.photoCount += 1;
    if (!item.coverPhotoId) {
      item.coverPhotoId = photo.id;
      item.latestDate = photo.uploadedAt;
    }
  });

  const channelsList = Array.from(channelMap.values());
  res.json({ channels: channelsList });
});

// Get all photos in a specific channel (for TV playback)
app.get('/api/channels/:channel/photos', (req, res) => {
  const requestedChannel = decodeURIComponent(req.params.channel).trim();
  const photos = getPhotos();

  const filtered = photos
    .filter(p => {
      const ch = (p.channel || p.category || 'General').trim();
      return ch.toLowerCase() === requestedChannel.toLowerCase();
    })
    .sort((a, b) => new Date(b.uploadedAt) - new Date(a.uploadedAt))
    .map(p => ({
      id: p.id,
      studentName: p.studentName,
      gradeSection: p.gradeSection,
      channel: p.channel || p.category,
      caption: p.caption,
      uploadedAt: p.uploadedAt,
      sizeFormatted: p.sizeFormatted,
      originalName: p.originalName
    }));

  res.json({
    channel: requestedChannel,
    count: filtered.length,
    photos: filtered
  });
});

// Public image view for CRT TV display (with no-download headers)
app.get('/api/photos/view/:id', (req, res) => {
  const photos = getPhotos();
  const photo = photos.find(p => p.id === req.params.id);

  if (!photo) {
    return res.status(404).json({ error: 'Photo not found.' });
  }

  const filePath = path.join(UPLOADS_DIR, photo.filename);
  if (!fs.existsSync(filePath)) {
    return res.status(404).json({ error: 'File missing on server.' });
  }

  // Send with inline content disposition
  res.setHeader('Content-Type', photo.mimetype || 'image/jpeg');
  res.setHeader('Content-Disposition', 'inline');
  res.sendFile(filePath);
});

// Students photo upload
app.post('/api/upload', (req, res) => {
  upload.array('photos', 20)(req, res, function (err) {
    if (err instanceof multer.MulterError) {
      if (err.code === 'LIMIT_FILE_SIZE') {
        return res.status(400).json({ error: 'One of the files is too large (max 25MB).' });
      }
      return res.status(400).json({ error: `Upload error: ${err.message}` });
    } else if (err) {
      return res.status(400).json({ error: err.message });
    }

    if (!req.files || req.files.length === 0) {
      return res.status(400).json({ error: 'Please select at least one photo to upload.' });
    }

    const studentName = (req.body.studentName || 'Anonymous Student').trim();
    const gradeSection = (req.body.gradeSection || 'Unspecified').trim();
    const channel = (req.body.channel || req.body.category || 'General Memories').trim();
    const caption = (req.body.caption || '').trim();

    const timestamp = new Date().toISOString();
    const existingPhotos = getPhotos();

    for (const file of req.files) {
      const entry = {
        id: crypto.randomUUID(),
        studentName,
        gradeSection,
        channel,
        category: channel,
        caption,
        originalName: file.originalname,
        filename: file.filename,
        size: file.size,
        sizeFormatted: formatBytes(file.size),
        mimetype: file.mimetype,
        uploadedAt: timestamp
      };
      existingPhotos.push(entry);
    }

    savePhotos(existingPhotos);

    res.json({
      success: true,
      message: `Successfully broadcasted ${req.files.length} photo(s) to ${channel}!`,
      count: req.files.length,
      studentName,
      channel,
      uploadedAt: timestamp
    });
  });
});

// -------------------------------------------------------------
// SSG AUTH & EXCLUSIVE ENDPOINTS
// -------------------------------------------------------------

// SSG PIN Login
app.post('/api/ssg/login', (req, res) => {
  const { pin } = req.body;
  const config = getConfig();

  if (!pin) {
    return res.status(400).json({ error: 'Please enter the SSG PIN.' });
  }

  if (String(pin).trim() !== String(config.ssgPin).trim()) {
    return res.status(401).json({ error: 'Incorrect SSG PIN. Access Denied.' });
  }

  const token = generateToken();
  res.json({
    success: true,
    message: 'Welcome SSG Officer! Access Granted.',
    token,
    schoolName: config.schoolName
  });
});

app.get('/api/ssg/verify', verifySsgAuth, (req, res) => {
  res.json({ success: true, valid: true });
});

// Get SSG stats
app.get('/api/ssg/stats', verifySsgAuth, (req, res) => {
  const photos = getPhotos();
  const totalPhotos = photos.length;
  const totalBytes = photos.reduce((sum, p) => sum + (p.size || 0), 0);

  const contributorsSet = new Set();
  const channelsCount = {};

  photos.forEach(p => {
    if (p.studentName) contributorsSet.add(p.studentName.toLowerCase());
    const ch = p.channel || p.category || 'General';
    channelsCount[ch] = (channelsCount[ch] || 0) + 1;
  });

  res.json({
    totalPhotos,
    totalContributors: contributorsSet.size,
    totalStorageBytes: totalBytes,
    totalStorageFormatted: formatBytes(totalBytes),
    channelsCount
  });
});

// SSG download single photo
app.get('/api/ssg/photos/:id/download', verifySsgAuth, (req, res) => {
  const photos = getPhotos();
  const photo = photos.find(p => p.id === req.params.id);

  if (!photo) {
    return res.status(404).json({ error: 'Photo not found.' });
  }

  const filePath = path.join(UPLOADS_DIR, photo.filename);
  if (!fs.existsSync(filePath)) {
    return res.status(404).json({ error: 'File missing on server.' });
  }

  const cleanChannel = (photo.channel || 'General').replace(/[^a-zA-Z0-9_-]/g, '_');
  const cleanStudent = (photo.studentName || 'Student').replace(/[^a-zA-Z0-9_-]/g, '_');
  const cleanOriginal = photo.originalName.replace(/[^a-zA-Z0-9_.-]/g, '_');
  const downloadName = `[${cleanChannel}]_${cleanStudent}_${cleanOriginal}`;

  res.download(filePath, downloadName);
});

// SSG download entire channel as ZIP
app.get('/api/ssg/channels/:channel/download-zip', verifySsgAuth, (req, res) => {
  const requestedChannel = decodeURIComponent(req.params.channel).trim();
  const photos = getPhotos().filter(p => {
    const ch = (p.channel || p.category || 'General').trim();
    return ch.toLowerCase() === requestedChannel.toLowerCase();
  });

  if (photos.length === 0) {
    return res.status(400).json({ error: 'No photos in this channel to download.' });
  }

  const archive = archiver('zip', { zlib: { level: 6 } });
  const cleanChannelName = requestedChannel.replace(/[^a-zA-Z0-9_-]/g, '_');
  const zipFileName = `SSG_Channel_${cleanChannelName}.zip`;

  res.attachment(zipFileName);
  res.setHeader('Content-Type', 'application/zip');

  archive.on('error', function (err) {
    console.error('Archiver error:', err);
    if (!res.headersSent) res.status(500).json({ error: 'Failed to create channel ZIP.' });
  });

  archive.pipe(res);

  photos.forEach((photo, index) => {
    const filePath = path.join(UPLOADS_DIR, photo.filename);
    if (fs.existsSync(filePath)) {
      const student = (photo.studentName || 'Student').replace(/[^a-zA-Z0-9 _-]/g, '_');
      const ext = path.extname(photo.filename) || '.jpg';
      const cleanOriginal = path.basename(photo.originalName, ext).replace(/[^a-zA-Z0-9 _-]/g, '_');
      archive.file(filePath, { name: `${student}_${index + 1}_${cleanOriginal}${ext}` });
    }
  });

  archive.finalize();
});

// SSG download ALL photos as ZIP
app.get('/api/ssg/download-all', verifySsgAuth, (req, res) => {
  const photos = getPhotos();

  if (photos.length === 0) {
    return res.status(400).json({ error: 'No photos to download yet.' });
  }

  const archive = archiver('zip', { zlib: { level: 6 } });
  const timestamp = new Date().toISOString().slice(0, 10);
  const zipFileName = `SSG_All_Channels_Vault_${timestamp}.zip`;

  res.attachment(zipFileName);
  res.setHeader('Content-Type', 'application/zip');

  archive.on('error', function (err) {
    console.error('Archiver error:', err);
    if (!res.headersSent) res.status(500).json({ error: 'Failed to create ZIP archive.' });
  });

  archive.pipe(res);

  photos.forEach((photo, index) => {
    const filePath = path.join(UPLOADS_DIR, photo.filename);
    if (fs.existsSync(filePath)) {
      const folder = (photo.channel || photo.category || 'General').replace(/[^a-zA-Z0-9 _-]/g, '_');
      const student = (photo.studentName || 'Student').replace(/[^a-zA-Z0-9 _-]/g, '_');
      const ext = path.extname(photo.filename) || '.jpg';
      const cleanOriginal = path.basename(photo.originalName, ext).replace(/[^a-zA-Z0-9 _-]/g, '_');
      const entryName = `${folder}/${student}_${index + 1}_${cleanOriginal}${ext}`;
      archive.file(filePath, { name: entryName });
    }
  });

  // Include index manifest
  let manifestText = `========================================================\n`;
  manifestText += `  SSG PHOTO VAULT - MASTER ARCHIVE (CHANNEL BROADCASTS)\n`;
  manifestText += `  Generated on: ${new Date().toLocaleString()}\n`;
  manifestText += `  Total Photos: ${photos.length}\n`;
  manifestText += `========================================================\n\n`;

  photos.forEach((p, idx) => {
    manifestText += `[${idx + 1}] File: ${p.originalName}\n`;
    manifestText += `    Channel: ${p.channel || p.category || 'General'}\n`;
    manifestText += `    Student: ${p.studentName} (${p.gradeSection || 'N/A'})\n`;
    manifestText += `    Caption: "${p.caption || 'No caption'}"\n`;
    manifestText += `    Uploaded: ${new Date(p.uploadedAt).toLocaleString()}\n`;
    manifestText += `    Size: ${p.sizeFormatted}\n\n`;
  });

  archive.append(manifestText, { name: 'CHANNELS_ARCHIVE_MANIFEST.txt' });
  archive.finalize();
});

// SSG delete photo
app.delete('/api/ssg/photos/:id', verifySsgAuth, (req, res) => {
  const photos = getPhotos();
  const photoIndex = photos.findIndex(p => p.id === req.params.id);

  if (photoIndex === -1) {
    return res.status(404).json({ error: 'Photo not found.' });
  }

  const [deletedPhoto] = photos.splice(photoIndex, 1);
  savePhotos(photos);

  const filePath = path.join(UPLOADS_DIR, deletedPhoto.filename);
  if (fs.existsSync(filePath)) {
    try {
      fs.unlinkSync(filePath);
    } catch (e) {
      console.warn('Could not delete file:', e.message);
    }
  }

  res.json({
    success: true,
    message: `Photo "${deletedPhoto.originalName}" removed successfully.`
  });
});

// SSG change PIN
app.post('/api/ssg/change-pin', verifySsgAuth, (req, res) => {
  const { newPin } = req.body;

  if (!newPin || String(newPin).trim().length < 4) {
    return res.status(400).json({ error: 'PIN must be at least 4 characters long.' });
  }

  const config = getConfig();
  config.ssgPin = String(newPin).trim();
  saveConfig(config);

  res.json({
    success: true,
    message: 'SSG PIN has been successfully updated!'
  });
});

// Start Server
app.listen(PORT, '0.0.0.0', () => {
  const networkInterfaces = os.networkInterfaces();
  console.log(`\n======================================================`);
  console.log(`  📺 Y2K RETRO TV PHOTO DROP & SSG VAULT ONLINE!`);
  console.log(`======================================================`);
  console.log(`  🖥️  Owner (This PC):       http://localhost:${PORT}`);

  for (const name of Object.keys(networkInterfaces)) {
    for (const net of networkInterfaces[name]) {
      if (net.family === 'IPv4' && !net.internal) {
        console.log(`  📱  Students & WiFi Link:  http://${net.address}:${PORT}`);
      }
    }
  }
  console.log(`  🔑  Default SSG PIN:       2026`);
  console.log(`======================================================\n`);
});
