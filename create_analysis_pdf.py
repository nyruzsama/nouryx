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
            self.drawString(45, 11 * inch - 30, "CASE STUDY ANALYSIS: TEACHER SALARY MANAGEMENT & FINANCIAL STABILITY")
            self.drawRightString(8.5 * inch - 45, 11 * inch - 30, "ACADEMIC & POLICY BRIEF")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.75)
            self.line(45, 11 * inch - 34, 8.5 * inch - 45, 11 * inch - 34)
            
        # Running Footer
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(45, 36, 8.5 * inch - 45, 36)
        
        self.setFont("Helvetica", 8)
        self.drawString(45, 24, "CASE ANALYSIS REPORT • PUBLIC JUNIOR HIGH SCHOOL TEACHERS")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 45, 24, page_str)
        self.restoreState()

def build_pdf(filename):
    # Dimensions: 8.5 x 11 inch. Printable width = 612 - 80 = 532 pt
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor("#0F172A")    # Deep Navy
    accent_color = colors.HexColor("#D97706")     # Amber Gold
    brand_blue = colors.HexColor("#1D4ED8")       # Academic Slate Blue
    body_color = colors.HexColor("#334155")       # Charcoal Slate Body
    box_bg = colors.HexColor("#F8FAFC")
    box_border = colors.HexColor("#CBD5E1")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
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
        fontSize=9.5,
        leading=12.5,
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
    story.append(Paragraph("CASE STUDY ANALYSIS: SALARY MANAGEMENT & FINANCIAL VULNERABILITY AMONG PUBLIC JUNIOR HIGH SCHOOL TEACHERS", title_style))
    story.append(Paragraph("A THEORETICAL & STRUCTURAL EXAMINATION OF THE 'LITERACY-AFFORDABILITY PARADOX'", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.2, color=brand_blue, spaceBefore=0, spaceAfter=6))

    story.append(Paragraph("1. EXECUTIVE SUMMARY", h1_style))
    story.append(Paragraph(
        "This case study investigates the salary allocation, budgeting dynamics, and economic realities of public junior high school teachers. "
        "A central finding is the <b>'Literacy-Affordability Paradox'</b>: despite teachers demonstrating a proven, high level of financial literacy "
        "(Garcia, 2025, mean score = 4.02), they consistently face severe financial distress, income dissatisfaction, and budgeting difficulties "
        "(Casingal & Ancho, 2022; Jardinico et al., 2024). This analysis isolates the core structural problems from surface-level symptoms, applies grounded "
        "economic and behavioral theories, and proposes a multi-tiered, realistic intervention system at individual, institutional, and policy levels.",
        body_style
    ))

    story.append(Paragraph("2. KEY FACTS & CASE SYNTHESIS", h1_style))
    key_facts_data = [
        [Paragraph("Dimension", table_header_style), Paragraph("Empirical Finding / Evidentiary Fact", table_header_style), Paragraph("Source Citation", table_header_style)],
        [
            Paragraph("<b>Cognitive Competency</b>", table_body_style),
            Paragraph("Public junior high school teachers demonstrate a <b>high level of financial literacy</b> (overall mean score: <b>4.02</b>).", table_body_style),
            Paragraph("Garcia (2025)", table_body_style)
        ],
        [
            Paragraph("<b>Income Satisfaction</b>", table_body_style),
            Paragraph("Teachers express active dissatisfaction with their current financial income and actively seek salary increases.", table_body_style),
            Paragraph("Casingal & Ancho (2022)", table_body_style)
        ],
        [
            Paragraph("<b>Budgeting Complexity</b>", table_body_style),
            Paragraph("Allocating monthly salary is strained by multiple, competing household expenses and external family financial responsibilities.", table_body_style),
            Paragraph("Casingal & Ancho (2022)", table_body_style)
        ],
        [
            Paragraph("<b>Socio-Economic Hardship</b>", table_body_style),
            Paragraph("Teachers face significant financial hardships, struggling to make ends meet while fulfilling their vital educational responsibilities.", table_body_style),
            Paragraph("Jardinico et al. (2024)", table_body_style)
        ],
        [
            Paragraph("<b>Operational Paradox</b>", table_body_style),
            Paragraph("Adequate financial knowledge and budgeting skills <b>do not eliminate</b> real-world economic hardships or handling difficulties.", table_body_style),
            Paragraph("Integrated Synthesis", table_body_style)
        ],
    ]
    facts_table = Table(key_facts_data, colWidths=[110, 312, 110])
    facts_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, box_border),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, box_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(facts_table)

    story.append(Paragraph("3. PROBLEM IDENTIFICATION: ROOT CAUSE VS. SYMPTOMS", h1_style))
    story.append(Paragraph(
        "A critical analytical error is treating behavioral distress as the problem rather than an outcome. To build effective solutions, root causes must be distinguished from visible symptoms:",
        body_style
    ))

    problem_box = (
        "<b>OBSERVED SYMPTOMS (Surface Manifestations):</b><br/>"
        "• Teacher dissatisfaction with monthly take-home pay and persistent demands for salary increases.<br/>"
        "• Subjective feelings of financial distress, budgeting friction, and struggle to make ends meet.<br/>"
        "• Inability to maintain regular savings or emergency buffers despite high theoretical literacy.<br/><br/>"
        "<b>ROOT CORE PROBLEM: THE STRUCTURAL-OBLIGATION IMBALANCE & 'BANDWIDTH DEFICIT'</b><br/>"
        "A fundamental mismatch exists between <b>rigid fixed public-sector base compensation</b> and <b>disproportionate multi-tiered financial obligations</b> (sandwich generation dependency, un-subsidized classroom out-of-pocket spending, and high cost-of-living inflation). Financial literacy optimizes the distribution of available capital, but it cannot mathematically bridge a persistent baseline cash-flow deficit."
    )
    prob_table = Table([[Paragraph(problem_box, callout_style)]], colWidths=[532])
    prob_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), box_bg),
        ('BOX', (0, 0), (-1, -1), 1, accent_color),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(prob_table)
    story.append(PageBreak())

    # ==================== PAGE 2 ====================
    story.append(Paragraph("4. THEORETICAL FRAMEWORKS & APPLICATION", h1_style))
    story.append(Paragraph(
        "To understand why high financial literacy (4.02) does not translate into financial ease, three grounded theoretical frameworks are applied:",
        body_style
    ))

    theory_data = [
        [Paragraph("Theoretical Framework", table_header_style), Paragraph("Core Premise", table_header_style), Paragraph("Direct Application to Public School Teachers", table_header_style)],
        [
            Paragraph("<b>1. Financial Literacy-Behavior Gap</b><br/>(Fernandes et al., 2014)", table_body_style),
            Paragraph("Knowledge alone accounts for minimal variance in financial well-being; environmental constraints and liquidity exert far greater control.", table_body_style),
            Paragraph("Teachers understand budgeting mechanics, interest compounding, and saving rules, but lack the disposable surplus required to execute them.", table_body_style)
        ],
        [
            Paragraph("<b>2. Scarcity Theory & Bandwidth Tax</b><br/>(Mullainathan & Shafir, 2013)", table_body_style),
            Paragraph("Chronic economic scarcity consumes cognitive bandwidth, forcing short-term bill firefighting rather than long-term strategic compounding.", table_body_style),
            Paragraph("Juggling household obligations while managing heavy teaching duties drains mental energy, inducing financial exhaustion and stress.", table_body_style)
        ],
        [
            Paragraph("<b>3. Mental Accounting & Obligation Hierarchy</b><br/>(Thaler, 1999)", table_body_style),
            Paragraph("Income is categorized into rigid psychological accounts where immediate social/family emergencies supersede personal wealth accumulation.", table_body_style),
            Paragraph("Teachers prioritize immediate survival and dependent welfare over retirement or personal insurance, causing vulnerability to debt traps.", table_body_style)
        ],
    ]
    theory_table = Table(theory_data, colWidths=[130, 192, 210])
    theory_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, box_border),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, box_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(theory_table)

    story.append(Paragraph("5. IN-DEPTH CASE DISCUSSION: THE TEACHER FINANCIAL PRESSURE MATRIX", h1_style))
    story.append(Paragraph(
        "Public school teachers operate at the intersection of four competing financial vectors that neutralize conventional budgeting techniques:",
        body_style
    ))

    matrix_data = [
        [Paragraph("Pressure Vector", table_header_style), Paragraph("Underlying Dynamic", table_header_style), Paragraph("Socio-Economic Impact on Teacher", table_header_style)],
        [
            Paragraph("<b>1. Fixed Inflow Constraints</b>", table_body_style),
            Paragraph("Standardized government salary grades with slow step increments and statutory deductions (tax, retirement, PhilHealth).", table_body_style),
            Paragraph("Income remains rigid and inelastic against sudden inflation spikes.", table_body_style)
        ],
        [
            Paragraph("<b>2. Extended Family Dependency</b>", table_body_style),
            Paragraph("The 'Sandwich Generation' burden: supporting aging parents and schooling siblings/children simultaneously.", table_body_style),
            Paragraph("Severe dilution of per-capita purchasing power across multiple households.", table_body_style)
        ],
        [
            Paragraph("<b>3. Hidden Occupational Subsidies</b>", table_body_style),
            Paragraph("Un-reimbursed out-of-pocket spending on instructional materials, printing, classroom repairs, and student welfare.", table_body_style),
            Paragraph("Subsidizes public institutional education directly from personal disposable salary.", table_body_style)
        ],
        [
            Paragraph("<b>4. Debt Coping Trap</b>", table_body_style),
            Paragraph("Reliance on salary loans, lending cooperatives, and commercial credit to finance emergency cash shortfalls.", table_body_style),
            Paragraph("Payroll deductions diminish monthly net take-home pay, perpetuating reliance on re-loaning.", table_body_style)
        ],
    ]
    matrix_table = Table(matrix_data, colWidths=[120, 202, 210])
    matrix_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, box_border),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, box_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(matrix_table)
    story.append(PageBreak())

    # ==================== PAGE 3 ====================
    story.append(Paragraph("6. STRATEGIC SOLUTIONS & MULTI-TIERED RECOMMENDATIONS", h1_style))
    story.append(Paragraph(
        "Sustainable resolution requires simultaneous interventions across individual, institutional, and macro-policy levels:",
        body_style
    ))

    sol_box = (
        "<b>TIER 1: INDIVIDUAL / MICRO-LEVEL STRATEGIES (TEACHER LEVEL)</b><br/>"
        "• <b>Priority 'Sinking-Fund' Allocation Model:</b> Replace generic percentage formulas (e.g. 50/30/20) with a Priority Floor Model: <code>Net Pay - (Fixed Survival Needs + Micro-Emergency Buffer) = Discretionary & Dependent Cap</code>. Establish non-negotiable boundaries on extended familial remittances.<br/>"
        "• <b>Separation of Personal & Occupational Accounts:</b> Maintain a distinct micro-fund specifically for school-related supplies to prevent teaching costs from silently eroding household groceries.<br/><br/>"
        "<b>TIER 2: INSTITUTIONAL / MESO-LEVEL STRATEGIES (SCHOOL & DISTRICT LEVEL)</b><br/>"
        "• <b>Centralized Instructional Supply Packs:</b> Establish robust, school-funded procurement for all classroom printing, visual aids, and supplies, guaranteeing zero teacher out-of-pocket expenditure.<br/>"
        "• <b>Workplace Cooperative Debt Refinancing:</b> Deploy school-accredited cooperative lending programs to consolidate high-interest private loans into low-interest, long-term amortizations.<br/>"
        "• <b>Emergency Contingency Welfare Desk:</b> Provide institutional hardship grants for acute medical or domestic emergencies.<br/><br/>"
        "<b>TIER 3: POLICY / MACRO-LEVEL STRATEGIES (GOVERNMENT & DEPED LEVEL)</b><br/>"
        "• <b>Inflation-Indexed Salary Calibration:</b> Adjust base compensation to reflect real regional Cost of Living (COL) and Consumer Price Index (CPI).<br/>"
        "• <b>Enforcement of Mandatory Net Take-Home Thresholds:</b> Enforce strict statutory net take-home pay floors to safeguard educators against predatory over-borrowing."
    )
    sol_table = Table([[Paragraph(sol_box, callout_style)]], colWidths=[532])
    sol_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), box_bg),
        ('BOX', (0, 0), (-1, -1), 1, brand_blue),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(sol_table)

    story.append(Paragraph("7. IMPLEMENTATION ROADMAP & EVALUATION METRICS", h1_style))
    roadmap_data = [
        [Paragraph("Implementation Phase", table_header_style), Paragraph("Target Intervention & Deliverables", table_header_style), Paragraph("Key Performance Indicator (KPI)", table_header_style)],
        [
            Paragraph("<b>Short-Term</b><br/>(Months 1–3)", table_body_style),
            Paragraph("Comprehensive audit of teacher out-of-pocket school expenses; institutional provision of full classroom supply kits.", table_body_style),
            Paragraph("<b>100% elimination</b> of personal teacher spending on mandatory instructional materials.", table_body_style)
        ],
        [
            Paragraph("<b>Medium-Term</b><br/>(Months 3–12)", table_body_style),
            Paragraph("Cooperative-led debt consolidation facility and implementation of the priority sinking-fund budgeting framework.", table_body_style),
            Paragraph("<b>≥ 25% reduction</b> in average monthly loan amortization deductions per teacher.", table_body_style)
        ],
        [
            Paragraph("<b>Long-Term</b><br/>(Years 1–3)", table_body_style),
            Paragraph("Legislative salary standardization adjustments, regional living wage allowances, and debt ceiling enforcement.", table_body_style),
            Paragraph("Statistically significant reduction in teacher financial distress scores and improved retention rates.", table_body_style)
        ],
    ]
    roadmap_table = Table(roadmap_data, colWidths=[100, 242, 190])
    roadmap_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, box_border),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, box_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(roadmap_table)

    story.append(Paragraph("8. CONCLUSION & ACADEMIC TAKEAWAY", h1_style))
    story.append(Paragraph(
        "Public junior high school teachers do not suffer from a deficit of financial literacy (evidenced by Garcia, 2025, score of 4.02). "
        "Rather, they operate within a <b>structural liquidity trap</b> where fixed compensation is overwhelmed by multi-household obligations, "
        "unreimbursed classroom costs, and high-interest debt cycles. Meaningful resolution demands moving beyond basic budgeting education to "
        "address institutional supply burdens, predatory credit, and macroeconomic compensation alignment.",
        body_style
    ))

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}")

if __name__ == '__main__':
    target = os.path.join(os.path.dirname(os.path.abspath(__file__)), "analysis.pdf")
    build_pdf(target)
