import os
import re
import json

def read_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def extract_body_parts(html_content):
    cover_match = re.search(r'<section\s+class=["\']cover["\'][^>]*>(.*?)</section>', html_content, re.DOTALL)
    cover_html = cover_match.group(1) if cover_match else ''
    
    nav_match = re.search(r'<div\s+class=["\']nav-inner["\'][^>]*>(.*?)</div>', html_content, re.DOTALL)
    nav_links = nav_match.group(1) if nav_match else ''
    
    main_match = re.search(r'<main\s+class=["\']main["\'][^>]*>(.*?)</main>', html_content, re.DOTALL)
    main_html = main_match.group(1) if main_match else ''
    
    style_match = re.search(r'<style>(.*?)</style>', html_content, re.DOTALL)
    style_html = style_match.group(1) if style_match else ''
    
    return cover_html, nav_links, main_html, style_html

mabkom_html = read_file('indexes/mabkom.index.html')
genscie_html = read_file('indexes/GenScieindex.html')
genmath_html = read_file('indexes/genmath.html')
finite_html = read_file('indexes/finite.html')

mk_cover, mk_nav, mk_main, mk_style = extract_body_parts(mabkom_html)
gs_cover, gs_nav, gs_main, gs_style = extract_body_parts(genscie_html)
gm_cover, gm_nav, gm_main, gm_style = extract_body_parts(genmath_html)
fn_cover, fn_nav, fn_main, fn_style = extract_body_parts(finite_html)

print("Parsed sections successfully:")
print("MabKom:", len(mk_main))
print("GenScie:", len(gs_main))
print("GenMath:", len(gm_main))
print("Finite:", len(fn_main))

# Clean & namespace CSS rules where needed
# All 4 files use .main, .ls, .lh, .card, .tg, .ti, .fb, .ml, .es, .ak, etc.
# These share a unified modern design language!

portal_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>MUJIB Study Hub &middot; Multi-Topic Summative Reviewer Portal</title>
  <meta name="description" content="All-in-One Comprehensive Summative Exam Reviewer Hub covering Mabisang Komunikasyon, General Science, General Mathematics, and Finite Mathematics 1."/>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet"/>

  <style>
/* ==========================================================================
   GLOBAL DESIGN TOKENS & SYSTEM
   ========================================================================== */
:root {
  --font-display: 'Outfit', sans-serif;
  --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Neutrals */
  --bg: #07090e;
  --bg-surface: #0e121a;
  --bg-card: #131924;
  --bg-card-hover: #182232;
  --border: #1e293b;
  --border-focus: #334155;
  --border-light: rgba(255, 255, 255, 0.08);

  --t1: #f8fafc;
  --t2: #94a3b8;
  --t3: #64748b;
  --t-muted: #475569;

  /* Subject Accent Colors */
  --mk-rose: #f43f5e;
  --mk-amber: #f59e0b;
  --mk-purple: #a855f7;
  --mk-grad: linear-gradient(135deg, #f43f5e, #f59e0b);

  --gs-teal: #14d9a4;
  --gs-cyan: #22d3ee;
  --gs-lime: #84cc16;
  --gs-grad: linear-gradient(135deg, #14d9a4, #22d3ee);

  --gm-blue: #3b82f6;
  --gm-indigo: #6366f1;
  --gm-teal: #14b8a6;
  --gm-grad: linear-gradient(135deg, #3b82f6, #8b5cf6);

  --fn-orange: #f97316;
  --fn-amber: #fbbf24;
  --fn-violet: #a78bfa;
  --fn-grad: linear-gradient(135deg, #f97316, #fbbf24);

  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 22px;
  --radius-xl: 32px;
  --radius-full: 9999px;

  --shadow-sm: 0 2px 8px rgba(0,0,0,0.3);
  --shadow-md: 0 8px 24px rgba(0,0,0,0.4);
  --shadow-lg: 0 16px 40px rgba(0,0,0,0.5);
  --shadow-glow-mk: 0 0 30px rgba(244,63,94,0.25);
  --shadow-glow-gs: 0 0 30px rgba(20,217,164,0.25);
  --shadow-glow-gm: 0 0 30px rgba(59,130,246,0.25);
  --shadow-glow-fn: 0 0 30px rgba(249,115,22,0.25);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  color-scheme: dark;
}

body {
  font-family: var(--font-body);
  background-color: var(--bg);
  color: var(--t1);
  line-height: 1.65;
  font-size: 15px;
  min-height: 100vh;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

::selection {
  background: rgba(59, 130, 246, 0.35);
  color: #ffffff;
}

::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
::-webkit-scrollbar-track {
  background: var(--bg);
}
::-webkit-scrollbar-thumb {
  background: #1e293b;
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: #334155;
}

/* ==========================================================================
   TOP GLOBAL BAR
   ========================================================================== */
.global-bar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(7, 9, 14, 0.9);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  padding: 10px 24px;
  transition: all 0.3s ease;
}

.global-bar-inner {
  max-width: 1300px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--t1);
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 18px;
  letter-spacing: -0.02em;
  cursor: pointer;
  user-select: none;
}

.brand-icon {
  width: 34px;
  height: 34px;
  border-radius: var(--radius-sm);
  background: linear-gradient(135deg, #3b82f6, #f43f5e);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

.brand-text span {
  color: #38bdf8;
}

.channel-nav-pills {
  display: flex;
  align-items: center;
  gap: 6px;
  overflow-x: auto;
  scrollbar-width: none;
}
.channel-nav-pills::-webkit-scrollbar { display: none; }

.cpill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  border-radius: var(--radius-full);
  font-size: 12.5px;
  font-weight: 600;
  color: var(--t2);
  text-decoration: none;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid transparent;
  transition: all 0.2s ease;
  white-space: nowrap;
  cursor: pointer;
}

.cpill:hover {
  color: var(--t1);
  background: rgba(255, 255, 255, 0.08);
}

.cpill.active-hub {
  background: rgba(59, 130, 246, 0.15);
  border-color: rgba(59, 130, 246, 0.4);
  color: #60a5fa;
}
.cpill.active-mk {
  background: rgba(244, 63, 94, 0.15);
  border-color: rgba(244, 63, 94, 0.4);
  color: #fb7185;
}
.cpill.active-gs {
  background: rgba(20, 217, 164, 0.15);
  border-color: rgba(20, 217, 164, 0.4);
  color: #2dd4bf;
}
.cpill.active-gm {
  background: rgba(59, 130, 246, 0.15);
  border-color: rgba(59, 130, 246, 0.4);
  color: #60a5fa;
}
.cpill.active-fn {
  background: rgba(249, 115, 22, 0.15);
  border-color: rgba(249, 115, 22, 0.4);
  color: #fb923c;
}

.global-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.search-trigger {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  padding: 6px 14px;
  border-radius: var(--radius-full);
  color: var(--t3);
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s ease;
}
.search-trigger:hover {
  border-color: var(--t2);
  color: var(--t1);
  background: rgba(255, 255, 255, 0.08);
}
.search-trigger kbd {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 4px;
  padding: 1px 6px;
  font-size: 10px;
  font-family: var(--font-mono);
}

/* ==========================================================================
   VIEW CONTAINERS & ROUTING
   ========================================================================== */
.view-container {
  display: none;
  animation: fadeIn 0.35s ease forwards;
}

.view-container.active-view {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ==========================================================================
   LANDING PAGE (TOPIC SELECTOR & PORTAL)
   ========================================================================== */
.landing-hero {
  position: relative;
  padding: 70px 24px 50px;
  text-align: center;
  overflow: hidden;
  background: radial-gradient(circle at 50% -10%, rgba(59, 130, 246, 0.15), transparent 70%),
              radial-gradient(circle at 85% 30%, rgba(244, 63, 94, 0.12), transparent 60%),
              radial-gradient(circle at 15% 40%, rgba(20, 217, 164, 0.12), transparent 60%);
}

.hero-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 18px;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-light);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #38bdf8;
  margin-bottom: 24px;
}

.hero-pill-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #22d3ee;
  box-shadow: 0 0 10px #22d3ee;
}

.landing-title {
  font-family: var(--font-display);
  font-size: clamp(38px, 6vw, 68px);
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -0.03em;
  margin-bottom: 18px;
  background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #94a3b8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.landing-title .grad-text {
  background: linear-gradient(135deg, #38bdf8, #818cf8, #f43f5e);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.landing-subtitle {
  font-size: clamp(16px, 2vw, 19px);
  color: var(--t2);
  max-width: 680px;
  margin: 0 auto 36px;
  line-height: 1.6;
}

/* Quick Stats Bar */
.stats-banner {
  display: flex;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
  margin: 0 auto 50px;
  max-width: 900px;
}

.stat-chip {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 12px 20px;
  display: flex;
  align-items: center;
  gap: 12px;
  text-align: left;
}

.stat-num {
  font-family: var(--font-display);
  font-size: 24px;
  font-weight: 800;
  color: var(--t1);
  line-height: 1;
}
.stat-lbl {
  font-size: 11.5px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--t3);
}

/* Topic Grid */
.landing-content {
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 24px 80px;
}

.section-header-row {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 28px;
  gap: 16px;
  flex-wrap: wrap;
}

.section-title-group h2 {
  font-family: var(--font-display);
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--t1);
}
.section-title-group p {
  font-size: 14px;
  color: var(--t3);
  margin-top: 4px;
}

.topics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

/* Subject Card Styles */
.subject-card {
  position: relative;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 32px 28px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
}

.subject-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  transition: all 0.3s ease;
}

.subject-card:hover {
  transform: translateY(-6px);
  background: var(--bg-card-hover);
  border-color: var(--border-focus);
}

/* Card Variants */
.card-mk::before { background: var(--mk-grad); }
.card-mk:hover { box-shadow: var(--shadow-glow-mk); border-color: rgba(244, 63, 94, 0.4); }
.card-gs::before { background: var(--gs-grad); }
.card-gs:hover { box-shadow: var(--shadow-glow-gs); border-color: rgba(20, 217, 164, 0.4); }
.card-gm::before { background: var(--gm-grad); }
.card-gm:hover { box-shadow: var(--shadow-glow-gm); border-color: rgba(59, 130, 246, 0.4); }
.card-fn::before { background: var(--fn-grad); }
.card-fn:hover { box-shadow: var(--shadow-glow-fn); border-color: rgba(249, 115, 22, 0.4); }

.card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.card-icon-wrap {
  width: 52px;
  height: 52px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
}
.card-mk .card-icon-wrap { background: rgba(244, 63, 94, 0.15); border: 1px solid rgba(244, 63, 94, 0.3); }
.card-gs .card-icon-wrap { background: rgba(20, 217, 164, 0.15); border: 1px solid rgba(20, 217, 164, 0.3); }
.card-gm .card-icon-wrap { background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.3); }
.card-fn .card-icon-wrap { background: rgba(249, 115, 22, 0.15); border: 1px solid rgba(249, 115, 22, 0.3); }

.card-badge {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 4px 12px;
  border-radius: var(--radius-full);
}
.card-mk .card-badge { background: rgba(244, 63, 94, 0.12); color: var(--mk-rose); border: 1px solid rgba(244, 63, 94, 0.25); }
.card-gs .card-badge { background: rgba(20, 217, 164, 0.12); color: var(--gs-teal); border: 1px solid rgba(20, 217, 164, 0.25); }
.card-gm .card-badge { background: rgba(59, 130, 246, 0.12); color: var(--gm-blue); border: 1px solid rgba(59, 130, 246, 0.25); }
.card-fn .card-badge { background: rgba(249, 115, 22, 0.12); color: var(--fn-orange); border: 1px solid rgba(249, 115, 22, 0.25); }

.card-title {
  font-family: var(--font-display);
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -0.02em;
  margin-bottom: 8px;
  color: var(--t1);
}

.card-desc {
  font-size: 13.5px;
  color: var(--t2);
  margin-bottom: 20px;
  line-height: 1.55;
}

.topic-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 26px;
}
.topic-tag {
  font-size: 11.5px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-sm);
  padding: 3px 8px;
  color: var(--t3);
}

.card-btn-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.enter-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 700;
  color: var(--t1);
  transition: gap 0.2s ease;
}
.subject-card:hover .enter-btn {
  gap: 12px;
}
.card-mk:hover .enter-btn { color: var(--mk-rose); }
.card-gs:hover .enter-btn { color: var(--gs-teal); }
.card-gm:hover .enter-btn { color: var(--gm-blue); }
.card-fn:hover .enter-btn { color: var(--fn-orange); }

.meta-stats {
  font-size: 12px;
  color: var(--t3);
}

/* ==========================================================================
   SUBJECT CHANNEL WRAPPER
   ========================================================================== */
.channel-header-bar {
  background: rgba(14, 18, 26, 0.95);
  border-bottom: 1px solid var(--border);
  padding: 12px 24px;
  position: sticky;
  top: 57px;
  z-index: 900;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
}

.channel-header-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}

.ch-title-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
}

.ch-back-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: var(--radius-sm);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  color: var(--t2);
  font-size: 12.5px;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.2s ease;
}
.ch-back-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: var(--t1);
}

.ch-name {
  font-family: var(--font-display);
  font-size: 17px;
  font-weight: 800;
  color: var(--t1);
}

.channel-quick-links {
  display: flex;
  align-items: center;
  gap: 6px;
  overflow-x: auto;
}

.ch-link {
  font-size: 12px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  color: var(--t3);
  text-decoration: none;
  transition: all 0.2s;
  white-space: nowrap;
}
.ch-link:hover {
  color: var(--t1);
  background: rgba(255,255,255,0.06);
}

.ch-tools {
  display: flex;
  align-items: center;
  gap: 8px;
}

.tool-pill-btn {
  font-size: 12px;
  font-weight: 600;
  padding: 5px 12px;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  color: var(--t2);
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
}
.tool-pill-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: var(--t1);
}

/* ==========================================================================
   SEARCH MODAL
   ========================================================================== */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(8px);
  z-index: 2000;
  display: none;
  align-items: flex-start;
  justify-content: center;
  padding: 80px 20px 20px;
}
.modal-backdrop.open {
  display: flex;
}
.search-modal {
  background: #0f172a;
  border: 1px solid var(--border-focus);
  border-radius: var(--radius-lg);
  width: 100%;
  max-width: 640px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
  overflow: hidden;
  animation: modalIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
@keyframes modalIn {
  from { opacity: 0; transform: scale(0.96) translateY(-10px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}
.modal-search-box {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 20px;
  border-bottom: 1px solid var(--border);
}
.modal-search-input {
  background: transparent;
  border: none;
  outline: none;
  color: var(--t1);
  font-size: 16px;
  width: 100%;
  font-family: inherit;
}
.modal-results {
  max-height: 380px;
  overflow-y: auto;
  padding: 10px;
}
.search-result-item {
  padding: 12px 14px;
  border-radius: var(--radius-sm);
  display: block;
  text-decoration: none;
  color: var(--t1);
  transition: background 0.15s ease;
  cursor: pointer;
}
.search-result-item:hover {
  background: rgba(255, 255, 255, 0.06);
}
.s-res-title { font-weight: 700; font-size: 14px; }
.s-res-badge { font-size: 10.5px; text-transform: uppercase; font-weight: 700; padding: 2px 6px; border-radius: 4px; margin-right: 6px; }
.s-res-snippet { font-size: 12.5px; color: var(--t2); margin-top: 2px; }

/* EMBEDDED REVIEWER CSS STYLES */
/* __STYLES_PLACEHOLDER__ */

/* Responsive adjustments */
@media (max-width: 800px) {
  .channel-nav-pills { display: none; }
  .channel-quick-links { display: none; }
  .landing-hero { padding: 50px 16px 30px; }
  .stats-banner { flex-direction: column; gap: 8px; }
}
  </style>
</head>
<body>

  <!-- ==========================================================================
       TOP GLOBAL HEADER
       ========================================================================== -->
  <header class="global-bar">
    <div class="global-bar-inner">
      <div class="brand-logo" onclick="switchChannel('landing')">
        <div class="brand-icon">&#127891;</div>
        <div class="brand-text">MUJIB <span>Study Hub</span></div>
      </div>

      <nav class="channel-nav-pills">
        <button class="cpill active-hub" id="pill-landing" onclick="switchChannel('landing')">&#127968; Topics Hub</button>
        <button class="cpill" id="pill-mk" onclick="switchChannel('mk')">&#128483;&#65039; Mabisang Komunikasyon</button>
        <button class="cpill" id="pill-gs" onclick="switchChannel('gs')">&#128300; General Science</button>
        <button class="cpill" id="pill-gm" onclick="switchChannel('gm')">&#128208; General Math</button>
        <button class="cpill" id="pill-fn" onclick="switchChannel('fn')">&#129513; Finite Math 1</button>
      </nav>

      <div class="global-actions">
        <button class="search-trigger" onclick="openSearch()">
          <span>&#128269; Search topics...</span>
          <kbd>Ctrl+K</kbd>
        </button>
      </div>
    </div>
  </header>

  <!-- ==========================================================================
       CHANNEL 0: LANDING PAGE & TOPIC SELECTOR
       ========================================================================== -->
  <div class="view-container active-view" id="view-landing">
    <section class="landing-hero">
      <div class="hero-pill">
        <span class="hero-pill-dot"></span>
        Summative Exam Reviewers &middot; 4 Subjects Available
      </div>
      <h1 class="landing-title">Choose Your <span class="grad-text">Study Channel</span></h1>
      <p class="landing-subtitle">
        Access comprehensive study notes, essential formulas, key term memorization lists, and mock exam questions tailored for your upcoming summatives.
      </p>

      <div class="stats-banner">
        <div class="stat-chip">
          <div class="stat-num" style="color:#f43f5e;">4</div>
          <div class="stat-lbl">Subject<br>Channels</div>
        </div>
        <div class="stat-chip">
          <div class="stat-num" style="color:#14d9a4;">16+</div>
          <div class="stat-lbl">Core Modules<br>&amp; Lessons</div>
        </div>
        <div class="stat-chip">
          <div class="stat-num" style="color:#38bdf8;">120+</div>
          <div class="stat-lbl">Exam Questions<br>&amp; Answer Keys</div>
        </div>
        <div class="stat-chip">
          <div class="stat-num" style="color:#fbbf24;">100%</div>
          <div class="stat-lbl">Summative<br>Aligned</div>
        </div>
      </div>
    </section>

    <main class="landing-content">
      <div class="section-header-row">
        <div class="section-title-group">
          <h2>Subject Reviewer Channels</h2>
          <p>Click any subject card below to enter the dedicated channel</p>
        </div>
      </div>

      <div class="topics-grid">
        <!-- Card 1: MabKom -->
        <div class="subject-card card-mk" onclick="switchChannel('mk')">
          <div>
            <div class="card-top">
              <div class="card-icon-wrap">&#128483;&#65039;</div>
              <span class="card-badge">Aralin 3 &amp; 4</span>
            </div>
            <h3 class="card-title">Mabisang Komunikasyon</h3>
            <p class="card-desc">
              Malinaw na pagpapahayag ng mga ideya, Intrapersonal na komunikasyon, Digital Identity &amp; Netiquette, at Pagninilay sa Kamalayang Kultural.
            </p>
            <div class="topic-tags">
              <span class="topic-tag">5 Elemento</span>
              <span class="topic-tag">Digital Footprint</span>
              <span class="topic-tag">Pormal vs. Di-Pormal</span>
              <span class="topic-tag">Kamalayang Kultural</span>
              <span class="topic-tag">Sensibilidad</span>
            </div>
          </div>
          <div class="card-btn-row">
            <span class="enter-btn">Buksan ang Channel &#8594;</span>
            <span class="meta-stats">2 Aralin &middot; 40+ Qs</span>
          </div>
        </div>

        <!-- Card 2: General Science -->
        <div class="subject-card card-gs" onclick="switchChannel('gs')">
          <div>
            <div class="card-top">
              <div class="card-icon-wrap">&#128300;</div>
              <span class="card-badge">Weeks 5 &amp; 6</span>
            </div>
            <h3 class="card-title">General Science</h3>
            <p class="card-desc">
              Six simple machines, Lever classes, Mechanical Advantage (IMA/AMA), Compound machines, Pascal's Principle, Hydraulic systems, and Archimedes' Principle.
            </p>
            <div class="topic-tags">
              <span class="topic-tag">Levers &amp; Pulleys</span>
              <span class="topic-tag">MA = Load / Effort</span>
              <span class="topic-tag">Pascal's Principle</span>
              <span class="topic-tag">Hydraulics</span>
              <span class="topic-tag">Buoyancy</span>
            </div>
          </div>
          <div class="card-btn-row">
            <span class="enter-btn">Enter Science Channel &#8594;</span>
            <span class="meta-stats">4 Topics &middot; 45+ Qs</span>
          </div>
        </div>

        <!-- Card 3: General Math -->
        <div class="subject-card card-gm" onclick="switchChannel('gm')">
          <div>
            <div class="card-top">
              <div class="card-icon-wrap">&#128208;</div>
              <span class="card-badge">Weeks 6, 7 &amp; 8</span>
            </div>
            <h3 class="card-title">General Mathematics</h3>
            <p class="card-desc">
              Percentages in business and finance, mark-ups, mark-downs, patterns in life and nature, Fibonacci sequence, and Arithmetic &amp; Geometric sequences.
            </p>
            <div class="topic-tags">
              <span class="topic-tag">Mark-up / Discount</span>
              <span class="topic-tag">Simple Interest</span>
              <span class="topic-tag">Nature Patterns</span>
              <span class="topic-tag">Arithmetic Seq</span>
              <span class="topic-tag">Geometric Seq</span>
            </div>
          </div>
          <div class="card-btn-row">
            <span class="enter-btn">Enter Gen Math Channel &#8594;</span>
            <span class="meta-stats">3 Weeks &middot; 35+ Qs</span>
          </div>
        </div>

        <!-- Card 4: Finite Math -->
        <div class="subject-card card-fn" onclick="switchChannel('fn')">
          <div>
            <div class="card-top">
              <div class="card-icon-wrap">&#129513;</div>
              <span class="card-badge">Lessons 3 &ndash; 7</span>
            </div>
            <h3 class="card-title">Finite Mathematics 1</h3>
            <p class="card-desc">
              Escher-type tessellations, frieze patterns, Golden Ratio (&Phi;), Fibonacci spirals, fractals (Sierpinski/Mandelbrot), and matrix operations.
            </p>
            <div class="topic-tags">
              <span class="topic-tag">Tessellations</span>
              <span class="topic-tag">Golden Ratio &Phi;</span>
              <span class="topic-tag">Fractals</span>
              <span class="topic-tag">Matrix Addition</span>
              <span class="topic-tag">Matrix Product</span>
            </div>
          </div>
          <div class="card-btn-row">
            <span class="enter-btn">Enter Finite Math Channel &#8594;</span>
            <span class="meta-stats">5 Lessons &middot; 50+ Qs</span>
          </div>
        </div>
      </div>
    </main>
  </div>

  <!-- ==========================================================================
       CHANNEL 1: MABISANG KOMUNIKASYON
       ========================================================================== -->
  <div class="view-container" id="view-mk">
    <div class="channel-header-bar">
      <div class="channel-header-inner">
        <div class="ch-title-wrap">
          <button class="ch-back-btn" onclick="switchChannel('landing')">&#8592; Topics Hub</button>
          <div class="ch-name">&#128483;&#65039; Mabisang Komunikasyon Channel</div>
        </div>
        <div class="channel-quick-links">
          <a href="#aralin3" class="ch-link">Aralin 3</a>
          <a href="#a3intra" class="ch-link">Intrapersonal</a>
          <a href="#a3digital" class="ch-link">Digital Identity</a>
          <a href="#a3exam" class="ch-link">Pagsusulit 3</a>
          <a href="#aralin4" class="ch-link">Aralin 4</a>
          <a href="#a4kultura" class="ch-link">Kamalayang Kultural</a>
          <a href="#a4exam" class="ch-link">Pagsusulit 4</a>
        </div>
        <div class="ch-tools">
          <a href="indexes/mabkom.index.html" target="_blank" class="tool-pill-btn">&#8599; Open Standalone</a>
        </div>
      </div>
    </div>

    <!-- MabKom Embedded Main Content -->
    <div class="channel-content-body">
      <!-- __MK_MAIN__ -->
    </div>
  </div>

  <!-- ==========================================================================
       CHANNEL 2: GENERAL SCIENCE
       ========================================================================== -->
  <div class="view-container" id="view-gs">
    <div class="channel-header-bar">
      <div class="channel-header-inner">
        <div class="ch-title-wrap">
          <button class="ch-back-btn" onclick="switchChannel('landing')">&#8592; Topics Hub</button>
          <div class="ch-name">&#128300; General Science Channel</div>
        </div>
        <div class="channel-quick-links">
          <a href="#w5simple" class="ch-link">W5 &middot; Simple Machines</a>
          <a href="#w5exam" class="ch-link">Simple Exam</a>
          <a href="#w5compound" class="ch-link">W5 &middot; Compound Machines</a>
          <a href="#w6pascal" class="ch-link">W6 &middot; Pascal's</a>
          <a href="#w6arch" class="ch-link">W6 &middot; Archimedes'</a>
          <a href="#w6aexam" class="ch-link">Science Exam</a>
        </div>
        <div class="ch-tools">
          <a href="indexes/GenScieindex.html" target="_blank" class="tool-pill-btn">&#8599; Open Standalone</a>
        </div>
      </div>
    </div>

    <!-- GenScie Embedded Main Content -->
    <div class="channel-content-body">
      <!-- __GS_MAIN__ -->
    </div>
  </div>

  <!-- ==========================================================================
       CHANNEL 3: GENERAL MATHEMATICS
       ========================================================================== -->
  <div class="view-container" id="view-gm">
    <div class="channel-header-bar">
      <div class="channel-header-inner">
        <div class="ch-title-wrap">
          <button class="ch-back-btn" onclick="switchChannel('landing')">&#8592; Topics Hub</button>
          <div class="ch-name">&#128208; General Mathematics Channel</div>
        </div>
        <div class="channel-quick-links">
          <a href="#w6" class="ch-link">W6 &middot; Business Percentages</a>
          <a href="#w6exam" class="ch-link">W6 Exam</a>
          <a href="#w7" class="ch-link">W7 &middot; Nature Patterns</a>
          <a href="#w8" class="ch-link">W8 &middot; Sequences &amp; Series</a>
          <a href="#w8exam" class="ch-link">Sequences Exam</a>
        </div>
        <div class="ch-tools">
          <a href="indexes/genmath.html" target="_blank" class="tool-pill-btn">&#8599; Open Standalone</a>
        </div>
      </div>
    </div>

    <!-- GenMath Embedded Main Content -->
    <div class="channel-content-body">
      <!-- __GM_MAIN__ -->
    </div>
  </div>

  <!-- ==========================================================================
       CHANNEL 4: FINITE MATHEMATICS 1
       ========================================================================== -->
  <div class="view-container" id="view-fn">
    <div class="channel-header-bar">
      <div class="channel-header-inner">
        <div class="ch-title-wrap">
          <button class="ch-back-btn" onclick="switchChannel('landing')">&#8592; Topics Hub</button>
          <div class="ch-name">&#129513; Finite Mathematics 1 Channel</div>
        </div>
        <div class="channel-quick-links">
          <a href="#l3tess" class="ch-link">L3 &middot; Tessellations</a>
          <a href="#l4golden" class="ch-link">L4 &middot; Golden Ratio</a>
          <a href="#l5fractals" class="ch-link">L5 &middot; Fractals</a>
          <a href="#l6matrix" class="ch-link">L6 &middot; Matrix Basics</a>
          <a href="#l7matmul" class="ch-link">L7 &middot; Matrix Mult</a>
          <a href="#l7exam" class="ch-link">Finite Exam</a>
        </div>
        <div class="ch-tools">
          <a href="indexes/finite.html" target="_blank" class="tool-pill-btn">&#8599; Open Standalone</a>
        </div>
      </div>
    </div>

    <!-- Finite Embedded Main Content -->
    <div class="channel-content-body">
      <!-- __FN_MAIN__ -->
    </div>
  </div>

  <!-- ==========================================================================
       GLOBAL SEARCH MODAL
       ========================================================================== -->
  <div class="modal-backdrop" id="searchModal" onclick="closeSearchOnBackdrop(event)">
    <div class="search-modal">
      <div class="modal-search-box">
        <span style="font-size:18px;">&#128269;</span>
        <input type="text" class="modal-search-input" id="globalSearchInput" placeholder="Search concepts, formulas, questions across all 4 subjects..." oninput="handleGlobalSearch(this.value)"/>
        <button onclick="closeSearch()" style="background:none;border:none;color:var(--t3);cursor:pointer;font-size:18px;">&times;</button>
      </div>
      <div class="modal-results" id="searchResultsList">
        <div style="padding:20px;text-align:center;color:var(--t3);font-size:13px;">
          Type a search term (e.g. <em>Pascal, Netiquette, Fibonacci, Levers, Markup, Matrix, Inclusivity</em>)...
        </div>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       SCRIPTS: CHANNEL SWITCHER & SEARCH
       ========================================================================== -->
  <script>
    const searchableItems = [
      // MabKom
      { title: "5 Elemento ng Komunikasyon", channel: "mk", anchor: "aralin3", badge: "MabKom", desc: "Tagapagpadala, Mensahe, Daluyan, Tagatanggap, at Tugon (Feedback)." },
      { title: "Intrapersonal na Komunikasyon", channel: "mk", anchor: "a3intra", badge: "MabKom", desc: "Talaarawan (Diary), Dyornal, Repleksyon, at Goal Setting sa sarili." },
      { title: "Digital Identity at Netiquette", channel: "mk", anchor: "a3digital", badge: "MabKom", desc: "Active & Passive digital footprint, 2FA password protection, tamang asal online." },
      { title: "Pormal vs. Di-Pormal na Wika", channel: "mk", anchor: "a3wika", badge: "MabKom", desc: "Pagpili ng angkop na wika batay sa awdyens at sitwasyon." },
      { title: "Public-Facing na Teksto", channel: "mk", anchor: "a3public", badge: "MabKom", desc: "Blog, Komentaryo, Advocacy Post, Inclusivity, Equality, at Social Awareness." },
      { title: "3 Proseso ng Komunikasyon", channel: "mk", anchor: "a4proseso", badge: "MabKom", desc: "Pagbibigay-kahulugan (Decoding), Pakikilahok (Participation), Pagpapahayag." },
      { title: "Kamalayang Kultural at Sensibilidad", channel: "mk", anchor: "a4kultura", badge: "MabKom", desc: "Paggamit ng po/opo, pag-unawa sa pagkakaiba ng tradisyon at pag-iingat sa pananalita." },
      { title: "Pagsusulit & Answer Key sa MabKom", channel: "mk", anchor: "a3exam", badge: "MabKom", desc: "Identification, Multiple Choice, True or False question banks." },

      // Gen Science
      { title: "Simple Machines & Lever Classes", channel: "gs", anchor: "w5simple", badge: "Science", desc: "1st, 2nd, and 3rd class levers (F-L-E middle positions) and mechanical advantage." },
      { title: "Wheel & Axle, Pulleys, Ramps & Screws", channel: "gs", anchor: "w5simple", badge: "Science", desc: "Fixed vs movable pulleys, inclined planes (IMA = L/H), wedges, and screws." },
      { title: "Compound Machines", channel: "gs", anchor: "w5compound", badge: "Science", desc: "Combined MA = MA1 x MA2 x ...; bicycles, scissors, can openers, and wheelbarrows." },
      { title: "Pascal's Principle & Hydraulics", channel: "gs", anchor: "w6pascal", badge: "Science", desc: "Pressure transmitted undiminished: F1/A1 = F2/A2; hydraulic lifts and brakes." },
      { title: "Archimedes' Principle & Buoyant Force", channel: "gs", anchor: "w6arch", badge: "Science", desc: "Fb = Weight of displaced fluid; sinking vs floating conditions." },
      { title: "General Science Exam Questions & Answers", channel: "gs", anchor: "w5exam", badge: "Science", desc: "Comprehensive problem solving and identification test bank." },

      // Gen Math
      { title: "Percentages in Business & Finance", channel: "gm", anchor: "w6", badge: "Gen Math", desc: "Mark-up, Mark-down, discounts, selling price, and profit margins." },
      { title: "Simple & Compound Interest", channel: "gm", anchor: "w6", badge: "Gen Math", desc: "I = Prt and Future Value calculations for banking and loans." },
      { title: "Patterns in Life and Nature", channel: "gm", anchor: "w7", badge: "Gen Math", desc: "Symmetry, spirals, tessellations in honeycombs, and Fibonacci numbers." },
      { title: "Arithmetic & Geometric Sequences", channel: "gm", anchor: "w8", badge: "Gen Math", desc: "Common difference (d), common ratio (r), nth term formulas, and sequence sums." },
      { title: "Gen Math Exam Questions & Answers", channel: "gm", anchor: "w6exam", badge: "Gen Math", desc: "Practice problems for business math, patterns, and sequences." },

      // Finite Math
      { title: "Escher-Type Tessellations & Frieze Patterns", channel: "fn", anchor: "l3tess", badge: "Finite", desc: "Translation, reflection, rotation, glide reflection, and the 7 frieze groups." },
      { title: "Golden Ratio (Phi) & Fibonacci", channel: "fn", anchor: "l4golden", badge: "Finite", desc: "Phi = 1.6180339887; Golden rectangle, spirals, and golden triangle proportions." },
      { title: "Fractals (Sierpinski & Mandelbrot)", channel: "fn", anchor: "l5fractals", badge: "Finite", desc: "Self-similarity, Hausdorff fractal dimensions, Koch snowflake, and Julia sets." },
      { title: "Matrix Fundamentals & Operations", channel: "fn", anchor: "l6matrix", badge: "Finite", desc: "Matrix order (m x n), row/column matrices, scalar multiplication, and addition." },
      { title: "Matrix Multiplication", channel: "fn", anchor: "l7matmul", badge: "Finite", desc: "Inner dimension matching (columns of A = rows of B) and dot product rows by columns." },
      { title: "Finite Math Exam Questions & Answers", channel: "fn", anchor: "l7exam", badge: "Finite", desc: "Identification, calculation problems, and complete step-by-step solutions." }
    ];

    function switchChannel(channelKey, targetAnchor = null) {
      const views = {
        'landing': document.getElementById('view-landing'),
        'mk': document.getElementById('view-mk'),
        'gs': document.getElementById('view-gs'),
        'gm': document.getElementById('view-gm'),
        'fn': document.getElementById('view-fn')
      };

      const pills = {
        'landing': document.getElementById('pill-landing'),
        'mk': document.getElementById('pill-mk'),
        'gs': document.getElementById('pill-gs'),
        'gm': document.getElementById('pill-gm'),
        'fn': document.getElementById('pill-fn')
      };

      // Hide all views & remove active states
      Object.keys(views).forEach(k => {
        if (views[k]) views[k].classList.remove('active-view');
        if (pills[k]) pills[k].className = 'cpill';
      });

      // Show selected view & pill
      if (views[channelKey]) {
        views[channelKey].classList.add('active-view');
        if (pills[channelKey]) {
          pills[channelKey].classList.add(channelKey === 'landing' ? 'active-hub' : `active-${channelKey}`);
        }

        // Update URL hash
        window.location.hash = channelKey === 'landing' ? '' : `channel-${channelKey}`;

        // Scroll to top or anchor
        if (targetAnchor) {
          setTimeout(() => {
            const el = document.getElementById(targetAnchor);
            if (el) el.scrollIntoView({ behavior: 'smooth' });
          }, 100);
        } else {
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      }
    }

    // Search Functions
    function openSearch() {
      const modal = document.getElementById('searchModal');
      modal.classList.add('open');
      const input = document.getElementById('globalSearchInput');
      input.focus();
      input.select();
    }

    function closeSearch() {
      document.getElementById('searchModal').classList.remove('open');
    }

    function closeSearchOnBackdrop(e) {
      if (e.target.id === 'searchModal') closeSearch();
    }

    function handleGlobalSearch(query) {
      const list = document.getElementById('searchResultsList');
      const q = query.trim().toLowerCase();
      if (!q) {
        list.innerHTML = '<div style="padding:20px;text-align:center;color:var(--t3);font-size:13px;">Type a search term...</div>';
        return;
      }

      const matches = searchableItems.filter(item => 
        item.title.toLowerCase().includes(q) || 
        item.desc.toLowerCase().includes(q) ||
        item.badge.toLowerCase().includes(q)
      );

      if (matches.length === 0) {
        list.innerHTML = `<div style="padding:20px;text-align:center;color:var(--t3);font-size:13px;">No topics found for "<strong>${query}</strong>". Try another keyword!</div>`;
        return;
      }

      list.innerHTML = matches.map(item => `
        <div class="search-result-item" onclick="selectSearchResult('${item.channel}', '${item.anchor}')">
          <div class="s-res-title">
            <span class="s-res-badge" style="background:rgba(255,255,255,0.1);">${item.badge}</span>
            ${item.title}
          </div>
          <div class="s-res-snippet">${item.desc}</div>
        </div>
      `).join('');
    }

    function selectSearchResult(channel, anchor) {
      closeSearch();
      switchChannel(channel, anchor);
    }

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        openSearch();
      }
      if (e.key === 'Escape') {
        closeSearch();
      }
    });

    // Handle initial routing via Hash
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

# Combine all stylesheets
combined_styles = f"""
/* MabKom Styles */
{mk_style}

/* General Science Styles */
{gs_style}

/* General Mathematics Styles */
{gm_style}

/* Finite Mathematics Styles */
{fn_style}
"""

final_html = portal_template.replace('/* __STYLES_PLACEHOLDER__ */', combined_styles)\
                            .replace('<!-- __MK_MAIN__ -->', mk_main)\
                            .replace('<!-- __GS_MAIN__ -->', gs_main)\
                            .replace('<!-- __GM_MAIN__ -->', gm_main)\
                            .replace('<!-- __FN_MAIN__ -->', fn_main)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
print('Wrote index.html (Root) successfully! Size:', len(final_html))

with open('indexes/hub.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
print('Wrote indexes/hub.html successfully! Size:', len(final_html))
