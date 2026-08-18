/* ==========================================================================
   ROMANTIC LIGHT BLUE AESTHETIC & CINEMATIC FADE INTRO/OUTRO ENGINE
   "Happy 1st Anniversary, Kaye" - Interactive Core Script
   Linear 1st to 12th Month Journey (3 Photos Per Month - Blank Text Ready)
   ========================================================================== */

// --- 1. MONTHLY DATA CONFIGURATION (MONTHS 1 TO 12, 3 PHOTOS PER MONTH) ---
// Letters and captions are kept blank so you can insert your own personal messages!
const MONTHS_DATA = [
  {
    index: 1,
    date: "08/22/25",
    title: "Month 1",
    greeting: "To my dearest Kaye,",
    folderName: "Month_01 (08-22-25)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_01 (08-22-25)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_01 (08-22-25)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_01 (08-22-25)/photo3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 2,
    date: "09/22/25",
    title: "Month 2",
    greeting: "To my dearest Kaye,",
    folderName: "Month_02 (09-22-25)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_02 (09-22-25)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_02 (09-22-25)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_02 (09-22-25)/photo3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 3,
    date: "10/22/25",
    title: "Month 3",
    greeting: "To my dearest Kaye,",
    folderName: "Month_03 (10-22-25)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_03 (10-22-25)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_03 (10-22-25)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_03 (10-22-25)/photo3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 4,
    date: "11/22/25",
    title: "Month 4",
    greeting: "To my dearest Kaye,",
    folderName: "Month_04 (11-22-25)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_04 (11-22-25)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_04 (11-22-25)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_04 (11-22-25)/photo3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 5,
    date: "12/22/25",
    title: "Month 5",
    greeting: "To my dearest Kaye,",
    folderName: "Month_05 (12-22-25)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_05 (12-22-25)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_05 (12-22-25)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_05 (12-22-25)/photo3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 6,
    date: "01/22/26",
    title: "Month 6",
    greeting: "To my dearest Kaye,",
    folderName: "Month_06 (01-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_06 (01-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_06 (01-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_06 (01-22-26)/photo3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 7,
    date: "02/22/26",
    title: "Month 7",
    greeting: "To my dearest Kaye,",
    folderName: "Month_07 (02-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_07 (02-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_07 (02-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_07 (02-22-26)/photo3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 8,
    date: "03/22/26",
    title: "Month 8",
    greeting: "To my dearest Kaye,",
    folderName: "Month_08 (03-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_08 (03-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_08 (03-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_08 (03-22-26)/photo3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 9,
    date: "04/22/26",
    title: "Month 9",
    greeting: "To my dearest Kaye,",
    folderName: "Month_09 (04-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_09 (04-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_09 (04-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_09 (04-22-26)/photo3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 10,
    date: "05/22/26",
    title: "Month 10",
    greeting: "To my dearest Kaye,",
    folderName: "Month_10 (05-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_10 (05-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_10 (05-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_10 (05-22-26)/photo3.jpg"
    ],
    captions: ["", "", ""],
    letter: ""
  },
  {
    index: 11,
    date: "06/22/26",
    title: "Month 11",
    greeting: "To my dearest Kaye,",
    folderName: "Month_11 (06-22-26)",
    images: [
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_11 (06-22-26)/photo1.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_11 (06-22-26)/photo2.jpg",
      "PHOTOS_ORGANIZED/02_MONTHS_CATEGORIES/Month_11 (06-22-26)/photo3.jpg"
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
    captions: ["", "", ""],
    isSpecial12th: true
  }
];

// --- 2. EXTENSIVE MOVING PHOTOS DATABASE ---
const MOVING_PHOTOS_DATA = [
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo1.jpg", fallbackSrc: "floating_photos/photo1.jpg", caption: "Photo 1", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo2.jpg", fallbackSrc: "floating_photos/photo2.jpg", caption: "Photo 2", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo3.jpg", fallbackSrc: "floating_photos/photo3.jpg", caption: "Photo 3", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo4.jpg", fallbackSrc: "floating_photos/photo4.jpg", caption: "Photo 4", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo5.jpg", fallbackSrc: "floating_photos/photo5.jpg", caption: "Photo 5", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo6.jpg", fallbackSrc: "floating_photos/photo6.jpg", caption: "Photo 6", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo7.jpg", fallbackSrc: "floating_photos/photo7.jpg", caption: "Photo 7", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo8.jpg", fallbackSrc: "floating_photos/photo8.jpg", caption: "Photo 8", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo9.jpg", fallbackSrc: "floating_photos/photo9.jpg", caption: "Photo 9", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo10.jpg", fallbackSrc: "floating_photos/photo10.jpg", caption: "Photo 10", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo11.jpg", fallbackSrc: "floating_photos/photo11.jpg", caption: "Photo 11", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo12.jpg", fallbackSrc: "floating_photos/photo12.jpg", caption: "Photo 12", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo13.jpg", fallbackSrc: "floating_photos/photo13.jpg", caption: "Photo 13", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo14.jpg", fallbackSrc: "floating_photos/photo14.jpg", caption: "Photo 14", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo15.jpg", fallbackSrc: "floating_photos/photo15.jpg", caption: "Photo 15", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo16.jpg", fallbackSrc: "floating_photos/photo16.jpg", caption: "Photo 16", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo17.jpg", fallbackSrc: "floating_photos/photo17.jpg", caption: "Photo 17", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo18.jpg", fallbackSrc: "floating_photos/photo18.jpg", caption: "Photo 18", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo19.jpg", fallbackSrc: "floating_photos/photo19.jpg", caption: "Photo 19", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo20.jpg", fallbackSrc: "floating_photos/photo20.jpg", caption: "Photo 20", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo21.jpg", fallbackSrc: "floating_photos/photo21.jpg", caption: "Photo 21", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo22.jpg", fallbackSrc: "floating_photos/photo22.jpg", caption: "Photo 22", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo23.jpg", fallbackSrc: "floating_photos/photo23.jpg", caption: "Photo 23", note: "" },
  { src: "PHOTOS_ORGANIZED/03_FLOATING_PHOTOS/photo24.jpg", fallbackSrc: "floating_photos/photo24.jpg", caption: "Photo 24", note: "" }
];

// --- 3. SLIDESHOW IMAGES (From 04_FINALE_SLIDESHOW (LAST)/ or LAST/) ---
const LAST_SLIDESHOW_IMAGES = [
  { src: "PHOTOS_ORGANIZED/04_FINALE_SLIDESHOW (LAST)/photo1.jpg", fallbackSrc: "LAST/photo1.jpg", caption: "" },
  { src: "PHOTOS_ORGANIZED/04_FINALE_SLIDESHOW (LAST)/photo2.jpg", fallbackSrc: "LAST/photo2.jpg", caption: "" },
  { src: "PHOTOS_ORGANIZED/04_FINALE_SLIDESHOW (LAST)/photo3.jpg", fallbackSrc: "LAST/photo3.jpg", caption: "" },
  { src: "PHOTOS_ORGANIZED/04_FINALE_SLIDESHOW (LAST)/photo4.jpg", fallbackSrc: "LAST/photo4.jpg", caption: "" },
  { src: "PHOTOS_ORGANIZED/04_FINALE_SLIDESHOW (LAST)/photo5.jpg", fallbackSrc: "LAST/photo5.jpg", caption: "" }
];

// --- 4. STATE VARIABLES ---
let currentChannelId = "channel-pin";
let pinAttempts = 0;
const CORRECT_PIN = "082225";
let pinSuccessScreenReady = false;
let currentMonthIndex = 1;
let slideshowTimer = null;
let currentSlideIndex = 0;
let isAudioPlaying = false;
let webAudioContext = null;

// 2-Click & Moving Photos State
let activeMovingPhotos = [];
let movingAnimationRequestId = null;
let currentlyFocusedPhoto = null;

// --- 5. DOM ELEMENTS ---
const pinCard = document.getElementById("pin-card");
const pinInputs = document.querySelectorAll(".pin-digit");
const pinFeedback = document.getElementById("pin-feedback");
const btnSubmitPin = document.getElementById("btn-submit-pin");
const pinEntryView = document.getElementById("pin-entry-view");
const pinSuccessBox = document.getElementById("pin-success-box");
const anniversaryAnnouncement = document.getElementById("anniversary-announcement");
const channelPin = document.getElementById("channel-pin");

const audioController = document.getElementById("audio-controller");
const bgAudio = document.getElementById("bg-audio");
const floatingPhotoLayer = document.getElementById("floating-photo-layer");
const photoFocusOverlay = document.getElementById("photo-focus-overlay");
const photoModalBackdrop = document.getElementById("photo-modal-backdrop");
const photoModalImg = document.getElementById("photo-modal-img");
const photoModalCaption = document.getElementById("photo-modal-caption");
const photoModalNote = document.getElementById("photo-modal-note");

// --- 6. INITIALIZATION ---
document.addEventListener("DOMContentLoaded", () => {
  setupRomanticClickEffects();
  initOverflowingMovingPhotosEngine();
  setupParticles();
  setupPinInputEvents();
  setupAudioController();
});

// --- 7. OVERFLOWING MOVING PHOTOS ENGINE ---
function initOverflowingMovingPhotosEngine() {
  if (!floatingPhotoLayer) return;
  floatingPhotoLayer.innerHTML = "";
  activeMovingPhotos = [];
  currentlyFocusedPhoto = null;

  const isMobile = window.innerWidth < 768;
  const photoCount = isMobile ? 14 : 22;
  const photosToUse = MOVING_PHOTOS_DATA.slice(0, photoCount);

  const screenW = window.innerWidth;
  const screenH = window.innerHeight;

  photosToUse.forEach((item, index) => {
    const el = document.createElement("div");
    
    const depth = index % 3;
    const depthClass = depth === 0 ? "depth-back" : depth === 1 ? "depth-mid" : "depth-front";
    el.className = `floating-polaroid ${depthClass}`;

    let baseWidth;
    if (isMobile) {
      baseWidth = depth === 0 ? 78 : depth === 1 ? 92 : 106;
    } else {
      baseWidth = depth === 0 ? 104 : depth === 1 ? 128 : 150;
    }
    el.style.width = `${baseWidth}px`;

    el.innerHTML = `
      <div class="polaroid-img-wrapper">
        <img src="${item.src}" alt="${item.caption || 'Memory'}"
             onerror="this.onerror=null; this.src='${item.fallbackSrc || ''}'; this.onerror=function(){this.parentElement.innerHTML='<div class=\\'placeholder-content\\' style=\\'padding:4px;\\'><span class=\\'placeholder-icon\\' style=\\'font-size:16px;\\'>📷</span><span class=\\'placeholder-text\\' style=\\'font-size:8px;\\'>Photo ${index+1}</span></div>';};">
      </div>
      <div class="polaroid-caption">${item.caption || `Photo ${index+1}`}</div>
      <div class="click-again-badge">Tap again to open</div>
    `;

    const photoObj = {
      el,
      item,
      x: Math.random() * (screenW - baseWidth),
      y: Math.random() * (screenH - 140),
      vx: 0,
      vy: 0,
      rot: (Math.random() - 0.5) * 16,
      rotSpeed: (Math.random() - 0.5) * 0.05,
      width: baseWidth,
      height: baseWidth * 1.25,
      isHovered: false,
      isBig: false
    };

    const speed = (isMobile ? 0.32 + Math.random() * 0.25 : 0.4 + Math.random() * 0.3) * (depth === 0 ? 0.8 : depth === 1 ? 1 : 1.15);
    const angle = Math.random() * Math.PI * 2;
    photoObj.vx = Math.cos(angle) * speed;
    photoObj.vy = Math.sin(angle) * speed;

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

  const screenW = window.innerWidth;
  const screenH = window.innerHeight;
  const zoomScale = screenW < 768 ? 2.1 : 2.6;

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

function updateMovingPhotosLoop() {
  const screenW = window.innerWidth;
  const screenH = window.innerHeight;

  activeMovingPhotos.forEach(p => {
    if (!p.isHovered && !p.isBig) {
      p.x += p.vx;
      p.y += p.vy;
      p.rot += p.rotSpeed;

      const margin = 110;
      if (p.x < -margin) p.x = screenW + 20;
      if (p.x > screenW + margin) p.x = -p.width - 20;
      if (p.y < -margin) p.y = screenH + 20;
      if (p.y > screenH + margin) p.y = -p.height - 20;

      p.el.style.transform = `translate3d(${p.x}px, ${p.y}px, 0) rotate(${p.rot}deg)`;
    }
  });

  movingAnimationRequestId = requestAnimationFrame(updateMovingPhotosLoop);
}

window.addEventListener("resize", () => {
  if (window.innerWidth < 768 && activeMovingPhotos.length > 15) {
    initOverflowingMovingPhotosEngine();
  } else if (window.innerWidth >= 768 && activeMovingPhotos.length < 18) {
    initOverflowingMovingPhotosEngine();
  }
});

// --- 8. OPENED MEMORY MODAL ---
function openPhotoModal(src, caption, note) {
  if (!photoModalBackdrop) return;
  photoModalImg.src = src;
  photoModalCaption.textContent = caption || "";
  if (photoModalNote) {
    photoModalNote.textContent = note || "";
  }
  photoModalBackdrop.classList.add("active");
}

function closePhotoModal() {
  if (photoModalBackdrop) photoModalBackdrop.classList.remove("active");
  dismissFocusedPhoto();
}

// --- 9. ROMANTIC CLICK & TAP EFFECTS (NO CURSOR TRACKING) ---
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

  for (let i = 0; i < 14; i++) {
    const angle = Math.random() * Math.PI * 2;
    const speed = Math.random() * 4.5 + 1.2;
    const vx = Math.cos(angle) * speed;
    const vy = Math.sin(angle) * speed - 1.2;
    const size = Math.random() * 5 + 3;
    const isHeart = Math.random() > 0.4;
    let alpha = 1;

    function renderSpark() {
      if (alpha <= 0) return;
      ctx.save();
      ctx.translate(x + vx * (1 - alpha) * 24, y + vy * (1 - alpha) * 24);
      
      if (isHeart) {
        ctx.beginPath();
        const h = size * alpha;
        ctx.moveTo(0, h * 0.3);
        ctx.bezierCurveTo(0, 0, -h / 2, 0, -h / 2, h * 0.3);
        ctx.bezierCurveTo(-h / 2, (h + h * 0.3) / 2, 0, h, 0, h * 1.3);
        ctx.bezierCurveTo(0, h, h / 2, (h + h * 0.3) / 2, h / 2, h * 0.3);
        ctx.bezierCurveTo(h / 2, 0, 0, 0, 0, h * 0.3);
        ctx.fillStyle = `rgba(165, 220, 255, ${alpha * 0.9})`;
        ctx.shadowBlur = 10;
        ctx.shadowColor = `rgba(70, 166, 247, ${alpha})`;
        ctx.fill();
      } else {
        ctx.beginPath();
        const r = size * alpha * 0.8;
        for (let j = 0; j < 4; j++) {
          ctx.lineTo(Math.cos((j * Math.PI) / 2) * r, Math.sin((j * Math.PI) / 2) * r);
          ctx.lineTo(Math.cos((j * Math.PI) / 2 + Math.PI / 4) * (r * 0.35), Math.sin((j * Math.PI) / 2 + Math.PI / 4) * (r * 0.35));
        }
        ctx.closePath();
        ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`;
        ctx.shadowBlur = 12;
        ctx.shadowColor = `rgba(140, 210, 255, ${alpha})`;
        ctx.fill();
      }

      ctx.restore();
      alpha -= 0.04;
      requestAnimationFrame(renderSpark);
    }
    renderSpark();
  }
}

// --- 10. CINEMATIC CHANNEL SWITCHING ENGINE (FADE IN & OUT) ---
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

// --- 11. PIN VALIDATION LOGIC ---
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

  // Click anywhere on anniversary announcement -> Directly open Month 1!
  if (channelPin) {
    channelPin.addEventListener("click", (e) => {
      if (pinSuccessScreenReady && !e.target.closest(".pin-digit") && !e.target.closest("button")) {
        openMonthLetter(1);
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

// --- 12. MONTHLY LETTER CHANNELS (SMOOTH PAGE TRANSITIONS) ---
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
        btnPrev.textContent = "← Start Over";
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
        
        const fallbackOldPath = `images/month${month.index}_${idx + 1}.jpg`;
        const fallbackSinglePath = `images/month${month.index}.jpg`;

        itemEl.innerHTML = `
          <div class="trio-img-container">
            <img src="${imgSrc}" alt="${cap}"
                 onerror="this.onerror=null; this.src='${fallbackOldPath}'; this.onerror=function(){this.src='${fallbackSinglePath}'; this.onerror=function(){this.parentElement.innerHTML='<div class=\\'placeholder-content\\'><span class=\\'placeholder-icon\\'>📷</span><span class=\\'placeholder-text\\'>Photo ${idx+1}</span><span class=\\'placeholder-sub\\'>photo${idx+1}.jpg</span></div>';};};">
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
    switchChannel("channel-pin");
  }
}

// --- 13. INTERMISSION (12TH MONTH - 08/22/26) ---
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

// --- 14. GRAND FINALE (SLIDESHOW & LAST TEXT) ---
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
    // Spawn celebratory starlight sparks on letter reveal
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

// --- 15. AUDIO CONTROLLER & SYNTHESIS ---
function setupAudioController() {
  if (!audioController) return;

  audioController.addEventListener("click", () => {
    if (isAudioPlaying) {
      pauseAudio();
    } else {
      startAudioPlayback();
    }
  });
}

function startAudioPlayback() {
  if (bgAudio) {
    bgAudio.play().then(() => {
      isAudioPlaying = true;
      audioController.classList.add("playing");
    }).catch(() => {
      startAmbientSynthMelody();
    });
  } else {
    startAmbientSynthMelody();
  }
}

function pauseAudio() {
  if (bgAudio) bgAudio.pause();
  stopAmbientSynthMelody();
  isAudioPlaying = false;
  if (audioController) audioController.classList.remove("playing");
}

function startAmbientSynthMelody() {
  try {
    if (!webAudioContext) {
      webAudioContext = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (webAudioContext.state === 'suspended') {
      webAudioContext.resume();
    }
    isAudioPlaying = true;
    if (audioController) audioController.classList.add("playing");

    playRomanticNotesSequence();
  } catch (err) {
    console.log("Audio notice:", err);
  }
}

function playRomanticNotesSequence() {
  if (!isAudioPlaying || !webAudioContext) return;

  const romanticScale = [261.63, 329.63, 392.00, 493.88, 523.25, 587.33, 659.25];
  const noteFreq = romanticScale[Math.floor(Math.random() * romanticScale.length)];

  const osc = webAudioContext.createOscillator();
  const gain = webAudioContext.createGain();

  osc.type = "sine";
  osc.frequency.setValueAtTime(noteFreq, webAudioContext.currentTime);

  gain.gain.setValueAtTime(0.0001, webAudioContext.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.09, webAudioContext.currentTime + 0.35);
  gain.gain.exponentialRampToValueAtTime(0.0001, webAudioContext.currentTime + 2.8);

  osc.connect(gain);
  gain.connect(webAudioContext.destination);

  osc.start();
  osc.stop(webAudioContext.currentTime + 2.9);

  if (isAudioPlaying) {
    setTimeout(playRomanticNotesSequence, 1600 + Math.random() * 1200);
  }
}

function stopAmbientSynthMelody() {
  isAudioPlaying = false;
}

// --- 16. PARTICLES & CONFETTI (ROMANTIC ETHEREAL PARTICLES) ---
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
  const count = window.innerWidth < 768 ? 22 : 36;

  for (let i = 0; i < count; i++) {
    particles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      size: Math.random() * 12 + 6,
      speedX: (Math.random() - 0.5) * 0.4,
      speedY: -(Math.random() * 0.5 + 0.25),
      swaySpeed: Math.random() * 0.02 + 0.01,
      swayOffset: Math.random() * Math.PI * 2,
      opacity: Math.random() * 0.5 + 0.3,
      type: Math.random() > 0.45 ? "heart" : "sparkle"
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
    ctx.shadowBlur = 12;
    ctx.shadowColor = `rgba(70, 166, 247, ${opacity * 0.9})`;
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
    ctx.shadowBlur = 10;
    ctx.shadowColor = `rgba(150, 220, 255, 0.85)`;
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

  for (let i = 0; i < 55; i++) {
    const angle = Math.random() * Math.PI * 2;
    const speed = Math.random() * 7 + 2;
    const vx = Math.cos(angle) * speed;
    const vy = Math.sin(angle) * speed;
    let life = 1;

    function renderParticle() {
      if (life <= 0) return;
      ctx.save();
      ctx.beginPath();
      ctx.arc(centerX + vx * (1 - life) * 45, centerY + vy * (1 - life) * 45, 4.5 * life, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(145, 215, 255, ${life})`;
      ctx.shadowBlur = 14;
      ctx.shadowColor = "rgba(70, 166, 247, 0.85)";
      ctx.fill();
      ctx.restore();
      life -= 0.03;
      requestAnimationFrame(renderParticle);
    }
    renderParticle();
  }
}

// Reset Story with smooth transition
function restartStory() {
  pinAttempts = 0;
  pinSuccessScreenReady = false;
  dismissFocusedPhoto();
  if (pinSuccessBox) pinSuccessBox.style.display = "none";
  if (anniversaryAnnouncement) anniversaryAnnouncement.style.display = "none";
  if (pinEntryView) pinEntryView.style.display = "block";
  pinInputs.forEach(input => input.value = "");
  switchChannel("channel-pin");
}
