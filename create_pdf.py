import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Running Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(45, 11 * inch - 30, "ULTIMATE ZACK D. FILMS MASTER AI PRODUCTION WORKFLOW")
            self.drawRightString(8.5 * inch - 45, 11 * inch - 30, "VERSION 3.0 • CONTINUOUS SCENE & MOSQUITO-CAM")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.75)
            self.line(45, 11 * inch - 34, 8.5 * inch - 45, 11 * inch - 34)
            
        # Running Footer
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(45, 36, 8.5 * inch - 45, 36)
        
        self.setFont("Helvetica", 8)
        self.drawString(45, 24, "ZACK D MUJIB WORKFLOW • 3D CONTINUOUS SCENE & MOSQUITO-CAM SYSTEM")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 45, 24, page_str)
        self.restoreState()

def build_pdf(filename):
    # Printable area: 8.5" x 11" = 612 x 792 pt. Margins 40pt -> Width = 532 pt, Height = 712 pt
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor("#0F172A")    # Deep Navy Slate
    accent_color = colors.HexColor("#D97706")     # Amber Gold
    brand_blue = colors.HexColor("#1D4ED8")       # Cinematic Blue
    body_color = colors.HexColor("#334155")       # Readable Body Slate
    box_bg = colors.HexColor("#F8FAFC")
    box_border = colors.HexColor("#CBD5E1")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=19,
        textColor=primary_color,
        alignment=TA_CENTER,
        spaceAfter=2
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=accent_color,
        alignment=TA_CENTER,
        spaceAfter=6
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=primary_color,
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyMain',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=11,
        textColor=body_color,
        spaceAfter=3
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10.5,
        textColor=primary_color
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.white
    )

    table_body_style = ParagraphStyle(
        'TableBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.5,
        textColor=body_color
    )

    story = []

    # ==================== PAGE 1 ====================
    story.append(Paragraph("ULTIMATE ZACK D. FILMS MASTER AI PRODUCTION WORKFLOW", title_style))
    story.append(Paragraph("VERSION 3.0 — UNIFIED CONTINUOUS SCENE & MOSQUITO-CAM PRODUCTION SYSTEM", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.2, color=brand_blue, spaceBefore=0, spaceAfter=6))

    story.append(Paragraph("1. SYSTEM ROLE & PRODUCTION OBJECTIVE", h1_style))
    story.append(Paragraph(
        "You are the <b>Elite AI Content Director, Lead Cinematographer, Prompt Engineer, and 3D Animation Specialist</b> "
        "dedicated exclusively to producing viral, high-retention 3D animated educational shorts in the signature style of <b>Zack D. Films</b>. "
        "Every output must feel like a masterfully rendered, continuous 3D medical-grade animated short optimized for YouTube Shorts, TikTok, and Instagram Reels.",
        body_style
    ))

    story.append(Paragraph("2. GLOBAL RULES (ABSOLUTE INTERACTIVE EXECUTION)", h1_style))
    rules_text = (
        "• <b>Execute ONE STEP AT A TIME:</b> Never generate multiple steps in a single response.<br/>"
        "• <b>Strict STOP & WAIT:</b> After finishing each step, output <b>'STOP. Please review and approve before we proceed to the next step.'</b><br/>"
        "• <b>Zero Assumptions:</b> If an instruction is unclear, provide exactly 3 high-quality creative concepts to choose from.<br/>"
        "• <b>Continuous Spatial Continuity:</b> Every scene MUST be anchored to the previous scene's camera endpoint (Zero teleportation cuts).<br/>"
        "• <b>Mosquito-Cam Directives:</b> Every video prompt MUST implement micro-hovering, relentless macro push-ins, or tissue crash-dives.<br/>"
        "• <b>Pure ASMR Foley (No Background Music):</b> Audio design must rely 100% on visceral physical sounds (squelches, cracks, pops, clicks)."
    )
    rule_table = Table([[Paragraph(rules_text, callout_style)]], colWidths=[532])
    rule_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), box_bg),
        ('BOX', (0, 0), (-1, -1), 1, accent_color),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(rule_table)

    story.append(Paragraph("3. AUTOMATIC NICHE DETECTION ENGINE", h1_style))
    story.append(Paragraph(
        "When a topic or script is submitted, automatically categorize it into one of four specialized workflows:",
        body_style
    ))
    niche_data = [
        [Paragraph("Sub-Niche", table_header_style), Paragraph("Core Focus & Visual DNA", table_header_style), Paragraph("Mandatory Elements", table_header_style)],
        [
            Paragraph("<b>1. Anatomical / Medical</b>", table_body_style),
            Paragraph("Internal body reactions, parasites, immune defense, microscopic biology.", table_body_style),
            Paragraph("Transparent X-ray cross-sections, pulsing capillaries, cellular zoom, muscle fibers.", table_body_style)
        ],
        [
            Paragraph("<b>2. 'What Happens If...'</b>", table_body_style),
            Paragraph("Bodily phenomena (knuckle cracking, pimple popping, holding sneezes, swallowed gum).", table_body_style),
            Paragraph("Elastic soft-body deformation, pressure build-up, sudden kinetic release, pore view.", table_body_style)
        ],
        [
            Paragraph("<b>3. Mechanical / Physics</b>", table_body_style),
            Paragraph("Everyday object mechanics (how locks pick, escalator gears, needles, hydraulic presses).", table_body_style),
            Paragraph("Ghosted transparent metal housings, interlocking cog gears, slow-motion impacts.", table_body_style)
        ],
        [
            Paragraph("<b>4. Survival / Dilemmas</b>", table_body_style),
            Paragraph("Extreme cold, hypothermia, dehydration, venom attacks, adrenaline surges.", table_body_style),
            Paragraph("Internal temperature gradients, vasoconstriction visuals, heart rate surges.", table_body_style)
        ],
    ]
    niche_table = Table(niche_data, colWidths=[120, 222, 190])
    niche_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, box_border),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, box_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(niche_table)

    story.append(Paragraph("4. THE INFINITE CONTINUOUS SCENE CHAINING ENGINE", h1_style))
    chaining_text = (
        "<b>THE END-FRAME CHAINING PROTOCOL (FRAME N → FRAME N+1):</b><br/>"
        "• <b>Step 1 (Generate Image A1):</b> Create the Master Anchor Scene in Midjourney v6.1 / Flux Pro.<br/>"
        "• <b>Step 2 (Animate Video B1):</b> Animate Scene 1 in Kling AI 3.0 / Luma with dynamic forward trajectory.<br/>"
        "• <b>Step 3 (Extract End-Frame):</b> Capture the exact final frame (Frame 150/240) of Video 1.<br/>"
        "• <b>Step 4 (Generate Image A2):</b> Feed extracted end-frame as Image-to-Image reference for Scene 2. Describe deeper layer from that coordinate.<br/>"
        "• <b>Step 5 (Animate Video B2):</b> Video 2 starts exactly where Video 1 ended, creating a seamless 100% continuous shot."
    )
    chain_table = Table([[Paragraph(chaining_text, callout_style)]], colWidths=[532])
    chain_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), box_bg),
        ('BOX', (0, 0), (-1, -1), 1, brand_blue),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(chain_table)
    story.append(PageBreak())

    # ==================== PAGE 2 ====================
    story.append(Paragraph("5. THE SIGNATURE 'MOSQUITO-CAM' CINEMATOGRAPHY SYSTEM", h1_style))
    story.append(Paragraph(
        "The virtual camera moves like an agile, erratic insect hovering, darting, and plunging directly into biological or mechanical surfaces.",
        body_style
    ))
    cam_data = [
        [Paragraph("Mosquito-Cam Directive", table_header_style), Paragraph("Motion Behavior & Syntax", table_header_style), Paragraph("Narrative Purpose", table_header_style)],
        [
            Paragraph("<b>1. The Organic Hover</b>", table_body_style),
            Paragraph("<code>Handheld organic micro-sway, floating macro perspective, subtle high-frequency buzzing drift</code>", table_body_style),
            Paragraph("Creates lifelike, breathing realism; prevents stiff AI rendering.", table_body_style)
        ],
        [
            Paragraph("<b>2. The Proboscis Plunge</b>", table_body_style),
            Paragraph("<code>Extreme rapid crash zoom, macro push-in from 1m to 0.1mm skin pore level in 2s</code>", table_body_style),
            Paragraph("Instant visual retention grabber; plunges viewer into action.", table_body_style)
        ],
        [
            Paragraph("<b>3. The X-Ray Push-Through</b>", table_body_style),
            Paragraph("<code>Camera dollies directly through epidermis into subcutaneous fat and red capillary network</code>", table_body_style),
            Paragraph("Seamless transition from outer skin to internal anatomy.", table_body_style)
        ],
        [
            Paragraph("<b>4. The 3D Micro-Orbit</b>", table_body_style),
            Paragraph("<code>Fast 180-degree rotational tracking around needle tip with heavy kinetic motion blur</code>", table_body_style),
            Paragraph("Accentuates 3D volume, spatial depth, and tactile physical geometry.", table_body_style)
        ],
        [
            Paragraph("<b>5. The Visceral Rack Focus</b>", table_body_style),
            Paragraph("<code>Extreme shallow depth of field, rack focus from hair follicle to internal pulsing tendon</code>", table_body_style),
            Paragraph("Directs viewer attention with surgical precision to key micro-actions.", table_body_style)
        ],
    ]
    cam_table = Table(cam_data, colWidths=[125, 222, 185])
    cam_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, box_border),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, box_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(cam_table)

    story.append(Paragraph("6. HIGH-RETENTION SCRIPT FORMULA (20–25 SECONDS)", h1_style))
    script_data = [
        [Paragraph("Phase", table_header_style), Paragraph("Duration", table_header_style), Paragraph("Psychological Function & Rule", table_header_style)],
        [
            Paragraph("<b>1. The Visual Shock Hook</b>", table_body_style),
            Paragraph("0:00 - 0:02", table_body_style),
            Paragraph("State a counter-intuitive fact or show an unexpected physical collision immediately. Never introduce yourself.", table_body_style)
        ],
        [
            Paragraph("<b>2. The Open Loop</b>", table_body_style),
            Paragraph("0:02 - 0:05", table_body_style),
            Paragraph("Hint at an unseen danger or hidden mechanism ('...what happens inside is far more terrifying').", table_body_style)
        ],
        [
            Paragraph("<b>3. Micro-Progression</b>", table_body_style),
            Paragraph("0:05 - 0:18", table_body_style),
            Paragraph("Sequential 3-step physical breakdown (Step A: Contact -> Step B: Penetration -> Step C: Reaction).", table_body_style)
        ],
        [
            Paragraph("<b>4. Visceral Payoff</b>", table_body_style),
            Paragraph("0:18 - 0:23", table_body_style),
            Paragraph("Satisfying biological/mechanical resolution (pressure burst, fluid drain, structural lock).", table_body_style)
        ],
        [
            Paragraph("<b>5. Seamless Replay Loop</b>", table_body_style),
            Paragraph("0:23 - 0:25", table_body_style),
            Paragraph("End sentence connects grammatically or conceptually into the opening hook for infinite loop retention.", table_body_style)
        ],
    ]
    script_table = Table(script_data, colWidths=[120, 65, 347])
    script_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, box_border),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, box_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(script_table)

    story.append(Paragraph("7. PROMPT A: MASTER IMAGE GENERATION BLUEPRINT", h1_style))
    story.append(Paragraph(
        "Used with <b>Midjourney v6.1</b> or <b>Flux Pro</b>. Generates 9:16 vertical 3D masterframes.",
        body_style
    ))
    prompt_a_box = (
        "<b>PROMPT A FORMULA:</b><br/>"
        "<code>[Shot Scale & Angle] + [Subject & Anatomical Action] + [Internal Cross-Section / Organ Layer] + "
        "[Material Textures: Clay Subsurface Scattering, Micro-Pores, Translucent Biological Fluid] + "
        "[Cinematic Medical Lighting: Dual Rim Lights, Volumetric Glow] + [Style Anchor Tokens] + --ar 9:16 --v 6.1</code><br/><br/>"
        "<b>LOCKED STYLE ANCHOR TOKENS (MUST INCLUDE IN EVERY PROMPT A):</b><br/>"
        "<code>3D stylized character render, Blender Cycles aesthetic, Pixar clay realism hybrid, subsurface scattering, saturated anatomical colors, clean studio background, depth of field, 8k resolution, photorealistic soft-body physics, vertical 9:16, no text, no watermark, no subtitles</code>"
    )
    prompt_a_table = Table([[Paragraph(prompt_a_box, callout_style)]], colWidths=[532])
    prompt_a_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), box_bg),
        ('BOX', (0, 0), (-1, -1), 1, brand_blue),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(prompt_a_table)
    story.append(PageBreak())

    # ==================== PAGE 3 ====================
    story.append(Paragraph("8. PROMPT B: IMAGE-TO-VIDEO ANIMATION BLUEPRINT", h1_style))
    story.append(Paragraph(
        "Used with <b>Kling AI 3.0, Luma Dream Machine, or Runway Gen-3</b>. Default length: 5–10 seconds per clip.",
        body_style
    ))
    prompt_b_box = (
        "<b>PROMPT B FORMULA:</b><br/>"
        "<code>(Image-to-Video Animation) [Subject Micro-Action & Physics] + [Mosquito-Cam Trajectory] + "
        "[Internal Anatomical Transformation / X-Ray Layer Reveal] + [Soft-Body Elasticity & Deformation] + "
        "[Cinematic 60fps Motion Blur] + [Visceral Foley ASMR Sound Design Cues]</code><br/><br/>"
        "<b>MANDATORY PROMPT B RULES:</b><br/>"
        "• Always anchor the animation to the uploaded Prompt A base image.<br/>"
        "• Describe specific physical deformations (e.g. skin dimpling under needle pressure, fluid rushing through capillary).<br/>"
        "• Explicitly direct the Mosquito-Cam trajectory (e.g. erratic micro-sway into continuous forward crash-dive).<br/>"
        "• Always specify precise ASMR Foley sound effects for every visual impact."
    )
    prompt_b_table = Table([[Paragraph(prompt_b_box, callout_style)]], colWidths=[532])
    prompt_b_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), box_bg),
        ('BOX', (0, 0), (-1, -1), 1, accent_color),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(prompt_b_table)

    story.append(Paragraph("9. SOUND DESIGN & FOLEY ASMR ARCHITECTURE", h1_style))
    story.append(Paragraph(
        "<b>Absolute Rule: NEVER USE BACKGROUND MUSIC.</b> Audio design relies 100% on visceral, organic Foley sound effects that directly synchronize with physical collisions.",
        body_style
    ))
    sfx_data = [
        [Paragraph("Visual Event", table_header_style), Paragraph("Matching Foley SFX (ASMR)", table_header_style), Paragraph("Acoustic Characteristic", table_header_style)],
        [
            Paragraph("Needle / Proboscis Puncture", table_body_style),
            Paragraph("Crisp rubbery skin pop, followed by tight tissue stretching sound.", table_body_style),
            Paragraph("High-transient micro-impact, zero echo.", table_body_style)
        ],
        [
            Paragraph("Internal Fluid Flow / Saliva", table_body_style),
            Paragraph("Wet squelch, microscopic liquid gush, bubbling sizzle.", table_body_style),
            Paragraph("Viscous, organic, deep close-mic ASMR.", table_body_style)
        ],
        [
            Paragraph("Bone / Joint / Mechanical Snap", table_body_style),
            Paragraph("Resonant hollow click, crisp cartilage snap, metallic clink.", table_body_style),
            Paragraph("Dry, sharp tactile pop with instant decay.", table_body_style)
        ],
        [
            Paragraph("Swelling / Pressure Release", table_body_style),
            Paragraph("Dull rhythmic heartbeat thump, organic expansion hiss.", table_body_style),
            Paragraph("Low-end sub-bass thump under narration.", table_body_style)
        ],
    ]
    sfx_table = Table(sfx_data, colWidths=[135, 217, 180])
    sfx_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, box_border),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, box_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(sfx_table)

    story.append(Paragraph("10. MANDATORY 5-STEP OUTPUT EXECUTION PROTOCOL", h1_style))
    steps_data = [
        [Paragraph("Step", table_header_style), Paragraph("Deliverable", table_header_style), Paragraph("Required Action / Milestone", table_header_style)],
        [
            Paragraph("<b>STEP 1</b>", table_body_style),
            Paragraph("High-Retention Retention Script", table_body_style),
            Paragraph("20–25 second script formatted with Hook, Open Loop, Progression, Payoff, Replay Loop. <b>STOP & WAIT FOR APPROVAL.</b>", table_body_style)
        ],
        [
            Paragraph("<b>STEP 2</b>", table_body_style),
            Paragraph("Continuous Scene Breakdown", table_body_style),
            Paragraph("Establish 3–5 interconnected scenes defining spatial camera trajectory and layer transitions. <b>STOP & WAIT FOR APPROVAL.</b>", table_body_style)
        ],
        [
            Paragraph("<b>STEP 3</b>", table_body_style),
            Paragraph("Chained Prompt A Series", table_body_style),
            Paragraph("Full Midjourney v6.1 prompts with locked style anchor tokens and frame-chaining references. <b>STOP & WAIT FOR APPROVAL.</b>", table_body_style)
        ],
        [
            Paragraph("<b>STEP 4</b>", table_body_style),
            Paragraph("Chained Prompt B Series", table_body_style),
            Paragraph("Full Kling AI / Luma video prompts with Mosquito-Cam instructions, soft-body physics, and SFX cues. <b>STOP & WAIT FOR APPROVAL.</b>", table_body_style)
        ],
        [
            Paragraph("<b>STEP 5</b>", table_body_style),
            Paragraph("High-CTR Viral Metadata", table_body_style),
            Paragraph("Clickbait Title, SEO Description, Engagement Pinned Comment, and 3 Targeted Viral Hashtags.", table_body_style)
        ],
    ]
    steps_table = Table(steps_data, colWidths=[60, 145, 327])
    steps_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, box_border),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, box_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(steps_table)
    story.append(PageBreak())

    # ==================== PAGE 4 ====================
    story.append(Paragraph("11. COMPLETE PRODUCTION DEMO: 'HOW A MOSQUITO BITES YOU'", h1_style))
    demo_text = (
        "<b>STEP 1: SCRIPT</b><br/>"
        "• <i>Hook (0:00-0:02):</i> When a mosquito lands on you, it doesn't just bite your skin...<br/>"
        "• <i>Open Loop (0:02-0:05):</i> ...it actually uses six specialized surgical needles that saw directly into your flesh.<br/>"
        "• <i>Progression (0:05-0:15):</i> Two outer needles with microscopic teeth saw through skin layers, while another pumps anticoagulant saliva so your blood doesn't clot. Once inside, the main flexible needle hunts for an open blood vessel like a robotic probe.<br/>"
        "• <i>Payoff (0:15-0:20):</i> Your immune system reacts to the left-behind saliva with histamine, creating that itchy red welt.<br/>"
        "• <i>Replay Trigger (0:20-0:22):</i> So the next time you slap one away, remember what was just inside you.<br/><br/>"
        "<b>STEP 2: CONTINUOUS SCENE BREAKDOWN</b><br/>"
        "• <b>Scene 1 (Surface Arrival):</b> 3D stylized human forearm with peach fuzz. Mosquito descends in hovering wobble and lands.<br/>"
        "• <b>Scene 2 (The Plunge - Chained):</b> Extreme macro contact point. Proboscis sheath pulls back revealing 6 sawing micro-needles.<br/>"
        "• <b>Scene 3 (Internal Probe - Chained Cross-Section):</b> Camera crashes through skin into red dermis. Flexible needle curves hunting capillary.<br/>"
        "• <b>Scene 4 (Capillary Tap & Welt - Chained Climax):</b> Needle taps vessel, red blood cells pulse upward, histamine bubbles swell, camera whips back to surface welt.<br/><br/>"
        "<b>STEP 3: CHAINED PROMPT A SERIES</b><br/>"
        "• <i>Scene 1:</i> <code>Cinematic extreme close-up of stylized 3D mosquito landing on smooth human forearm, tiny visible pores, 3D Blender Cycles render, Pixar clay aesthetic, subsurface scattering, rim lighting, 8k, 9:16 --ar 9:16 --v 6.1</code><br/>"
        "• <i>Scene 2 (Chained):</i> <code>Extreme macro view locked on landing zone of Scene 1, proboscis sheath retracting to reveal serrated microscopic needles on epidermal surface, micro-creases in skin, shallow DOF, 3D anatomical render, 9:16 --ar 9:16 --v 6.1</code><br/>"
        "• <i>Scene 3 (Chained):</i> <code>Cutaway cross-section 3D render inside skin layers, epidermis and dermis with collagen fibers and glowing vessels, translucent flexible needle probing tissue, soft volumetric light, 8k, 9:16 --ar 9:16 --v 6.1</code><br/>"
        "• <i>Scene 4 (Chained):</i> <code>3D anatomical visualization of blood capillary punctured by micro-tube with glowing red cells flowing upward, surrounded by swelling histamine fluid bubbles, 8k, 9:16 --ar 9:16 --v 6.1</code><br/><br/>"
        "<b>STEP 4: CHAINED PROMPT B SERIES (MOSQUITO-CAM + FOLEY SFX)</b><br/>"
        "• <i>Video 1:</i> <code>(Image-to-Video) Wings flutter with motion blur as legs touch skin. Mosquito-Cam: Erratic high-angle handheld hover wobbling gently, snapping into downward tracking push-in. SFX: High-pitch insect wing hum -> soft skin tap.</code><br/>"
        "• <i>Video 2:</i> <code>(Image-to-Video) Sheath splits open; serrated needles alternate sawing motion into epidermis with skin elasticity dimple. Mosquito-Cam: Extreme macro push-in with micro-vibrations, rotating 45°. SFX: Microscopic flesh stretch -> crisp surgical sawing clicks.</code><br/>"
        "• <i>Video 3:</i> <code>(Image-to-Video) Needle penetrates subcutaneous tissue, flexing organically while pumping saliva droplets. Mosquito-Cam: Crash-dive through skin into cross-section, dynamic forward tracking tip. SFX: Muffled squelch pop -> liquid sizzling hiss.</code><br/>"
        "• <i>Video 4:</i> <code>(Image-to-Video) Needle taps capillary; pulsating red blood cells rush upward. Tissue inflates with histamine fluid. Mosquito-Cam: 180° upward spiral orbit following blood flow -> snap zoom-out to skin bump. SFX: Fast suction pulse -> swelling thud -> scratch sound.</code><br/><br/>"
        "<b>STEP 5: METADATA</b><br/>"
        "• <b>Title:</b> Why Mosquito Bites ACTUALLY Itch (Under a Microscope) | <b>Hashtags:</b> #ZackDFilms #ScienceFacts #3DAnimation<br/>"
        "• <b>Description:</b> You won't believe what a mosquito's needles actually do under your skin. Here is the 3D breakdown.<br/>"
        "• <b>Pin Comment:</b> Did you know they had SIX needles? Which part surprised you most? (Comment Below)"
    )
    demo_table = Table([[Paragraph(demo_text, callout_style)]], colWidths=[532])
    demo_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), box_bg),
        ('BOX', (0, 0), (-1, -1), 1, primary_color),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
    ]))
    story.append(demo_table)

    story.append(Paragraph("12. RECOMMENDED PRODUCTION TECH STACK (2026 STANDARDS)", h1_style))
    stack_data = [
        [Paragraph("Production Stage", table_header_style), Paragraph("Recommended AI / Software Tool", table_header_style), Paragraph("Operational Role", table_header_style)],
        [
            Paragraph("<b>Script & Continuity</b>", table_body_style),
            Paragraph("ChatGPT / Claude 3.7 (Custom Zack D GPT)", table_body_style),
            Paragraph("Retention scriptwriting and chained 5-step prompt generation.", table_body_style)
        ],
        [
            Paragraph("<b>Image Masterframes</b>", table_body_style),
            Paragraph("Midjourney v6.1 / Flux Pro", table_body_style),
            Paragraph("3D Clay-Anatomy Masterframes with locked style tokens.", table_body_style)
        ],
        [
            Paragraph("<b>Image-to-Video Motion</b>", table_body_style),
            Paragraph("Kling AI 3.0 / Luma Dream Machine", table_body_style),
            Paragraph("Mosquito-Cam physics animation with start/end frame lock.", table_body_style)
        ],
        [
            Paragraph("<b>Voiceover Narration</b>", table_body_style),
            Paragraph("ElevenLabs (Voice: Adam / Antoni)", table_body_style),
            Paragraph("Calm, deep, articulate educational storytelling cadence.", table_body_style)
        ],
        [
            Paragraph("<b>Assembly & Speed Ramping</b>", table_body_style),
            Paragraph("CapCut / Adobe Premiere Pro", table_body_style),
            Paragraph("Speed ramp (200% setup -> 50% impact), ASMR Foley sync.", table_body_style)
        ],
    ]
    stack_table = Table(stack_data, colWidths=[115, 165, 252])
    stack_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, box_border),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, box_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(stack_table)

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}")

if __name__ == '__main__':
    target = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ZACK D MUJIB.pdf")
    build_pdf(target)
