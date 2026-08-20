/* ==========================================================================
   ROMANTIC LIGHT BLUE AESTHETIC & LIVE LOVE CLOCK ENGINE
   "Happy 1st Anniversary, Kaye" - Interactive Core Script
   Months Timeline: 09/22/25 to 08/22/26 (3 Photos Per Month)
   ========================================================================== */

// --- 1. SPECIAL DATES & CONFIGURATION ---
// August 22, 2025 at 9:43 PM (Month index 7 is August in JS)
const LOVE_START_DATE = new Date(2025, 7, 22, 21, 43, 0);
let loveClockInterval = null;

// Secret Riddle Password ("HAPPY")
const CORRECT_RIDDLE_PASSWORD = "HAPPY"; 

// --- 2. MULTI-TRACK ROMANTIC AUDIO PLAYLIST (AUDIOS FOLDER) ---
const AUDIO_PLAYLIST = [
  { title: "Song 1", src: "audios/1.mp3", fallbackSrc: "audio/1.mp3" },
  { title: "Song 2", src: "audios/2.mp3", fallbackSrc: "audio/2.mp3" },
  { title: "Song 3", src: "audios/3.mp3", fallbackSrc: "audio/3.mp3" },
  { title: "Memories", src: "ssstik.io_@fayy.creates_1787037209737.mp4", fallbackSrc: "" }
];
let currentAudioIndex = 0;
let isAudioPlaying = false;
let webAudioContext = null;

// --- 3. MONTHLY DATA CONFIGURATION (MONTHS 1 TO 12: 09/22/25 -> 08/22/26) ---
// Blank templates ready for user's own photos & personal letters
const MONTHS_DATA = [
  {
    index: 1,
    date: "09/22/25",
    title: "Month 1",
    greeting: "To my dearest Kaye,",
    folderName: "Month_01 (09-22-25)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_01 (09-22-25)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_01 (09-22-25)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_01 (09-22-25)/photo3.jpg"
    ],
    altPaths: [
      "images/month1_1.jpg",
      "images/month1_2.jpg",
      "images/month1_3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 2,
    date: "10/22/25",
    title: "Month 2",
    greeting: "To my dearest Kaye,",
    folderName: "Month_02 (10-22-25)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_02 (10-22-25)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_02 (10-22-25)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_02 (10-22-25)/photo3.jpg"
    ],
    altPaths: [
      "images/month2_1.jpg",
      "images/month2_2.jpg",
      "images/month2_3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 3,
    date: "11/22/25",
    title: "Month 3",
    greeting: "To my dearest Kaye,",
    folderName: "Month_03 (11-22-25)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_03 (11-22-25)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_03 (11-22-25)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_03 (11-22-25)/photo3.jpg"
    ],
    altPaths: [
      "images/month3_1.jpg",
      "images/month3_2.jpg",
      "images/month3_3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 4,
    date: "12/22/25",
    title: "Month 4",
    greeting: "To my dearest Kaye,",
    folderName: "Month_04 (12-22-25)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_04 (12-22-25)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_04 (12-22-25)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_04 (12-22-25)/photo3.jpg"
    ],
    altPaths: [
      "images/month4_1.jpg",
      "images/month4_2.jpg",
      "images/month4_3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 5,
    date: "01/22/26",
    title: "Month 5",
    greeting: "To my dearest Kaye,",
    folderName: "Month_05 (01-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_05 (01-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_05 (01-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_05 (01-22-26)/photo3.jpg"
    ],
    altPaths: [
      "images/month5_1.jpg",
      "images/month5_2.jpg",
      "images/month5_3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 6,
    date: "02/22/26",
    title: "Month 6",
    greeting: "To my dearest Kaye,",
    folderName: "Month_06 (02-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_06 (02-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_06 (02-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_06 (02-22-26)/photo3.jpg"
    ],
    altPaths: [
      "images/month6_1.jpg",
      "images/month6_2.jpg",
      "images/month6_3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 7,
    date: "03/22/26",
    title: "Month 7",
    greeting: "To my dearest Kaye,",
    folderName: "Month_07 (03-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_07 (03-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_07 (03-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_07 (03-22-26)/photo3.jpg"
    ],
    altPaths: [
      "images/month7_1.jpg",
      "images/month7_2.jpg",
      "images/month7_3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 8,
    date: "04/22/26",
    title: "Month 8",
    greeting: "To my dearest Kaye,",
    folderName: "Month_08 (04-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_08 (04-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_08 (04-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_08 (04-22-26)/photo3.jpg"
    ],
    altPaths: [
      "images/month8_1.jpg",
      "images/month8_2.jpg",
      "images/month8_3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 9,
    date: "05/22/26",
    title: "Month 9",
    greeting: "To my dearest Kaye,",
    folderName: "Month_09 (05-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_09 (05-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_09 (05-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_09 (05-22-26)/photo3.jpg"
    ],
    altPaths: [
      "images/month9_1.jpg",
      "images/month9_2.jpg",
      "images/month9_3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 10,
    date: "06/22/26",
    title: "Month 10",
    greeting: "To my dearest Kaye,",
    folderName: "Month_10 (06-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_10 (06-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_10 (06-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_10 (06-22-26)/photo3.jpg"
    ],
    altPaths: [
      "images/month10_1.jpg",
      "images/month10_2.jpg",
      "images/month10_3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 11,
    date: "07/22/26",
    title: "Month 11",
    greeting: "To my dearest Kaye,",
    folderName: "Month_11 (07-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_11 (07-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_11 (07-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_11 (07-22-26)/photo3.jpg"
    ],
    altPaths: [
      "images/month11_1.jpg",
      "images/month11_2.jpg",
      "images/month11_3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 12,
    date: "08/22/26",
    title: "Month 12",
    folderName: "Month_12 (08-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_12 (08-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_12 (08-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_12 (08-22-26)/photo3.jpg"
    ],
    altPaths: [
      "images/month12_1.jpg",
      "images/month12_2.jpg",
      "images/month12_3.jpg"
    ],
    captions: ["", "", ""],
    isSpecial12th: true
  }
];

// --- 4. 28 UNIQUE FLOATING PHOTOS (NO DUPLICATES) ---
const UNIQUE_FLOATING_PHOTOS = [
  "01decfb3-4137-48b1-8bdf-1a774fa715cd (1).jpg",
  "03993175-edf1-471c-b492-de98f400c0f8.jpg",
  "044c3867-7e89-4247-afec-65b09395d6bf.jpg",
  "11a946c0-367d-4b46-a346-3d171f6ed365.jpg",
  "1f919dd8-2419-40cc-bedc-c1d7d8117b99.jpg",
  "2b6f6570-da3d-4d46-84e7-6892cf740e03.jpg",
  "2da7eb6e-8797-43b8-9750-5618e15b015a (1).jpg",
  "3af7b64d-cf20-4bfa-8ce9-8f4a0a7daaba.jpg",
  "3b3a4b3a-1ba7-4f46-aee3-99b295c55f6b.jpg",
  "4fed4cfb-3c90-46c6-919c-79bbb93b149f.jpg",
  "645ebf7e-ffef-4c4c-9046-69966ec19b6c.jpg",
  "6b87fefd-e87f-44ec-9ef0-a335970a3815.jpg",
  "6cea3c4d-6dad-4107-8378-03da50e40069.jpg",
  "72d0d26d-7acc-48d6-a1d3-5e4f79a3327d.jpg",
  "753b6859-fadc-41a2-af90-96dbcf3b6920.jpg",
  "77603abf-da95-4ee6-8f16-2773be99c4b7.jpg",
  "7a536360-69c4-4b43-aa24-1bdf3602b680.jpg",
  "824bbce4-11f0-4a7d-8413-f0557dd331ff.jpg",
  "9185ef90-d177-4603-9bb3-57ac5f21e81c.jpg",
  "97c171d3-82f1-4d74-974a-22caa18b594f.jpg",
  "98e424b6-46df-462a-a975-482385e2c22a.jpg",
  "bad8d70e-f9b1-4464-856a-3a2e1db9a49b.jpg",
  "cb06954d-e7fb-41fa-88a1-b89833c0868d.jpg",
  "cf272746-db6b-455e-bc90-9ea070d8b7dd.jpg",
  "d14fcdc3-4335-4df9-ac03-d69e946c4499.jpg",
  "d75a2c7e-7533-4e6f-98f7-e53376264c5b (1).jpg",
  "ecdf8be8-2d9f-4c49-945a-b5fb7aa6ede3.jpg",
  "f031cce5-7671-418a-9976-a90750d2a66e.jpg"
];

const MOVING_PHOTOS_DATA = UNIQUE_FLOATING_PHOTOS.map((filename, i) => ({
  src: `PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/${filename}`,
  fallbackSrc: `images/photo${i+1}.jpg`,
  caption: `Memory ${i+1}`,
  note: ""
}));

// --- 5. SLIDESHOW IMAGES (TEMPLATES READY FOR USER) ---
const LAST_SLIDESHOW_IMAGES = [
  { src: "PHOTOS_ORGANIZED/04_FINALE_SLIDESHOW (LAST)/photo1.jpg", fallbackSrc: "LAST/photo1.jpg", caption: "" },
  { src: "PHOTOS_ORGANIZED/04_FINALE_SLIDESHOW (LAST)/photo2.jpg", fallbackSrc: "LAST/photo2.jpg", caption: "" },
  { src: "PHOTOS_ORGANIZED/04_FINALE_SLIDESHOW (LAST)/photo3.jpg", fallbackSrc: "LAST/photo3.jpg", caption: "" },
  { src: "PHOTOS_ORGANIZED/04_FINALE_SLIDESHOW (LAST)/photo4.jpg", fallbackSrc: "LAST/photo4.jpg", caption: "" },
  { src: "PHOTOS_ORGANIZED/04_FINALE_SLIDESHOW (LAST)/photo5.jpg", fallbackSrc: "LAST/photo5.jpg", caption: "" }
];

// --- 6. STATE VARIABLES ---
let currentChannelId = "channel-pin";
let pinAttempts = 0;
const CORRECT_PIN = "082225";
let pinSuccessScreenReady = false;

// Riddle Channel State
let riddleAttempts = 0;
let isClueAnimationRunning = false;

let currentMonthIndex = 1;
let slideshowTimer = null;
let currentSlideIndex = 0;

// 2-Click & Moving Photos State
let activeMovingPhotos = [];
let movingAnimationRequestId = null;
let currentlyFocusedPhoto = null;

// --- 7. DOM ELEMENTS ---
const pinCard = document.getElementById("pin-card");
const pinInputs = document.querySelectorAll(".pin-digit");
const pinFeedback = document.getElementById("pin-feedback");
const btnSubmitPin = document.getElementById("btn-submit-pin");
const pinEntryView = document.getElementById("pin-entry-view");
const pinSuccessBox = document.getElementById("pin-success-box");
const anniversaryAnnouncement = document.getElementById("anniversary-announcement");
const channelPin = document.getElementById("channel-pin");

// Riddle Channel Elements
const passwordRiddleCard = document.getElementById("password-riddle-card");
const passwordTextInput = document.getElementById("password-text-input");
const btnSubmitPassword = document.getElementById("btn-submit-password");
const riddleFeedbackText = document.getElementById("riddle-feedback-text");
const btnClueTrigger = document.getElementById("btn-clue-trigger");
const seqOops = document.getElementById("seq-oops");
const seqTeka = document.getElementById("seq-teka");
const riddleMainTitle = document.getElementById("riddle-main-title");

const audioController = document.getElementById("audio-controller");
const audioLabelText = document.getElementById("audio-label-text");
const bgAudio = document.getElementById("bg-audio");
const floatingPhotoLayer = document.getElementById("floating-photo-layer");
const photoFocusOverlay = document.getElementById("photo-focus-overlay");
const photoModalBackdrop = document.getElementById("photo-modal-backdrop");
const photoModalImg = document.getElementById("photo-modal-img");
const photoModalCaption = document.getElementById("photo-modal-caption");
const photoModalNote = document.getElementById("photo-modal-note");

// --- 8. INITIALIZATION ---
document.addEventListener("DOMContentLoaded", () => {
  setupRomanticClickEffects();
  initOverflowingMovingPhotosEngine();
  setupParticles();
  setupPinInputEvents();
  setupRiddleChannelEvents();
  setupAudioController();
  initLoveClock();
});

// --- 9. LIVE LOVE CLOCK ENGINE (COUNTING SINCE 08/22/25 9:43 PM) ---
function initLoveClock() {
  updateLoveClock();
  if (loveClockInterval) clearInterval(loveClockInterval);
  loveClockInterval = setInterval(updateLoveClock, 1000);
}

function updateLoveClock() {
  const daysEl = document.getElementById("clock-days");
  const hoursEl = document.getElementById("clock-hours");
  const minEl = document.getElementById("clock-minutes");
  const secEl = document.getElementById("clock-seconds");

  if (!daysEl || !hoursEl || !minEl || !secEl) return;

  const now = new Date();
  const diffMs = now - LOVE_START_DATE;

  if (diffMs < 0) {
    daysEl.textContent = "0";
    hoursEl.textContent = "00";
    minEl.textContent = "00";
    secEl.textContent = "00";
    return;
  }

  const totalSeconds = Math.floor(diffMs / 1000);
  const days = Math.floor(totalSeconds / (3600 * 24));
  const hours = Math.floor((totalSeconds % (3600 * 24)) / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;

  daysEl.textContent = days.toLocaleString();
  hoursEl.textContent = String(hours).padStart(2, '0');
  minEl.textContent = String(minutes).padStart(2, '0');
  secEl.textContent = String(seconds).padStart(2, '0');
}

// Utility: Fisher-Yates Shuffle
function shuffleArray(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// --- 10. RANDOMIZED FLOATING PHOTOS (GENTLE REBOUND - NO DASH OUT) ---
function initOverflowingMovingPhotosEngine() {
  if (!floatingPhotoLayer) return;
  floatingPhotoLayer.innerHTML = "";
  activeMovingPhotos = [];
  currentlyFocusedPhoto = null;

  const isMobile = window.innerWidth < 768;
  const photoCount = isMobile ? 14 : 20;

  // Randomize the 28 unique photos every time
  const shuffledPhotos = shuffleArray(MOVING_PHOTOS_DATA);
  const photosToUse = shuffledPhotos.slice(0, Math.min(photoCount, shuffledPhotos.length));

  const screenW = window.innerWidth;
  const screenH = window.innerHeight;

  photosToUse.forEach((item, index) => {
    const el = document.createElement("div");
    
    const depth = index % 3;
    const depthClass = depth === 0 ? "depth-back" : depth === 1 ? "depth-mid" : "depth-front";
    el.className = `floating-polaroid ${depthClass}`;

    let baseWidth;
    if (isMobile) {
      baseWidth = depth === 0 ? 76 : depth === 1 ? 90 : 104;
    } else {
      baseWidth = depth === 0 ? 100 : depth === 1 ? 122 : 144;
    }
    el.style.width = `${baseWidth}px`;

    el.innerHTML = `
      <div class="polaroid-img-wrapper">
        <img src="${item.src}" alt="${item.caption || 'Memory'}"
             onerror="this.onerror=null; this.src='${item.fallbackSrc || ''}'; this.onerror=function(){this.parentElement.innerHTML='<div class=\\'placeholder-content\\' style=\\'padding:4px;\\'><span class=\\'placeholder-icon\\' style=\\'font-size:16px;\\'>📷</span><span class=\\'placeholder-text\\' style=\\'font-size:8px;\\'>Photo</span></div>';};">
      </div>
      <div class="polaroid-caption">${item.caption || `Photo`}</div>
      <div class="click-again-badge">Tap again to open</div>
    `;

    const startX = Math.max(16, Math.min(screenW - baseWidth - 16, Math.random() * (screenW - baseWidth)));
    const startY = Math.max(16, Math.min(screenH - baseWidth * 1.25 - 16, Math.random() * (screenH - baseWidth * 1.25)));

    const photoObj = {
      el,
      item,
      x: startX,
      y: startY,
      vx: (Math.random() - 0.5) * (isMobile ? 0.35 : 0.45),
      vy: (Math.random() - 0.5) * (isMobile ? 0.35 : 0.45),
      rot: (Math.random() - 0.5) * 16,
      rotSpeed: (Math.random() - 0.5) * 0.04,
      width: baseWidth,
      height: baseWidth * 1.25,
      isHovered: false,
      isBig: false
    };

    // Ensure non-zero velocity
    if (Math.abs(photoObj.vx) < 0.15) photoObj.vx = photoObj.vx < 0 ? -0.22 : 0.22;
    if (Math.abs(photoObj.vy) < 0.15) photoObj.vy = photoObj.vy < 0 ? -0.22 : 0.22;

    el.addEventListener("pointerdown", (e) => {
      e.stopPropagation();
    });

    el.addEventListener("click", (e) => {
      e.stopPropagation();
      handlePhotoClick(photoObj);
    });

    el.addEventListener("mouseenter", () => {
      if (!photoObj.isBig) photoObj.isHovered = true;
    });
    el.addEventListener("mouseleave", () => {
      if (!photoObj.isBig) photoObj.isHovered = false;
    });

    floatingPhotoLayer.appendChild(el);
    activeMovingPhotos.push(photoObj);
  });

  if (movingAnimationRequestId) cancelAnimationFrame(movingAnimationRequestId);
  updateMovingPhotosLoop();
}

function handlePhotoClick(photoObj) {
  if (currentlyFocusedPhoto === photoObj) {
    dismissFocusedPhoto(false);
    openPhotoModal(photoObj.item.src, photoObj.item.caption, photoObj.item.note);
    return;
  }

  if (currentlyFocusedPhoto) {
    dismissFocusedPhoto(false);
  }

  currentlyFocusedPhoto = photoObj;
  photoObj.isBig = true;
  photoObj.isHovered = true;

  if (floatingPhotoLayer) {
    floatingPhotoLayer.classList.add("has-focused");
  }

  const screenW = window.innerWidth;
  const screenH = window.innerHeight;
  const maxW = Math.min(screenW * 0.84, 300);
  const zoomScale = Math.max(1.8, maxW / photoObj.width);

  const targetX = (screenW - photoObj.width) / 2;
  const targetY = (screenH - photoObj.height) / 2;

  photoObj.el.classList.add("focused-big");
  photoObj.el.style.transform = `translate3d(${targetX}px, ${targetY}px, 0) scale(${zoomScale}) rotate(0deg)`;

  if (photoFocusOverlay) {
    photoFocusOverlay.classList.add("active");
  }
}

function dismissFocusedPhoto(resumeHover = true) {
  if (currentlyFocusedPhoto) {
    const p = currentlyFocusedPhoto;
    p.el.classList.remove("focused-big");
    p.isBig = false;
    if (!resumeHover) p.isHovered = false;

    p.el.style.transform = `translate3d(${p.x}px, ${p.y}px, 0) rotate(${p.rot}deg)`;
    currentlyFocusedPhoto = null;
  }
  if (floatingPhotoLayer) {
    floatingPhotoLayer.classList.remove("has-focused");
  }
  if (photoFocusOverlay) {
    photoFocusOverlay.classList.remove("active");
  }
}

if (photoFocusOverlay) {
  photoFocusOverlay.addEventListener("click", (e) => {
    e.stopPropagation();
    dismissFocusedPhoto();
  });
}

// Gentle continuous drift & soft viewport rebound
function updateMovingPhotosLoop() {
  const screenW = window.innerWidth;
  const screenH = window.innerHeight;
  const pad = 12;

  activeMovingPhotos.forEach(p => {
    if (!p.isHovered && !p.isBig) {
      p.x += p.vx;
      p.y += p.vy;
      p.rot += p.rotSpeed;

      // Soft rebound from screen boundaries (Zero jumping / zero sudden dash)
      if (p.x <= pad) {
        p.x = pad;
        p.vx = Math.abs(p.vx);
      } else if (p.x >= screenW - p.width - pad) {
        p.x = screenW - p.width - pad;
        p.vx = -Math.abs(p.vx);
      }

      if (p.y <= pad) {
        p.y = pad;
        p.vy = Math.abs(p.vy);
      } else if (p.y >= screenH - p.height - pad) {
        p.y = screenH - p.height - pad;
        p.vy = -Math.abs(p.vy);
      }

      p.el.style.transform = `translate3d(${p.x}px, ${p.y}px, 0) rotate(${p.rot}deg)`;
    }
  });

  movingAnimationRequestId = requestAnimationFrame(updateMovingPhotosLoop);
}

window.addEventListener("resize", () => {
  if (window.innerWidth < 768 && activeMovingPhotos.length > 16) {
    initOverflowingMovingPhotosEngine();
  } else if (window.innerWidth >= 768 && activeMovingPhotos.length < 18) {
    initOverflowingMovingPhotosEngine();
  }
});

// --- 11. OPENED MEMORY MODAL ---
function openPhotoModal(src, caption, note) {
  if (!photoModalBackdrop) return;
  photoModalImg.src = src;
  photoModalImg.onerror = function() {
    this.onerror = null;
    this.src = 'PHOTOS_ORGANIZED/01_PIN_AND_HERO/pin_photo.jpg';
  };
  photoModalCaption.textContent = caption || "";
  if (photoModalNote) {
    photoModalNote.textContent = note || "";
    photoModalNote.style.display = note ? "block" : "none";
  }
  photoModalBackdrop.classList.add("active");
}

function closePhotoModal() {
  if (photoModalBackdrop) photoModalBackdrop.classList.remove("active");
  dismissFocusedPhoto();
}

// --- 12. ROMANTIC CLICK & TAP EFFECTS ---
function setupRomanticClickEffects() {
  window.addEventListener("pointerdown", (e) => {
    if (!e.target.closest(".photo-modal-card") && !e.target.closest("input")) {
      spawnRomanticBlossom(e.clientX, e.clientY);
    }
  });
}

function spawnRomanticBlossom(x, y) {
  const canvas = document.getElementById("particles-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");

  for (let i = 0; i < 16; i++) {
    const angle = Math.random() * Math.PI * 2;
    const speed = Math.random() * 4.8 + 1.2;
    const vx = Math.cos(angle) * speed;
    const vy = Math.sin(angle) * speed - 1.2;
    const size = Math.random() * 5.5 + 3.5;
    const isHeart = Math.random() > 0.4;
    let alpha = 1;

    function renderSpark() {
      if (alpha <= 0) return;
      ctx.save();
      ctx.translate(x + vx * (1 - alpha) * 26, y + vy * (1 - alpha) * 26);
      
      if (isHeart) {
        ctx.beginPath();
        const h = size * alpha;
        ctx.moveTo(0, h * 0.3);
        ctx.bezierCurveTo(0, 0, -h / 2, 0, -h / 2, h * 0.3);
        ctx.bezierCurveTo(-h / 2, (h + h * 0.3) / 2, 0, h, 0, h * 1.3);
        ctx.bezierCurveTo(0, h, h / 2, (h + h * 0.3) / 2, h / 2, h * 0.3);
        ctx.bezierCurveTo(h / 2, 0, 0, 0, 0, h * 0.3);
        ctx.fillStyle = `rgba(175, 225, 255, ${alpha * 0.95})`;
        ctx.shadowBlur = 12;
        ctx.shadowColor = `rgba(50, 150, 240, ${alpha})`;
        ctx.fill();
      } else {
        ctx.beginPath();
        const r = size * alpha * 0.85;
        for (let j = 0; j < 4; j++) {
          ctx.lineTo(Math.cos((j * Math.PI) / 2) * r, Math.sin((j * Math.PI) / 2) * r);
          ctx.lineTo(Math.cos((j * Math.PI) / 2 + Math.PI / 4) * (r * 0.35), Math.sin((j * Math.PI) / 2 + Math.PI / 4) * (r * 0.35));
        }
        ctx.closePath();
        ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`;
        ctx.shadowBlur = 14;
        ctx.shadowColor = `rgba(130, 205, 255, ${alpha})`;
        ctx.fill();
      }

      ctx.restore();
      alpha -= 0.038;
      requestAnimationFrame(renderSpark);
    }
    renderSpark();
  }
}

// --- 13. CINEMATIC CHANNEL SWITCHING ENGINE (FADE IN & OUT) ---
function switchChannel(targetChannelId, callback) {
  const currentActive = document.querySelector(".channel.active");
  const targetChannel = document.getElementById(targetChannelId);

  if (!targetChannel || currentActive === targetChannel) return;

  dismissFocusedPhoto();

  if (currentActive) {
    currentActive.classList.add("fading-out");

    setTimeout(() => {
      currentActive.classList.remove("active", "fading-out");
      currentActive.style.visibility = "hidden";

      targetChannel.style.visibility = "visible";
      targetChannel.classList.add("active");
      currentChannelId = targetChannelId;
      window.scrollTo({ top: 0, behavior: "smooth" });

      if (typeof callback === "function") callback();
    }, 450);
  } else {
    targetChannel.classList.add("active");
    targetChannel.style.visibility = "visible";
    currentChannelId = targetChannelId;
    window.scrollTo({ top: 0, behavior: "smooth" });

    if (typeof callback === "function") callback();
  }
}

// --- 14. PIN VALIDATION LOGIC ---
function setupPinInputEvents() {
  pinInputs.forEach((input, idx) => {
    input.addEventListener("input", (e) => {
      const val = e.target.value;
      if (val.length === 1 && idx < pinInputs.length - 1) {
        pinInputs[idx + 1].focus();
      }
    });

    input.addEventListener("keydown", (e) => {
      if (e.key === "Backspace" && !e.target.value && idx > 0) {
        pinInputs[idx - 1].focus();
      } else if (e.key === "Enter") {
        validatePin();
      }
    });

    input.addEventListener("focus", (e) => e.target.select());
  });

  if (btnSubmitPin) {
    btnSubmitPin.addEventListener("click", validatePin);
  }

  // Click anywhere on anniversary announcement -> Open Secret Riddle Channel!
  if (channelPin) {
    channelPin.addEventListener("click", (e) => {
      if (pinSuccessScreenReady && !e.target.closest(".pin-digit") && !e.target.closest("button")) {
        switchChannel("channel-password", () => {
          startRiddleSequence();
        });
      }
    });
  }
}

function validatePin() {
  let enteredPin = "";
  pinInputs.forEach(input => enteredPin += input.value.trim());

  if (enteredPin === CORRECT_PIN) {
    handlePinSuccess();
  } else {
    handlePinFailure();
  }
}

function handlePinFailure() {
  pinAttempts++;
  pinCard.classList.remove("shake");
  void pinCard.offsetWidth;
  pinCard.classList.add("shake");

  let errorMsg = "";
  if (pinAttempts === 1) {
    errorMsg = "Aww You Don't Know? :(";
  } else if (pinAttempts === 2) {
    errorMsg = "You don't remember that day? :(";
  } else {
    errorMsg = "That day you answered me :(";
  }

  pinFeedback.textContent = errorMsg;
  pinInputs.forEach(input => input.value = "");
  if (pinInputs[0]) pinInputs[0].focus();
}

function handlePinSuccess() {
  pinFeedback.textContent = "";
  pinEntryView.style.display = "none";
  pinSuccessBox.style.display = "flex";

  createGrandConfetti();

  setTimeout(() => {
    pinSuccessBox.style.opacity = "0";
    pinSuccessBox.style.filter = "blur(8px)";
    pinSuccessBox.style.transition = "opacity 0.7s ease, filter 0.7s ease";

    setTimeout(() => {
      pinSuccessBox.style.display = "none";
      anniversaryAnnouncement.style.display = "flex";
      anniversaryAnnouncement.style.opacity = "1";
      pinSuccessScreenReady = true;
    }, 700);
  }, 3000);
}

// --- 15. RIDDLE / PASSWORD CHANNEL LOGIC (PASSWORD: "HAPPY") ---
function setupRiddleChannelEvents() {
  if (btnSubmitPassword) {
    btnSubmitPassword.addEventListener("click", validateRiddlePassword);
  }

  if (passwordTextInput) {
    passwordTextInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        validateRiddlePassword();
      }
    });
  }

  if (btnClueTrigger) {
    btnClueTrigger.addEventListener("click", handleClueTriggerClick);
  }
}

function startRiddleSequence() {
  if (passwordTextInput) {
    passwordTextInput.value = "";
    setTimeout(() => passwordTextInput.focus(), 500);
  }

  // Smooth entrance sequence: "OOPS!" -> "Teka may isa pa" -> "Ano muna password?"
  if (seqOops) {
    seqOops.style.opacity = "0";
    seqOops.style.transform = "translateY(-10px)";
  }
  if (seqTeka) {
    seqTeka.style.opacity = "0";
    seqTeka.style.transform = "translateY(-10px)";
  }
  if (riddleMainTitle) {
    riddleMainTitle.style.opacity = "0";
    riddleMainTitle.style.transform = "translateY(-10px)";
  }

  setTimeout(() => {
    if (seqOops) {
      seqOops.style.opacity = "1";
      seqOops.style.transform = "translateY(0)";
    }
  }, 200);

  setTimeout(() => {
    if (seqTeka) {
      seqTeka.style.opacity = "1";
      seqTeka.style.transform = "translateY(0)";
    }
  }, 1000);

  setTimeout(() => {
    if (riddleMainTitle) {
      riddleMainTitle.style.opacity = "1";
      riddleMainTitle.style.transform = "translateY(0)";
    }
  }, 1800);
}

function validateRiddlePassword() {
  if (!passwordTextInput) return;
  const rawInput = passwordTextInput.value.trim().toUpperCase();
  if (!rawInput) return;

  // Clean out any extra punctuation/spaces (e.g. "HAPPY!", "happy", " HAPPY ")
  const cleaned = rawInput.replace(/[^A-Z]/g, "");

  if (cleaned === CORRECT_RIDDLE_PASSWORD || rawInput === CORRECT_RIDDLE_PASSWORD) {
    handleRiddleSuccess();
  } else {
    handleRiddleFailure();
  }
}

function handleRiddleSuccess() {
  if (riddleFeedbackText) {
    riddleFeedbackText.style.color = "var(--sky-deep)";
    riddleFeedbackText.textContent = "✨ Yeheeey! You unlocked it na bebb! ✨";
  }
  if (btnClueTrigger) btnClueTrigger.style.display = "none";

  createGrandConfetti();

  setTimeout(() => {
    switchChannel("channel-clock");
  }, 1600);
}

function handleRiddleFailure() {
  riddleAttempts++;
  if (passwordRiddleCard) {
    passwordRiddleCard.classList.remove("shake");
    void passwordRiddleCard.offsetWidth;
    passwordRiddleCard.classList.add("shake");
  }

  if (riddleAttempts === 1) {
    if (riddleFeedbackText) {
      riddleFeedbackText.style.color = "#e54d60";
      riddleFeedbackText.textContent = "Clue Clue?";
    }
    if (btnClueTrigger) {
      btnClueTrigger.style.display = "inline-flex";
    }
  } else if (riddleAttempts === 2) {
    if (btnClueTrigger) btnClueTrigger.style.display = "none";
    if (riddleFeedbackText) {
      riddleFeedbackText.style.color = "#e54d60";
      riddleFeedbackText.textContent = "letters ngani";
    }
  } else {
    if (btnClueTrigger) btnClueTrigger.style.display = "none";
    if (riddleFeedbackText) {
      riddleFeedbackText.style.color = "#e54d60";
      riddleFeedbackText.textContent = "observe all the letters that I gave you";
    }
  }
}

function handleClueTriggerClick() {
  if (isClueAnimationRunning) return;
  isClueAnimationRunning = true;

  if (btnClueTrigger) btnClueTrigger.style.display = "none";

  // Step 1: "kiss mo muna ako 😙"
  if (riddleFeedbackText) {
    riddleFeedbackText.style.color = "var(--sky-deep)";
    riddleFeedbackText.textContent = "kiss mo muna ako 😙";
  }

  // Step 2: "JOKE LAANG wag ka umaliss"
  setTimeout(() => {
    if (riddleFeedbackText) {
      riddleFeedbackText.textContent = "JOKE LAANG wag ka umaliss";
    }
  }, 1800);

  // Step 3: "eto na"
  setTimeout(() => {
    if (riddleFeedbackText) {
      riddleFeedbackText.textContent = "eto na...";
    }
  }, 3400);

  // Step 4: "Letters"
  setTimeout(() => {
    if (riddleFeedbackText) {
      riddleFeedbackText.style.color = "var(--sky-deep)";
      riddleFeedbackText.textContent = "💡 Letters";
    }
    isClueAnimationRunning = false;
  }, 5000);
}

// --- 16. MONTHLY LETTER CHANNELS (SMOOTH PAGE TRANSITIONS) ---
function openMonthLetter(monthIndex) {
  currentMonthIndex = monthIndex;
  const month = MONTHS_DATA.find(m => m.index === monthIndex);
  if (!month) return;

  const letterCard = document.querySelector(".letter-paper-card");
  const letterDateStamp = document.getElementById("letter-date-stamp");
  const letterMonthCount = document.getElementById("letter-month-count");
  const letterGreeting = document.getElementById("letter-greeting");
  const letterParagraphs = document.getElementById("letter-paragraphs");
  const letterPhotosGallery = document.getElementById("letter-photos-gallery");
  const btnPrev = document.getElementById("btn-prev-month");
  const btnNext = document.getElementById("btn-next-month");

  function renderMonthContent() {
    if (letterDateStamp) letterDateStamp.textContent = `📅 ${month.date}`;
    if (letterMonthCount) letterMonthCount.textContent = `Month ${month.index} of 12`;
    if (letterGreeting) letterGreeting.textContent = month.greeting || "To my dearest Kaye,";
    if (letterParagraphs) letterParagraphs.textContent = month.letter || "";

    if (btnPrev) {
      if (monthIndex === 1) {
        btnPrev.textContent = "← Live Clock";
      } else {
        btnPrev.textContent = `← Month ${monthIndex - 1}`;
      }
    }

    if (btnNext) {
      if (monthIndex < 11) {
        btnNext.textContent = `Next: Month ${monthIndex + 1} →`;
      } else {
        btnNext.textContent = `Next: 1st Year Finale ✨ →`;
      }
    }

    // Render 3 Interactive Polaroid Photos for this Month
    if (letterPhotosGallery) {
      letterPhotosGallery.innerHTML = "";

      month.images.forEach((imgSrc, idx) => {
        const cap = (month.captions && month.captions[idx]) ? month.captions[idx] : `Photo ${idx + 1}`;
        const itemEl = document.createElement("div");
        itemEl.className = "trio-polaroid-item";
        
        const altPath = (month.altPaths && month.altPaths[idx]) ? month.altPaths[idx] : `images/month${month.index}_${idx + 1}.jpg`;
        const fallbackOldPath = `images/month${month.index}_${idx + 1}.jpg`;
        const fallbackSinglePath = `images/month${month.index}.jpg`;

        itemEl.innerHTML = `
          <div class="trio-img-container">
            <img src="${imgSrc}" alt="${cap}"
                 onerror="this.onerror=null; this.src='${altPath}'; this.onerror=function(){this.src='${fallbackOldPath}'; this.onerror=function(){this.src='${fallbackSinglePath}'; this.onerror=function(){this.parentElement.innerHTML='<div class=\\'placeholder-content\\'><span class=\\'placeholder-icon\\'>📷</span><span class=\\'placeholder-text\\'>Photo ${idx+1}</span><span class=\\'placeholder-sub\\'>photo${idx+1}.jpg</span></div>';};};};">
          </div>
          <div class="trio-caption">${cap}</div>
        `;

        itemEl.addEventListener("click", () => {
          openPhotoModal(imgSrc, cap, "");
        });

        letterPhotosGallery.appendChild(itemEl);
      });
    }
  }

  // If already on letter channel, apply smooth content flip
  if (currentChannelId === "channel-letter" && letterCard) {
    letterCard.classList.add("page-transitioning");
    setTimeout(() => {
      renderMonthContent();
      letterCard.classList.remove("page-transitioning");
    }, 220);
  } else {
    renderMonthContent();
    switchChannel("channel-letter");
  }
}

function navigateNextMonth() {
  if (currentMonthIndex < 11) {
    openMonthLetter(currentMonthIndex + 1);
  } else {
    showIntermissionCategory();
  }
}

function navigatePrevMonth() {
  if (currentMonthIndex > 1) {
    openMonthLetter(currentMonthIndex - 1);
  } else {
    switchChannel("channel-clock");
  }
}

// --- 17. INTERMISSION (12TH MONTH - 08/22/26) ---
function showIntermissionCategory() {
  const intermissionGallery = document.getElementById("intermission-photos-gallery");
  const month12 = MONTHS_DATA.find(m => m.index === 12);

  if (intermissionGallery && month12) {
    intermissionGallery.innerHTML = "";
    month12.images.forEach((imgSrc, idx) => {
      const cap = (month12.captions && month12.captions[idx]) ? month12.captions[idx] : `Photo ${idx + 1}`;
      const itemEl = document.createElement("div");
      itemEl.className = "trio-polaroid-item";
      
      const fallbackOldPath = `images/month12_${idx + 1}.jpg`;
      const fallbackSinglePath = `images/month12.jpg`;

      itemEl.innerHTML = `
        <div class="trio-img-container">
          <img src="${imgSrc}" alt="${cap}"
               onerror="this.onerror=null; this.src='${fallbackOldPath}'; this.onerror=function(){this.src='${fallbackSinglePath}'; this.onerror=function(){this.parentElement.innerHTML='<div class=\\'placeholder-content\\'><span class=\\'placeholder-icon\\'>🎁</span><span class=\\'placeholder-text\\'>Photo ${idx+1}</span><span class=\\'placeholder-sub\\'>photo${idx+1}.jpg</span></div>';};};">
        </div>
        <div class="trio-caption">${cap}</div>
      `;

      itemEl.addEventListener("click", (e) => {
        e.stopPropagation();
        openPhotoModal(imgSrc, cap, "");
      });

      intermissionGallery.appendChild(itemEl);
    });
  }

  switchChannel("channel-intermission");
}

const channelIntermission = document.getElementById("channel-intermission");
if (channelIntermission) {
  channelIntermission.addEventListener("click", () => {
    startGrandFinale();
  });
}

// --- 18. GRAND FINALE (SLIDESHOW & LAST TEXT) ---
function startGrandFinale() {
  switchChannel("channel-finale", () => {
    startAudioPlayback();
    initFinaleSlideshow();
  });
}

function initFinaleSlideshow() {
  const slideshowViewport = document.getElementById("slideshow-viewport");
  const slideshowCaption = document.getElementById("slideshow-caption");
  const lastTextBox = document.getElementById("last-text-box");
  const slideshowWrapper = document.querySelector(".slideshow-wrapper");

  if (!slideshowViewport) return;
  slideshowViewport.innerHTML = "";

  LAST_SLIDESHOW_IMAGES.forEach((item, index) => {
    const img = document.createElement("img");
    img.src = item.src;
    img.className = `slideshow-image ${index === 0 ? 'active-slide' : ''}`;
    img.alt = `Slideshow photo ${index + 1}`;

    img.onerror = () => {
      img.onerror = null;
      if (item.fallbackSrc) {
        img.src = item.fallbackSrc;
      } else {
        img.style.display = "none";
        const ph = document.createElement("div");
        ph.className = `placeholder-content slideshow-image ${index === 0 ? 'active-slide' : ''}`;
        ph.innerHTML = `<span class="placeholder-icon">✨</span><span class="placeholder-text">Photo ${index + 1}</span><span class="placeholder-sub">photo${index + 1}.jpg</span>`;
        slideshowViewport.appendChild(ph);
      }
    };

    slideshowViewport.appendChild(img);
  });

  if (slideshowCaption) {
    slideshowCaption.textContent = LAST_SLIDESHOW_IMAGES[0].caption || "";
  }

  let cycles = 0;
  clearInterval(slideshowTimer);
  currentSlideIndex = 0;

  slideshowTimer = setInterval(() => {
    const slides = slideshowViewport.querySelectorAll(".slideshow-image");
    if (slides.length === 0) return;

    slides[currentSlideIndex].classList.remove("active-slide");
    currentSlideIndex = (currentSlideIndex + 1) % slides.length;
    slides[currentSlideIndex].classList.add("active-slide");

    if (slideshowCaption && LAST_SLIDESHOW_IMAGES[currentSlideIndex]) {
      slideshowCaption.textContent = LAST_SLIDESHOW_IMAGES[currentSlideIndex].caption || "";
    }

    cycles++;
    if (cycles >= LAST_SLIDESHOW_IMAGES.length && lastTextBox && !lastTextBox.classList.contains("visible")) {
      revealLastText();
    }
  }, 3600);

  setTimeout(() => {
    if (lastTextBox && !lastTextBox.classList.contains("visible")) {
      revealLastText();
    }
  }, 4200);
}

function revealLastText() {
  const lastTextBox = document.getElementById("last-text-box");
  const finaleHint = document.getElementById("finale-click-hint");
  const slideshowWrapper = document.querySelector(".slideshow-wrapper");

  if (slideshowWrapper) {
    slideshowWrapper.style.transform = "translateY(-12px)";
    slideshowWrapper.style.opacity = "0.9";
  }

  if (lastTextBox) {
    lastTextBox.classList.add("visible");
    spawnRomanticBlossom(window.innerWidth / 2, window.innerHeight * 0.55);
  }

  if (finaleHint) {
    setTimeout(() => {
      finaleHint.style.display = "inline-flex";
      finaleHint.style.opacity = "1";
    }, 1200);
  }

  const channelFinale = document.getElementById("channel-finale");
  if (channelFinale) {
    channelFinale.onclick = (e) => {
      if (e.target.closest("button") || e.target.closest(".audio-controller")) return;
      switchChannel("channel-closing");
    };
  }
}

// --- 19. AUDIO CONTROLLER & MULTI-TRACK PLAYLIST (MP3 ONLY) ---
function setupAudioController() {
  if (!audioController || !bgAudio) return;

  // Set initial volume & source
  bgAudio.volume = 1.0;
  if (!bgAudio.src || !bgAudio.src.includes(AUDIO_PLAYLIST[currentAudioIndex].src)) {
    bgAudio.src = AUDIO_PLAYLIST[currentAudioIndex].src;
  }

  // When a track ends, automatically advance to the next MP3
  bgAudio.addEventListener("ended", () => {
    playNextAudioTrack();
  });

  // Track play state changes
  bgAudio.addEventListener("play", () => {
    isAudioPlaying = true;
    audioController.classList.add("playing");
    if (audioLabelText) audioLabelText.textContent = `${AUDIO_PLAYLIST[currentAudioIndex].title} 🎵`;
  });

  bgAudio.addEventListener("pause", () => {
    isAudioPlaying = false;
    audioController.classList.remove("playing");
    if (audioLabelText) audioLabelText.textContent = "Music";
  });

  audioController.addEventListener("click", () => {
    if (isAudioPlaying) {
      pauseAudio();
    } else {
      startAudioPlayback();
    }
  });

  // 1. Immediate Autoplay Attempt on page load
  startAudioPlayback();

  // 2. Global Autoplay Trigger: On first gesture, immediately start MP3 playback
  const triggerMp3Autoplay = () => {
    if (bgAudio && bgAudio.paused) {
      startAudioPlayback();
    }
  };

  ["pointerdown", "click", "touchstart", "keydown", "focusin", "scroll"].forEach(evt => {
    window.addEventListener(evt, triggerMp3Autoplay, { passive: true });
    document.addEventListener(evt, triggerMp3Autoplay, { passive: true });
  });
}

function startAudioPlayback() {
  if (!bgAudio) return;

  const track = AUDIO_PLAYLIST[currentAudioIndex];
  if (!bgAudio.src || !bgAudio.src.includes(encodeURI(track.src))) {
    bgAudio.src = track.src;
  }

  const playPromise = bgAudio.play();
  if (playPromise !== undefined) {
    playPromise.then(() => {
      isAudioPlaying = true;
      if (audioController) audioController.classList.add("playing");
      if (audioLabelText) audioLabelText.textContent = `${track.title} 🎵`;
    }).catch(err => {
      // Browser blocked zero-interaction autoplay; waiting for first tap/click
      console.log("Audio waiting for first gesture:", err);
    });
  }
}

function playNextAudioTrack() {
  if (!bgAudio) return;
  currentAudioIndex = (currentAudioIndex + 1) % AUDIO_PLAYLIST.length;
  const nextTrack = AUDIO_PLAYLIST[currentAudioIndex];
  bgAudio.src = nextTrack.src;
  bgAudio.play().then(() => {
    isAudioPlaying = true;
    if (audioController) audioController.classList.add("playing");
    if (audioLabelText) audioLabelText.textContent = `${nextTrack.title} 🎵`;
  }).catch(err => {
    console.log("Error advancing track:", err);
  });
}

function pauseAudio() {
  if (bgAudio) bgAudio.pause();
  isAudioPlaying = false;
  if (audioController) audioController.classList.remove("playing");
  if (audioLabelText) audioLabelText.textContent = "Music";
}

// --- 20. PARTICLES & CONFETTI (ROMANTIC ETHEREAL PARTICLES) ---
function setupParticles() {
  const canvas = document.getElementById("particles-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");

  let width = (canvas.width = window.innerWidth);
  let height = (canvas.height = window.innerHeight);

  window.addEventListener("resize", () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  const particles = [];
  const count = window.innerWidth < 768 ? 24 : 38;

  for (let i = 0; i < count; i++) {
    particles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      size: Math.random() * 12 + 6,
      speedX: (Math.random() - 0.5) * 0.35,
      speedY: -(Math.random() * 0.45 + 0.22),
      swaySpeed: Math.random() * 0.02 + 0.01,
      swayOffset: Math.random() * Math.PI * 2,
      opacity: Math.random() * 0.5 + 0.32,
      type: Math.random() > 0.42 ? "heart" : "sparkle"
    });
  }

  function drawHeart(cx, cy, size, opacity) {
    ctx.save();
    ctx.translate(cx, cy);
    ctx.beginPath();
    const topCurveHeight = size * 0.3;
    ctx.moveTo(0, topCurveHeight);
    ctx.bezierCurveTo(0, 0, -size / 2, 0, -size / 2, topCurveHeight);
    ctx.bezierCurveTo(-size / 2, (size + topCurveHeight) / 2, 0, size, 0, size * 1.3);
    ctx.bezierCurveTo(0, size, size / 2, (size + topCurveHeight) / 2, size / 2, topCurveHeight);
    ctx.bezierCurveTo(size / 2, 0, 0, 0, 0, topCurveHeight);
    ctx.closePath();
    ctx.fillStyle = `rgba(165, 218, 255, ${opacity})`;
    ctx.shadowBlur = 14;
    ctx.shadowColor = `rgba(55, 155, 245, ${opacity * 0.95})`;
    ctx.fill();
    ctx.restore();
  }

  function drawSparkle(cx, cy, size, opacity) {
    ctx.save();
    ctx.translate(cx, cy);
    ctx.beginPath();
    for (let i = 0; i < 4; i++) {
      ctx.lineTo(Math.cos((i * Math.PI) / 2) * size, Math.sin((i * Math.PI) / 2) * size);
      ctx.lineTo(
        Math.cos((i * Math.PI) / 2 + Math.PI / 4) * (size * 0.35),
        Math.sin((i * Math.PI) / 2 + Math.PI / 4) * (size * 0.35)
      );
    }
    ctx.closePath();
    ctx.fillStyle = `rgba(255, 255, 255, ${opacity})`;
    ctx.shadowBlur = 12;
    ctx.shadowColor = `rgba(145, 215, 255, 0.9)`;
    ctx.fill();
    ctx.restore();
  }

  let frameTick = 0;
  function animateParticles() {
    ctx.clearRect(0, 0, width, height);
    frameTick++;

    particles.forEach(p => {
      p.x += p.speedX + Math.sin(frameTick * p.swaySpeed + p.swayOffset) * 0.35;
      p.y += p.speedY;

      if (p.y < -30) {
        p.y = height + 20;
        p.x = Math.random() * width;
      }
      if (p.x < -30) p.x = width + 20;
      if (p.x > width + 30) p.x = -20;

      if (p.type === "heart") {
        drawHeart(p.x, p.y, p.size, p.opacity);
      } else {
        drawSparkle(p.x, p.y, p.size * 0.85, p.opacity);
      }
    });

    requestAnimationFrame(animateParticles);
  }

  animateParticles();
}

function createGrandConfetti() {
  const canvas = document.getElementById("particles-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const centerX = window.innerWidth / 2;
  const centerY = window.innerHeight / 2;

  for (let i = 0; i < 60; i++) {
    const angle = Math.random() * Math.PI * 2;
    const speed = Math.random() * 7.5 + 2.5;
    const vx = Math.cos(angle) * speed;
    const vy = Math.sin(angle) * speed;
    let life = 1;

    function renderParticle() {
      if (life <= 0) return;
      ctx.save();
      ctx.beginPath();
      ctx.arc(centerX + vx * (1 - life) * 48, centerY + vy * (1 - life) * 48, 4.5 * life, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(140, 210, 255, ${life})`;
      ctx.shadowBlur = 15;
      ctx.shadowColor = "rgba(55, 155, 245, 0.9)";
      ctx.fill();
      ctx.restore();
      life -= 0.028;
      requestAnimationFrame(renderParticle);
    }
    renderParticle();
  }
}

// Reset Story with smooth transition
function restartStory() {
  pinAttempts = 0;
  riddleAttempts = 0;
  pinSuccessScreenReady = false;
  dismissFocusedPhoto();
  if (pinSuccessBox) pinSuccessBox.style.display = "none";
  if (anniversaryAnnouncement) anniversaryAnnouncement.style.display = "none";
  if (pinEntryView) pinEntryView.style.display = "block";
  pinInputs.forEach(input => input.value = "");
  if (passwordTextInput) passwordTextInput.value = "";
  if (riddleFeedbackText) riddleFeedbackText.textContent = "";
  if (btnClueTrigger) btnClueTrigger.style.display = "none";
  switchChannel("channel-pin");
}
