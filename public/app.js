// State Management
let channelsList = [];
let activeChannel = null;
let activeChannelPhotos = [];
let currentPhotoIndex = 0;
let ssgToken = localStorage.getItem('ssg_session_token') || null;
let modalSelectedFiles = [];

// DOM Ready
document.addEventListener('DOMContentLoaded', async () => {
  fetchNetworkInfo();
  await loadChannels();
  
  if (ssgToken) {
    verifySsgToken();
  }

  // Check URL hash or default to Channel Guide
  if (window.location.hash.startsWith('#ch=')) {
    const chName = decodeURIComponent(window.location.hash.replace('#ch=', ''));
    tuneChannel(chName);
  } else {
    showChannelGuide();
  }
});

// -------------------------------------------------------------
// NETWORK INFO
// -------------------------------------------------------------
async function fetchNetworkInfo() {
  try {
    const res = await fetch('/api/info');
    if (res.ok) {
      const data = await res.json();
      if (data.ipAddresses && data.ipAddresses.length > 0) {
        const ip = data.ipAddresses[0].address;
        const infoEl = document.getElementById('headerConnectionInfo');
        if (infoEl) {
          infoEl.innerHTML = `<i class="fa-solid fa-wifi text-emerald-300"></i> WiFi: http://${ip}:${data.port}`;
          infoEl.title = `Students on the same WiFi can open: http://${ip}:${data.port}`;
        }
      }
    }
  } catch (e) {
    console.warn('Network info unavailable:', e);
  }
}

// -------------------------------------------------------------
// CHANNELS LOADING & GUIDE VIEW
// -------------------------------------------------------------
async function loadChannels() {
  try {
    const res = await fetch('/api/channels');
    if (res.ok) {
      const data = await res.json();
      channelsList = data.channels || [];
      renderChannelsGrid();
      populateUploadChannelDropdown();
    }
  } catch (e) {
    console.error('Failed to load channels:', e);
  }
}

function renderChannelsGrid() {
  const container = document.getElementById('channelsGridContainer');
  if (!container) return;

  container.innerHTML = '';

  channelsList.forEach((ch, index) => {
    const card = document.createElement('div');
    card.className = 'channel-guide-card p-4 flex flex-col justify-between cursor-pointer group';
    card.onclick = () => tuneChannel(ch.name);

    // Channel preview image or fallback retro TV static icon
    let previewHtml = '';
    if (ch.coverPhotoId) {
      previewHtml = `
        <div class="relative aspect-video rounded-xl overflow-hidden bg-slate-950 border border-slate-700 mb-3 shadow-inner">
          <img src="/api/photos/view/${ch.coverPhotoId}" alt="${escapeHtml(ch.name)}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" />
          <span class="absolute top-2 left-2 px-2 py-0.5 rounded bg-black/75 text-emerald-400 font-vt323 text-lg border border-emerald-500/50">
            CH ${ch.channelNumber}
          </span>
        </div>
      `;
    } else {
      previewHtml = `
        <div class="relative aspect-video rounded-xl overflow-hidden bg-gradient-to-br from-slate-900 to-slate-800 border border-slate-700 mb-3 flex flex-col items-center justify-center text-slate-500">
          <i class="fa-solid fa-tv text-3xl mb-1 group-hover:text-cyan-400 transition-colors"></i>
          <span class="font-pixel text-[10px] text-slate-400">Ready for Broadcast</span>
          <span class="absolute top-2 left-2 px-2 py-0.5 rounded bg-black/75 text-emerald-400 font-vt323 text-lg border border-emerald-500/50">
            CH ${ch.channelNumber}
          </span>
        </div>
      `;
    }

    card.innerHTML = `
      <div>
        ${previewHtml}
        <div class="flex items-start justify-between gap-1">
          <h3 class="font-pixel text-sm font-bold text-slate-950 group-hover:text-blue-700 transition-colors leading-snug">
            ${escapeHtml(ch.name)}
          </h3>
        </div>
        <p class="text-xs text-slate-600 mt-1">
          ${ch.photoCount} photo broadcast${ch.photoCount === 1 ? '' : 's'}
        </p>
      </div>

      <div class="mt-4 pt-3 border-t border-slate-200 flex items-center justify-between">
        <span class="text-[11px] font-bold text-blue-600 group-hover:underline flex items-center gap-1 font-pixel">
          📺 TUNE IN NOW <i class="fa-solid fa-arrow-right text-[10px]"></i>
        </span>
        <button
          type="button"
          onclick="event.stopPropagation(); openUploadModalForChannel('${escapeHtml(ch.name)}')"
          class="win98-btn text-[10px] py-0.5 px-2 bg-emerald-100 hover:bg-emerald-200"
        >
          + Drop Photo
        </button>
      </div>
    `;

    container.appendChild(card);
  });
}

function populateUploadChannelDropdown() {
  const select = document.getElementById('uploadChannelSelect');
  if (!select) return;

  const currentVal = select.value;
  select.innerHTML = '';

  channelsList.forEach(ch => {
    const opt = document.createElement('option');
    opt.value = ch.name;
    opt.textContent = `CH ${ch.channelNumber}: ${ch.name}`;
    select.appendChild(opt);
  });

  const newOpt = document.createElement('option');
  newOpt.value = '__NEW__';
  newOpt.textContent = '+ Create New Channel...';
  select.appendChild(newOpt);

  if (currentVal && currentVal !== '__NEW__') {
    select.value = currentVal;
  }
}

// -------------------------------------------------------------
// NAVIGATION: CHANNEL GUIDE vs TV PLAYER
// -------------------------------------------------------------
function showChannelGuide() {
  document.getElementById('channelGuideView').classList.remove('hidden');
  document.getElementById('tvPlayerView').classList.add('hidden');
  window.location.hash = '';

  const navGuide = document.getElementById('navBtnGuide');
  const navTv = document.getElementById('navBtnTv');
  if (navGuide) navGuide.className = 'win98-btn flex items-center gap-1.5 bg-[#cbd5e1] font-bold';
  if (navTv) navTv.className = 'win98-btn flex items-center gap-1.5';
}

function showTvPlayer() {
  if (!activeChannel && channelsList.length > 0) {
    tuneChannel(channelsList[0].name);
    return;
  }
  document.getElementById('channelGuideView').classList.add('hidden');
  document.getElementById('tvPlayerView').classList.remove('hidden');

  const navGuide = document.getElementById('navBtnGuide');
  const navTv = document.getElementById('navBtnTv');
  if (navGuide) navGuide.className = 'win98-btn flex items-center gap-1.5';
  if (navTv) navTv.className = 'win98-btn flex items-center gap-1.5 bg-[#cbd5e1] font-bold';
}

// THE USER REQUESTED: "whenever I want to Back, I can just Back."
function backToChannels() {
  showChannelGuide();
}

// -------------------------------------------------------------
// TV CHANNEL PLAYBACK & SURFING
// -------------------------------------------------------------
async function tuneChannel(channelName) {
  activeChannel = channelName;
  window.location.hash = `ch=${encodeURIComponent(channelName)}`;

  // Switch to TV View
  showTvPlayer();

  const chObj = channelsList.find(c => c.name.toLowerCase() === channelName.toLowerCase());
  const chNumber = chObj ? chObj.channelNumber : '01';

  // Update OSD and remote indicators
  document.getElementById('tvOsdDisplay').textContent = `CH ${chNumber} [AV-1]`;
  document.getElementById('remoteChIndicator').textContent = `CH ${chNumber}`;
  document.getElementById('navActiveChannelLabel').textContent = `Live (CH ${chNumber})`;

  // Update Pixel banner (if channel includes words like Birthday / Intramurals)
  const bannerEl = document.getElementById('tvBannerTitle');
  if (channelName.toLowerCase().includes('birthday') || channelName.toLowerCase().includes('day')) {
    bannerEl.textContent = 'BIRTHDAY !!';
  } else {
    bannerEl.textContent = channelName.toUpperCase().slice(0, 16);
  }

  // Fetch photos for this channel
  await loadChannelPhotos(channelName);
}

async function loadChannelPhotos(channelName) {
  try {
    const res = await fetch(`/api/channels/${encodeURIComponent(channelName)}/photos`);
    if (res.ok) {
      const data = await res.json();
      activeChannelPhotos = data.photos || [];
      currentPhotoIndex = 0;
      renderCurrentBroadcastPhoto();
    }
  } catch (e) {
    console.error('Failed to fetch channel photos:', e);
  }
}

function renderCurrentBroadcastPhoto() {
  const tvImage = document.getElementById('tvMainImage');
  const noPhotosState = document.getElementById('tvNoPhotosState');
  const sysMessageDate = document.getElementById('sysMessageDate');
  const sysMessageStudent = document.getElementById('sysMessageStudent');
  const photoIndexEl = document.getElementById('remotePhotoIndex');
  const chObj = channelsList.find(c => c.name.toLowerCase() === (activeChannel || '').toLowerCase());
  const chNumber = chObj ? chObj.channelNumber : '01';

  if (activeChannelPhotos.length === 0) {
    // No photos on this channel yet
    tvImage.classList.add('hidden');
    noPhotosState.classList.remove('hidden');
    document.getElementById('tvEmptyChNum').textContent = chNumber;

    sysMessageDate.textContent = `${activeChannel}`;
    sysMessageStudent.textContent = 'Awaiting student photo submissions!';
    photoIndexEl.textContent = '0 / 0';
    return;
  }

  // Active photo display
  noPhotosState.classList.add('hidden');
  tvImage.classList.remove('hidden');

  const photo = activeChannelPhotos[currentPhotoIndex];
  tvImage.src = `/api/photos/view/${photo.id}`;

  // Update Windows 98 System Message dialog box
  sysMessageDate.textContent = photo.caption ? photo.caption : `${photo.channel}`;
  sysMessageStudent.textContent = `By: ${photo.studentName} (${photo.gradeSection || 'Student'})`;

  // Update photo index counter
  photoIndexEl.textContent = `${currentPhotoIndex + 1} / ${activeChannelPhotos.length}`;
}

// Channel Up / Down
function nextChannel() {
  if (channelsList.length === 0) return;
  const currentIndex = channelsList.findIndex(c => c.name === activeChannel);
  const nextIdx = (currentIndex + 1) % channelsList.length;
  tuneChannel(channelsList[nextIdx].name);
}

function prevChannel() {
  if (channelsList.length === 0) return;
  const currentIndex = channelsList.findIndex(c => c.name === activeChannel);
  const prevIdx = (currentIndex - 1 + channelsList.length) % channelsList.length;
  tuneChannel(channelsList[prevIdx].name);
}

// Photo Next / Prev on current channel
function nextPhoto() {
  if (activeChannelPhotos.length === 0) return;
  currentPhotoIndex = (currentPhotoIndex + 1) % activeChannelPhotos.length;
  renderCurrentBroadcastPhoto();
}

function prevPhoto() {
  if (activeChannelPhotos.length === 0) return;
  currentPhotoIndex = (currentPhotoIndex - 1 + activeChannelPhotos.length) % activeChannelPhotos.length;
  renderCurrentBroadcastPhoto();
}

function handleSysMessageOk() {
  if (activeChannelPhotos.length > 0) {
    const p = activeChannelPhotos[currentPhotoIndex];
    alert(`📺 Broadcast Info:\nStudent: ${p.studentName}\nSection: ${p.gradeSection}\nDate: ${new Date(p.uploadedAt).toLocaleString()}\nCaption: ${p.caption || 'No caption'}\n\n🔒 Note: Photo saving is restricted to SSG officers with PIN.`);
  } else {
    openUploadModal();
  }
}

// -------------------------------------------------------------
// UPLOAD MODAL & SUBMISSION (STUDENTS)
// -------------------------------------------------------------
function openUploadModal() {
  modalSelectedFiles = [];
  renderModalPreviews();
  populateUploadChannelDropdown();

  if (activeChannel) {
    document.getElementById('uploadChannelSelect').value = activeChannel;
    document.getElementById('uploadCustomChannelInput').classList.add('hidden');
  }

  document.getElementById('uploadModal').classList.remove('hidden');
}

function openUploadModalForChannel(channelName) {
  openUploadModal();
  document.getElementById('uploadChannelSelect').value = channelName;
}

function closeUploadModal() {
  document.getElementById('uploadModal').classList.add('hidden');
  modalSelectedFiles = [];
}

function handleChannelSelectChange(select) {
  const customInput = document.getElementById('uploadCustomChannelInput');
  if (select.value === '__NEW__') {
    customInput.classList.remove('hidden');
    customInput.focus();
  } else {
    customInput.classList.add('hidden');
  }
}

function handleModalFilesSelected(event) {
  const files = Array.from(event.target.files);
  const imageFiles = files.filter(f => f.type.startsWith('image/') || /\.(jpe?g|png|webp|gif|heic|bmp)$/i.test(f.name));

  if (imageFiles.length === 0) {
    alert('Please select valid image files (JPG, PNG, WEBP, GIF, HEIC).');
    return;
  }

  const combined = [...modalSelectedFiles, ...imageFiles];
  if (combined.length > 20) {
    alert('Maximum 20 photos allowed per broadcast. Taking first 20.');
    modalSelectedFiles = combined.slice(0, 20);
  } else {
    modalSelectedFiles = combined;
  }

  renderModalPreviews();
}

function renderModalPreviews() {
  const container = document.getElementById('modalPreviewContainer');
  const grid = document.getElementById('modalPreviewGrid');
  const countEl = document.getElementById('modalPreviewCount');

  if (modalSelectedFiles.length === 0) {
    container.classList.add('hidden');
    countEl.textContent = '0';
    return;
  }

  countEl.textContent = modalSelectedFiles.length;
  container.classList.remove('hidden');
  grid.innerHTML = '';

  modalSelectedFiles.forEach((file, idx) => {
    const thumb = document.createElement('div');
    thumb.className = 'relative aspect-square bg-slate-900 border border-slate-600 rounded overflow-hidden';

    const img = document.createElement('img');
    img.src = URL.createObjectURL(file);
    img.className = 'w-full h-full object-cover';

    const removeBtn = document.createElement('button');
    removeBtn.type = 'button';
    removeBtn.className = 'absolute top-0.5 right-0.5 bg-rose-600 text-white w-4 h-4 rounded text-[9px] flex items-center justify-center';
    removeBtn.textContent = '✕';
    removeBtn.onclick = (e) => {
      e.stopPropagation();
      modalSelectedFiles.splice(idx, 1);
      renderModalPreviews();
    };

    thumb.appendChild(img);
    thumb.appendChild(removeBtn);
    grid.appendChild(thumb);
  });
}

async function handleChannelUpload(event) {
  event.preventDefault();

  if (modalSelectedFiles.length === 0) {
    alert('Please select at least one photo to broadcast!');
    return;
  }

  const select = document.getElementById('uploadChannelSelect');
  const customInput = document.getElementById('uploadCustomChannelInput');
  let targetChannel = select.value;

  if (targetChannel === '__NEW__') {
    targetChannel = customInput.value.trim();
    if (!targetChannel) {
      alert('Please enter a name for the new channel!');
      return;
    }
  }

  const studentName = document.getElementById('uploadStudentName').value.trim();
  const gradeSection = document.getElementById('uploadGradeSection').value.trim();
  const caption = document.getElementById('uploadCaption').value.trim();

  const formData = new FormData();
  formData.append('studentName', studentName);
  formData.append('gradeSection', gradeSection);
  formData.append('channel', targetChannel);
  formData.append('category', targetChannel);
  formData.append('caption', caption);

  modalSelectedFiles.forEach(f => {
    formData.append('photos', f);
  });

  const progress = document.getElementById('modalUploadProgress');
  const progressBar = document.getElementById('modalUploadProgressBar');
  const percentText = document.getElementById('modalUploadPercent');
  const submitBtn = document.getElementById('modalSubmitBtn');

  progress.classList.remove('hidden');
  submitBtn.disabled = true;

  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/api/upload', true);

  xhr.upload.onprogress = (e) => {
    if (e.lengthComputable) {
      const p = Math.round((e.loaded / e.total) * 100);
      progressBar.style.width = p + '%';
      percentText.textContent = p + '%';
    }
  };

  xhr.onload = async () => {
    submitBtn.disabled = false;
    progress.classList.add('hidden');
    progressBar.style.width = '0%';

    if (xhr.status >= 200 && xhr.status < 300) {
      alert(`🎉 Photos successfully broadcasted to ${targetChannel}!`);
      closeUploadModal();
      
      // Reload channels and tune directly to this channel
      await loadChannels();
      tuneChannel(targetChannel);
    } else {
      try {
        const err = JSON.parse(xhr.responseText);
        alert('Upload failed: ' + (err.error || 'Server error'));
      } catch (e) {
        alert('Upload failed.');
      }
    }
  };

  xhr.onerror = () => {
    submitBtn.disabled = false;
    progress.classList.add('hidden');
    alert('Network error while broadcasting photo.');
  };

  xhr.send(formData);
}

// -------------------------------------------------------------
// SSG PORTAL & MASTER CONTROLS
// -------------------------------------------------------------
function openSsgModal() {
  if (ssgToken) {
    showSsgUnlockedModal();
  } else {
    showSsgLockedModal();
  }
  document.getElementById('ssgModal').classList.remove('hidden');
}

function closeSsgModal() {
  document.getElementById('ssgModal').classList.add('hidden');
}

function showSsgLockedModal() {
  document.getElementById('ssgModalLocked').classList.remove('hidden');
  document.getElementById('ssgModalUnlocked').classList.add('hidden');
  document.getElementById('ssgLockIcon').className = 'fa-solid fa-key text-amber-700';
  document.getElementById('remoteBtnZipChannel').classList.add('hidden');
}

function showSsgUnlockedModal() {
  document.getElementById('ssgModalLocked').classList.add('hidden');
  document.getElementById('ssgModalUnlocked').classList.remove('hidden');
  document.getElementById('ssgLockIcon').className = 'fa-solid fa-lock-open text-emerald-600';
  document.getElementById('remoteBtnZipChannel').classList.remove('hidden');
}

async function verifySsgToken() {
  try {
    const res = await fetch('/api/ssg/verify', {
      headers: { 'Authorization': `Bearer ${ssgToken}` }
    });
    if (res.ok) {
      document.getElementById('ssgLockIcon').className = 'fa-solid fa-lock-open text-emerald-600';
      document.getElementById('remoteBtnZipChannel').classList.remove('hidden');
    } else {
      ssgToken = null;
      localStorage.removeItem('ssg_session_token');
    }
  } catch (e) {
    // Network error
  }
}

async function handleSsgModalPinSubmit(event) {
  event.preventDefault();
  const pinInput = document.getElementById('ssgModalPinInput');
  const errorEl = document.getElementById('ssgModalError');
  const pin = pinInput.value.trim();

  if (!pin) return;
  errorEl.classList.add('hidden');

  try {
    const res = await fetch('/api/ssg/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ pin })
    });

    const data = await res.json();
    if (res.ok && data.success) {
      ssgToken = data.token;
      localStorage.setItem('ssg_session_token', ssgToken);
      pinInput.value = '';
      showSsgUnlockedModal();
    } else {
      errorEl.textContent = data.error || 'Incorrect SSG PIN.';
      errorEl.classList.remove('hidden');
    }
  } catch (e) {
    alert('Connection error. Please try again.');
  }
}

function lockSsgVaultModal() {
  ssgToken = null;
  localStorage.removeItem('ssg_session_token');
  showSsgLockedModal();
}

function downloadCurrentChannelZip() {
  if (!activeChannel) return;
  if (!ssgToken) {
    openSsgModal();
    return;
  }
  const url = `/api/ssg/channels/${encodeURIComponent(activeChannel)}/download-zip?token=${encodeURIComponent(ssgToken)}`;
  window.location.href = url;
}

function downloadAllChannelsZip() {
  if (!ssgToken) {
    openSsgModal();
    return;
  }
  const url = `/api/ssg/download-all?token=${encodeURIComponent(ssgToken)}`;
  window.location.href = url;
}

async function deleteActivePhoto() {
  if (activeChannelPhotos.length === 0) return;
  const photo = activeChannelPhotos[currentPhotoIndex];
  if (!confirm(`Delete photo from ${photo.studentName}?`)) return;

  try {
    const res = await fetch(`/api/ssg/photos/${photo.id}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${ssgToken}` }
    });

    if (res.ok) {
      alert('Photo removed from broadcast.');
      await loadChannels();
      await loadChannelPhotos(activeChannel);
    } else {
      const d = await res.json();
      alert('Delete failed: ' + (d.error || 'Unknown error'));
    }
  } catch (e) {
    alert('Error deleting photo.');
  }
}

// Helper: Escape HTML
function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
