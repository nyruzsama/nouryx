# 🏫 Campus Photo Drop & SSG Memory Vault

A modern, responsive school photo collection website built for events, yearbooks, intramurals, and campus memories.

---

## 👥 How the Two Roles Work

### 1. **"STUDENTS" (Normal Visitors)**
- Open the website link on their phone or laptop.
- Drag and drop or tap to select photos (from their phone camera roll or computer).
- Enter their **Name**, **Grade & Section**, **Event Category**, and an optional **Memory Caption**.
- See live previews of selected photos before submitting.
- Hit **"Send Photos to SSG Vault"** with real-time upload progress.
- Receive a digital confirmation receipt.
- **🔒 Privacy Protected**: Normal visitors **CANNOT** view or download photos submitted by others.

### 2. **"SSG" (Exclusive Visitors / Supreme Student Government / Owner)**
- Click on the **"SSG Portal"** tab.
- Protected by a secure **Master PIN** (Default: `2026`).
- Once unlocked, SSG officers have access to:
  - **Master Photo Gallery**: Browse all submitted student photos.
  - **High-Res Lightbox**: Click any photo to view full-screen with student details and date.
  - **📦 One-Click "Download All as ZIP"**: Downloads all photos in a neatly organized `.zip` file with a text manifest index!
  - **Individual Photo Downloads**: Direct download of any specific picture.
  - **Search & Filter**: Search by student name, section, or filter by event category.
  - **Photo Moderation**: Delete unwanted or duplicate submissions.
  - **Dashboard Metrics**: Total photos, total contributors, storage usage.
  - **Change PIN**: Change the SSG PIN directly from the dashboard.

---

## 🚀 Quick Start (Running Locally)

### 1. Start the Server
Open your terminal in this directory (`c:\Psychoogy\WEBSITES\SCHOOL`) and run:

```bash
npm start
```

### 2. Open on your PC (Owner)
Open your browser and go to:
```
http://localhost:3000
```

### 3. Share with Students on Campus / Same WiFi / Mobile Hotspot
When you run `npm start`, the server automatically displays your local network address:
```
📱 Students & WiFi Link:  http://192.168.X.X:3000
```
- Any student connected to the **same school WiFi or your phone's personal hotspot** can simply type that address into their mobile browser and start dropping photos immediately! No installation required!

---

## 🌐 Free Online Deployment (Share with Anyone on the Internet)

If you want students to be able to upload from anywhere using their own mobile data (4G/5G):

### Option A: Deploy on Render.com (Recommended & Free)
1. Push this project to GitHub (or upload the folder).
2. Go to [render.com](https://render.com) and click **New Web Service**.
3. Connect your repository.
4. Set:
   - **Runtime**: `Node`
   - **Build Command**: `npm install`
   - **Start Command**: `node server.js`
5. Render will give you a public URL like `https://school-photo-vault.onrender.com`. Share that link with everyone!

### Option B: Quick Temporary Public Link (Using Localtunnel or Ngrok)
To instantly generate a public link without deploying:
```bash
npx localtunnel --port 3000
```
This will give you a live HTTPS link to send to students right away!

---

## 🔑 Default SSG Credentials

- **Default SSG PIN**: `2026`
- You can change the PIN inside the SSG Portal anytime by clicking **"Change PIN"**, or by editing the `.env` file (`SSG_PIN=your_pin`).

---

## 📁 File Structure

```
├── server.js            # Express backend & ZIP streaming engine
├── package.json         # Node.js dependencies
├── .env                 # Port & PIN settings
├── data/
│   ├── config.json      # SSG configuration & PIN
│   └── photos.json      # Metadata database (student name, category, etc.)
├── uploads/             # High-resolution stored image files
└── public/
    ├── index.html       # Responsive UI (Students Dropzone + SSG Portal)
    ├── app.js           # Client logic, PIN auth, drag-drop, gallery
    └── style.css        # Styles, animations & effects
```
