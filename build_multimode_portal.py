import os
import json
import re

from build_quiz_data import QUIZ_DATA
quiz_json_str = json.dumps(QUIZ_DATA)

# Read the full detailed content from the original HTML files if available
def read_content(path):
    if os.path.exists(path):
        return open(path, 'r', encoding='utf-8', errors='ignore').read()
    return ''

# Let's construct the complete Python builder
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
  <title>MUJIB Study Hub &middot; Detailed &amp; Summary Summative Reviewer</title>
  <meta name="description" content="All-in-One Comprehensive Summative Exam Reviewer with Detailed Long-form and Summary Short-form modes for Mabisang Komunikasyon, General Science, General Mathematics, and Finite Mathematics 1."/>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet"/>

  <!-- Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

  <style>
/* ==========================================================================
   LIGHT MODERN THEME & DESIGN TOKENS
   ========================================================================== */
:root {
  --font-display: 'Outfit', sans-serif;
  --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Crisp Light Theme */
  --bg: #f8fafc;
  --bg-surface: #ffffff;
  --bg-subtle: #f1f5f9;
  --bg-card: #ffffff;
  --border: #e2e8f0;
  --border-focus: #cbd5e1;

  --t1: #0f172a;       /* Primary text */
  --t2: #334155;       /* Secondary body text */
  --t3: #64748b;       /* Muted text */
  --t-light: #94a3b8;

  /* Subject Accent Colors */
  --mk-color: #e11d48;
  --mk-bg: #fff1f2;
  --mk-border: #fecdd3;
  --mk-grad: linear-gradient(135deg, #e11d48, #f59e0b);

  --gs-color: #0d9488;
  --gs-bg: #f0fdfa;
  --gs-border: #ccfbf1;
  --gs-grad: linear-gradient(135deg, #0d9488, #06b6d4);

  --gm-color: #2563eb;
  --gm-bg: #eff6ff;
  --gm-border: #dbeafe;
  --gm-grad: linear-gradient(135deg, #2563eb, #7c3aed);

  --fn-color: #d97706;
  --fn-bg: #fffbeb;
  --fn-border: #fef3c7;
  --fn-grad: linear-gradient(135deg, #d97706, #ea580c);

  /* Functional Colors */
  --success: #10b981;
  --success-bg: #ecfdf5;
  --error: #ef4444;
  --error-bg: #fef2f2;

  --radius-sm: 10px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-full: 9999px;

  --shadow-sm: 0 2px 6px rgba(0, 0, 0, 0.03);
  --shadow-md: 0 8px 20px rgba(15, 23, 42, 0.06);
  --shadow-lg: 0 16px 36px rgba(15, 23, 42, 0.08);
  --shadow-card: 0 4px 16px rgba(0, 0, 0, 0.04);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}

html {
  scroll-behavior: smooth;
  color-scheme: light;
}

body {
  font-family: var(--font-body);
  background-color: var(--bg);
  color: var(--t1);
  line-height: 1.65;
  font-size: 15px;
  min-height: 100vh;
  letter-spacing: 0.01em;
  padding-bottom: 75px;
}

::selection {
  background: rgba(37, 99, 235, 0.2);
  color: var(--t1);
}

/* ==========================================================================
   TOP GLOBAL BAR
   ========================================================================== */
.top-bar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.94);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  padding: 10px 20px;
  transition: all 0.3s;
}

.top-bar-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
}

.brand-badge {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  background: linear-gradient(135deg, #2563eb, #e11d48);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25);
}

.brand-text {
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 18px;
  letter-spacing: -0.02em;
  color: var(--t1);
}
.brand-text span {
  color: #2563eb;
}

.top-center-mode {
  display: flex;
  align-items: center;
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-full);
  padding: 3px;
  gap: 3px;
}

.mode-btn {
  padding: 6px 14px;
  border-radius: var(--radius-full);
  font-size: 12px;
  font-weight: 700;
  border: none;
  background: transparent;
  color: var(--t3);
  cursor: pointer;
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}
.mode-btn.active-mode {
  background: #ffffff;
  color: var(--t1);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
}
.mode-btn.active-mode.mode-summary { color: #2563eb; }
.mode-btn.active-mode.mode-detailed { color: #7c3aed; }

.top-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn-search {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  border-radius: var(--radius-full);
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  color: var(--t2);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-search:hover {
  background: #ffffff;
  border-color: #cbd5e1;
  color: var(--t1);
}

/* ==========================================================================
   MOBILE BOTTOM NAVIGATION
   ========================================================================== */
.mobile-bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 6px 4px max(6px, env(safe-area-inset-bottom));
  box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.04);
}
@media (min-width: 861px) {
  .mobile-bottom-nav { display: none; }
  body { padding-bottom: 0; }
}

.mob-tab {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  background: transparent;
  border: none;
  color: var(--t3);
  padding: 6px 10px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  flex: 1;
  font-family: inherit;
  transition: all 0.2s;
}
.mob-tab-icon { font-size: 18px; }
.mob-tab-lbl { font-size: 10px; font-weight: 700; letter-spacing: -0.01em; }
.mob-tab.active-tab { color: #2563eb; }
.mob-tab.active-tab.tab-mk { color: #e11d48; }
.mob-tab.active-tab.tab-gs { color: #0d9488; }
.mob-tab.active-tab.tab-gm { color: #2563eb; }
.mob-tab.active-tab.tab-fn { color: #d97706; }

/* Desktop Channel Tabs */
.desktop-pills {
  display: flex;
  align-items: center;
  gap: 6px;
}
@media (max-width: 860px) {
  .desktop-pills { display: none; }
}

.dpill {
  padding: 6px 14px;
  border-radius: var(--radius-full);
  font-size: 12.5px;
  font-weight: 700;
  border: 1px solid transparent;
  background: transparent;
  color: var(--t3);
  cursor: pointer;
  transition: all 0.2s;
}
.dpill:hover { color: var(--t1); background: var(--bg-subtle); }
.dpill.active-hub { background: #eff6ff; color: #2563eb; border-color: #bfdbfe; }
.dpill.active-mk { background: #fff1f2; color: #e11d48; border-color: #fecdd3; }
.dpill.active-gs { background: #f0fdfa; color: #0d9488; border-color: #99f6e4; }
.dpill.active-gm { background: #eff6ff; color: #2563eb; border-color: #bfdbfe; }
.dpill.active-fn { background: #fffbeb; color: #d97706; border-color: #fde68a; }

/* ==========================================================================
   VIEW SWITCHING & MODE LOGIC
   ========================================================================== */
.view-container {
  display: none;
  animation: viewFade 0.25s ease forwards;
}
.view-container.active-view {
  display: block;
}
@keyframes viewFade {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Visibility based on Mode */
body.mode-is-summary .mode-detailed-content { display: none !important; }
body.mode-is-summary .mode-summary-content { display: block !important; }

body.mode-is-detailed .mode-summary-content { display: none !important; }
body.mode-is-detailed .mode-detailed-content { display: block !important; }

/* ==========================================================================
   LANDING PAGE HERO & MODE SELECTION
   ========================================================================== */
.hero {
  padding: 40px 20px 30px;
  text-align: center;
  background: radial-gradient(circle at 50% 0%, #eff6ff 0%, #ffffff 75%);
  border-bottom: 1px solid var(--border);
}

.hero-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 14px;
  border-radius: var(--radius-full);
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  color: #2563eb;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin-bottom: 16px;
}

.hero-title {
  font-family: var(--font-display);
  font-size: clamp(28px, 6vw, 48px);
  font-weight: 900;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: var(--t1);
  margin-bottom: 12px;
}
.hero-title .grad-text {
  background: linear-gradient(135deg, #2563eb, #e11d48, #d97706);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: clamp(14px, 2.5vw, 16px);
  color: var(--t2);
  max-width: 620px;
  margin: 0 auto 24px;
  line-height: 1.6;
}

/* Landing Page Mode Choice Cards */
.mode-choice-container {
  max-width: 740px;
  margin: 0 auto 30px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}
@media (max-width: 600px) {
  .mode-choice-container { grid-template-columns: 1fr; }
}

.mode-card {
  background: #ffffff;
  border: 2px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 18px 20px;
  text-align: left;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  box-shadow: var(--shadow-sm);
}
.mode-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}
.mode-card.selected-mode-card {
  border-color: #2563eb;
  background: #f8faff;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
}
.mode-card.card-detailed.selected-mode-card {
  border-color: #7c3aed;
  background: #faf8ff;
  box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.15);
}

.mode-card-badge {
  display: inline-block;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: var(--radius-full);
  margin-bottom: 8px;
}
.mode-card.card-summary .mode-card-badge { background: #eff6ff; color: #2563eb; }
.mode-card.card-detailed .mode-card-badge { background: #f5f3ff; color: #7c3aed; }

.mode-card-title {
  font-family: var(--font-display);
  font-size: 17px;
  font-weight: 800;
  color: var(--t1);
  margin-bottom: 4px;
}
.mode-card-desc {
  font-size: 12.5px;
  color: var(--t2);
  line-height: 1.45;
}

/* Subject Grid */
.landing-grid-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px 20px 60px;
}
.section-head { margin-bottom: 20px; }
.section-head h2 {
  font-family: var(--font-display);
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--t1);
}
.section-head p { font-size: 13px; color: var(--t3); }

.topics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

.subject-card {
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-card);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  cursor: pointer;
  transition: transform 0.25s, box-shadow 0.25s, border-color 0.25s;
  position: relative;
  overflow: hidden;
}
.subject-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
}
.subject-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}

.card-mk::before { background: var(--mk-grad); }
.card-mk:hover { border-color: var(--mk-border); }
.card-gs::before { background: var(--gs-grad); }
.card-gs:hover { border-color: var(--gs-border); }
.card-gm::before { background: var(--gm-grad); }
.card-gm:hover { border-color: var(--gm-border); }
.card-fn::before { background: var(--fn-grad); }
.card-fn:hover { border-color: var(--fn-border); }

.card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}
.card-icon-box {
  width: 46px;
  height: 46px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
}
.card-mk .card-icon-box { background: var(--mk-bg); color: var(--mk-color); }
.card-gs .card-icon-box { background: var(--gs-bg); color: var(--gs-color); }
.card-gm .card-icon-box { background: var(--gm-bg); color: var(--gm-color); }
.card-fn .card-icon-box { background: var(--fn-bg); color: var(--fn-color); }

.card-badge {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: var(--radius-full);
}
.card-mk .card-badge { background: var(--mk-bg); color: var(--mk-color); border: 1px solid var(--mk-border); }
.card-gs .card-badge { background: var(--gs-bg); color: var(--gs-color); border: 1px solid var(--gs-border); }
.card-gm .card-badge { background: var(--gm-bg); color: var(--gm-color); border: 1px solid var(--gm-border); }
.card-fn .card-badge { background: var(--fn-bg); color: var(--fn-color); border: 1px solid var(--fn-border); }

.card-title {
  font-family: var(--font-display);
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--t1);
  margin-bottom: 8px;
}
.card-desc {
  font-size: 13.5px;
  color: var(--t2);
  line-height: 1.5;
  margin-bottom: 16px;
}

.keyword-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 20px;
}
.kw-chip {
  font-size: 11px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  background: var(--bg-subtle);
  color: var(--t3);
}

.card-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 14px;
  border-top: 1px solid var(--border);
}
.btn-open-channel {
  font-size: 13px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.card-mk .btn-open-channel { color: var(--mk-color); }
.card-gs .btn-open-channel { color: var(--gs-color); }
.card-gm .btn-open-channel { color: var(--gm-color); }
.card-fn .btn-open-channel { color: var(--fn-color); }

/* ==========================================================================
   SUBJECT CHANNEL STYLES
   ========================================================================== */
.channel-top-bar {
  background: #ffffff;
  border-bottom: 1px solid var(--border);
  padding: 10px 20px;
  position: sticky;
  top: 57px;
  z-index: 90;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}

.ch-back-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 700;
  color: var(--t2);
  cursor: pointer;
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  background: var(--bg-subtle);
  border: 1px solid var(--border);
}
.ch-back-link:hover { background: #ffffff; color: var(--t1); }

.ch-heading {
  font-family: var(--font-display);
  font-size: 16px;
  font-weight: 800;
  color: var(--t1);
}

.channel-container {
  max-width: 960px;
  margin: 0 auto;
  padding: 24px 20px 80px;
}

/* Subject Header Banner */
.subj-header-card {
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-bottom: 24px;
  border: 1px solid;
}
.subj-header-card.mk { background: var(--mk-bg); border-color: var(--mk-border); }
.subj-header-card.gs { background: var(--gs-bg); border-color: var(--gs-border); }
.subj-header-card.gm { background: var(--gm-bg); border-color: var(--gm-border); }
.subj-header-card.fn { background: var(--fn-bg); border-color: var(--fn-border); }

.shc-badge {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 8px;
}
.shc-badge.mk { color: var(--mk-color); }
.shc-badge.gs { color: var(--gs-color); }
.shc-badge.gm { color: var(--gm-color); }
.shc-badge.fn { color: var(--fn-color); }

.shc-title {
  font-family: var(--font-display);
  font-size: clamp(22px, 4vw, 32px);
  font-weight: 900;
  letter-spacing: -0.02em;
  color: var(--t1);
  margin-bottom: 8px;
}
.shc-desc { font-size: 14px; color: var(--t2); line-height: 1.5; }

/* Lesson Card */
.lesson-card {
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
}

.lesson-head {
  display: flex;
  align-items: center;
  gap: 12px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 18px;
}
.lesson-num {
  width: 38px;
  height: 38px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-display);
  font-weight: 900;
  font-size: 15px;
}
.lesson-num.mk { background: var(--mk-bg); color: var(--mk-color); }
.lesson-num.gs { background: var(--gs-bg); color: var(--gs-color); }
.lesson-num.gm { background: var(--gm-bg); color: var(--gm-color); }
.lesson-num.fn { background: var(--fn-bg); color: var(--fn-color); }

.lesson-title {
  font-family: var(--font-display);
  font-size: 18px;
  font-weight: 800;
  color: var(--t1);
}

/* Keyword Concept Grid */
.concept-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 12px;
  margin-bottom: 18px;
}

.concept-item {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 12px 14px;
}
.c-keyword {
  font-weight: 800;
  font-size: 13.5px;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.c-keyword.mk { color: var(--mk-color); }
.c-keyword.gs { color: var(--gs-color); }
.c-keyword.gm { color: var(--gm-color); }
.c-keyword.fn { color: var(--fn-color); }
.c-meaning {
  font-size: 13px;
  color: var(--t2);
  line-height: 1.45;
}

/* Detailed Long-Form Styles */
.detailed-section {
  margin: 16px 0 20px;
}
.det-p {
  font-size: 14.5px;
  color: var(--t2);
  line-height: 1.7;
  margin-bottom: 14px;
}
.det-list {
  padding-left: 20px;
  margin-bottom: 16px;
  color: var(--t2);
}
.det-list li { margin-bottom: 8px; font-size: 14px; line-height: 1.6; }
.det-list strong { color: var(--t1); }

.det-example-box {
  background: #f8fafc;
  border-left: 4px solid #2563eb;
  padding: 14px 18px;
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  margin: 14px 0;
  font-size: 13.5px;
  color: var(--t2);
  line-height: 1.6;
}
.det-example-box.mk { border-color: var(--mk-color); background: var(--mk-bg); }
.det-example-box.gs { border-color: var(--gs-color); background: var(--gs-bg); }
.det-example-box.gm { border-color: var(--gm-color); background: var(--gm-bg); }
.det-example-box.fn { border-color: var(--fn-color); background: var(--fn-bg); }

.det-subtitle {
  font-family: var(--font-display);
  font-size: 15.5px;
  font-weight: 800;
  color: var(--t1);
  margin: 16px 0 8px;
}

/* Formula Box */
.formula-box {
  background: #ffffff;
  border: 1.5px dashed #cbd5e1;
  border-radius: var(--radius-md);
  padding: 14px 18px;
  margin: 16px 0;
  font-family: var(--font-mono);
  font-size: 13.5px;
  font-weight: 700;
  color: var(--t1);
}
.formula-label {
  font-family: var(--font-body);
  font-size: 11px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--t3);
  margin-bottom: 6px;
}

/* Infographic Image Card */
.diagram-card {
  margin: 20px 0;
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid var(--border);
  background: #ffffff;
  box-shadow: var(--shadow-sm);
}
.diagram-card img {
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
}
.diagram-caption {
  padding: 10px 14px;
  font-size: 12px;
  font-weight: 600;
  color: var(--t3);
  background: var(--bg-subtle);
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 6px;
}

/* QUIZ ACTION BUTTON AT END OF LESSON */
.quiz-cta-box {
  margin-top: 20px;
  padding: 16px;
  border-radius: var(--radius-md);
  background: linear-gradient(135deg, #eff6ff, #f8fafc);
  border: 1px solid #bfdbfe;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}
.quiz-cta-info h4 {
  font-family: var(--font-display);
  font-size: 15px;
  font-weight: 800;
  color: var(--t1);
}
.quiz-cta-info p { font-size: 12.5px; color: var(--t3); }

.btn-start-quiz {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: var(--radius-full);
  font-size: 13px;
  font-weight: 800;
  color: #ffffff;
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  border: none;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
  transition: all 0.2s;
}
.btn-start-quiz:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(37, 99, 235, 0.4);
}
.btn-start-quiz.mk { background: var(--mk-grad); box-shadow: 0 4px 12px rgba(225, 29, 72, 0.3); }
.btn-start-quiz.gs { background: var(--gs-grad); box-shadow: 0 4px 12px rgba(13, 148, 136, 0.3); }
.btn-start-quiz.gm { background: var(--gm-grad); box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3); }
.btn-start-quiz.fn { background: var(--fn-grad); box-shadow: 0 4px 12px rgba(217, 119, 6, 0.3); }

/* ==========================================================================
   INTERACTIVE QUIZ MODAL
   ========================================================================== */
.quiz-modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 2000;
  background: rgba(15, 23, 42, 0.65);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 16px;
}
.quiz-modal-backdrop.open { display: flex; }

.quiz-card-modal {
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  width: 100%;
  max-width: 580px;
  box-shadow: var(--shadow-lg);
  overflow: hidden;
  animation: popIn 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
  max-height: 90vh;
}
@keyframes popIn {
  from { opacity: 0; transform: scale(0.94); }
  to { opacity: 1; transform: scale(1); }
}

.quiz-modal-header {
  padding: 16px 20px;
  background: var(--bg-subtle);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.quiz-modal-title {
  font-family: var(--font-display);
  font-size: 15px;
  font-weight: 800;
  color: var(--t1);
}
.btn-close-quiz {
  background: none;
  border: none;
  font-size: 20px;
  color: var(--t3);
  cursor: pointer;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.btn-close-quiz:hover { background: rgba(0,0,0,0.05); color: var(--t1); }

.quiz-progress-bar-wrap {
  height: 4px;
  background: #e2e8f0;
  width: 100%;
}
.quiz-progress-bar-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #2563eb, #10b981);
  transition: width 0.3s ease;
}

.quiz-body { padding: 24px 20px; overflow-y: auto; }
.quiz-q-counter {
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--t3);
  margin-bottom: 8px;
}
.quiz-q-text {
  font-family: var(--font-display);
  font-size: 18px;
  font-weight: 800;
  color: var(--t1);
  line-height: 1.35;
  margin-bottom: 20px;
}

.quiz-options-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
}

.quiz-opt-btn {
  background: #ffffff;
  border: 1.5px solid var(--border);
  border-radius: var(--radius-md);
  padding: 14px 16px;
  text-align: left;
  font-family: var(--font-body);
  font-size: 14px;
  font-weight: 600;
  color: var(--t1);
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 12px;
}
.quiz-opt-btn:hover:not(:disabled) {
  border-color: #94a3b8;
  background: #f8fafc;
}
.quiz-opt-letter {
  width: 26px;
  height: 26px;
  border-radius: 6px;
  background: var(--bg-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 800;
  color: var(--t3);
  flex-shrink: 0;
}

/* Correct/Wrong Option States */
.quiz-opt-btn.opt-correct {
  background: var(--success-bg) !important;
  border-color: var(--success) !important;
  color: #065f46 !important;
}
.quiz-opt-btn.opt-correct .quiz-opt-letter {
  background: var(--success) !important;
  color: #ffffff !important;
}
.quiz-opt-btn.opt-wrong {
  background: var(--error-bg) !important;
  border-color: var(--error) !important;
  color: #991b1b !important;
  animation: shake 0.3s ease;
}
.quiz-opt-btn.opt-wrong .quiz-opt-letter {
  background: var(--error) !important;
  color: #ffffff !important;
}
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-4px); }
  75% { transform: translateX(4px); }
}

.quiz-feedback-box {
  display: none;
  padding: 12px 16px;
  border-radius: var(--radius-md);
  margin-bottom: 16px;
  font-size: 13.5px;
  font-weight: 700;
}
.quiz-feedback-box.correct-fb {
  display: block;
  background: var(--success-bg);
  color: #065f46;
  border: 1px solid #a7f3d0;
}
.quiz-feedback-box.wrong-fb {
  display: block;
  background: var(--error-bg);
  color: #b91c1c;
  border: 1px solid #fecaca;
}

.quiz-modal-footer {
  padding: 14px 20px;
  background: var(--bg-subtle);
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.btn-quiz-next {
  padding: 10px 24px;
  border-radius: var(--radius-full);
  font-size: 14px;
  font-weight: 800;
  color: #ffffff;
  background: #2563eb;
  border: none;
  cursor: pointer;
  display: none;
}
.btn-quiz-next.show { display: inline-flex; align-items: center; gap: 6px; }

/* Finished View */
.quiz-finished-view { text-align: center; padding: 30px 10px; }
.quiz-finished-emoji { font-size: 48px; margin-bottom: 12px; }
.quiz-finished-score {
  font-family: var(--font-display);
  font-size: 26px;
  font-weight: 900;
  color: var(--t1);
  margin-bottom: 6px;
}
.quiz-finished-msg { font-size: 14px; color: var(--t2); margin-bottom: 24px; }
.btn-continue-topic {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 28px;
  border-radius: var(--radius-full);
  font-size: 15px;
  font-weight: 800;
  color: #ffffff;
  background: linear-gradient(135deg, #10b981, #059669);
  border: none;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35);
  transition: all 0.2s;
}
.btn-continue-topic:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.45);
}

/* ==========================================================================
   SEARCH MODAL
   ========================================================================== */
.search-modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 2000;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(8px);
  display: none;
  align-items: flex-start;
  justify-content: center;
  padding: 60px 16px 20px;
}
.search-modal-backdrop.open { display: flex; }
.search-dialog {
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  width: 100%;
  max-width: 580px;
  box-shadow: var(--shadow-lg);
  overflow: hidden;
}
.search-input-box {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 18px;
  border-bottom: 1px solid var(--border);
}
.search-input {
  border: none;
  outline: none;
  font-size: 15px;
  font-family: inherit;
  width: 100%;
  color: var(--t1);
}
.search-results-list { max-height: 360px; overflow-y: auto; padding: 8px; }
.s-res-card {
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: background 0.15s;
}
.s-res-card:hover { background: var(--bg-subtle); }
.s-res-t { font-weight: 800; font-size: 13.5px; color: var(--t1); }
.s-res-d { font-size: 12px; color: var(--t3); margin-top: 2px; }

</style>
</head>
<body class="mode-is-summary">

  <!-- ==========================================================================
       TOP GLOBAL HEADER
       ========================================================================== -->
  <header class="top-bar">
    <div class="top-bar-inner">
      <div class="brand" onclick="switchChannel('landing')">
        <div class="brand-badge">&#127891;</div>
        <div class="brand-text">MUJIB <span>Reviewer</span></div>
      </div>

      <!-- Quick Mode Switcher in Header -->
      <div class="top-center-mode">
        <button class="mode-btn active-mode mode-summary" id="topBtnSummary" onclick="setReviewerMode('summary')">
          <span>&#9889;</span> Short Summary
        </button>
        <button class="mode-btn mode-detailed" id="topBtnDetailed" onclick="setReviewerMode('detailed')">
          <span>&#128214;</span> Long Detailed
        </button>
      </div>

      <!-- Desktop Channel Navigation -->
      <nav class="desktop-pills">
        <button class="dpill active-hub" id="dpill-landing" onclick="switchChannel('landing')">&#127968; Hub</button>
        <button class="dpill" id="dpill-mk" onclick="switchChannel('mk')">&#128483;&#65039; MabKom</button>
        <button class="dpill" id="dpill-gs" onclick="switchChannel('gs')">&#128300; Science</button>
        <button class="dpill" id="dpill-gm" onclick="switchChannel('gm')">&#128208; Gen Math</button>
        <button class="dpill" id="dpill-fn" onclick="switchChannel('fn')">&#129513; Finite Math</button>
      </nav>

      <div class="top-actions">
        <button class="btn-search" onclick="openSearch()">
          <span>&#128269; Search...</span>
        </button>
      </div>
    </div>
  </header>

  <!-- ==========================================================================
       MOBILE BOTTOM NAVIGATION
       ========================================================================== -->
  <nav class="mobile-bottom-nav">
    <button class="mob-tab active-tab" id="mtab-landing" onclick="switchChannel('landing')">
      <span class="mob-tab-icon">&#127968;</span>
      <span class="mob-tab-lbl">Hub</span>
    </button>
    <button class="mob-tab" id="mtab-mk" onclick="switchChannel('mk')">
      <span class="mob-tab-icon">&#128483;&#65039;</span>
      <span class="mob-tab-lbl">MabKom</span>
    </button>
    <button class="mob-tab" id="mtab-gs" onclick="switchChannel('gs')">
      <span class="mob-tab-icon">&#128300;</span>
      <span class="mob-tab-lbl">Science</span>
    </button>
    <button class="mob-tab" id="mtab-gm" onclick="switchChannel('gm')">
      <span class="mob-tab-icon">&#128208;</span>
      <span class="mob-tab-lbl">Gen Math</span>
    </button>
    <button class="mob-tab" id="mtab-fn" onclick="switchChannel('fn')">
      <span class="mob-tab-icon">&#129513;</span>
      <span class="mob-tab-lbl">Finite</span>
    </button>
  </nav>

  <!-- ==========================================================================
       VIEW 0: LANDING PAGE & TOPIC SELECTOR (WITH 2 CHOICES)
       ========================================================================== -->
  <div class="view-container active-view" id="view-landing">
    <section class="hero">
      <div class="hero-pill">&#10024; Summative Reviewer Portal</div>
      <h1 class="hero-title">Master Your <span class="grad-text">Summatives</span></h1>
      <p class="hero-subtitle">
        Choose your preferred study depth below, then pick a subject channel to start reviewing.
      </p>

      <!-- The Two Reviewer Choices (Detailed vs. Summary) -->
      <div class="mode-choice-container">
        <!-- Choice 1: Short Summary -->
        <div class="mode-card card-summary selected-mode-card" id="landingCardSummary" onclick="setReviewerMode('summary')">
          <span class="mode-card-badge">&#9889; Fast Review</span>
          <h3 class="mode-card-title">Short Reviewer (SUMMARY)</h3>
          <p class="mode-card-desc">
            High-yield keywords, flashcards, essential formula cheatsheets, and quick visual infographics.
          </p>
        </div>

        <!-- Choice 2: Long Detailed -->
        <div class="mode-card card-detailed" id="landingCardDetailed" onclick="setReviewerMode('detailed')">
          <span class="mode-card-badge">&#128214; In-Depth Mastery</span>
          <h3 class="mode-card-title">Long Reviewer (DETAILED)</h3>
          <p class="mode-card-desc">
            Complete lessons, deep explanations, step-by-step math problems, Tagalog context, and full question banks.
          </p>
        </div>
      </div>
    </section>

    <main class="landing-grid-container">
      <div class="section-head">
        <h2>Choose a Subject Channel</h2>
        <p>Tap a topic card to enter its channel</p>
      </div>

      <div class="topics-grid">
        <!-- 1. MabKom -->
        <div class="subject-card card-mk" onclick="switchChannel('mk')">
          <div>
            <div class="card-top">
              <div class="card-icon-box">&#128483;&#65039;</div>
              <span class="card-badge">Aralin 3 &amp; 4</span>
            </div>
            <h3 class="card-title">Mabisang Komunikasyon</h3>
            <p class="card-desc">
              5 Elemento ng komunikasyon, Intrapersonal (Diary/Journal), Digital Identity, Netiquette, 2FA, Kamalayang Kultural, at Sensibilidad.
            </p>
            <div class="keyword-chips">
              <span class="kw-chip">#5Elemento</span>
              <span class="kw-chip">#Netiquette</span>
              <span class="kw-chip">#ActiveFootprint</span>
              <span class="kw-chip">#KamalayangKultural</span>
            </div>
          </div>
          <div class="card-bottom">
            <span class="btn-open-channel">Buksan ang Channel &#8594;</span>
            <span style="font-size:12px;color:var(--t3);font-weight:600;">2 Quizzes Available</span>
          </div>
        </div>

        <!-- 2. Science -->
        <div class="subject-card card-gs" onclick="switchChannel('gs')">
          <div>
            <div class="card-top">
              <div class="card-icon-box">&#128300;</div>
              <span class="card-badge">Weeks 5 &amp; 6</span>
            </div>
            <h3 class="card-title">General Science</h3>
            <p class="card-desc">
              6 Simple machines, Lever classes (F-L-E), Mechanical Advantage (IMA/AMA), Compound machines, Pascal's Principle, Hydraulics, and Archimedes' Principle.
            </p>
            <div class="keyword-chips">
              <span class="kw-chip">#Levers</span>
              <span class="kw-chip">#MA=Load/Effort</span>
              <span class="kw-chip">#PascalPrinciple</span>
              <span class="kw-chip">#BuoyantForce</span>
            </div>
          </div>
          <div class="card-bottom">
            <span class="btn-open-channel">Open Science Channel &#8594;</span>
            <span style="font-size:12px;color:var(--t3);font-weight:600;">2 Quizzes Available</span>
          </div>
        </div>

        <!-- 3. Gen Math -->
        <div class="subject-card card-gm" onclick="switchChannel('gm')">
          <div>
            <div class="card-top">
              <div class="card-icon-box">&#128208;</div>
              <span class="card-badge">Weeks 6, 7 &amp; 8</span>
            </div>
            <h3 class="card-title">General Mathematics</h3>
            <p class="card-desc">
              Business percentages, mark-up, mark-down, Simple interest (I=Prt), Nature symmetry, Fibonacci sequence, Arithmetic and Geometric sequences.
            </p>
            <div class="keyword-chips">
              <span class="kw-chip">#Markup</span>
              <span class="kw-chip">#SimpleInterest</span>
              <span class="kw-chip">#Fibonacci</span>
              <span class="kw-chip">#ArithmeticSeq</span>
            </div>
          </div>
          <div class="card-bottom">
            <span class="btn-open-channel">Open Math Channel &#8594;</span>
            <span style="font-size:12px;color:var(--t3);font-weight:600;">2 Quizzes Available</span>
          </div>
        </div>

        <!-- 4. Finite Math -->
        <div class="subject-card card-fn" onclick="switchChannel('fn')">
          <div>
            <div class="card-top">
              <div class="card-icon-box">&#129513;</div>
              <span class="card-badge">Lessons 3 &ndash; 7</span>
            </div>
            <h3 class="card-title">Finite Mathematics 1</h3>
            <p class="card-desc">
              Escher tessellations, 7 frieze patterns, Golden Ratio (&Phi; ≈ 1.618), Fractals (Sierpinski self-similarity), Matrix dimensions, and Matrix multiplication.
            </p>
            <div class="keyword-chips">
              <span class="kw-chip">#Tessellations</span>
              <span class="kw-chip">#Phi=1.618</span>
              <span class="kw-chip">#Fractals</span>
              <span class="kw-chip">#MatrixMult</span>
            </div>
          </div>
          <div class="card-bottom">
            <span class="btn-open-channel">Open Finite Channel &#8594;</span>
            <span style="font-size:12px;color:var(--t3);font-weight:600;">2 Quizzes Available</span>
          </div>
        </div>
      </div>
    </main>
  </div>

  <!-- ==========================================================================
       VIEW 1: MABISANG KOMUNIKASYON CHANNEL
       ========================================================================== -->
  <div class="view-container" id="view-mk">
    <div class="channel-top-bar">
      <button class="ch-back-link" onclick="switchChannel('landing')">&#8592; Topics Hub</button>
      <div class="ch-heading">&#128483;&#65039; Mabisang Komunikasyon</div>
      <div></div>
    </div>

    <main class="channel-container">
      <div class="subj-header-card mk">
        <div class="shc-badge mk">&#128218; Filipino &middot; Aralin 3 &amp; 4</div>
        <h2 class="shc-title">Mabisang Komunikasyon Reviewer</h2>
        <p class="shc-desc">Pagpapahayag ng ideya, intrapersonal, digital safety, proseso at kamalayang kultural.</p>
      </div>

      <!-- Sample Visual Diagram -->
      <div class="diagram-card">
        <img src="./assets/images/communication_netiquette.jpg" alt="Elements of Communication and Netiquette Tips" loading="lazy"/>
        <div class="diagram-caption">&#128204; <strong>Visual Infographic:</strong> 5 Elemento ng Komunikasyon &amp; Netiquette Safety Guide</div>
      </div>

      <!-- LESSON 1 -->
      <section class="lesson-card" id="lesson-mk-a3">
        <div class="lesson-head">
          <div class="lesson-num mk">A3</div>
          <div class="lesson-title">Aralin 3: Malinaw na Pagpapahayag at Digital Identity</div>
        </div>

        <!-- SUMMARY CONTENT -->
        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword mk">Tagapagpadala (Sender)</div><div class="c-meaning">Pinagmumulan ng mensahe o impormasyon.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Mensahe (Message)</div><div class="c-meaning">Ideya, impormasyon, o damdaming nais iparating.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Daluyan (Channel)</div><div class="c-meaning">Paraan ng pagpapadala (pasalita, pasulat, online/chat).</div></div>
            <div class="concept-item"><div class="c-keyword mk">Tagatanggap (Receiver)</div><div class="c-meaning">Tumatanggap at nag-iinterpret sa mensahe.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Tugon (Feedback)</div><div class="c-meaning">Sagot o reaksyon upang matiyak ang pagkakaunawaan.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Intrapersonal</div><div class="c-meaning">Talaarawan (Diary), Dyornal (sistematiko), Repleksyon, Goal Setting.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Active Footprint</div><div class="c-meaning">Kusang ibinabahagi online (post, photos, comments).</div></div>
            <div class="concept-item"><div class="c-keyword mk">Passive Footprint</div><div class="c-meaning">Awtomatikong nakokolekta (cookies, browsing history).</div></div>
            <div class="concept-item"><div class="c-keyword mk">Netiquette</div><div class="c-meaning">Wastong asal online: magalang, iwas fake news, mag-isip bago mag-post.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Public-Facing</div><div class="c-meaning">Blog, Komentaryo, Advocacy &rarr; Inclusivity, Equality, Social Awareness.</div></div>
          </div>
        </div>

        <!-- DETAILED CONTENT -->
        <div class="mode-detailed-content">
          <div class="detailed-section">
            <h4 class="det-subtitle">1. Kahulugan at Elemento ng Komunikasyon</h4>
            <p class="det-p">
              Ang <strong>komunikasyon</strong> ay ang proseso ng pagpapadala, pagtanggap, at pagpapalitan ng impormasyon, ideya, damdamin, opinyon, at mensahe sa pagitan ng dalawa o higit pang tao upang magkaroon ng pagkakaunawaan at mabuting ugnayan.
            </p>
            <ul class="det-list">
              <li><strong>Tagapagpadala (Sender):</strong> Ang nagpapadala at pinagmumulan ng mensahe.</li>
              <li><strong>Mensahe (Message):</strong> Ang impormasyon, kaisipan, o damdaming nais iparating.</li>
              <li><strong>Daluyan (Channel):</strong> Ang paraan o midyum ng pagpapadala (pasalita, pasulat, online/chat).</li>
              <li><strong>Tagatanggap (Receiver):</strong> Ang tumatanggap at nagpoproseso sa mensahe.</li>
              <li><strong>Tugon (Feedback):</strong> Ang sagot o reaksyon ng tagatanggap na nagpapatunay kung naunawaan ang mensahe.</li>
            </ul>

            <h4 class="det-subtitle">2. Anyo ng Personal at Interpersonal na Pagpapahayag</h4>
            <ul class="det-list">
              <li><strong>Pagtatanong:</strong> Paraan ng pagkuha ng impormasyon o paghingi ng linaw (hal. <em>"Ano po ang takdang-aralin?"</em>).</li>
              <li><strong>Pagkukuwento:</strong> Pagsasalaysay ng karanasan upang magbahagi ng impormasyon o magbigay-aliw.</li>
              <li><strong>Paglalahad ng Obserbasyon:</strong> Pagbibigay ng impormasyon batay sa nakita o narinig <strong>nang hindi agad nagbibigay ng sariling paghuhusga</strong>.</li>
              <li><strong>Pagpapahayag ng Opinyon:</strong> Pagbibigay ng sariling pananaw nang may paggalang at batayan.</li>
            </ul>

            <h4 class="det-subtitle">3. Intrapersonal na Komunikasyon</h4>
            <p class="det-p">Pakikipag-usap sa sarili upang mas makilala ang sarili at makagawa ng matalinong desisyon:</p>
            <ul class="det-list">
              <li><strong>Talaarawan (Diary):</strong> Personal na talaan ng mga pang-araw-araw na karanasan at damdamin.</li>
              <li><strong>Dyornal (Journal):</strong> Mas sistematikong pagsulat ng mga natutuhan, obserbasyon, at pagninilay.</li>
              <li><strong>Repleksyon (Reflection):</strong> Malalim na pagninilay sa sariling kilos at desisyon.</li>
              <li><strong>Goal Setting:</strong> Pagtatakda ng malinaw na layunin sa hinaharap.</li>
            </ul>

            <h4 class="det-subtitle">4. Digital Identity, Netiquette at Proteksyon sa Datos</h4>
            <div class="det-example-box mk">
              <strong>Active Footprint:</strong> Kusang ipinost (status, videos, comments).<br>
              <strong>Passive Footprint:</strong> Awtomatikong nakolekta ng web browsers (cookies, history, IP location).<br>
              <strong>Netiquette:</strong> Mag-isip bago mag-post, iwas cyberbullying, gumamit ng 2FA (Two-Factor Authentication) at malakas na password.
            </div>

            <h4 class="det-subtitle">5. Public-Facing Texts at Layuning Panlipunan</h4>
            <p class="det-p">Mga tekstong para sa madla (Blog, Komentaryo, Advocacy Post, Maikling Kolumn) na nagtataguyod ng:</p>
            <ul class="det-list">
              <li><strong>Inclusivity:</strong> Pantay na paggalang at pagtanggap sa lahat anuman ang kasarian, edad, o kultura.</li>
              <li><strong>Equality:</strong> Pantay na karapatan at pagtrato nang walang diskriminasyon.</li>
              <li><strong>Social Awareness:</strong> Pagkilala at paglahok sa paghahanap ng solusyon sa mga isyung panlipunan.</li>
            </ul>
          </div>
        </div>

        <div class="quiz-cta-box">
          <div class="quiz-cta-info">
            <h4>Ready to test Aralin 3?</h4>
            <p>5 Quick Multiple Choice questions to test your recall.</p>
          </div>
          <button class="btn-start-quiz mk" onclick="startLessonQuiz('mk-a3')">🎯 Answer Quiz (5 Qs)</button>
        </div>
      </section>

      <!-- LESSON 2 -->
      <section class="lesson-card" id="lesson-mk-a4">
        <div class="lesson-head">
          <div class="lesson-num mk">A4</div>
          <div class="lesson-title">Aralin 4: Proseso at Kamalayang Kultural</div>
        </div>

        <!-- SUMMARY CONTENT -->
        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword mk">Dinamikong Proseso</div><div class="c-meaning">Tuloy-tuloy at interaktibo; bumubuo ng relasyon at lumulutas ng suliranin.</div></div>
            <div class="concept-item"><div class="c-keyword mk">3 Proseso</div><div class="c-meaning">1. Pagbibigay-kahulugan (Decoding), 2. Pakikilahok (Participation), 3. Pagpapahayag.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Konteksto at Noise</div><div class="c-meaning">Lugar, oras, sitwasyon; Hadlang (Noise) = ingay, mahinang signal, emosyon.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Kamalayang Kultural</div><div class="c-meaning">Pag-unawa sa tradisyon (hal. paggamit ng "po" at "opo").</div></div>
            <div class="concept-item"><div class="c-keyword mk">Sensibilidad</div><div class="c-meaning">Pag-iisip sa damdamin ng kausap (<em>"Mayroon akong ibang pananaw"</em>).</div></div>
          </div>
        </div>

        <!-- DETAILED CONTENT -->
        <div class="mode-detailed-content">
          <div class="detailed-section">
            <h4 class="det-subtitle">1. Ang Dinamikong Kalikasan ng Komunikasyon</h4>
            <p class="det-p">
              Ang komunikasyon ay hindi lamang simpleng pagpapalitan ng impormasyon. Ito ay dinamiko, tuloy-tuloy, at interaktibo kung saan nabubuo ang relasyon, naipapahayag ang damdamin, at nalulutas ang mga suliranin.
            </p>
            <div class="det-example-box mk">
              <strong>Halimbawa ng Lalim ng Mensahe:</strong> Kapag sinabi ng Nanay <em>"Umuwi ka nang maaga"</em>, hindi lamang ito utos &mdash; nagpapakita ito ng kaniyang pag-aalala sa iyong kaligtasan.
            </div>

            <h4 class="det-subtitle">2. Tatlong Mahahalagang Proseso</h4>
            <ul class="det-list">
              <li><strong>1. Pagbibigay-kahulugan (Decoding):</strong> Pag-unawa sa mensahe batay sa sariling karanasan, emosyon, at kultura. Halimbawa, ang chat na <code>"Okay."</code> ay maaaring mangahulugang sang-ayon, galit, o pagod depende sa konteksto.</li>
              <li><strong>2. Pakikilahok (Active Participation):</strong> Hindi lamang pagsasalita, kundi aktibong pakikinig, pagtatanong, at pakikiisa sa talakayan.</li>
              <li><strong>3. Pagpapahayag (Expression):</strong> Malinaw na pagbabahagi gamit ang salita, kilos, at ekspresyon ng mukha.</li>
            </ul>

            <h4 class="det-subtitle">3. Apat na Konteksto ng Komunikasyon</h4>
            <ul class="det-list">
              <li><strong>Personal (Intrapersonal):</strong> Pakikipag-usap sa sarili.</li>
              <li><strong>Interpersonal:</strong> Pakikipag-usap sa kapwa o kaibigan.</li>
              <li><strong>Sosyal:</strong> Komunikasyon sa loob ng pangkat o komunidad.</li>
              <li><strong>Kultural:</strong> Isinasaalang-alang ang kultura at paniniwala.</li>
            </ul>

            <h4 class="det-subtitle">4. Kamalayang Kultural at Sensibilidad</h4>
            <p class="det-p">
              <strong>Kamalayang Kultural:</strong> Pag-unawa na magkakaiba ang kaugalian ng mga tao (hal. ang "po" at "opo" sa Pilipinas).<br>
              <strong>Sensibilidad sa Komunikasyon:</strong> Pag-iisip muna bago magsalita upang hindi makasakit (hal. sa halip na <em>"Mali ka!"</em>, sabihing <em>"Mayroon akong ibang pananaw ukol diyan"</em>).
            </p>
          </div>
        </div>

        <div class="quiz-cta-box">
          <div class="quiz-cta-info">
            <h4>Ready to test Aralin 4?</h4>
            <p>5 Quick Multiple Choice questions to test your recall.</p>
          </div>
          <button class="btn-start-quiz mk" onclick="startLessonQuiz('mk-a4')">🎯 Answer Quiz (5 Qs)</button>
        </div>
      </section>
    </main>
  </div>

  <!-- ==========================================================================
       VIEW 2: GENERAL SCIENCE CHANNEL
       ========================================================================== -->
  <div class="view-container" id="view-gs">
    <div class="channel-top-bar">
      <button class="ch-back-link" onclick="switchChannel('landing')">&#8592; Topics Hub</button>
      <div class="ch-heading">&#128300; General Science</div>
      <div></div>
    </div>

    <main class="channel-container">
      <div class="subj-header-card gs">
        <div class="shc-badge gs">&#9889; Science &middot; Weeks 5 &amp; 6</div>
        <h2 class="shc-title">General Science Reviewer</h2>
        <p class="shc-desc">Simple &amp; compound machines, mechanical advantage, Pascal's &amp; Archimedes' principles.</p>
      </div>

      <!-- Sample Visual Diagram -->
      <div class="diagram-card">
        <img src="./assets/images/simple_machines.jpg" alt="Simple Machines Types" loading="lazy"/>
        <div class="diagram-caption">&#128204; <strong>Visual Infographic:</strong> The 6 Simple Machines &amp; Force Trade-offs</div>
      </div>

      <!-- LESSON 1 -->
      <section class="lesson-card" id="lesson-gs-w5simple">
        <div class="lesson-head">
          <div class="lesson-num gs">W5</div>
          <div class="lesson-title">Week 5: Simple Machines &amp; Mechanical Advantage</div>
        </div>

        <!-- SUMMARY CONTENT -->
        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gs">Work Conservation</div><div class="c-meaning">W = F x d. Simple machines do <strong>NOT reduce total work</strong>; they reduce effort force by increasing distance.</div></div>
            <div class="concept-item"><div class="c-keyword gs">1st Class Lever</div><div class="c-meaning"><strong>Fulcrum middle</strong> (Seesaw, crowbar, scissors). Redirects &amp; multiplies force.</div></div>
            <div class="concept-item"><div class="c-keyword gs">2nd Class Lever</div><div class="c-meaning"><strong>Load middle</strong> (Wheelbarrow, nutcracker). Always <strong>MA &gt; 1</strong>.</div></div>
            <div class="concept-item"><div class="c-keyword gs">3rd Class Lever</div><div class="c-meaning"><strong>Effort middle</strong> (Tweezers, fishing rod, broom). <strong>MA &lt; 1</strong> (multiplies speed).</div></div>
            <div class="concept-item"><div class="c-keyword gs">Pulleys</div><div class="c-meaning"><strong>Fixed:</strong> MA=1. <strong>Movable:</strong> MA=2. <strong>Block &amp; Tackle:</strong> MA = number of supporting rope segments.</div></div>
            <div class="concept-item"><div class="c-keyword gs">Inclined Plane</div><div class="c-meaning">IMA = Length / Height. Wedge &amp; Screw are derived from inclined planes.</div></div>
          </div>
        </div>

        <!-- DETAILED CONTENT -->
        <div class="mode-detailed-content">
          <div class="detailed-section">
            <h4 class="det-subtitle">1. Principles of Simple Machines &amp; Work</h4>
            <p class="det-p">
              A <strong>simple machine</strong> changes the direction or magnitude of a force. It makes work easier by decreasing the effort force needed &mdash; but it <strong>never reduces the total work done</strong> (\(W = F \times d\)). Less force requires moving over a greater distance.
            </p>
            <ul class="det-list">
              <li><strong>Mechanical Advantage (MA):</strong> \(MA = \frac{\text{Load Force}}{\text{Effort Force}}\). If \(MA > 1\), it multiplies force. If \(MA < 1\), it multiplies speed.</li>
              <li><strong>IMA (Ideal):</strong> Calculated from distances assuming zero friction: \(IMA = \frac{d_{\text{effort}}}{d_{\text{load}}}\).</li>
              <li><strong>AMA (Actual):</strong> Calculated from real measured forces with friction: \(AMA = \frac{F_{\text{load}}}{F_{\text{effort}}}\).</li>
              <li><strong>Efficiency:</strong> \(\text{Efficiency} = \left(\frac{AMA}{IMA}\right) \times 100\%\) (always \(< 100\%\) in real machines).</li>
            </ul>

            <h4 class="det-subtitle">2. The Three Classes of Levers</h4>
            <div class="det-example-box gs">
              <strong>1st Class (Fulcrum in the Middle):</strong> Effort &mdash; Fulcrum &mdash; Load. Ex: Seesaw, scissors, crowbar, pliers.<br>
              <strong>2nd Class (Load in the Middle):</strong> Fulcrum &mdash; Load &mdash; Effort. Always \(MA > 1\). Ex: Wheelbarrow, nutcracker, bottle opener.<br>
              <strong>3rd Class (Effort in the Middle):</strong> Fulcrum &mdash; Effort &mdash; Load. \(MA < 1\); multiplies speed &amp; range. Ex: Tweezers, fishing rod, baseball bat, broom.
            </div>

            <h4 class="det-subtitle">3. Wheel and Axle, Pulleys, and Inclined Planes</h4>
            <ul class="det-list">
              <li><strong>Wheel and Axle:</strong> Two concentric circular objects. \(IMA = \frac{R_{\text{wheel}}}{R_{\text{axle}}}\) (Doorknob, steering wheel, screwdriver).</li>
              <li><strong>Fixed Pulley:</strong> Attached to a support; changes force direction only (\(MA = 1\)).</li>
              <li><strong>Movable Pulley:</strong> Attached to the load; multiplies force (\(MA = 2\)).</li>
              <li><strong>Block and Tackle:</strong> Combination of fixed and movable pulleys; \(MA =\) number of supporting rope strands.</li>
              <li><strong>Inclined Plane (Ramp):</strong> Flat sloped surface. \(IMA = \frac{\text{Length}}{\text{Height}}\).</li>
              <li><strong>Wedge:</strong> Two inclined planes back-to-back (Axe, knife, chisel).</li>
              <li><strong>Screw:</strong> Inclined plane wrapped around a cylinder; finer threads \(=\) higher MA.</li>
            </ul>
          </div>
        </div>

        <div class="formula-box">
          <div class="formula-label">Key Formulas</div>
          MA = Load Force / Effort Force<br>
          IMA (Ramp) = Length / Height<br>
          Efficiency = (AMA / IMA) x 100%
        </div>

        <div class="quiz-cta-box">
          <div class="quiz-cta-info">
            <h4>Ready to test Simple Machines?</h4>
            <p>5 Quick Multiple Choice questions to test your recall.</p>
          </div>
          <button class="btn-start-quiz gs" onclick="startLessonQuiz('gs-w5simple')">🎯 Answer Quiz (5 Qs)</button>
        </div>
      </section>

      <!-- LESSON 2 -->
      <section class="lesson-card" id="lesson-gs-w6pascal">
        <div class="lesson-head">
          <div class="lesson-num gs">W6</div>
          <div class="lesson-title">Week 6: Compound Machines, Pascal &amp; Archimedes</div>
        </div>

        <!-- Sample Visual Diagram 2 -->
        <div class="diagram-card">
          <img src="./assets/images/pascal_archimedes.jpg" alt="Pascal and Archimedes Principles" loading="lazy"/>
          <div class="diagram-caption">&#128204; <strong>Visual Infographic:</strong> Hydraulic Lift Mechanics &amp; Buoyant Force</div>
        </div>

        <!-- SUMMARY CONTENT -->
        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gs">Compound Machine</div><div class="c-meaning">Two or more simple machines combined: <strong>MA_total = MA1 x MA2 x ...</strong> (Scissors, bicycle, can opener).</div></div>
            <div class="concept-item"><div class="c-keyword gs">Pascal's Principle</div><div class="c-meaning">Pressure applied to enclosed fluid is transmitted <strong>undiminished in all directions</strong> (F1/A1 = F2/A2).</div></div>
            <div class="concept-item"><div class="c-keyword gs">Archimedes' Principle</div><div class="c-meaning">Buoyant Force (Fb) = <strong>Weight of fluid displaced</strong> by submerged object.</div></div>
            <div class="concept-item"><div class="c-keyword gs">Floating / Sinking</div><div class="c-meaning"><strong>Floats:</strong> Fb &ge; Weight (Density &le; fluid). <strong>Sinks:</strong> Fb &lt; Weight.</div></div>
          </div>
        </div>

        <!-- DETAILED CONTENT -->
        <div class="mode-detailed-content">
          <div class="detailed-section">
            <h4 class="det-subtitle">1. Compound Machines &amp; Combined Advantage</h4>
            <p class="det-p">
              A <strong>compound machine</strong> links two or more simple machines so the output of one becomes the input of the next. Total mechanical advantage is the product:
              \[MA_{\text{total}} = MA_1 \times MA_2 \times MA_3 \dots\]
              <em>Trade-off:</em> More moving parts produce more friction, resulting in lower efficiency than individual simple machines.
            </p>

            <h4 class="det-subtitle">2. Pascal's Principle &amp; Hydraulic Systems</h4>
            <p class="det-p">
              <strong>Pascal's Principle:</strong> Pressure applied to an enclosed static fluid is transmitted undiminished to every portion of the fluid and container walls:
              \[P_1 = P_2 \implies \frac{F_1}{A_1} = \frac{F_2}{A_2} \implies F_2 = F_1 \times \left(\frac{A_2}{A_1}\right)\]
              A small force applied to a small piston creates a large lifting force on a large piston (used in hydraulic car lifts and automotive brakes).
            </p>

            <h4 class="det-subtitle">3. Archimedes' Principle &amp; Buoyancy</h4>
            <p class="det-p">
              <strong>Archimedes' Principle:</strong> Any object submerged in a fluid experiences an upward buoyant force equal to the weight of the fluid displaced:
              \[F_b = \rho_{\text{fluid}} \times V_{\text{submerged}} \times g = \text{Weight}_{\text{displaced fluid}}\]
            </p>
            <ul class="det-list">
              <li><strong>Floating:</strong> If \(F_b \ge F_g\) (\(\rho_{\text{object}} \le \rho_{\text{fluid}}\)), the object floats on the surface.</li>
              <li><strong>Sinking:</strong> If \(F_b < F_g\) (\(\rho_{\text{object}} > \rho_{\text{fluid}}\)), the object sinks to the bottom.</li>
              <li><strong>Applications:</strong> Steel ships float because their hollow hull displaces a huge volume of water, generating buoyant force greater than their total weight. Submarines use ballast tanks to control density.</li>
            </ul>
          </div>
        </div>

        <div class="formula-box">
          <div class="formula-label">Key Formulas</div>
          Pascal: F1 / A1 = F2 / A2  &rarr;  F2 = F1 x (A2 / A1)<br>
          Buoyant Force: Fb = &rho; x V x g = Weight_displaced
        </div>

        <div class="quiz-cta-box">
          <div class="quiz-cta-info">
            <h4>Ready to test Pascal &amp; Archimedes?</h4>
            <p>5 Quick Multiple Choice questions to test your recall.</p>
          </div>
          <button class="btn-start-quiz gs" onclick="startLessonQuiz('gs-w6pascal')">🎯 Answer Quiz (5 Qs)</button>
        </div>
      </section>
    </main>
  </div>

  <!-- ==========================================================================
       VIEW 3: GENERAL MATHEMATICS CHANNEL
       ========================================================================== -->
  <div class="view-container" id="view-gm">
    <div class="channel-top-bar">
      <button class="ch-back-link" onclick="switchChannel('landing')">&#8592; Topics Hub</button>
      <div class="ch-heading">&#128208; General Mathematics</div>
      <div></div>
    </div>

    <main class="channel-container">
      <div class="subj-header-card gm">
        <div class="shc-badge gm">&#128290; Math &middot; Weeks 6, 7 &amp; 8</div>
        <h2 class="shc-title">General Mathematics Reviewer</h2>
        <p class="shc-desc">Business percentages, mark-ups, simple interest, nature symmetry, and sequences.</p>
      </div>

      <!-- LESSON 1 -->
      <section class="lesson-card" id="lesson-gm-w6">
        <div class="lesson-head">
          <div class="lesson-num gm">W6</div>
          <div class="lesson-title">Week 6: Percentages in Business &amp; Finance</div>
        </div>

        <!-- SUMMARY CONTENT -->
        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gm">Mark-up</div><div class="c-meaning">Added to cost: <strong>Mark-up = Selling Price - Cost</strong>.</div></div>
            <div class="concept-item"><div class="c-keyword gm">Mark-down</div><div class="c-meaning">Discount: <strong>Sale Price = Regular Price - Discount</strong>.</div></div>
            <div class="concept-item"><div class="c-keyword gm">Simple Interest</div><div class="c-meaning"><strong>I = Prt</strong> (P = Principal, r = annual rate, t = time in years).</div></div>
            <div class="concept-item"><div class="c-keyword gm">Future Value</div><div class="c-meaning">Total sum: <strong>F = P + I = P(1 + rt)</strong>.</div></div>
          </div>
        </div>

        <!-- DETAILED CONTENT -->
        <div class="mode-detailed-content">
          <div class="detailed-section">
            <h4 class="det-subtitle">1. Mark-up, Mark-down and Pricing Strategies</h4>
            <p class="det-p">In business, prices are calculated to cover operating expenses and profit:</p>
            <ul class="det-list">
              <li><strong>Cost Price (C):</strong> Original purchase price of the item.</li>
              <li><strong>Selling Price (SP):</strong> Price at which the item is sold: \(SP = C + M\).</li>
              <li><strong>Mark-up (M):</strong> Amount added to cost: \(M = SP - C\).</li>
              <li><strong>Mark-up Rate on Cost:</strong> \(\text{Rate} = \left(\frac{M}{C}\right) \times 100\%\).</li>
              <li><strong>Mark-down (Discount, D):</strong> Reduction from original price: \(D = \text{Regular Price} \times \text{Discount Rate}\).</li>
              <li><strong>Sale Price:</strong> \(\text{Sale Price} = \text{Regular Price} - D\).</li>
            </ul>

            <h4 class="det-subtitle">2. Simple Interest and Financial Calculations</h4>
            <p class="det-p">
              <strong>Simple Interest (I):</strong> Fee paid for borrowing money or return on investment:
              \[I = P \cdot r \cdot t\]
              where \(P =\) Principal, \(r =\) annual interest rate (as decimal), \(t =\) time in years.
            </p>
            <div class="det-example-box gm">
              <strong>Example:</strong> Borrow ₱10,000 at 5% simple annual interest for 3 years.<br>
              \(I = 10,000 \times 0.05 \times 3 = ₱1,500\).<br>
              <strong>Future Value (Maturity Value):</strong> \(F = P + I = 10,000 + 1,500 = ₱11,500\).
            </div>
          </div>
        </div>

        <div class="formula-box">
          <div class="formula-label">Quick Calculation Cheatsheet</div>
          I = P x r x t<br>
          Mark-up Rate = (Mark-up / Cost) x 100%<br>
          F = P(1 + rt)
        </div>

        <div class="quiz-cta-box">
          <div class="quiz-cta-info">
            <h4>Ready to test Business Percentages?</h4>
            <p>5 Quick Multiple Choice questions to test your recall.</p>
          </div>
          <button class="btn-start-quiz gm" onclick="startLessonQuiz('gm-w6')">🎯 Answer Quiz (5 Qs)</button>
        </div>
      </section>

      <!-- LESSON 2 -->
      <section class="lesson-card" id="lesson-gm-w7w8">
        <div class="lesson-head">
          <div class="lesson-num gm">W7-8</div>
          <div class="lesson-title">Weeks 7 &amp; 8: Patterns in Nature &amp; Sequences</div>
        </div>

        <!-- Sample Visual Diagram -->
        <div class="diagram-card">
          <img src="./assets/images/fibonacci_fractals.jpg" alt="Fibonacci and Fractals in Nature" loading="lazy"/>
          <div class="diagram-caption">&#128204; <strong>Visual Infographic:</strong> Golden Ratio, Fibonacci Spiral &amp; Sierpinski Fractals</div>
        </div>

        <!-- SUMMARY CONTENT -->
        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gm">Fibonacci Sequence</div><div class="c-meaning">0, 1, 1, 2, 3, 5, 8, 13, 21, 34... Sum of previous two terms.</div></div>
            <div class="concept-item"><div class="c-keyword gm">Arithmetic Sequence</div><div class="c-meaning">Constant difference <strong>d</strong>: <strong>an = a1 + (n - 1)d</strong>.</div></div>
            <div class="concept-item"><div class="c-keyword gm">Geometric Sequence</div><div class="c-meaning">Constant ratio <strong>r</strong>: <strong>an = a1 x r^(n - 1)</strong>.</div></div>
            <div class="concept-item"><div class="c-keyword gm">Symmetry</div><div class="c-meaning"><strong>Bilateral:</strong> Mirror reflection. <strong>Radial:</strong> Rotational central axis.</div></div>
          </div>
        </div>

        <!-- DETAILED CONTENT -->
        <div class="mode-detailed-content">
          <div class="detailed-section">
            <h4 class="det-subtitle">1. Patterns in Life &amp; Nature</h4>
            <ul class="det-list">
              <li><strong>Symmetry:</strong> Bilateral (human face, butterfly) vs. Radial (starfish, sunflower florets).</li>
              <li><strong>Tessellations:</strong> Hexagonal honeycomb cells maximize volume with minimal wax.</li>
              <li><strong>Fibonacci Sequence:</strong> \(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55\dots\) found in sunflower seed spirals, pinecone scales, and nautilus shell chambers.</li>
            </ul>

            <h4 class="det-subtitle">2. Arithmetic and Geometric Sequences</h4>
            <div class="det-example-box gm">
              <strong>Arithmetic Sequence:</strong> Difference between consecutive terms is constant (\(d\)).<br>
              \(n\)-th term: \(a_n = a_1 + (n - 1)d\)<br>
              Sum of \(n\) terms: \(S_n = \frac{n}{2}(a_1 + a_n)\)<br><br>
              <strong>Geometric Sequence:</strong> Ratio between consecutive terms is constant (\(r\)).<br>
              \(n\)-th term: \(a_n = a_1 \cdot r^{n - 1}\)<br>
              Sum of \(n\) terms: \(S_n = \frac{a_1(1 - r^n)}{1 - r}\)
            </div>
          </div>
        </div>

        <div class="quiz-cta-box">
          <div class="quiz-cta-info">
            <h4>Ready to test Patterns &amp; Sequences?</h4>
            <p>5 Quick Multiple Choice questions to test your recall.</p>
          </div>
          <button class="btn-start-quiz gm" onclick="startLessonQuiz('gm-w7w8')">🎯 Answer Quiz (5 Qs)</button>
        </div>
      </section>
    </main>
  </div>

  <!-- ==========================================================================
       VIEW 4: FINITE MATHEMATICS 1 CHANNEL
       ========================================================================== -->
  <div class="view-container" id="view-fn">
    <div class="channel-top-bar">
      <button class="ch-back-link" onclick="switchChannel('landing')">&#8592; Topics Hub</button>
      <div class="ch-heading">&#129513; Finite Mathematics 1</div>
      <div></div>
    </div>

    <main class="channel-container">
      <div class="subj-header-card fn">
        <div class="shc-badge fn">&#128736;&#65039; Finite Math &middot; Lessons 3 &ndash; 7</div>
        <h2 class="shc-title">Finite Mathematics 1 Reviewer</h2>
        <p class="shc-desc">Tessellations, frieze groups, golden ratio, fractals, and matrix algebra.</p>
      </div>

      <!-- LESSON 1 -->
      <section class="lesson-card" id="lesson-fn-l3l4">
        <div class="lesson-head">
          <div class="lesson-num fn">L3-4</div>
          <div class="lesson-title">Lessons 3 &amp; 4: Tessellations &amp; Golden Ratio</div>
        </div>

        <!-- SUMMARY CONTENT -->
        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword fn">Tessellation (Tiling)</div><div class="c-meaning">Covering a 2D plane with shapes with <strong>no overlaps and no gaps</strong> (M.C. Escher art).</div></div>
            <div class="concept-item"><div class="c-keyword fn">4 Isometries</div><div class="c-meaning"><strong>Translation</strong> (slide), <strong>Reflection</strong> (flip), <strong>Rotation</strong> (turn), <strong>Glide Reflection</strong> (slide + flip).</div></div>
            <div class="concept-item"><div class="c-keyword fn">7 Frieze Patterns</div><div class="c-meaning">Exactly <strong>7 infinite 1D border symmetry groups</strong> describe all repeating band patterns.</div></div>
            <div class="concept-item"><div class="c-keyword fn">Golden Ratio (&Phi;)</div><div class="c-meaning"><strong>&Phi; = (1 + &radic;5)/2 &asymp; 1.6180339887</strong>. Ratio of consecutive Fibonacci numbers converges to &Phi;.</div></div>
          </div>
        </div>

        <!-- DETAILED CONTENT -->
        <div class="mode-detailed-content">
          <div class="detailed-section">
            <h4 class="det-subtitle">1. Tessellations and Frieze Patterns (Lesson 3)</h4>
            <p class="det-p">
              A <strong>tessellation</strong> is a pattern formed by repeating figures to cover a plane completely without any gaps or overlaps.
            </p>
            <ul class="det-list">
              <li><strong>4 Rigid Motions (Isometries):</strong> Translation (linear slide), Reflection (mirror flip), Rotation (turn about a center point), Glide Reflection (slide followed by reflection).</li>
              <li><strong>Frieze Patterns:</strong> An infinite border pattern repeating along a single direction. There are exactly <strong>7 distinct symmetry classes</strong> of frieze patterns.</li>
            </ul>

            <h4 class="det-subtitle">2. Golden Ratio &amp; Fibonacci (Lesson 4)</h4>
            <p class="det-p">
              The <strong>Golden Ratio (\(\phi\))</strong> is the unique positive number satisfying \(\frac{a+b}{a} = \frac{a}{b} = \phi\):
              \[\phi = \frac{1 + \sqrt{5}}{2} \approx 1.6180339887\]
            </p>
            <div class="det-example-box fn">
              <strong>Golden Rectangle:</strong> A rectangle whose side lengths are in the ratio \(1 : \phi \approx 1 : 1.618\). Subdividing it into squares creates the logarithmic Golden Spiral found in nature and classical architecture (Parthenon).
            </div>
          </div>
        </div>

        <div class="quiz-cta-box">
          <div class="quiz-cta-info">
            <h4>Ready to test Tessellations &amp; Golden Ratio?</h4>
            <p>5 Quick Multiple Choice questions to test your recall.</p>
          </div>
          <button class="btn-start-quiz fn" onclick="startLessonQuiz('fn-l3l4')">🎯 Answer Quiz (5 Qs)</button>
        </div>
      </section>

      <!-- LESSON 2 -->
      <section class="lesson-card" id="lesson-fn-l5l6l7">
        <div class="lesson-head">
          <div class="lesson-num fn">L5-7</div>
          <div class="lesson-title">Lessons 5, 6 &amp; 7: Fractals &amp; Matrix Algebra</div>
        </div>

        <!-- SUMMARY CONTENT -->
        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword fn">Fractals &amp; Self-Similarity</div><div class="c-meaning">Figures where every sub-part is a reduced-scale replica of the whole (Sierpinski, Mandelbrot).</div></div>
            <div class="concept-item"><div class="c-keyword fn">Matrix Order</div><div class="c-meaning">Size: <strong>rows x columns (m x n)</strong>.</div></div>
            <div class="concept-item"><div class="c-keyword fn">Matrix Addition</div><div class="c-meaning">Requires <strong>identical dimensions</strong> (add corresponding elements).</div></div>
            <div class="concept-item"><div class="c-keyword fn">Matrix Product Rule</div><div class="c-meaning"><strong>Columns of A = Rows of B</strong>: (m x k) • (k x n) = (m x n).</div></div>
          </div>
        </div>

        <!-- DETAILED CONTENT -->
        <div class="mode-detailed-content">
          <div class="detailed-section">
            <h4 class="det-subtitle">1. Fractals &amp; Self-Similarity (Lesson 5)</h4>
            <p class="det-p">
              A <strong>fractal</strong> is a complex geometric shape that exhibits <strong>self-similarity</strong> &mdash; zooming in at any scale reveals structural details resembling the overall object (Sierpinski Gasket, Koch Snowflake, Mandelbrot Set, fern leaves, coastlines).
            </p>

            <h4 class="det-subtitle">2. Matrix Fundamentals &amp; Operations (Lesson 6)</h4>
            <ul class="det-list">
              <li><strong>Order / Dimensions:</strong> Array of numbers arranged in \(m\) rows and \(n\) columns (\(m \times n\)).</li>
              <li><strong>Matrix Addition/Subtraction:</strong> Only possible when matrices have the exact same dimensions. Add/subtract corresponding entries: \((A + B)_{ij} = A_{ij} + B_{ij}\).</li>
              <li><strong>Scalar Multiplication:</strong> Multiply every entry by real number \(k\): \((kA)_{ij} = k \cdot A_{ij}\).</li>
            </ul>

            <h4 class="det-subtitle">3. Matrix Multiplication (Lesson 7)</h4>
            <div class="det-example-box fn">
              <strong>Inner Dimension Rule:</strong> Product \(AB\) exists if and only if the number of columns in \(A\) equals the number of rows in \(B\):
              \[[m \times k] \cdot [k \times n] = [m \times n]\]
              Each entry \(C_{ij}\) is the dot product of row \(i\) from Matrix A and column \(j\) from Matrix B. Note: Matrix multiplication is non-commutative (\(AB \neq BA\)).
            </div>
          </div>
        </div>

        <div class="formula-box">
          <div class="formula-label">Matrix Multiplication Rule</div>
          Matrix A [m x k]  &bull;  Matrix B [k x n]  =  Matrix C [m x n]<br>
          Inner dimensions (k) must match! Result has outer dimensions (m x n).
        </div>

        <div class="quiz-cta-box">
          <div class="quiz-cta-info">
            <h4>Ready to test Fractals &amp; Matrices?</h4>
            <p>5 Quick Multiple Choice questions to test your recall.</p>
          </div>
          <button class="btn-start-quiz fn" onclick="startLessonQuiz('fn-l5l6l7')">🎯 Answer Quiz (5 Qs)</button>
        </div>
      </section>
    </main>
  </div>

  <!-- ==========================================================================
       INTERACTIVE QUIZ MODAL (ONE QUESTION AT A TIME)
       ========================================================================== -->
  <div class="quiz-modal-backdrop" id="quizModal">
    <div class="quiz-card-modal">
      <div class="quiz-modal-header">
        <div class="quiz-modal-title" id="quizModalTitle">Lesson Quiz</div>
        <button class="btn-close-quiz" onclick="closeQuiz()">&times;</button>
      </div>

      <div class="quiz-progress-bar-wrap">
        <div class="quiz-progress-bar-fill" id="quizProgressFill"></div>
      </div>

      <div class="quiz-body" id="quizBody">
        <!-- Question Active State -->
        <div id="quizQuestionView">
          <div class="quiz-q-counter" id="quizQuestionCounter">Question 1 of 5</div>
          <div class="quiz-q-text" id="quizQuestionText">Question text here?</div>

          <div class="quiz-options-list" id="quizOptionsList">
            <!-- Options dynamically injected -->
          </div>

          <div class="quiz-feedback-box" id="quizFeedbackBox"></div>
        </div>

        <!-- Finished State -->
        <div class="quiz-finished-view" id="quizFinishedView" style="display:none;">
          <div class="quiz-finished-emoji" id="quizFinishedEmoji">&#127881;</div>
          <div class="quiz-finished-score" id="quizFinishedScore">Score: 5 / 5</div>
          <div class="quiz-finished-msg" id="quizFinishedMsg">Amazing recall! You are fully prepared for this topic.</div>
          <button class="btn-continue-topic" onclick="continueToTopic()">Continue to the topic &#8594;</button>
        </div>
      </div>

      <div class="quiz-modal-footer" id="quizModalFooter">
        <button class="btn-quiz-next" id="btnQuizNext" onclick="nextQuestion()">Next Question &#8594;</button>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       GLOBAL SEARCH MODAL
       ========================================================================== -->
  <div class="search-modal-backdrop" id="searchModal" onclick="closeSearchOnBackdrop(event)">
    <div class="search-dialog">
      <div class="search-input-box">
        <span style="font-size:18px;">&#128269;</span>
        <input type="text" class="search-input" id="globalSearchInput" placeholder="Search keywords across all 4 subjects..." oninput="handleSearch(this.value)"/>
        <button onclick="closeSearch()" style="background:none;border:none;color:var(--t3);cursor:pointer;font-size:18px;">&times;</button>
      </div>
      <div class="search-results-list" id="searchResultsContainer">
        <div style="padding:16px;text-align:center;color:var(--t3);font-size:13px;">
          Type any keyword (e.g. <em>Pascal, Netiquette, Fibonacci, Levers, Matrix, Markup</em>)...
        </div>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       JAVASCRIPT ENGINE: QUIZZES, MODES, ROUTING
       ========================================================================== -->
  <script>
    // Quiz Database
    const QUIZ_DATABASE = {quiz_json_str};

    let activeQuizKey = null;
    let currentQIndex = 0;
    let currentScore = 0;
    let isAnswered = false;

    // Reviewer Mode Switcher (Summary vs. Detailed)
    function setReviewerMode(mode) {
      if (mode === 'detailed') {
        document.body.className = 'mode-is-detailed';
        document.getElementById('topBtnDetailed').classList.add('active-mode');
        document.getElementById('topBtnSummary').classList.remove('active-mode');
        
        const cardDet = document.getElementById('landingCardDetailed');
        const cardSum = document.getElementById('landingCardSummary');
        if (cardDet) cardDet.classList.add('selected-mode-card');
        if (cardSum) cardSum.classList.remove('selected-mode-card');
      } else {
        document.body.className = 'mode-is-summary';
        document.getElementById('topBtnSummary').classList.add('active-mode');
        document.getElementById('topBtnDetailed').classList.remove('active-mode');

        const cardDet = document.getElementById('landingCardDetailed');
        const cardSum = document.getElementById('landingCardSummary');
        if (cardSum) cardSum.classList.add('selected-mode-card');
        if (cardDet) cardDet.classList.remove('selected-mode-card');
      }
    }

    // Audio Chimes using Web Audio API
    function playAudioTone(isCorrect) {
      try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        if (isCorrect) {
          osc.type = 'sine';
          osc.frequency.setValueAtTime(587.33, ctx.currentTime);
          osc.frequency.setValueAtTime(880, ctx.currentTime + 0.1);
          gain.gain.setValueAtTime(0.2, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.35);
          osc.start();
          osc.stop(ctx.currentTime + 0.35);
        } else {
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(220, ctx.currentTime);
          osc.frequency.setValueAtTime(160, ctx.currentTime + 0.12);
          gain.gain.setValueAtTime(0.2, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
          osc.start();
          osc.stop(ctx.currentTime + 0.3);
        }
      } catch (e) {}
    }

    // Navigation Switcher
    function switchChannel(channelKey, targetLessonId = null) {
      const views = {
        'landing': document.getElementById('view-landing'),
        'mk': document.getElementById('view-mk'),
        'gs': document.getElementById('view-gs'),
        'gm': document.getElementById('view-gm'),
        'fn': document.getElementById('view-fn')
      };

      const dpills = {
        'landing': document.getElementById('dpill-landing'),
        'mk': document.getElementById('dpill-mk'),
        'gs': document.getElementById('dpill-gs'),
        'gm': document.getElementById('dpill-gm'),
        'fn': document.getElementById('dpill-fn')
      };

      const mtabs = {
        'landing': document.getElementById('mtab-landing'),
        'mk': document.getElementById('mtab-mk'),
        'gs': document.getElementById('mtab-gs'),
        'gm': document.getElementById('mtab-gm'),
        'fn': document.getElementById('mtab-fn')
      };

      Object.keys(views).forEach(k => {
        if (views[k]) views[k].classList.remove('active-view');
        if (dpills[k]) dpills[k].className = 'dpill';
        if (mtabs[k]) mtabs[k].className = 'mob-tab';
      });

      if (views[channelKey]) {
        views[channelKey].classList.add('active-view');
        
        if (dpills[channelKey]) {
          dpills[channelKey].classList.add(channelKey === 'landing' ? 'active-hub' : `active-${channelKey}`);
        }

        if (mtabs[channelKey]) {
          mtabs[channelKey].classList.add('active-tab');
          if (channelKey !== 'landing') mtabs[channelKey].classList.add(`tab-${channelKey}`);
        }

        window.location.hash = channelKey === 'landing' ? '' : `channel-${channelKey}`;

        if (targetLessonId) {
          setTimeout(() => {
            const el = document.getElementById(targetLessonId);
            if (el) el.scrollIntoView({ behavior: 'smooth' });
          }, 100);
        } else {
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      }
    }

    // Quiz Execution
    function startLessonQuiz(quizKey) {
      const quiz = QUIZ_DATABASE[quizKey];
      if (!quiz) return;

      activeQuizKey = quizKey;
      currentQIndex = 0;
      currentScore = 0;
      isAnswered = false;

      document.getElementById('quizModalTitle').textContent = quiz.title;
      document.getElementById('quizQuestionView').style.display = 'block';
      document.getElementById('quizFinishedView').style.display = 'none';
      document.getElementById('quizModalFooter').style.display = 'flex';
      document.getElementById('btnQuizNext').classList.remove('show');
      
      document.getElementById('quizModal').classList.add('open');
      renderQuestion();
    }

    function renderQuestion() {
      const quiz = QUIZ_DATABASE[activeQuizKey];
      const q = quiz.questions[currentQIndex];
      const total = quiz.questions.length;
      isAnswered = false;

      const progressPercent = ((currentQIndex) / total) * 100;
      document.getElementById('quizProgressFill').style.width = progressPercent + '%';

      document.getElementById('quizQuestionCounter').textContent = `Question ${currentQIndex + 1} of ${total}`;
      document.getElementById('quizQuestionText').textContent = q.q;

      const letters = ['A', 'B', 'C', 'D'];
      const optList = document.getElementById('quizOptionsList');
      optList.innerHTML = q.options.map((opt, idx) => `
        <button class="quiz-opt-btn" id="optBtn-${idx}" onclick="selectAnswer(${idx})">
          <span class="quiz-opt-letter">${letters[idx]}</span>
          <span>${opt}</span>
        </button>
      `).join('');

      const fb = document.getElementById('quizFeedbackBox');
      fb.className = 'quiz-feedback-box';
      fb.style.display = 'none';
      document.getElementById('btnQuizNext').classList.remove('show');
    }

    function selectAnswer(selectedIdx) {
      if (isAnswered) return;
      isAnswered = true;

      const quiz = QUIZ_DATABASE[activeQuizKey];
      const q = quiz.questions[currentQIndex];
      const isCorrect = (selectedIdx === q.answer);

      const fb = document.getElementById('quizFeedbackBox');
      const selectedBtn = document.getElementById(`optBtn-${selectedIdx}`);
      const correctBtn = document.getElementById(`optBtn-${q.answer}`);

      q.options.forEach((_, idx) => {
        document.getElementById(`optBtn-${idx}`).disabled = true;
      });

      if (isCorrect) {
        currentScore++;
        selectedBtn.classList.add('opt-correct');
        fb.className = 'quiz-feedback-box correct-fb';
        fb.innerHTML = '&#10004; Tumpak! Correct answer.';
        fb.style.display = 'block';
        playAudioTone(true);
      } else {
        selectedBtn.classList.add('opt-wrong');
        correctBtn.classList.add('opt-correct');
        fb.className = 'quiz-feedback-box wrong-fb';
        fb.innerHTML = '&#10006; <strong>haha mali &#128540;</strong> &mdash; ' + q.hint;
        fb.style.display = 'block';
        playAudioTone(false);
      }

      const nextBtn = document.getElementById('btnQuizNext');
      if (currentQIndex < quiz.questions.length - 1) {
        nextBtn.textContent = 'Next Question &rarr;';
      } else {
        nextBtn.textContent = 'See Results &rarr;';
      }
      nextBtn.classList.add('show');
    }

    function nextQuestion() {
      const quiz = QUIZ_DATABASE[activeQuizKey];
      if (currentQIndex < quiz.questions.length - 1) {
        currentQIndex++;
        renderQuestion();
      } else {
        showQuizResults();
      }
    }

    function showQuizResults() {
      const quiz = QUIZ_DATABASE[activeQuizKey];
      const total = quiz.questions.length;
      document.getElementById('quizProgressFill').style.width = '100%';

      document.getElementById('quizQuestionView').style.display = 'none';
      document.getElementById('quizModalFooter').style.display = 'none';
      document.getElementById('quizFinishedView').style.display = 'block';

      document.getElementById('quizFinishedScore').textContent = `Score: ${currentScore} / ${total}`;
      
      if (currentScore === total) {
        document.getElementById('quizFinishedEmoji').textContent = '&#127881;';
        document.getElementById('quizFinishedMsg').textContent = 'Perfect score! Outstanding mastery of this topic.';
        try { confetti({ particleCount: 80, spread: 70, origin: { y: 0.6 } }); } catch(e){}
      } else if (currentScore >= total / 2) {
        document.getElementById('quizFinishedEmoji').textContent = '&#128079;';
        document.getElementById('quizFinishedMsg').textContent = 'Great job! A quick review of the notes will make it 100%.';
      } else {
        document.getElementById('quizFinishedEmoji').textContent = '&#128170;';
        document.getElementById('quizFinishedMsg').textContent = 'Keep practicing! Review the detailed lessons or summary above.';
      }
    }

    function continueToTopic() {
      closeQuiz();
      const lessonTarget = `lesson-${activeQuizKey}`;
      const el = document.getElementById(lessonTarget);
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    }

    function closeQuiz() {
      document.getElementById('quizModal').classList.remove('open');
    }

    // Search Engine
    const searchTerms = [
      { title: "5 Elemento ng Komunikasyon", channel: "mk", lessonId: "lesson-mk-a3", desc: "Sender, Message, Channel, Receiver, Feedback" },
      { title: "Intrapersonal (Diary, Journal, Reflection)", channel: "mk", lessonId: "lesson-mk-a3", desc: "Pakikipag-usap sa sarili at goal setting" },
      { title: "Digital Identity, Footprint & Netiquette", channel: "mk", lessonId: "lesson-mk-a3", desc: "Active vs passive footprint, 2FA, online privacy" },
      { title: "3 Proseso & Kamalayang Kultural", channel: "mk", lessonId: "lesson-mk-a4", desc: "Decoding, pakikilahok, ekspresyon, sensibilidad sa usapan" },
      { title: "Simple Machines & 3 Lever Classes", channel: "gs", lessonId: "lesson-gs-w5simple", desc: "1st, 2nd, 3rd class levers (F-L-E middle rules), MA=Load/Effort" },
      { title: "Pulleys, Inclined Planes & Screws", channel: "gs", lessonId: "lesson-gs-w5simple", desc: "Fixed vs movable pulleys, IMA=Length/Height" },
      { title: "Pascal's Principle & Hydraulics", channel: "gs", lessonId: "lesson-gs-w6pascal", desc: "Pressure transmitted undiminished: F1/A1 = F2/A2" },
      { title: "Archimedes' Principle & Buoyancy", channel: "gs", lessonId: "lesson-gs-w6pascal", desc: "Fb = Weight of displaced fluid; sinking vs floating" },
      { title: "Business Percentages & Mark-up", channel: "gm", lessonId: "lesson-gm-w6", desc: "Cost, Selling Price, Mark-down, Discounts" },
      { title: "Simple Interest (I = Prt)", channel: "gm", lessonId: "lesson-gm-w6", desc: "Principal, annual interest rate, time in years" },
      { title: "Fibonacci Sequence & Nature Patterns", channel: "gm", lessonId: "lesson-gm-w7w8", desc: "0, 1, 1, 2, 3, 5, 8, 13, 21... Radial & Bilateral symmetry" },
      { title: "Arithmetic & Geometric Sequences", channel: "gm", lessonId: "lesson-gm-w7w8", desc: "Common difference (d) vs common ratio (r)" },
      { title: "Tessellations & 7 Frieze Groups", channel: "fn", lessonId: "lesson-fn-l3l4", desc: "Plane tiling with no gaps; 4 isometries" },
      { title: "Golden Ratio (Phi = 1.618)", channel: "fn", lessonId: "lesson-fn-l3l4", desc: "Phi = (1+sqrt(5))/2; Golden rectangles & spirals" },
      { title: "Fractals & Sierpinski Triangle", channel: "fn", lessonId: "lesson-fn-l5l6l7", desc: "Self-similarity repeating at infinite scales" },
      { title: "Matrix Multiplication (m x k • k x n)", channel: "fn", lessonId: "lesson-fn-l5l6l7", desc: "Inner dimensions must match; matrix operations" }
    ];

    function openSearch() {
      const m = document.getElementById('searchModal');
      m.classList.add('open');
      const input = document.getElementById('globalSearchInput');
      input.focus();
    }
    function closeSearch() {
      document.getElementById('searchModal').classList.remove('open');
    }
    function closeSearchOnBackdrop(e) {
      if (e.target.id === 'searchModal') closeSearch();
    }

    function handleSearch(val) {
      const q = val.trim().toLowerCase();
      const cont = document.getElementById('searchResultsContainer');
      if (!q) {
        cont.innerHTML = '<div style="padding:16px;text-align:center;color:var(--t3);font-size:13px;">Type any keyword...</div>';
        return;
      }
      const matches = searchTerms.filter(t => t.title.toLowerCase().includes(q) || t.desc.toLowerCase().includes(q));
      if (matches.length === 0) {
        cont.innerHTML = `<div style="padding:16px;text-align:center;color:var(--t3);font-size:13px;">No keywords matching "<strong>${val}</strong>".</div>`;
        return;
      }
      cont.innerHTML = matches.map(m => `
        <div class="s-res-card" onclick="selectSearchMatch('${m.channel}', '${m.lessonId}')">
          <div class="s-res-t">${m.title}</div>
          <div class="s-res-d">${m.desc}</div>
        </div>
      `).join('');
    }

    function selectSearchMatch(channelKey, lessonId) {
      closeSearch();
      switchChannel(channelKey, lessonId);
    }

    window.addEventListener('DOMContentLoaded', () => {
      const hash = window.location.hash;
      if (hash.startsWith('#channel-')) {
        const ch = hash.replace('#channel-', '');
        if (['mk', 'gs', 'gm', 'fn'].includes(ch)) {
          switchChannel(ch);
        }
      }
    });
  </script>
</body>
</html>
"""

# Clean any surrogate escapes
html_clean = html_template.replace('\\uD83C\\uDF89', '🎉')\
                          .replace('\\uD83D\\uDC4F', '👏')\
                          .replace('\\uD83D\\uDCAA', '💪')\
                          .replace('\&rarr;', '➔')

# Write index.html at root and in indexes/
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)
print("Wrote index.html (Master Light Multimode Portal) successfully! Length:", len(html_clean))

with open('indexes/hub.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)
print("Wrote indexes/hub.html successfully!")

with open('indexes/index.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)
print("Wrote indexes/index.html successfully!")

# Standalone pages with default view activated
with open('indexes/mabkom.index.html', 'w', encoding='utf-8') as f:
    f.write(html_clean.replace('active-view', '').replace('id="view-mk"', 'id="view-mk" class="view-container active-view"'))

with open('indexes/1mabkom.index.html', 'w', encoding='utf-8') as f:
    f.write(html_clean.replace('active-view', '').replace('id="view-mk"', 'id="view-mk" class="view-container active-view"'))

with open('indexes/GenScieindex.html', 'w', encoding='utf-8') as f:
    f.write(html_clean.replace('active-view', '').replace('id="view-gs"', 'id="view-gs" class="view-container active-view"'))

with open('indexes/genmath.html', 'w', encoding='utf-8') as f:
    f.write(html_clean.replace('active-view', '').replace('id="view-gm"', 'id="view-gm" class="view-container active-view"'))

with open('indexes/finite.html', 'w', encoding='utf-8') as f:
    f.write(html_clean.replace('active-view', '').replace('id="view-fn"', 'id="view-fn" class="view-container active-view"'))

print("All files synchronized with the Dual-Mode (Detailed vs Summary) Light Mobile Engine!")
