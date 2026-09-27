/**
 * Grind. Coffee - Mobile-First Interactive Web App
 * Features: Channel Navigation with Back Stack, Interactive Digital Menu,
 * Vintage Sheet Viewer, "Find Your Grind" Quiz, Live Hours, and Delivery Integration.
 */

// Global State
let menuData = { categories: [], items: [] };
let activeCategory = 'all';
let searchQuery = '';
let channelHistory = ['home'];
let currentZoom = 1;

// Document Ready
document.addEventListener('DOMContentLoaded', async () => {
  initLiveHours();
  await loadMenuData();
  setupChannelNavigation();
  setupMenuFilters();
  setupSearch();
  setupQuiz();
  setupSheetModal();
  setupScrollTracking();
});

/* ==========================================================================
   1. LIVE OPERATING HOURS (PHILIPPINES UTC+8)
   ========================================================================== */
function initLiveHours() {
  const updateStatus = () => {
    // Current time in Asia/Manila (UTC+8)
    const now = new Date();
    const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
    const pht = new Date(utc + (3600000 * 8));

    const hours = pht.getHours();
    const minutes = pht.getMinutes();
    const currentMins = hours * 60 + minutes;

    // Main Branch: 9:00 AM (540m) to 10:00 PM (1320m)
    const openTime = 9 * 60;   // 9:00 AM
    const closeTime = 22 * 60; // 10:00 PM

    const isOpen = currentMins >= openTime && currentMins < closeTime;

    const badges = document.querySelectorAll('.live-status-badge');
    badges.forEach(badge => {
      if (isOpen) {
        const remainingHours = Math.floor((closeTime - currentMins) / 60);
        const remainingMins = (closeTime - currentMins) % 60;
        let timeString = remainingHours > 0 ? `${remainingHours}h ${remainingMins}m` : `${remainingMins}m`;
        
        badge.innerHTML = `
          <span class="status-dot open"></span>
          <span class="text-emerald-700 font-semibold">Open Now</span>
          <span class="text-xs text-stone-500 hidden sm:inline">· Closes in ${timeString} (10:00 PM)</span>
        `;
      } else {
        badge.innerHTML = `
          <span class="status-dot closed"></span>
          <span class="text-rose-700 font-semibold">Closed Now</span>
          <span class="text-xs text-stone-500 hidden sm:inline">· Opens at 9:00 AM daily</span>
        `;
      }
    });
  };

  updateStatus();
  setInterval(updateStatus, 60000); // Check every minute
}

/* ==========================================================================
   2. CHANNEL NAVIGATION & BACK SYSTEM ("Click Back Whenever I Like It")
   ========================================================================== */
function setupChannelNavigation() {
  const channelButtons = document.querySelectorAll('[data-channel]');
  
  channelButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const targetChannel = btn.dataset.channel;
      switchChannel(targetChannel);
    });
  });

  // Global Back buttons (Dock Back button & Header Back button)
  const backButtons = document.querySelectorAll('.back-trigger');
  backButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      handleGlobalBack();
    });
  });

  // Handle browser back button (popstate)
  window.addEventListener('popstate', (e) => {
    if (e.state && e.state.channel) {
      applyChannel(e.state.channel, false);
    } else {
      applyChannel('home', false);
    }
  });

  // Initial State
  history.replaceState({ channel: 'home' }, '', window.location.pathname);
}

function switchChannel(channelId, addToHistory = true) {
  // Close any open modals first
  closeAllModals();

  if (channelId === channelHistory[channelHistory.length - 1]) {
    // If clicking the current channel, smoothly scroll to top of that section
    scrollToSection(channelId);
    return;
  }

  if (addToHistory) {
    channelHistory.push(channelId);
    history.pushState({ channel: channelId }, '', `#${channelId}`);
  }

  applyChannel(channelId);
}

function applyChannel(channelId) {
  // Update channel dock buttons
  document.querySelectorAll('.channel-btn').forEach(btn => {
    if (btn.dataset.channel === channelId) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // Update header back button visibility
  const headerBackBtn = document.getElementById('headerBackBtn');
  if (headerBackBtn) {
    if (channelId !== 'home' || channelHistory.length > 1) {
      headerBackBtn.classList.remove('opacity-0', 'pointer-events-none');
      headerBackBtn.classList.add('opacity-100', 'pointer-events-auto');
    } else {
      headerBackBtn.classList.add('opacity-0', 'pointer-events-none');
      headerBackBtn.classList.remove('opacity-100', 'pointer-events-auto');
    }
  }

  scrollToSection(channelId);
}

function scrollToSection(sectionId) {
  const element = document.getElementById(sectionId);
  if (element) {
    const yOffset = -70; // Header offset
    const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
    window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' });
  }
}

function handleGlobalBack() {
  // Priority 1: Check if any modal is open
  const activeModal = document.querySelector('.modal-overlay.active');
  if (activeModal) {
    closeAllModals();
    return;
  }

  // Priority 2: Pop history stack
  if (channelHistory.length > 1) {
    channelHistory.pop(); // Remove current
    const prevChannel = channelHistory[channelHistory.length - 1];
    applyChannel(prevChannel);
  } else {
    // At root, scroll to top of home smoothly
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

function setupScrollTracking() {
  // Highlight active channel based on scroll position
  const sections = ['home', 'specialty', 'menu', 'quiz', 'story', 'visit', 'order'];
  window.addEventListener('scroll', () => {
    const scrollPos = window.scrollY + 200;
    
    for (let i = sections.length - 1; i >= 0; i--) {
      const section = document.getElementById(sections[i]);
      if (section && section.offsetTop <= scrollPos) {
        document.querySelectorAll('.channel-btn').forEach(btn => {
          if (btn.dataset.channel === sections[i]) {
            btn.classList.add('active');
          } else if (btn.dataset.channel) {
            btn.classList.remove('active');
          }
        });
        break;
      }
    }
  }, { passive: true });
}

/* ==========================================================================
   3. MENU DATA & RENDERING
   ========================================================================== */
async function loadMenuData() {
  try {
    const res = await fetch('data/menu.json');
    if (!res.ok) throw new Error('Failed to load menu.json');
    menuData = await res.json();
    renderCategoryPills();
    renderMenuItems();
  } catch (err) {
    console.error('Error loading menu:', err);
    document.getElementById('menuGrid').innerHTML = `
      <div class="col-span-full text-center py-12 text-stone-500">
        <p class="font-medium">Unable to load interactive menu items right now.</p>
        <p class="text-sm mt-1">Please use the "View Original Menu Boards" button to see our full menu.</p>
      </div>
    `;
  }
}

function renderCategoryPills() {
  const container = document.getElementById('categoryPills');
  if (!container) return;

  const html = menuData.categories.map(cat => {
    const count = cat.id === 'all' 
      ? menuData.items.length 
      : menuData.items.filter(item => item.category === cat.id).length;
    
    return `
      <button 
        class="category-pill whitespace-nowrap px-4 py-2 rounded-full text-xs sm:text-sm font-semibold transition-all flex items-center gap-2 border ${
          cat.id === activeCategory
            ? 'bg-[#4A2E1B] text-white border-[#4A2E1B] shadow-sm'
            : 'bg-white text-stone-700 border-stone-200 hover:border-amber-700 hover:bg-stone-50'
        }"
        data-cat="${cat.id}">
        <span>${cat.name}</span>
        <span class="text-[10px] px-1.5 py-0.5 rounded-full ${
          cat.id === activeCategory ? 'bg-amber-700/60 text-amber-100' : 'bg-stone-100 text-stone-500'
        }">${count}</span>
      </button>
    `;
  }).join('');

  container.innerHTML = html;

  container.querySelectorAll('.category-pill').forEach(btn => {
    btn.addEventListener('click', () => {
      activeCategory = btn.dataset.cat;
      renderCategoryPills();
      renderMenuItems();
    });
  });
}

function setupMenuFilters() {
  // Listen for changes or custom triggers
}

function setupSearch() {
  const searchInput = document.getElementById('menuSearch');
  if (!searchInput) return;

  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value.toLowerCase().trim();
    renderMenuItems();
  });
}

function renderMenuItems() {
  const grid = document.getElementById('menuGrid');
  if (!grid) return;

  let items = menuData.items;

  // Filter by category
  if (activeCategory !== 'all') {
    items = items.filter(item => item.category === activeCategory);
  }

  // Filter by search query
  if (searchQuery) {
    items = items.filter(item => 
      item.name.toLowerCase().includes(searchQuery) ||
      (item.desc && item.desc.toLowerCase().includes(searchQuery)) ||
      item.category.toLowerCase().includes(searchQuery)
    );
  }

  if (items.length === 0) {
    grid.innerHTML = `
      <div class="col-span-full text-center py-16 px-4 bg-white rounded-2xl border border-dashed border-stone-300">
        <div class="w-12 h-12 mx-auto rounded-full bg-amber-50 flex items-center justify-center text-amber-800 mb-3">
          <i data-lucide="search-x" class="w-6 h-6"></i>
        </div>
        <h4 class="font-cinzel text-lg font-bold text-stone-800">No items found</h4>
        <p class="text-sm text-stone-500 mt-1">Try another search term or select another category</p>
        <button onclick="resetMenuFilter()" class="mt-4 px-4 py-2 bg-[#4A2E1B] text-white text-xs font-semibold rounded-full hover:bg-amber-900 transition">
          Clear Search
        </button>
      </div>
    `;
    if (window.lucide) lucide.createIcons();
    return;
  }

  const cardsHtml = items.map(item => {
    const hasImage = !!item.image;
    const isSinglePrice = item.price !== undefined;

    return `
      <div class="menu-card bg-white rounded-2xl border border-stone-200/90 overflow-hidden flex flex-col justify-between p-4 shadow-sm hover:shadow-md transition cursor-pointer" onclick="openItemModal('${item.id}')">
        <div>
          ${hasImage ? `
            <div class="w-full h-36 mb-3 rounded-xl overflow-hidden bg-stone-100 flex items-center justify-center relative">
              <img src="${item.image}" alt="${item.name}" class="w-full h-full object-cover object-center group-hover:scale-105 transition duration-300" loading="lazy">
              ${item.bestseller ? `
                <span class="absolute top-2 right-2 bg-amber-600/95 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-sm backdrop-blur-sm">
                  ⭐ Bestseller
                </span>
              ` : ''}
            </div>
          ` : `
            <div class="flex items-start justify-between gap-2 mb-2">
              <div class="flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-[#C88A42]"></span>
                <span class="text-[11px] font-semibold uppercase tracking-wider text-[#C88A42]">${item.type || getCategoryLabel(item.category)}</span>
              </div>
              ${item.bestseller ? `
                <span class="bg-amber-100 text-amber-800 text-[10px] font-bold px-2 py-0.5 rounded-full">
                  ⭐ Favorite
                </span>
              ` : ''}
            </div>
          `}

          <h3 class="font-cinzel text-base font-bold text-stone-900 leading-snug">${item.name}</h3>
          <p class="text-xs text-stone-500 mt-1 line-clamp-2 leading-relaxed">${item.desc || 'Prepared fresh with premium ingredients at Grind. Coffee.'}</p>
        </div>

        <div class="mt-4 pt-3 border-t border-stone-100 flex items-center justify-between">
          <div>
            ${isSinglePrice ? `
              <div class="flex items-baseline gap-1">
                <span class="text-xs text-stone-400 font-medium">₱</span>
                <span class="text-lg font-bold text-[#4A2E1B]">${item.price}</span>
              </div>
            ` : `
              <div class="flex items-center gap-2">
                <div class="text-left">
                  <span class="text-[10px] text-stone-400 uppercase font-bold block leading-none">Grande</span>
                  <span class="text-sm font-bold text-[#4A2E1B]">₱${item.priceGrande}</span>
                </div>
                ${item.priceVenti ? `
                  <span class="text-stone-300">/</span>
                  <div class="text-left">
                    <span class="text-[10px] text-stone-400 uppercase font-bold block leading-none">Venti</span>
                    <span class="text-sm font-bold text-[#4A2E1B]">₱${item.priceVenti}</span>
                  </div>
                ` : ''}
              </div>
            `}
          </div>

          <button class="w-8 h-8 rounded-full bg-amber-50 text-[#C88A42] flex items-center justify-center hover:bg-[#C88A42] hover:text-white transition" title="View Details">
            <i data-lucide="plus" class="w-4 h-4"></i>
          </button>
        </div>
      </div>
    `;
  }).join('');

  grid.innerHTML = cardsHtml;
  if (window.lucide) lucide.createIcons();
}

function getCategoryLabel(catId) {
  const map = {
    'coffee': 'Coffee',
    'house-creations': 'Signature',
    'matcha-strawberry': 'Matcha & Berry',
    'frappes': 'Frappe',
    'teas': 'Tea',
    'pastries': 'Pastry',
    'cheesecakes': 'Cheesecake',
    'cookies': 'Cookie',
    'pasta-rice': 'Main Dish'
  };
  return map[catId] || 'Specialty';
}

function resetMenuFilter() {
  activeCategory = 'all';
  searchQuery = '';
  const searchInput = document.getElementById('menuSearch');
  if (searchInput) searchInput.value = '';
  renderCategoryPills();
  renderMenuItems();
}

/* ==========================================================================
   4. ITEM DETAIL MODAL
   ========================================================================== */
function openItemModal(itemId) {
  const item = menuData.items.find(i => i.id === itemId);
  if (!item) return;

  const modal = document.getElementById('itemModal');
  const body = document.getElementById('itemModalBody');
  if (!modal || !body) return;

  const isSinglePrice = item.price !== undefined;

  body.innerHTML = `
    <div class="relative">
      ${item.image ? `
        <div class="w-full h-56 bg-stone-100 rounded-t-2xl overflow-hidden relative">
          <img src="${item.image}" alt="${item.name}" class="w-full h-full object-cover">
          <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
          <span class="absolute bottom-3 left-4 text-xs font-semibold px-2.5 py-1 bg-amber-600 text-white rounded-full">
            ${getCategoryLabel(item.category)}
          </span>
        </div>
      ` : `
        <div class="p-6 bg-gradient-to-br from-[#4A2E1B] to-[#28170F] text-white rounded-t-2xl">
          <span class="text-xs uppercase tracking-wider text-amber-300 font-semibold">${getCategoryLabel(item.category)} · ${item.type || 'House Recipe'}</span>
          <h2 class="font-cinzel text-2xl font-bold mt-1">${item.name}</h2>
        </div>
      `}

      <div class="p-6">
        ${item.image ? `
          <h2 class="font-cinzel text-2xl font-bold text-stone-900">${item.name}</h2>
        ` : ''}

        <p class="text-sm text-stone-600 mt-2 leading-relaxed">
          ${item.desc || 'Prepared freshly with passion and premium ingredients at Grind. Coffee, Calamba City.'}
        </p>

        <!-- Pricing Card -->
        <div class="my-6 p-4 rounded-xl bg-stone-50 border border-stone-200">
          <div class="text-xs font-bold uppercase tracking-wider text-stone-500 mb-2">Available Serving & Price:</div>
          ${isSinglePrice ? `
            <div class="flex items-center justify-between">
              <span class="font-semibold text-stone-800 text-sm">Regular Serving</span>
              <span class="font-bold text-xl text-[#4A2E1B]">₱${item.price}</span>
            </div>
          ` : `
            <div class="grid grid-cols-2 gap-3">
              <div class="p-2.5 rounded-lg bg-white border border-stone-200 text-center">
                <span class="text-[11px] font-bold text-stone-500 uppercase block">Grande (16 oz)</span>
                <span class="text-lg font-bold text-[#4A2E1B]">₱${item.priceGrande}</span>
              </div>
              ${item.priceVenti ? `
                <div class="p-2.5 rounded-lg bg-white border border-stone-200 text-center">
                  <span class="text-[11px] font-bold text-stone-500 uppercase block">Venti (22 oz)</span>
                  <span class="text-lg font-bold text-[#4A2E1B]">₱${item.priceVenti}</span>
                </div>
              ` : `
                <div class="p-2.5 rounded-lg bg-stone-100 border border-stone-200 text-center opacity-60">
                  <span class="text-[11px] font-bold text-stone-500 uppercase block">Venti</span>
                  <span class="text-xs text-stone-500">Not Available</span>
                </div>
              `}
            </div>
          `}
        </div>

        <!-- Action Buttons -->
        <div class="flex flex-col gap-3">
          <a href="https://www.foodpanda.ph/restaurant/qlei/grind-jp-rizal" target="_blank" rel="noopener noreferrer" 
             class="w-full py-3.5 px-4 rounded-xl bg-[#D70F64] text-white font-bold text-sm flex items-center justify-center gap-2 hover:bg-[#b00c52] transition shadow-md">
            <span>Order on foodpanda</span>
            <i data-lucide="external-link" class="w-4 h-4"></i>
          </a>

          <button onclick="closeItemModal()" 
                  class="w-full py-3 px-4 rounded-xl bg-stone-100 text-stone-700 font-semibold text-sm hover:bg-stone-200 transition flex items-center justify-center gap-2">
            <i data-lucide="arrow-left" class="w-4 h-4"></i>
            <span>Back to Menu</span>
          </button>
        </div>
      </div>
    </div>
  `;

  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
  if (window.lucide) lucide.createIcons();
}

function closeItemModal() {
  const modal = document.getElementById('itemModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
}

/* ==========================================================================
   5. ORIGINAL VINTAGE MENU SHEET VIEWER
   ========================================================================== */
function setupSheetModal() {
  const viewSheetBtns = document.querySelectorAll('.open-sheets-btn');
  viewSheetBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      openSheetModal();
    });
  });
}

function openSheetModal(sheetIndex = 1) {
  const modal = document.getElementById('sheetModal');
  if (!modal) return;

  switchSheet(sheetIndex);
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeSheetModal() {
  const modal = document.getElementById('sheetModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
}

function switchSheet(index) {
  const sheets = [
    { title: 'Drinks Menu 1: Coffee & Matcha', src: 'assets/images/menu-drinks-1.png' },
    { title: 'Drinks Menu 2: Frappes & House Creations', src: 'assets/images/menu-drinks-2.png' },
    { title: 'Food Menu: Pastries, Pastas & Rice Meals', src: 'assets/images/menu-food.png' }
  ];

  const target = sheets[index - 1];
  const sheetImg = document.getElementById('activeSheetImg');
  const sheetTitle = document.getElementById('activeSheetTitle');
  const tabButtons = document.querySelectorAll('.sheet-tab-btn');

  if (sheetImg && target) {
    sheetImg.src = target.src;
    sheetImg.style.transform = `scale(1)`;
    currentZoom = 1;
  }
  if (sheetTitle && target) {
    sheetTitle.textContent = target.title;
  }

  tabButtons.forEach((btn, idx) => {
    if (idx + 1 === index) {
      btn.classList.add('bg-[#4A2E1B]', 'text-white');
      btn.classList.remove('bg-white', 'text-stone-700');
    } else {
      btn.classList.remove('bg-[#4A2E1B]', 'text-white');
      btn.classList.add('bg-white', 'text-stone-700');
    }
  });
}

function zoomSheet(delta) {
  const img = document.getElementById('activeSheetImg');
  if (!img) return;

  currentZoom = Math.min(2.5, Math.max(0.8, currentZoom + delta));
  img.style.transform = `scale(${currentZoom})`;
}

function closeAllModals() {
  closeItemModal();
  closeSheetModal();
  closeOrderModal();
}

/* ==========================================================================
   6. "FIND YOUR GRIND" INTERACTIVE BEVERAGE QUIZ
   ========================================================================== */
function setupQuiz() {
  const quizForm = document.getElementById('quizForm');
  if (!quizForm) return;

  const quizSteps = document.querySelectorAll('.quiz-step');
  const progressFill = document.getElementById('quizProgressFill');
  let currentStep = 1;

  const userSelections = {
    vibe: '',
    temp: '',
    type: ''
  };

  // Step 1 option clicks
  document.querySelectorAll('[data-quiz-vibe]').forEach(btn => {
    btn.addEventListener('click', () => {
      userSelections.vibe = btn.dataset.quizVibe;
      goToStep(2);
    });
  });

  // Step 2 option clicks
  document.querySelectorAll('[data-quiz-temp]').forEach(btn => {
    btn.addEventListener('click', () => {
      userSelections.temp = btn.dataset.quizTemp;
      goToStep(3);
    });
  });

  // Step 3 option clicks
  document.querySelectorAll('[data-quiz-type]').forEach(btn => {
    btn.addEventListener('click', () => {
      userSelections.type = btn.dataset.quizType;
      showQuizResult(userSelections);
    });
  });

  function goToStep(step) {
    currentStep = step;
    quizSteps.forEach(s => {
      if (parseInt(s.dataset.step) === step) {
        s.classList.remove('hidden');
      } else {
        s.classList.add('hidden');
      }
    });

    if (progressFill) {
      progressFill.style.width = `${(step / 3) * 100}%`;
    }
  }

  window.restartQuiz = () => {
    goToStep(1);
    document.getElementById('quizResult').classList.add('hidden');
    document.getElementById('quizStepsContainer').classList.remove('hidden');
  };
}

function showQuizResult(answers) {
  const stepsContainer = document.getElementById('quizStepsContainer');
  const resultContainer = document.getElementById('quizResult');
  const cardContainer = document.getElementById('quizResultCard');

  if (!stepsContainer || !resultContainer || !cardContainer) return;

  stepsContainer.classList.add('hidden');
  resultContainer.classList.remove('hidden');

  // Recommendation Logic
  let recommendedId = 'c7'; // Default: Spanish Latte
  let reason = 'The balanced, crowd-pleasing favorite of Calamba City.';

  if (answers.vibe === 'energy') {
    if (answers.temp === 'iced') {
      recommendedId = 'hc3'; // White Cream Cold Brew
      reason = 'Slow-steeped cold brew topped with handcrafted sweet salted cream for maximum focus!';
    } else {
      recommendedId = 'c7'; // Spanish Latte
      reason = 'Smooth espresso sweetened with condensed milk for an invigorating morning boost.';
    }
  } else if (answers.vibe === 'sweet') {
    if (answers.temp === 'blended') {
      recommendedId = 'fr4'; // Java Chip Frappe
      reason = 'Loaded with crunchy chocolate chips and velvety espresso cream.';
    } else {
      recommendedId = 'hc7'; // Velvet Muscovado
      reason = 'Rich unrefined local muscovado sugar paired with espresso and cream.';
    }
  } else if (answers.vibe === 'fruity') {
    if (answers.type === 'tea') {
      recommendedId = 't1'; // Peachberry Fruit Tea
      reason = 'Juicy ripe peach and wild berry tea shaken over crushed ice.';
    } else {
      recommendedId = 'ms2'; // Strawberry Matcha
      reason = 'Vibrant layers of fresh strawberries, creamy milk, and ceremonial green tea matcha.';
    }
  } else if (answers.vibe === 'food') {
    recommendedId = 'pa1'; // Chicken Pesto
    reason = 'Al dente pasta tossed in fragrant basil pesto, grilled chicken, and shaved parmesan.';
  }

  const item = menuData.items.find(i => i.id === recommendedId) || menuData.items[0];

  cardContainer.innerHTML = `
    <div class="p-6 bg-gradient-to-br from-[#FAF6F0] to-[#F2E9DE] rounded-2xl border border-amber-800/20 text-center">
      <div class="inline-block px-3 py-1 bg-amber-600 text-white rounded-full text-xs font-bold mb-3 uppercase tracking-wider">
        ✨ Your Perfect Match
      </div>
      <h3 class="font-cinzel text-2xl font-bold text-stone-900">${item.name}</h3>
      <p class="text-xs text-amber-900/80 font-medium italic mt-1">"${reason}"</p>
      
      <p class="text-sm text-stone-600 mt-3 max-w-md mx-auto">${item.desc}</p>

      <div class="mt-4 flex items-center justify-center gap-4 text-sm font-bold text-[#4A2E1B]">
        ${item.price ? `<span>₱${item.price}</span>` : `
          <span>Grande: ₱${item.priceGrande}</span>
          ${item.priceVenti ? `<span>·</span><span>Venti: ₱${item.priceVenti}</span>` : ''}
        `}
      </div>

      <div class="mt-6 flex flex-col sm:flex-row items-center justify-center gap-3">
        <a href="https://www.foodpanda.ph/restaurant/qlei/grind-jp-rizal" target="_blank" rel="noopener noreferrer"
           class="w-full sm:w-auto px-6 py-3 rounded-full bg-[#D70F64] text-white font-bold text-xs flex items-center justify-center gap-2 hover:bg-[#b00c52] transition shadow">
          <span>Order This on foodpanda</span>
          <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
        </a>
        <button onclick="restartQuiz()" class="w-full sm:w-auto px-6 py-3 rounded-full bg-white text-stone-700 font-semibold text-xs border border-stone-300 hover:bg-stone-50 transition">
          Take Quiz Again
        </button>
      </div>
    </div>
  `;

  if (window.lucide) lucide.createIcons();
}

/* ==========================================================================
   7. ORDER MODAL (FOODPANDA & STORE PICKUP)
   ========================================================================== */
function openOrderModal() {
  const modal = document.getElementById('orderModal');
  if (modal) {
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}

function closeOrderModal() {
  const modal = document.getElementById('orderModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
}

// Attach to window for HTML accessibility
window.openItemModal = openItemModal;
window.closeItemModal = closeItemModal;
window.openSheetModal = openSheetModal;
window.closeSheetModal = closeSheetModal;
window.switchSheet = switchSheet;
window.zoomSheet = zoomSheet;
window.openOrderModal = openOrderModal;
window.closeOrderModal = closeOrderModal;
window.switchChannel = switchChannel;
window.handleGlobalBack = handleGlobalBack;
