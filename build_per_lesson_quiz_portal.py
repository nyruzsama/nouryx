import os
import json
import re

from build_quiz_data import ALL_LESSON_QUIZZES

quiz_json = json.dumps(ALL_LESSON_QUIZZES)

def build_portal():
    html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
  <title>MUJIB Study Hub &middot; Summative Reviewer &amp; Interactive Lesson Quizzes</title>
  <meta name="description" content="All-in-One Comprehensive Summative Exam Reviewer with Short Summary and Long Detailed modes, sample visual diagrams, and multiple-choice quizzes after every lesson."/>
  
  <!-- Modern Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet"/>

  <!-- Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

  <style>
/* ==========================================================================
   LIGHT MODERN THEME & TOKENS
   ========================================================================== */
:root {{
  --font-display: 'Outfit', sans-serif;
  --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Crisp Light Colors */
  --bg: #f8fafc;
  --bg-surface: #ffffff;
  --bg-subtle: #f1f5f9;
  --bg-card: #ffffff;
  --border: #e2e8f0;
  --border-focus: #cbd5e1;

  --t1: #0f172a;       /* Primary dark */
  --t2: #334155;       /* Secondary body */
  --t3: #64748b;       /* Muted */

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
  --success-border: #a7f3d0;
  --error: #ef4444;
  --error-bg: #fef2f2;
  --error-border: #fecaca;

  --radius-sm: 10px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-full: 9999px;

  --shadow-sm: 0 2px 6px rgba(0, 0, 0, 0.03);
  --shadow-md: 0 8px 20px rgba(15, 23, 42, 0.06);
  --shadow-lg: 0 16px 36px rgba(15, 23, 42, 0.09);
  --shadow-card: 0 4px 16px rgba(0, 0, 0, 0.04);
}}

*, *::before, *::after {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}}

html {{
  scroll-behavior: smooth;
  color-scheme: light;
}}

body {{
  font-family: var(--font-body);
  background-color: var(--bg);
  color: var(--t1);
  line-height: 1.65;
  font-size: 15px;
  min-height: 100vh;
  letter-spacing: 0.01em;
  padding-bottom: 75px;
}}

::selection {{
  background: rgba(37, 99, 235, 0.2);
  color: var(--t1);
}}

/* ==========================================================================
   TOP GLOBAL BAR
   ========================================================================== */
.top-bar {{
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  padding: 10px 20px;
  transition: all 0.3s;
}}

.top-bar-inner {{
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}}

.brand {{
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
}}

.brand-badge {{
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
}}

.brand-text {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 18px;
  letter-spacing: -0.02em;
  color: var(--t1);
}}
.brand-text span {{ color: #2563eb; }}

.top-center-mode {{
  display: flex;
  align-items: center;
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-full);
  padding: 3px;
  gap: 3px;
}}

.mode-btn {{
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
}}
.mode-btn.active-mode {{
  background: #ffffff;
  color: var(--t1);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
}}
.mode-btn.active-mode.mode-summary {{ color: #2563eb; }}
.mode-btn.active-mode.mode-detailed {{ color: #7c3aed; }}

.top-actions {{
  display: flex;
  align-items: center;
  gap: 8px;
}}

.btn-search {{
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
}}
.btn-search:hover {{
  background: #ffffff;
  border-color: #cbd5e1;
  color: var(--t1);
}}

/* Desktop Channels */
.desktop-pills {{
  display: flex;
  align-items: center;
  gap: 6px;
}}
@media (max-width: 860px) {{
  .desktop-pills {{ display: none; }}
}}

.dpill {{
  padding: 6px 14px;
  border-radius: var(--radius-full);
  font-size: 12.5px;
  font-weight: 700;
  border: 1px solid transparent;
  background: transparent;
  color: var(--t3);
  cursor: pointer;
  transition: all 0.2s;
}}
.dpill:hover {{ color: var(--t1); background: var(--bg-subtle); }}
.dpill.active-hub {{ background: #eff6ff; color: #2563eb; border-color: #bfdbfe; }}
.dpill.active-mk {{ background: #fff1f2; color: #e11d48; border-color: #fecdd3; }}
.dpill.active-gs {{ background: #f0fdfa; color: #0d9488; border-color: #99f6e4; }}
.dpill.active-gm {{ background: #eff6ff; color: #2563eb; border-color: #bfdbfe; }}
.dpill.active-fn {{ background: #fffbeb; color: #d97706; border-color: #fde68a; }}

/* ==========================================================================
   MOBILE BOTTOM NAVIGATION
   ========================================================================== */
.mobile-bottom-nav {{
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
}}
@media (min-width: 861px) {{
  .mobile-bottom-nav {{ display: none; }}
  body {{ padding-bottom: 0; }}
}}

.mob-tab {{
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
}}
.mob-tab-icon {{ font-size: 18px; }}
.mob-tab-lbl {{ font-size: 10px; font-weight: 700; letter-spacing: -0.01em; }}
.mob-tab.active-tab {{ color: #2563eb; }}
.mob-tab.active-tab.tab-mk {{ color: #e11d48; }}
.mob-tab.active-tab.tab-gs {{ color: #0d9488; }}
.mob-tab.active-tab.tab-gm {{ color: #2563eb; }}
.mob-tab.active-tab.tab-fn {{ color: #d97706; }}

/* ==========================================================================
   VIEW SWITCHING & MODE LOGIC
   ========================================================================== */
.view-container {{
  display: none;
  animation: viewFade 0.25s ease forwards;
}}
.view-container.active-view {{
  display: block;
}}
@keyframes viewFade {{
  from {{ opacity: 0; transform: translateY(6px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}

/* Mode content toggling */
body.mode-is-summary .mode-detailed-content {{ display: none !important; }}
body.mode-is-summary .mode-summary-content {{ display: block !important; }}

body.mode-is-detailed .mode-summary-content {{ display: none !important; }}
body.mode-is-detailed .mode-detailed-content {{ display: block !important; }}

/* ==========================================================================
   LANDING PAGE (WITH 2 CHOICES)
   ========================================================================== */
.hero {{
  padding: 40px 20px 30px;
  text-align: center;
  background: radial-gradient(circle at 50% 0%, #eff6ff 0%, #ffffff 75%);
  border-bottom: 1px solid var(--border);
}}

.hero-pill {{
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
}}

.hero-title {{
  font-family: var(--font-display);
  font-size: clamp(28px, 6vw, 48px);
  font-weight: 900;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: var(--t1);
  margin-bottom: 12px;
}}
.hero-title .grad-text {{
  background: linear-gradient(135deg, #2563eb, #e11d48, #d97706);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}}

.hero-subtitle {{
  font-size: clamp(14px, 2.5vw, 16px);
  color: var(--t2);
  max-width: 640px;
  margin: 0 auto 24px;
  line-height: 1.6;
}}

/* Landing Page 2 Choices */
.mode-choice-container {{
  max-width: 760px;
  margin: 0 auto 26px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}}
@media (max-width: 600px) {{
  .mode-choice-container {{ grid-template-columns: 1fr; }}
}}

.mode-card {{
  background: #ffffff;
  border: 2px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 18px 20px;
  text-align: left;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  box-shadow: var(--shadow-sm);
}}
.mode-card:hover {{
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}}
.mode-card.selected-mode-card {{
  border-color: #2563eb;
  background: #f8faff;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
}}
.mode-card.card-detailed.selected-mode-card {{
  border-color: #7c3aed;
  background: #faf8ff;
  box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.15);
}}

.mode-card-badge {{
  display: inline-block;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: var(--radius-full);
  margin-bottom: 8px;
}}
.mode-card.card-summary .mode-card-badge {{ background: #eff6ff; color: #2563eb; }}
.mode-card.card-detailed .mode-card-badge {{ background: #f5f3ff; color: #7c3aed; }}

.mode-card-title {{
  font-family: var(--font-display);
  font-size: 17px;
  font-weight: 800;
  color: var(--t1);
  margin-bottom: 4px;
}}
.mode-card-desc {{
  font-size: 12.5px;
  color: var(--t2);
  line-height: 1.45;
}}

/* Topics Grid */
.landing-grid-container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px 20px 60px;
}}
.section-head {{ margin-bottom: 20px; }}
.section-head h2 {{
  font-family: var(--font-display);
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--t1);
}}
.section-head p {{ font-size: 13px; color: var(--t3); }}

.topics-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}}

.subject-card {{
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
}}
.subject-card::before {{
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
}}
.subject-card:hover {{
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}}

.card-mk::before {{ background: var(--mk-grad); }}
.card-mk:hover {{ border-color: var(--mk-border); }}
.card-gs::before {{ background: var(--gs-grad); }}
.card-gs:hover {{ border-color: var(--gs-border); }}
.card-gm::before {{ background: var(--gm-grad); }}
.card-gm:hover {{ border-color: var(--gm-border); }}
.card-fn::before {{ background: var(--fn-grad); }}
.card-fn:hover {{ border-color: var(--fn-border); }}

.card-top {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}}
.card-icon-box {{
  width: 46px;
  height: 46px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
}}
.card-mk .card-icon-box {{ background: var(--mk-bg); color: var(--mk-color); }}
.card-gs .card-icon-box {{ background: var(--gs-bg); color: var(--gs-color); }}
.card-gm .card-icon-box {{ background: var(--gm-bg); color: var(--gm-color); }}
.card-fn .card-icon-box {{ background: var(--fn-bg); color: var(--fn-color); }}

.card-badge {{
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: var(--radius-full);
}}
.card-mk .card-badge {{ background: var(--mk-bg); color: var(--mk-color); border: 1px solid var(--mk-border); }}
.card-gs .card-badge {{ background: var(--gs-bg); color: var(--gs-color); border: 1px solid var(--gs-border); }}
.card-gm .card-badge {{ background: var(--gm-bg); color: var(--gm-color); border: 1px solid var(--gm-border); }}
.card-fn .card-badge {{ background: var(--fn-bg); color: var(--fn-color); border: 1px solid var(--fn-border); }}

.card-title {{
  font-family: var(--font-display);
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--t1);
  margin-bottom: 8px;
}}
.card-desc {{
  font-size: 13.5px;
  color: var(--t2);
  line-height: 1.5;
  margin-bottom: 16px;
}}

.keyword-chips {{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 20px;
}}
.kw-chip {{
  font-size: 11px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  background: var(--bg-subtle);
  color: var(--t3);
}}

.card-bottom {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 14px;
  border-top: 1px solid var(--border);
}}
.btn-open-channel {{
  font-size: 13px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}}
.card-mk .btn-open-channel {{ color: var(--mk-color); }}
.card-gs .btn-open-channel {{ color: var(--gs-color); }}
.card-gm .btn-open-channel {{ color: var(--gm-color); }}
.card-fn .btn-open-channel {{ color: var(--fn-color); }}

/* ==========================================================================
   SUBJECT CHANNEL STYLES
   ========================================================================== */
.channel-top-bar {{
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
}}

.ch-back-link {{
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
}}
.ch-back-link:hover {{ background: #ffffff; color: var(--t1); }}

.ch-heading {{
  font-family: var(--font-display);
  font-size: 16px;
  font-weight: 800;
  color: var(--t1);
}}

.channel-container {{
  max-width: 960px;
  margin: 0 auto;
  padding: 24px 20px 80px;
}}

/* Subject Header Banner */
.subj-header-card {{
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-bottom: 24px;
  border: 1px solid;
}}
.subj-header-card.mk {{ background: var(--mk-bg); border-color: var(--mk-border); }}
.subj-header-card.gs {{ background: var(--gs-bg); border-color: var(--gs-border); }}
.subj-header-card.gm {{ background: var(--gm-bg); border-color: var(--gm-border); }}
.subj-header-card.fn {{ background: var(--fn-bg); border-color: var(--fn-border); }}

.shc-badge {{
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 8px;
}}
.shc-badge.mk {{ color: var(--mk-color); }}
.shc-badge.gs {{ color: var(--gs-color); }}
.shc-badge.gm {{ color: var(--gm-color); }}
.shc-badge.fn {{ color: var(--fn-color); }}

.shc-title {{
  font-family: var(--font-display);
  font-size: clamp(22px, 4vw, 32px);
  font-weight: 900;
  letter-spacing: -0.02em;
  color: var(--t1);
  margin-bottom: 8px;
}}
.shc-desc {{ font-size: 14px; color: var(--t2); line-height: 1.5; }}

/* Lesson Card */
.lesson-card {{
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
}}

.lesson-head {{
  display: flex;
  align-items: center;
  gap: 12px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 18px;
}}
.lesson-num {{
  width: 38px;
  height: 38px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-display);
  font-weight: 900;
  font-size: 15px;
}}
.lesson-num.mk {{ background: var(--mk-bg); color: var(--mk-color); }}
.lesson-num.gs {{ background: var(--gs-bg); color: var(--gs-color); }}
.lesson-num.gm {{ background: var(--gm-bg); color: var(--gm-color); }}
.lesson-num.fn {{ background: var(--fn-bg); color: var(--fn-color); }}

.lesson-title {{
  font-family: var(--font-display);
  font-size: 18px;
  font-weight: 800;
  color: var(--t1);
}}

/* Concept Grid */
.concept-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 12px;
  margin-bottom: 18px;
}}

.concept-item {{
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 12px 14px;
}}
.c-keyword {{
  font-weight: 800;
  font-size: 13.5px;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}}
.c-keyword.mk {{ color: var(--mk-color); }}
.c-keyword.gs {{ color: var(--gs-color); }}
.c-keyword.gm {{ color: var(--gm-color); }}
.c-keyword.fn {{ color: var(--fn-color); }}
.c-meaning {{
  font-size: 13px;
  color: var(--t2);
  line-height: 1.45;
}}

/* Detailed Long-Form Styles */
.detailed-section {{
  margin: 16px 0 20px;
}}
.det-p {{
  font-size: 14.5px;
  color: var(--t2);
  line-height: 1.7;
  margin-bottom: 14px;
}}
.det-list {{
  padding-left: 20px;
  margin-bottom: 16px;
  color: var(--t2);
}}
.det-list li {{ margin-bottom: 8px; font-size: 14px; line-height: 1.6; }}
.det-list strong {{ color: var(--t1); }}

.det-example-box {{
  background: #f8fafc;
  border-left: 4px solid #2563eb;
  padding: 14px 18px;
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  margin: 14px 0;
  font-size: 13.5px;
  color: var(--t2);
  line-height: 1.6;
}}
.det-example-box.mk {{ border-color: var(--mk-color); background: var(--mk-bg); }}
.det-example-box.gs {{ border-color: var(--gs-color); background: var(--gs-bg); }}
.det-example-box.gm {{ border-color: var(--gm-color); background: var(--gm-bg); }}
.det-example-box.fn {{ border-color: var(--fn-color); background: var(--fn-bg); }}

.det-subtitle {{
  font-family: var(--font-display);
  font-size: 15.5px;
  font-weight: 800;
  color: var(--t1);
  margin: 16px 0 8px;
}}

/* Formula Box */
.formula-box {{
  background: #ffffff;
  border: 1.5px dashed #cbd5e1;
  border-radius: var(--radius-md);
  padding: 14px 18px;
  margin: 16px 0;
  font-family: var(--font-mono);
  font-size: 13.5px;
  font-weight: 700;
  color: var(--t1);
}}
.formula-label {{
  font-family: var(--font-body);
  font-size: 11px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--t3);
  margin-bottom: 6px;
}}

/* Infographic Image Card */
.diagram-card {{
  margin: 20px 0;
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid var(--border);
  background: #ffffff;
  box-shadow: var(--shadow-sm);
}}
.diagram-card img {{
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
}}
.diagram-caption {{
  padding: 10px 14px;
  font-size: 12px;
  font-weight: 600;
  color: var(--t3);
  background: var(--bg-subtle);
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 6px;
}}

/* ==========================================================================
   DEDICATED QUIZ BUTTON CATEGORY AFTER EVERY LESSON
   ========================================================================== */
.quiz-category-box {{
  margin-top: 22px;
  padding: 16px 18px;
  border-radius: var(--radius-md);
  background: #ffffff;
  border: 1.5px solid var(--border);
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
  transition: all 0.2s;
}}
.quiz-category-box:hover {{
  border-color: #cbd5e1;
  box-shadow: 0 6px 16px rgba(15, 23, 42, 0.06);
}}

.quiz-cat-left {{
  display: flex;
  align-items: center;
  gap: 12px;
}}
.quiz-cat-icon {{
  width: 42px;
  height: 42px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  background: #eff6ff;
  color: #2563eb;
  flex-shrink: 0;
}}
.quiz-cat-title {{
  font-family: var(--font-display);
  font-size: 14.5px;
  font-weight: 800;
  color: var(--t1);
}}
.quiz-cat-sub {{
  font-size: 12px;
  color: var(--t3);
}}

.btn-start-quiz {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 22px;
  border-radius: var(--radius-full);
  font-size: 13.5px;
  font-weight: 800;
  color: #ffffff;
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  border: none;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
  transition: all 0.2s;
  white-space: nowrap;
}}
.btn-start-quiz:hover {{
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(37, 99, 235, 0.4);
}}
.btn-start-quiz.mk {{ background: var(--mk-grad); box-shadow: 0 4px 12px rgba(225, 29, 72, 0.3); }}
.btn-start-quiz.gs {{ background: var(--gs-grad); box-shadow: 0 4px 12px rgba(13, 148, 136, 0.3); }}
.btn-start-quiz.gm {{ background: var(--gm-grad); box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3); }}
.btn-start-quiz.fn {{ background: var(--fn-grad); box-shadow: 0 4px 12px rgba(217, 119, 6, 0.3); }}

/* ==========================================================================
   INTERACTIVE QUIZ MODAL (ONE QUESTION AT A TIME)
   ========================================================================== */
.quiz-modal-backdrop {{
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
}}
.quiz-modal-backdrop.open {{ display: flex; }}

.quiz-card-modal {{
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
}}
@keyframes popIn {{
  from {{ opacity: 0; transform: scale(0.94); }}
  to {{ opacity: 1; transform: scale(1); }}
}}

.quiz-modal-header {{
  padding: 16px 20px;
  background: var(--bg-subtle);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}}
.quiz-modal-title {{
  font-family: var(--font-display);
  font-size: 15px;
  font-weight: 800;
  color: var(--t1);
}}
.btn-close-quiz {{
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
}}
.btn-close-quiz:hover {{ background: rgba(0,0,0,0.05); color: var(--t1); }}

.quiz-progress-bar-wrap {{
  height: 4px;
  background: #e2e8f0;
  width: 100%;
}}
.quiz-progress-bar-fill {{
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #2563eb, #10b981);
  transition: width 0.3s ease;
}}

.quiz-body {{ padding: 24px 20px; overflow-y: auto; }}
.quiz-q-counter {{
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--t3);
  margin-bottom: 8px;
}}
.quiz-q-text {{
  font-family: var(--font-display);
  font-size: 18px;
  font-weight: 800;
  color: var(--t1);
  line-height: 1.35;
  margin-bottom: 20px;
}}

.quiz-options-list {{
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
}}

.quiz-opt-btn {{
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
  width: 100%;
}}
.quiz-opt-btn:hover:not(:disabled) {{
  border-color: #94a3b8;
  background: #f8fafc;
}}
.quiz-opt-letter {{
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
}}

/* Correct/Wrong Option States */
.quiz-opt-btn.opt-correct {{
  background: var(--success-bg) !important;
  border-color: var(--success) !important;
  color: #065f46 !important;
}}
.quiz-opt-btn.opt-correct .quiz-opt-letter {{
  background: var(--success) !important;
  color: #ffffff !important;
}}
.quiz-opt-btn.opt-wrong {{
  background: var(--error-bg) !important;
  border-color: var(--error) !important;
  color: #991b1b !important;
  animation: shake 0.3s ease;
}}
.quiz-opt-btn.opt-wrong .quiz-opt-letter {{
  background: var(--error) !important;
  color: #ffffff !important;
}}
@keyframes shake {{
  0%, 100% {{ transform: translateX(0); }}
  25% {{ transform: translateX(-4px); }}
  75% {{ transform: translateX(4px); }}
}}

/* Feedback Box */
.quiz-feedback-box {{
  display: none;
  padding: 12px 16px;
  border-radius: var(--radius-md);
  margin-bottom: 16px;
  font-size: 13.5px;
  font-weight: 700;
}}
.quiz-feedback-box.correct-fb {{
  display: block;
  background: var(--success-bg);
  color: #065f46;
  border: 1px solid var(--success-border);
}}
.quiz-feedback-box.wrong-fb {{
  display: block;
  background: var(--error-bg);
  color: #b91c1c;
  border: 1px solid var(--error-border);
}}
.wrong-tag {{
  display: inline-block;
  background: #fee2e2;
  color: #ef4444;
  padding: 2px 8px;
  border-radius: 4px;
  font-weight: 900;
  margin-right: 4px;
}}

.quiz-modal-footer {{
  padding: 14px 20px;
  background: var(--bg-subtle);
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 10px;
}}

.btn-quiz-next {{
  padding: 10px 24px;
  border-radius: var(--radius-full);
  font-size: 14px;
  font-weight: 800;
  color: #ffffff;
  background: #2563eb;
  border: none;
  cursor: pointer;
  display: none;
}}
.btn-quiz-next.show {{ display: inline-flex; align-items: center; gap: 6px; }}

.btn-continue-topic {{
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
}}
.btn-continue-topic:hover {{
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.45);
}}

/* Finished View */
.quiz-finished-view {{ text-align: center; padding: 30px 10px; }}
.quiz-finished-emoji {{ font-size: 48px; margin-bottom: 12px; }}
.quiz-finished-score {{
  font-family: var(--font-display);
  font-size: 26px;
  font-weight: 900;
  color: var(--t1);
  margin-bottom: 6px;
}}
.quiz-finished-msg {{ font-size: 14px; color: var(--t2); margin-bottom: 24px; }}

/* ==========================================================================
   SEARCH MODAL
   ========================================================================== */
.search-modal-backdrop {{
  position: fixed;
  inset: 0;
  z-index: 2000;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(8px);
  display: none;
  align-items: flex-start;
  justify-content: center;
  padding: 60px 16px 20px;
}}
.search-modal-backdrop.open {{ display: flex; }}
.search-dialog {{
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  width: 100%;
  max-width: 580px;
  box-shadow: var(--shadow-lg);
  overflow: hidden;
}}
.search-input-box {{
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 18px;
  border-bottom: 1px solid var(--border);
}}
.search-input {{
  border: none;
  outline: none;
  font-size: 15px;
  font-family: inherit;
  width: 100%;
  color: var(--t1);
}}
.search-results-list {{ max-height: 360px; overflow-y: auto; padding: 8px; }}
.s-res-card {{
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: background 0.15s;
}}
.s-res-card:hover {{ background: var(--bg-subtle); }}
.s-res-t {{ font-weight: 800; font-size: 13.5px; color: var(--t1); }}
.s-res-d {{ font-size: 12px; color: var(--t3); margin-top: 2px; }}

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
        Choose your preferred study depth below, then tap a subject to start reviewing with interactive quizzes after every lesson.
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
            <span style="font-size:12px;color:var(--t3);font-weight:600;">5 Quizzes Available</span>
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
            <span style="font-size:12px;color:var(--t3);font-weight:600;">5 Quizzes Available</span>
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
            <span style="font-size:12px;color:var(--t3);font-weight:600;">4 Quizzes Available</span>
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
            <span style="font-size:12px;color:var(--t3);font-weight:600;">4 Quizzes Available</span>
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

      <!-- MK LESSON 1 -->
      <section class="lesson-card" id="lesson-mk-elem">
        <div class="lesson-head">
          <div class="lesson-num mk">1</div>
          <div class="lesson-title">Aralin 3: 5 Elemento ng Komunikasyon</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword mk">Tagapagpadala (Sender)</div><div class="c-meaning">Pinagmumulan ng mensahe o impormasyon.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Mensahe (Message)</div><div class="c-meaning">Ideya, impormasyon, o damdaming nais iparating.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Daluyan (Channel)</div><div class="c-meaning">Paraan ng pagpapadala (pasalita, pasulat, online/chat).</div></div>
            <div class="concept-item"><div class="c-keyword mk">Tagatanggap (Receiver)</div><div class="c-meaning">Tumatanggap at nag-iinterpret sa mensahe.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Tugon (Feedback)</div><div class="c-meaning">Sagot o reaksyon upang matiyak ang pagkakaunawaan.</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <p class="det-p">Ang <strong>komunikasyon</strong> ay ang proseso ng pagpapadala, pagtanggap, at pagpapalitan ng impormasyon, ideya, at damdamin sa pagitan ng dalawa o higit pang tao upang magkaroon ng pagkakaunawaan.</p>
            <ul class="det-list">
              <li><strong>Tagapagpadala (Sender):</strong> Ang taong may layuning magbahagi ng kaisipan o impormasyon.</li>
              <li><strong>Mensahe (Message):</strong> Ang mismong nilalaman ng komunikasyon &mdash; maaaring pormal, impormal, pasulat, o pasalita.</li>
              <li><strong>Daluyan (Channel):</strong> Ang daluyan o teknolohiyang ginagamit tulad ng bibig (pasalita), papel (liham), o internet (chat/video).</li>
              <li><strong>Tagatanggap (Receiver):</strong> Ang nagdedekowd at umiintindi sa mensahe.</li>
              <li><strong>Tugon (Feedback):</strong> Ang pagtugon na nagpapatunay kung naging matagumpay ang komunikasyon.</li>
            </ul>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: 5 Elemento ng Komunikasyon</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz mk" onclick="startLessonQuiz('mk-elem')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- MK LESSON 2 -->
      <section class="lesson-card" id="lesson-mk-intra">
        <div class="lesson-head">
          <div class="lesson-num mk">2</div>
          <div class="lesson-title">Aralin 3: Intrapersonal na Komunikasyon</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword mk">Intrapersonal</div><div class="c-meaning">Pakikipag-usap sa sarili para sa self-awareness at pagpapasya.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Talaarawan (Diary)</div><div class="c-meaning">Personal na talaan ng pang-araw-araw na damdamin at karanasan.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Dyornal (Journal)</div><div class="c-meaning">Sistematikong talaan ng mga aral, obserbasyon, at pagninilay.</div></div>
            <div class="concept-item"><div class="c-keyword mk">Goal Setting</div><div class="c-meaning">Pagtatakda ng malinaw na mithiin sa hinaharap.</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <p class="det-p">Ang <strong>Intrapersonal na Komunikasyon</strong> ay ang panloob na pakikipag-usap sa sarili. Mahalaga ito upang:</p>
            <ul class="det-list">
              <li>Makilala ang sariling kalakasan, kahinaan, at emosyon.</li>
              <li>Makatulong sa matalinong pagpapasya bago magsalita o kumilos.</li>
              <li><strong>Talaarawan (Diary):</strong> Talaan ng mga pang-araw-araw na nangyari at nilalaman ng puso.</li>
              <li><strong>Dyornal (Journal):</strong> Mas malalim na pagsusuri sa natutuhan at pagninilay sa sariling pag-unlad.</li>
              <li><strong>Repleksyon at Goal Setting:</strong> Pagtatasa sa sariling kilos at paglalatag ng plano para sa kinabukasan.</li>
            </ul>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Intrapersonal na Komunikasyon</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz mk" onclick="startLessonQuiz('mk-intra')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- MK LESSON 3 -->
      <section class="lesson-card" id="lesson-mk-digital">
        <div class="lesson-head">
          <div class="lesson-num mk">3</div>
          <div class="lesson-title">Aralin 3: Digital Identity, Footprint at Netiquette</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword mk">Active Footprint</div><div class="c-meaning">Kusang ibinabahagi online (post, photos, comments, status).</div></div>
            <div class="concept-item"><div class="c-keyword mk">Passive Footprint</div><div class="c-meaning">Awtomatikong nakokolekta (cookies, IP address, browsing history).</div></div>
            <div class="concept-item"><div class="c-keyword mk">Netiquette</div><div class="c-meaning">Wastong asal online: magalang, iwas fake news, mag-isip bago mag-post.</div></div>
            <div class="concept-item"><div class="c-keyword mk">2FA Security</div><div class="c-meaning">Two-Factor Authentication para sa proteksyon ng personal na datos.</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <h4 class="det-subtitle">Digital Identity &amp; Online Safety</h4>
            <p class="det-p">Ang bawat kilos natin sa internet ay lumilikha ng <strong>Digital Footprint</strong> na maaaring maging permanente.</p>
            <div class="det-example-box mk">
              <strong>Active Footprint:</strong> Mga bagay na kusang-loob nating inilalathala (posts, pictures, vlogs).<br>
              <strong>Passive Footprint:</strong> Datos na tahimik na naitatala ng servers (searches, device location, cookies).<br>
              <strong>Netiquette:</strong> Tamang pag-uugali &mdash; paggalang sa kapwa, pag-iwas sa cyberbullying, pagberipika ng balita bago i-share, at paggamit ng Two-Factor Authentication (2FA).
            </div>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Digital Identity &amp; Netiquette</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz mk" onclick="startLessonQuiz('mk-digital')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- MK LESSON 4 -->
      <section class="lesson-card" id="lesson-mk-proseso">
        <div class="lesson-head">
          <div class="lesson-num mk">4</div>
          <div class="lesson-title">Aralin 4: 3 Proseso ng Komunikasyon</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword mk">1. Pagbibigay-kahulugan</div><div class="c-meaning">Decoding batay sa sariling karanasan, kultura, at damdamin.</div></div>
            <div class="concept-item"><div class="c-keyword mk">2. Pakikilahok</div><div class="c-meaning">Aktibong pakikinig, pagtatanong, at pakikiisa sa talakayan.</div></div>
            <div class="concept-item"><div class="c-keyword mk">3. Pagpapahayag</div><div class="c-meaning">Paggamit ng salita, kilos, at simbolo upang maipahayag ang sarili.</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <p class="det-p">Ang komunikasyon ay dinamiko at binubuo ng tatlong magkakaugnay na proseso:</p>
            <ul class="det-list">
              <li><strong>1. Pagbibigay-kahulugan (Decoding):</strong> Ang pag-unawa sa kahulugan ng mensahe. Ang salitang <code>"Sige"</code> ay maaaring magbago ang ibig sabihin depende sa tono at sitwasyon.</li>
              <li><strong>2. Pakikilahok (Participation):</strong> Ang hindi lamang pananahimik kundi aktibong pagbibigay ng atensyon at bukas na kaisipan.</li>
              <li><strong>3. Pagpapahayag (Expression):</strong> Ang paggamit ng angkop na wika at body language upang malinaw na maiparating ang kaisipan.</li>
            </ul>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: 3 Proseso ng Komunikasyon</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz mk" onclick="startLessonQuiz('mk-proseso')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- MK LESSON 5 -->
      <section class="lesson-card" id="lesson-mk-kultural">
        <div class="lesson-head">
          <div class="lesson-num mk">5</div>
          <div class="lesson-title">Aralin 4: Kamalayang Kultural at Sensibilidad</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword mk">Kamalayang Kultural</div><div class="c-meaning">Pag-unawa sa tradisyon ng iba (hal. paggamit ng "po" at "opo").</div></div>
            <div class="concept-item"><div class="c-keyword mk">Sensibilidad</div><div class="c-meaning">Pag-iisip sa damdamin ng kausap (<em>"Mayroon akong ibang pananaw"</em>).</div></div>
            <div class="concept-item"><div class="c-keyword mk">Hadlang (Noise)</div><div class="c-meaning">Ingay sa paligid, mahinang signal, at matinding galit/emosyon.</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <p class="det-p"><strong>Kamalayang Kultural:</strong> Ang bawat kultura ay may sariling pamantayan sa komunikasyon. Ang pag-alam dito ay nag-iiwas sa hindi pagkakaunawaan.</p>
            <p class="det-p"><strong>Sensibilidad sa Komunikasyon:</strong> Ang pagpili ng mga salitang magalang at hindi mapanghusga kahit may pagkakaiba sa pananaw.</p>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Kamalayang Kultural at Sensibilidad</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz mk" onclick="startLessonQuiz('mk-kultural')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
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

      <!-- GS LESSON 1 -->
      <section class="lesson-card" id="lesson-gs-levers">
        <div class="lesson-head">
          <div class="lesson-num gs">1</div>
          <div class="lesson-title">Week 5: Simple Machines &amp; Lever Classes</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gs">Work (W = F x d)</div><div class="c-meaning">Machines do <strong>NOT reduce work</strong>; they reduce effort force by increasing distance.</div></div>
            <div class="concept-item"><div class="c-keyword gs">1st Class Lever</div><div class="c-meaning"><strong>Fulcrum in middle</strong> (Seesaw, crowbar, scissors). Redirects &amp; multiplies force.</div></div>
            <div class="concept-item"><div class="c-keyword gs">2nd Class Lever</div><div class="c-meaning"><strong>Load in middle</strong> (Wheelbarrow, nutcracker). Always <strong>MA &gt; 1</strong>.</div></div>
            <div class="concept-item"><div class="c-keyword gs">3rd Class Lever</div><div class="c-meaning"><strong>Effort in middle</strong> (Tweezers, fishing rod, broom). <strong>MA &lt; 1</strong> (multiplies speed).</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <h4 class="det-subtitle">Lever Classes &amp; The F-L-E Rule</h4>
            <div class="det-example-box gs">
              <strong>1st Class (Fulcrum in Middle):</strong> Effort &mdash; Fulcrum &mdash; Load (Seesaw, pliers, crowbar).<br>
              <strong>2nd Class (Load in Middle):</strong> Fulcrum &mdash; Load &mdash; Effort (Wheelbarrow, nutcracker, bottle opener). Always MA &gt; 1.<br>
              <strong>3rd Class (Effort in Middle):</strong> Fulcrum &mdash; Effort &mdash; Load (Tweezers, broom, fishing rod, tongs). Multiplies speed (MA &lt; 1).
            </div>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Three Classes of Levers</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz gs" onclick="startLessonQuiz('gs-levers')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- GS LESSON 2 -->
      <section class="lesson-card" id="lesson-gs-pulleys">
        <div class="lesson-head">
          <div class="lesson-num gs">2</div>
          <div class="lesson-title">Week 5: Pulleys, Wheels, &amp; Inclined Planes</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gs">Fixed Pulley</div><div class="c-meaning">MA = 1 (changes force direction only, e.g. flagpole).</div></div>
            <div class="concept-item"><div class="c-keyword gs">Movable Pulley</div><div class="c-meaning">MA = 2 (multiplies effort force).</div></div>
            <div class="concept-item"><div class="c-keyword gs">Block &amp; Tackle</div><div class="c-meaning">MA = number of supporting rope segments.</div></div>
            <div class="concept-item"><div class="c-keyword gs">Inclined Plane</div><div class="c-meaning">IMA = Length / Height (Ramp, Wedge, Screw).</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <h4 class="det-subtitle">Pulleys and Inclined Planes</h4>
            <ul class="det-list">
              <li><strong>Wheel and Axle:</strong> IMA = R_wheel / R_axle (Doorknobs, steering wheels).</li>
              <li><strong>Ramp / Inclined Plane:</strong> IMA = Length / Height. Greater length reduces required pushing force.</li>
              <li><strong>Wedge:</strong> Two back-to-back inclined planes (Axes, knives, chisels).</li>
              <li><strong>Screw:</strong> An inclined plane wrapped around a cylinder in a spiral.</li>
            </ul>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Pulleys, Wheels &amp; Inclined Planes</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz gs" onclick="startLessonQuiz('gs-pulleys')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- GS LESSON 3 -->
      <section class="lesson-card" id="lesson-gs-compound">
        <div class="lesson-head">
          <div class="lesson-num gs">3</div>
          <div class="lesson-title">Week 5: Compound Machines &amp; Combined Advantage</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gs">Compound Machine</div><div class="c-meaning">Two or more simple machines combined: <strong>MA_total = MA1 x MA2 x ...</strong></div></div>
            <div class="concept-item"><div class="c-keyword gs">Friction Trade-off</div><div class="c-meaning">More moving parts create more friction, reducing overall efficiency.</div></div>
            <div class="concept-item"><div class="c-keyword gs">Examples</div><div class="c-meaning">Scissors (levers + wedges), Bicycle (wheel &amp; axle + pulleys/gears).</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <p class="det-p">When simple machines are combined into a <strong>compound machine</strong>, the output force of one component becomes the input of the next. Total MA is multiplicative:</p>
            <div class="formula-box">MA_total = MA1 x MA2 x MA3 ...</div>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Compound Machines</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz gs" onclick="startLessonQuiz('gs-compound')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- Sample Visual Diagram 2 -->
      <div class="diagram-card">
        <img src="./assets/images/pascal_archimedes.jpg" alt="Pascal and Archimedes Principles" loading="lazy"/>
        <div class="diagram-caption">&#128204; <strong>Visual Infographic:</strong> Hydraulic Lift Mechanics &amp; Buoyant Force</div>
      </div>

      <!-- GS LESSON 4 -->
      <section class="lesson-card" id="lesson-gs-pascal">
        <div class="lesson-head">
          <div class="lesson-num gs">4</div>
          <div class="lesson-title">Week 6: Pascal's Principle &amp; Hydraulics</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gs">Pascal's Principle</div><div class="c-meaning">Pressure applied to enclosed fluid is transmitted <strong>undiminished in all directions</strong>.</div></div>
            <div class="concept-item"><div class="c-keyword gs">Hydraulic Lift</div><div class="c-meaning">F2 = F1 x (A2 / A1). Small force on small piston lifts heavy load on large piston.</div></div>
            <div class="concept-item"><div class="c-keyword gs">Applications</div><div class="c-meaning">Hydraulic car lifts, automotive hydraulic brakes, heavy construction excavators.</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <p class="det-p"><strong>Pascal's Principle:</strong> Pressure in an enclosed static fluid is transmitted equally everywhere: P1 = P2 &rarr; F1/A1 = F2/A2.</p>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Pascal's Principle &amp; Hydraulics</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz gs" onclick="startLessonQuiz('gs-pascal')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- GS LESSON 5 -->
      <section class="lesson-card" id="lesson-gs-archimedes">
        <div class="lesson-head">
          <div class="lesson-num gs">5</div>
          <div class="lesson-title">Week 6: Archimedes' Principle &amp; Buoyancy</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gs">Archimedes' Principle</div><div class="c-meaning">Buoyant Force (Fb) = <strong>Weight of fluid displaced</strong> by the submerged object.</div></div>
            <div class="concept-item"><div class="c-keyword gs">Floating Condition</div><div class="c-meaning">Object floats if Fb &ge; Weight (Density &le; fluid density).</div></div>
            <div class="concept-item"><div class="c-keyword gs">Sinking Condition</div><div class="c-meaning">Object sinks if Fb &lt; Weight (Density &gt; fluid density).</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <p class="det-p"><strong>Archimedes' Law:</strong> Fb = &rho; &bull; V &bull; g. Steel ships float because the hollow air-filled hull displaces a gigantic volume of water, creating an upward buoyant force greater than the entire ship's weight.</p>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Archimedes' Principle &amp; Buoyancy</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz gs" onclick="startLessonQuiz('gs-archimedes')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
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

      <!-- GM LESSON 1 -->
      <section class="lesson-card" id="lesson-gm-markup">
        <div class="lesson-head">
          <div class="lesson-num gm">1</div>
          <div class="lesson-title">Week 6: Mark-up, Mark-down &amp; Discounts</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gm">Mark-up</div><div class="c-meaning"><strong>Mark-up = Selling Price - Cost</strong>.</div></div>
            <div class="concept-item"><div class="c-keyword gm">Mark-down</div><div class="c-meaning"><strong>Sale Price = Regular Price - Discount</strong>.</div></div>
            <div class="concept-item"><div class="c-keyword gm">Mark-up Rate</div><div class="c-meaning">Rate = (Mark-up / Cost) x 100%.</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <h4 class="det-subtitle">Business Percentages Cheatsheet</h4>
            <div class="det-example-box gm">
              Cost = ₱400, Selling Price = ₱550 &rarr; Mark-up = ₱150.<br>
              Regular Price = ₱1,000 with 25% discount &rarr; Discount = ₱250, Sale Price = ₱750.
            </div>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Mark-up &amp; Mark-down</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz gm" onclick="startLessonQuiz('gm-markup')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- GM LESSON 2 -->
      <section class="lesson-card" id="lesson-gm-interest">
        <div class="lesson-head">
          <div class="lesson-num gm">2</div>
          <div class="lesson-title">Week 6: Simple Interest &amp; Maturity Value</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gm">Simple Interest</div><div class="c-meaning"><strong>I = Prt</strong> (P = Principal, r = annual decimal rate, t = time in years).</div></div>
            <div class="concept-item"><div class="c-keyword gm">Maturity Value</div><div class="c-meaning"><strong>F = P + I = P(1 + rt)</strong>.</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <p class="det-p"><strong>Simple Interest Formula:</strong> I = P &bull; r &bull; t. If you invest ₱20,000 at 4% for 2 years: \(I = 20,000 \times 0.04 \times 2 = ₱1,600\). Maturity Value = ₱21,600.</p>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Simple Interest &amp; Future Value</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz gm" onclick="startLessonQuiz('gm-interest')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- Sample Visual Diagram -->
      <div class="diagram-card">
        <img src="./assets/images/fibonacci_fractals.jpg" alt="Fibonacci and Fractals in Nature" loading="lazy"/>
        <div class="diagram-caption">&#128204; <strong>Visual Infographic:</strong> Golden Ratio, Fibonacci Spiral &amp; Sierpinski Fractals</div>
      </div>

      <!-- GM LESSON 3 -->
      <section class="lesson-card" id="lesson-gm-patterns">
        <div class="lesson-head">
          <div class="lesson-num gm">3</div>
          <div class="lesson-title">Week 7: Patterns in Nature &amp; Fibonacci</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gm">Fibonacci Sequence</div><div class="c-meaning">0, 1, 1, 2, 3, 5, 8, 13, 21, 34... Each term is sum of previous two.</div></div>
            <div class="concept-item"><div class="c-keyword gm">Radial Symmetry</div><div class="c-meaning">Rotational symmetry around center (starfish, sunflower florets).</div></div>
            <div class="concept-item"><div class="c-keyword gm">Honeycomb Packing</div><div class="c-meaning">Hexagons maximize storage area with minimal wax boundary.</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <p class="det-p">Nature uses mathematical optimization: Fibonacci sequences appear in pinecone spirals, nautilus shell chambers, and sunflower seed packing.</p>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Patterns in Nature &amp; Fibonacci</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz gm" onclick="startLessonQuiz('gm-patterns')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- GM LESSON 4 -->
      <section class="lesson-card" id="lesson-gm-sequences">
        <div class="lesson-head">
          <div class="lesson-num gm">4</div>
          <div class="lesson-title">Week 8: Arithmetic &amp; Geometric Sequences</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword gm">Arithmetic Sequence</div><div class="c-meaning">Constant difference <strong>d</strong>: an = a1 + (n - 1)d.</div></div>
            <div class="concept-item"><div class="c-keyword gm">Geometric Sequence</div><div class="c-meaning">Constant ratio <strong>r</strong>: an = a1 &bull; r^(n - 1).</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <div class="formula-box">
              Arithmetic nth term: an = a1 + (n - 1)d<br>
              Arithmetic Sum: Sn = (n / 2) * (a1 + an)<br>
              Geometric nth term: an = a1 * r^(n - 1)<br>
              Geometric Sum: Sn = a1 * (1 - r^n) / (1 - r)
            </div>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Arithmetic &amp; Geometric Sequences</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz gm" onclick="startLessonQuiz('gm-sequences')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
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

      <!-- FN LESSON 1 -->
      <section class="lesson-card" id="lesson-fn-tess">
        <div class="lesson-head">
          <div class="lesson-num fn">1</div>
          <div class="lesson-title">Lesson 3: Tessellations &amp; 7 Frieze Patterns</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword fn">Tessellation</div><div class="c-meaning">Covering a 2D plane with shapes with <strong>no overlaps and no gaps</strong> (M.C. Escher).</div></div>
            <div class="concept-item"><div class="c-keyword fn">4 Isometries</div><div class="c-meaning">Translation (slide), Reflection (flip), Rotation (turn), Glide Reflection.</div></div>
            <div class="concept-item"><div class="c-keyword fn">7 Frieze Groups</div><div class="c-meaning">Exactly 7 infinite 1D symmetry groups classify all repeating band patterns.</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <p class="det-p"><strong>4 Rigid Motions (Isometries):</strong> Translation (slide), Reflection (flip), Rotation (turn), Glide Reflection (slide + flip). There are exactly 7 infinite frieze symmetry groups.</p>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Tessellations &amp; 7 Frieze Groups</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz fn" onclick="startLessonQuiz('fn-tess')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- FN LESSON 2 -->
      <section class="lesson-card" id="lesson-fn-golden">
        <div class="lesson-head">
          <div class="lesson-num fn">2</div>
          <div class="lesson-title">Lesson 4: Golden Ratio (&Phi;) &amp; Spirals</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword fn">Golden Ratio (&Phi;)</div><div class="c-meaning"><strong>&Phi; = (1 + &radic;5)/2 &asymp; 1.6180339887</strong>.</div></div>
            <div class="concept-item"><div class="c-keyword fn">Golden Rectangle</div><div class="c-meaning">Side ratio 1 : 1.618 &rarr; subdivides into logarithmic Golden Spiral.</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <p class="det-p">The Golden Ratio is found in ancient classical architecture, the human body, and logarithmic spirals in galaxies and seashells.</p>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Golden Ratio &amp; Spirals</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz fn" onclick="startLessonQuiz('fn-golden')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- FN LESSON 3 -->
      <section class="lesson-card" id="lesson-fn-fractals">
        <div class="lesson-head">
          <div class="lesson-num fn">3</div>
          <div class="lesson-title">Lesson 5: Fractals &amp; Self-Similarity</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword fn">Self-Similarity</div><div class="c-meaning">Every part has the exact same character as the whole at all magnification scales.</div></div>
            <div class="concept-item"><div class="c-keyword fn">Examples</div><div class="c-meaning">Sierpinski Gasket / Triangle, Koch Snowflake, Mandelbrot set, fern leaves.</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <p class="det-p">A fractal has infinite detail and non-integer Hausdorff dimension, commonly seen in lightning bolts, river branches, and lung bronchi.</p>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Fractals &amp; Self-Similarity</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz fn" onclick="startLessonQuiz('fn-fractals')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
        </div>
      </section>

      <!-- FN LESSON 4 -->
      <section class="lesson-card" id="lesson-fn-matrix">
        <div class="lesson-head">
          <div class="lesson-num fn">4</div>
          <div class="lesson-title">Lessons 6 &amp; 7: Matrix Algebra &amp; Multiplication</div>
        </div>

        <div class="mode-summary-content">
          <div class="concept-grid">
            <div class="concept-item"><div class="c-keyword fn">Matrix Order</div><div class="c-meaning">Size: <strong>rows x columns (m x n)</strong>.</div></div>
            <div class="concept-item"><div class="c-keyword fn">Addition / Subtraction</div><div class="c-meaning">Requires <strong>identical dimensions</strong> (add corresponding elements).</div></div>
            <div class="concept-item"><div class="c-keyword fn">Multiplication Rule</div><div class="c-meaning"><strong>Columns of A = Rows of B</strong>: (m x k) • (k x n) = (m x n).</div></div>
          </div>
        </div>

        <div class="mode-detailed-content">
          <div class="detailed-section">
            <div class="formula-box">
              Matrix Multiplication Rule:<br>
              Matrix A [m x k] &bull; Matrix B [k x n] = Matrix C [m x n]<br>
              Inner dimensions (k) must match! Matrix multiplication is non-commutative (AB != BA).
            </div>
          </div>
        </div>

        <!-- Dedicated Quiz Category Button -->
        <div class="quiz-category-box">
          <div class="quiz-cat-left">
            <div class="quiz-cat-icon">&#9997;&#65039;</div>
            <div>
              <div class="quiz-cat-title">Quiz: Matrix Operations &amp; Multiplication</div>
              <div class="quiz-cat-sub">Multiple Choice &middot; 1 question at a time &middot; Instant feedback</div>
            </div>
          </div>
          <button class="btn-start-quiz fn" onclick="startLessonQuiz('fn-matrix')">
            <span>&#127919;</span> Take Lesson Quiz
          </button>
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
          <div class="quiz-q-counter" id="quizQuestionCounter">Question 1 of 3</div>
          <div class="quiz-q-text" id="quizQuestionText">Question text here?</div>

          <div class="quiz-options-list" id="quizOptionsList">
            <!-- Options dynamically injected -->
          </div>

          <div class="quiz-feedback-box" id="quizFeedbackBox"></div>
        </div>

        <!-- Finished State -->
        <div class="quiz-finished-view" id="quizFinishedView" style="display:none;">
          <div class="quiz-finished-emoji" id="quizFinishedEmoji">&#127881;</div>
          <div class="quiz-finished-score" id="quizFinishedScore">Score: 3 / 3</div>
          <div class="quiz-finished-msg" id="quizFinishedMsg">Amazing recall! You are fully prepared for this topic.</div>
          <button class="btn-continue-topic" onclick="continueToTopic()">continue to the topic &#8594;</button>
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
       JAVASCRIPT ENGINE
       ========================================================================== -->
  <script>
    // Complete Quiz Database
    const QUIZ_DATABASE = {quiz_json};

    let activeQuizKey = null;
    let currentQIndex = 0;
    let currentScore = 0;
    let isAnswered = false;

    // Reviewer Mode Switcher
    function setReviewerMode(mode) {{
      if (mode === 'detailed') {{
        document.body.className = 'mode-is-detailed';
        document.getElementById('topBtnDetailed').classList.add('active-mode');
        document.getElementById('topBtnSummary').classList.remove('active-mode');
        
        const cardDet = document.getElementById('landingCardDetailed');
        const cardSum = document.getElementById('landingCardSummary');
        if (cardDet) cardDet.classList.add('selected-mode-card');
        if (cardSum) cardSum.classList.remove('selected-mode-card');
      }} else {{
        document.body.className = 'mode-is-summary';
        document.getElementById('topBtnSummary').classList.add('active-mode');
        document.getElementById('topBtnDetailed').classList.remove('active-mode');

        const cardDet = document.getElementById('landingCardDetailed');
        const cardSum = document.getElementById('landingCardSummary');
        if (cardSum) cardSum.classList.add('selected-mode-card');
        if (cardDet) cardDet.classList.remove('selected-mode-card');
      }}
    }}

    // Audio tones
    function playAudioTone(isCorrect) {{
      try {{
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        if (isCorrect) {{
          osc.type = 'sine';
          osc.frequency.setValueAtTime(587.33, ctx.currentTime);
          osc.frequency.setValueAtTime(880, ctx.currentTime + 0.1);
          gain.gain.setValueAtTime(0.2, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.35);
          osc.start();
          osc.stop(ctx.currentTime + 0.35);
        }} else {{
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(220, ctx.currentTime);
          osc.frequency.setValueAtTime(160, ctx.currentTime + 0.12);
          gain.gain.setValueAtTime(0.2, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
          osc.start();
          osc.stop(ctx.currentTime + 0.3);
        }}
      }} catch (e) {{}}
    }}

    // Channel Switcher
    function switchChannel(channelKey, targetLessonId = null) {{
      const views = {{
        'landing': document.getElementById('view-landing'),
        'mk': document.getElementById('view-mk'),
        'gs': document.getElementById('view-gs'),
        'gm': document.getElementById('view-gm'),
        'fn': document.getElementById('view-fn')
      }};

      const dpills = {{
        'landing': document.getElementById('dpill-landing'),
        'mk': document.getElementById('dpill-mk'),
        'gs': document.getElementById('dpill-gs'),
        'gm': document.getElementById('dpill-gm'),
        'fn': document.getElementById('dpill-fn')
      }};

      const mtabs = {{
        'landing': document.getElementById('mtab-landing'),
        'mk': document.getElementById('mtab-mk'),
        'gs': document.getElementById('mtab-gs'),
        'gm': document.getElementById('mtab-gm'),
        'fn': document.getElementById('mtab-fn')
      }};

      Object.keys(views).forEach(k => {{
        if (views[k]) views[k].classList.remove('active-view');
        if (dpills[k]) dpills[k].className = 'dpill';
        if (mtabs[k]) mtabs[k].className = 'mob-tab';
      }});

      if (views[channelKey]) {{
        views[channelKey].classList.add('active-view');
        
        if (dpills[channelKey]) {{
          dpills[channelKey].classList.add(channelKey === 'landing' ? 'active-hub' : `active-${{channelKey}}`);
        }}

        if (mtabs[channelKey]) {{
          mtabs[channelKey].classList.add('active-tab');
          if (channelKey !== 'landing') mtabs[channelKey].classList.add(`tab-${{channelKey}}`);
        }}

        window.location.hash = channelKey === 'landing' ? '' : `channel-${{channelKey}}`;

        if (targetLessonId) {{
          setTimeout(() => {{
            const el = document.getElementById(targetLessonId);
            if (el) el.scrollIntoView({{ behavior: 'smooth' }});
          }}, 100);
        }} else {{
          window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}
      }}
    }}

    // ==========================================
    // INTERACTIVE QUIZ ENGINE
    // ==========================================
    function startLessonQuiz(quizKey) {{
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
    }}

    function renderQuestion() {{
      const quiz = QUIZ_DATABASE[activeQuizKey];
      const q = quiz.questions[currentQIndex];
      const total = quiz.questions.length;
      isAnswered = false;

      // Progress bar
      const progressPercent = ((currentQIndex) / total) * 100;
      document.getElementById('quizProgressFill').style.width = progressPercent + '%';

      document.getElementById('quizQuestionCounter').textContent = `Question ${{currentQIndex + 1}} of ${{total}}`;
      document.getElementById('quizQuestionText').textContent = q.q;

      const letters = ['A', 'B', 'C', 'D'];
      const optList = document.getElementById('quizOptionsList');
      optList.innerHTML = q.options.map((opt, idx) => `
        <button class="quiz-opt-btn" id="optBtn-${{idx}}" onclick="selectAnswer(${{idx}})">
          <span class="quiz-opt-letter">${{letters[idx]}}</span>
          <span>${{opt}}</span>
        </button>
      `).join('');

      const fb = document.getElementById('quizFeedbackBox');
      fb.className = 'quiz-feedback-box';
      fb.style.display = 'none';
      document.getElementById('btnQuizNext').classList.remove('show');
    }}

    function selectAnswer(selectedIdx) {{
      if (isAnswered) return;
      isAnswered = true;

      const quiz = QUIZ_DATABASE[activeQuizKey];
      const q = quiz.questions[currentQIndex];
      const isCorrect = (selectedIdx === q.answer);

      const fb = document.getElementById('quizFeedbackBox');
      const selectedBtn = document.getElementById(`optBtn-${{selectedIdx}}`);
      const correctBtn = document.getElementById(`optBtn-${{q.answer}}`);

      // Disable all options
      q.options.forEach((_, idx) => {{
        document.getElementById(`optBtn-${{idx}}`).disabled = true;
      }});

      if (isCorrect) {{
        currentScore++;
        selectedBtn.classList.add('opt-correct');
        fb.className = 'quiz-feedback-box correct-fb';
        fb.innerHTML = '&#10004; Tumpak! Correct answer.';
        fb.style.display = 'block';
        playAudioTone(true);
      }} else {{
        selectedBtn.classList.add('opt-wrong');
        correctBtn.classList.add('opt-correct');
        fb.className = 'quiz-feedback-box wrong-fb';
        // EXACT REQUIRED TEXT: "haha mali"
        fb.innerHTML = '<span class="wrong-tag">&#10006; haha mali</span> ' + q.hint;
        fb.style.display = 'block';
        playAudioTone(false);
      }}

      // Check if last question
      const nextBtn = document.getElementById('btnQuizNext');
      if (currentQIndex < quiz.questions.length - 1) {{
        nextBtn.textContent = 'Next Question &rarr;';
        nextBtn.onclick = nextQuestion;
        nextBtn.classList.add('show');
      }} else {{
        // On last question, show "continue to the topic" or see results
        nextBtn.textContent = 'continue to the topic &rarr;';
        nextBtn.onclick = showQuizResults;
        nextBtn.classList.add('show');
      }}
    }}

    function nextQuestion() {{
      const quiz = QUIZ_DATABASE[activeQuizKey];
      if (currentQIndex < quiz.questions.length - 1) {{
        currentQIndex++;
        renderQuestion();
      }} else {{
        showQuizResults();
      }}
    }}

    function showQuizResults() {{
      const quiz = QUIZ_DATABASE[activeQuizKey];
      const total = quiz.questions.length;
      document.getElementById('quizProgressFill').style.width = '100%';

      document.getElementById('quizQuestionView').style.display = 'none';
      document.getElementById('quizModalFooter').style.display = 'none';
      document.getElementById('quizFinishedView').style.display = 'block';

      document.getElementById('quizFinishedScore').textContent = `Score: ${{currentScore}} / ${{total}}`;
      
      if (currentScore === total) {{
        document.getElementById('quizFinishedEmoji').textContent = '&#127881;';
        document.getElementById('quizFinishedMsg').textContent = 'Perfect score! Outstanding mastery of this lesson.';
        try {{ confetti({{ particleCount: 80, spread: 70, origin: {{ y: 0.6 }} }}); }} catch(e){{}}
      }} else if (currentScore >= total / 2) {{
        document.getElementById('quizFinishedEmoji').textContent = '&#128079;';
        document.getElementById('quizFinishedMsg').textContent = 'Great effort! A quick review will make it 100%.';
      }} else {{
        document.getElementById('quizFinishedEmoji').textContent = '&#128170;';
        document.getElementById('quizFinishedMsg').textContent = 'Keep practicing! Review the lesson notes above.';
      }}
    }}

    // Redirect to the reviewer topic
    function continueToTopic() {{
      closeQuiz();
      const quiz = QUIZ_DATABASE[activeQuizKey];
      const targetId = (quiz && quiz.lessonId) ? quiz.lessonId : activeQuizKey;
      const el = document.getElementById(targetId);
      if (el) {{
        el.scrollIntoView({{ behavior: 'smooth' }});
      }}
    }}

    function closeQuiz() {{
      document.getElementById('quizModal').classList.remove('open');
    }}

    // Search Engine
    const searchTerms = [
      {{ title: "5 Elemento ng Komunikasyon", channel: "mk", lessonId: "lesson-mk-elem", desc: "Sender, Message, Channel, Receiver, Feedback" }},
      {{ title: "Intrapersonal (Diary, Journal, Reflection)", channel: "mk", lessonId: "lesson-mk-intra", desc: "Pakikipag-usap sa sarili at goal setting" }},
      {{ title: "Digital Identity, Footprint & Netiquette", channel: "mk", lessonId: "lesson-mk-digital", desc: "Active vs passive footprint, 2FA, online privacy" }},
      {{ title: "3 Proseso ng Komunikasyon", channel: "mk", lessonId: "lesson-mk-proseso", desc: "Decoding, pakikilahok, ekspresyon" }},
      {{ title: "Kamalayang Kultural at Sensibilidad", channel: "mk", lessonId: "lesson-mk-kultural", desc: "Paggalang sa kultura, Noise, at sensibilidad" }},
      {{ title: "Simple Machines & 3 Lever Classes", channel: "gs", lessonId: "lesson-gs-levers", desc: "1st, 2nd, 3rd class levers (F-L-E middle rules)" }},
      {{ title: "Pulleys, Inclined Planes & Screws", channel: "gs", lessonId: "lesson-gs-pulleys", desc: "Fixed vs movable pulleys, IMA=Length/Height" }},
      {{ title: "Compound Machines & Combined MA", channel: "gs", lessonId: "lesson-gs-compound", desc: "Total MA = MA1 x MA2 x MA3..." }},
      {{ title: "Pascal's Principle & Hydraulics", channel: "gs", lessonId: "lesson-gs-pascal", desc: "Pressure transmitted undiminished: F1/A1 = F2/A2" }},
      {{ title: "Archimedes' Principle & Buoyancy", channel: "gs", lessonId: "lesson-gs-archimedes", desc: "Fb = Weight of displaced fluid; sinking vs floating" }},
      {{ title: "Mark-up, Mark-down & Discounts", channel: "gm", lessonId: "lesson-gm-markup", desc: "Cost, Selling Price, Mark-down, Discounts" }},
      {{ title: "Simple Interest (I = Prt)", channel: "gm", lessonId: "lesson-gm-interest", desc: "Principal, annual interest rate, time in years" }},
      {{ title: "Patterns in Nature & Fibonacci", channel: "gm", lessonId: "lesson-gm-patterns", desc: "0, 1, 1, 2, 3, 5, 8, 13, 21... Radial & Bilateral symmetry" }},
      {{ title: "Arithmetic & Geometric Sequences", channel: "gm", lessonId: "lesson-gm-sequences", desc: "Common difference (d) vs common ratio (r)" }},
      {{ title: "Tessellations & 7 Frieze Groups", channel: "fn", lessonId: "lesson-fn-tess", desc: "Plane tiling with no gaps; 4 isometries" }},
      {{ title: "Golden Ratio (Phi = 1.618)", channel: "fn", lessonId: "lesson-fn-golden", desc: "Phi = (1+sqrt(5))/2; Golden rectangles & spirals" }},
      {{ title: "Fractals & Sierpinski Triangle", channel: "fn", lessonId: "lesson-fn-fractals", desc: "Self-similarity repeating at infinite scales" }},
      {{ title: "Matrix Algebra & Multiplication", channel: "fn", lessonId: "lesson-fn-matrix", desc: "Inner dimensions must match; matrix operations" }}
    ];

    function openSearch() {{
      const m = document.getElementById('searchModal');
      m.classList.add('open');
      const input = document.getElementById('globalSearchInput');
      input.focus();
    }}
    function closeSearch() {{
      document.getElementById('searchModal').classList.remove('open');
    }}
    function closeSearchOnBackdrop(e) {{
      if (e.target.id === 'searchModal') closeSearch();
    }}

    function handleSearch(val) {{
      const q = val.trim().toLowerCase();
      const cont = document.getElementById('searchResultsContainer');
      if (!q) {{
        cont.innerHTML = '<div style="padding:16px;text-align:center;color:var(--t3);font-size:13px;">Type any keyword...</div>';
        return;
      }}
      const matches = searchTerms.filter(t => t.title.toLowerCase().includes(q) || t.desc.toLowerCase().includes(q));
      if (matches.length === 0) {{
        cont.innerHTML = `<div style="padding:16px;text-align:center;color:var(--t3);font-size:13px;">No keywords matching "<strong>${{val}}</strong>".</div>`;
        return;
      }}
      cont.innerHTML = matches.map(m => `
        <div class="s-res-card" onclick="selectSearchMatch('${{m.channel}}', '${{m.lessonId}}')">
          <div class="s-res-t">${{m.title}}</div>
          <div class="s-res-d">${{m.desc}}</div>
        </div>
      `).join('');
    }}

    function selectSearchMatch(channelKey, lessonId) {{
      closeSearch();
      switchChannel(channelKey, lessonId);
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      const hash = window.location.hash;
      if (hash.startsWith('#channel-')) {{
        const ch = hash.replace('#channel-', '');
        if (['mk', 'gs', 'gm', 'fn'].includes(ch)) {{
          switchChannel(ch);
        }}
      }}
    }});
  </script>
</body>
</html>
"""
    return html_code

# Generate and write
portal_html = build_portal()

# Replace any escaped characters with clean UTF-8
portal_html = portal_html.replace('\&rarr;', '➔')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(portal_html)

with open('indexes/hub.html', 'w', encoding='utf-8') as f:
    f.write(portal_html)

with open('indexes/index.html', 'w', encoding='utf-8') as f:
    f.write(portal_html)

# Standalone pages with default view activated
with open('indexes/mabkom.index.html', 'w', encoding='utf-8') as f:
    f.write(portal_html.replace('active-view', '').replace('id="view-mk"', 'id="view-mk" class="view-container active-view"'))

with open('indexes/1mabkom.index.html', 'w', encoding='utf-8') as f:
    f.write(portal_html.replace('active-view', '').replace('id="view-mk"', 'id="view-mk" class="view-container active-view"'))

with open('indexes/GenScieindex.html', 'w', encoding='utf-8') as f:
    f.write(portal_html.replace('active-view', '').replace('id="view-gs"', 'id="view-gs" class="view-container active-view"'))

with open('indexes/genmath.html', 'w', encoding='utf-8') as f:
    f.write(portal_html.replace('active-view', '').replace('id="view-gm"', 'id="view-gm" class="view-container active-view"'))

with open('indexes/finite.html', 'w', encoding='utf-8') as f:
    f.write(portal_html.replace('active-view', '').replace('id="view-fn"', 'id="view-fn" class="view-container active-view"'))

print("All files successfully built with dedicated per-lesson quiz buttons!")
