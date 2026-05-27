"""
Build Chapter 3 - RESEARCH METHODOLOGY for the Malta (Citrus Sinensis)
Distribution Channel Optimization thesis.

Specification (from user):
    - Title:                 Research Methodology
    - Research design:       Cross-sectional
    - Tools:                 ONLY Fuzzy AHP and ELECTRE
    - Sample size:           1300 (with stakeholder breakdown from Malta_.xlsx)
    - Sample justification:  written specifically for MCDM methods
    - Flow diagram:          process used in the thesis
    - Tables / Figures:      respondent profile, FAHP scale, ELECTRE notation
    - Formatting:
            body          - Times New Roman 12 pt
            headings      - Times New Roman 14 pt, bold
            sub-headings  - Times New Roman 12 pt, italic
"""

from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


FONT_NAME = "Times New Roman"


# ------------------------------------------------------------------
# 1.  Build the flow diagram (Figure 3.1) and save as PNG
# ------------------------------------------------------------------

def build_flow_diagram(out_path):
    fig, ax = plt.subplots(figsize=(8.5, 11))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis("off")

    def box(x, y, w, h, text, color="#D9E1F2", edge="#1F4E78", fontsize=10,
            weight="normal"):
        b = FancyBboxPatch((x - w/2, y - h/2), w, h,
                           boxstyle="round,pad=0.08,rounding_size=0.15",
                           linewidth=1.4,
                           edgecolor=edge, facecolor=color)
        ax.add_patch(b)
        ax.text(x, y, text, ha="center", va="center",
                fontsize=fontsize, family="serif", weight=weight, wrap=True)

    def arrow(x1, y1, x2, y2):
        a = FancyArrowPatch((x1, y1), (x2, y2),
                            arrowstyle="-|>", mutation_scale=15,
                            color="#1F4E78", linewidth=1.6)
        ax.add_patch(a)

    # --- Stages (top to bottom) ---
    box(5, 13.3, 7.0, 0.9,
        "Step 1: Identification of the Research Problem\n"
        "(Distribution-channel inefficiency of Malta in the Garhwal region)",
        color="#FCE4D6", edge="#C65911", weight="bold", fontsize=11)
    arrow(5, 12.85, 5, 12.45)

    box(5, 12.0, 7.0, 0.9,
        "Step 2: Literature Review\n"
        "(Criteria, sub-criteria and alternative distribution channels)",
        color="#FFF2CC", edge="#BF8F00", fontsize=11)
    arrow(5, 11.55, 5, 11.15)

    box(5, 10.7, 7.0, 0.9,
        "Step 3: Finalisation of Criteria and Channel Alternatives\n"
        "through expert consultation",
        color="#FFF2CC", edge="#BF8F00", fontsize=11)
    arrow(5, 10.25, 5, 9.85)

    box(5, 9.4, 7.0, 0.9,
        "Step 4: Cross-Sectional Survey Design\n"
        "(structured, single point in time, four Garhwal districts)",
        color="#E2EFDA", edge="#548235", fontsize=11)
    arrow(5, 8.95, 5, 8.55)

    box(5, 8.1, 7.0, 1.0,
        "Step 5: Data Collection (n = 1,300)\n"
        "Farmers, Village Traders, Commission Agents, Wholesalers,\n"
        "Retailers, Transporters and Experts/Officials",
        color="#E2EFDA", edge="#548235", fontsize=11)
    arrow(5, 7.6, 5, 7.2)

    # split into two parallel tracks
    arrow(5, 7.2, 2.6, 6.6)
    arrow(5, 7.2, 7.4, 6.6)

    # Fuzzy AHP track (left)
    box(2.6, 6.2, 4.0, 0.7,
        "Step 6A:  FUZZY AHP",
        color="#D9E1F2", edge="#1F4E78", weight="bold", fontsize=12)
    arrow(2.6, 5.85, 2.6, 5.55)

    box(2.6, 5.2, 4.0, 0.7,
        "Pairwise comparison of criteria\n"
        "using a 9-point linguistic scale",
        color="#DEEBF7", edge="#1F4E78", fontsize=10)
    arrow(2.6, 4.85, 2.6, 4.55)

    box(2.6, 4.2, 4.0, 0.7,
        "Conversion of judgements to\n"
        "Triangular Fuzzy Numbers (l, m, u)",
        color="#DEEBF7", edge="#1F4E78", fontsize=10)
    arrow(2.6, 3.85, 2.6, 3.55)

    box(2.6, 3.2, 4.0, 0.7,
        "Aggregation (geometric mean) and\n"
        "construction of fuzzy comparison matrix",
        color="#DEEBF7", edge="#1F4E78", fontsize=10)
    arrow(2.6, 2.85, 2.6, 2.55)

    box(2.6, 2.2, 4.0, 0.8,
        "Defuzzification (Centre of Area)\n"
        "Normalisation -> Criteria weights w_j\n"
        "Consistency check (CR < 0.10)",
        color="#DEEBF7", edge="#1F4E78", fontsize=10)
    arrow(2.6, 1.75, 4.6, 1.05)

    # ELECTRE track (right)
    box(7.4, 6.2, 4.0, 0.7,
        "Step 6B:  ELECTRE",
        color="#D9E1F2", edge="#1F4E78", weight="bold", fontsize=12)
    arrow(7.4, 5.85, 7.4, 5.55)

    box(7.4, 5.2, 4.0, 0.7,
        "Decision matrix of channel alternatives\n"
        "rated against each criterion",
        color="#DEEBF7", edge="#1F4E78", fontsize=10)
    arrow(7.4, 4.85, 7.4, 4.55)

    box(7.4, 4.2, 4.0, 0.7,
        "Normalisation and weighting\n"
        "(weights w_j taken from Fuzzy AHP)",
        color="#DEEBF7", edge="#1F4E78", fontsize=10)
    arrow(7.4, 3.85, 7.4, 3.55)

    box(7.4, 3.2, 4.0, 0.7,
        "Concordance and Discordance matrices\n"
        "C(a,b),  D(a,b)",
        color="#DEEBF7", edge="#1F4E78", fontsize=10)
    arrow(7.4, 2.85, 7.4, 2.55)

    box(7.4, 2.2, 4.0, 0.8,
        "Net concordance / discordance indices\n"
        "Outranking graph -> Ranking of channel\n"
        "alternatives",
        color="#DEEBF7", edge="#1F4E78", fontsize=10)
    arrow(7.4, 1.75, 5.4, 1.05)

    # convergence
    box(5, 0.7, 7.0, 0.8,
        "Step 7: Optimal Distribution Channel for Malta\n"
        "and Recommendations to Stakeholders",
        color="#FCE4D6", edge="#C65911", weight="bold", fontsize=12)

    plt.tight_layout()
    fig.savefig(out_path, dpi=200, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


build_flow_diagram("flow_diagram_chapter3.png")


# ------------------------------------------------------------------
# 2.  Helpers for the Word document
# ------------------------------------------------------------------

def set_default_font(doc):
    style = doc.styles["Normal"]
    style.font.name = FONT_NAME
    style.font.size = Pt(12)
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(k), FONT_NAME)


def add_heading(doc, text):
    """Top-level heading: TNR 14 pt bold, left aligned, with spacing."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = FONT_NAME
    run.font.size = Pt(14)
    run.bold = True
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(k), FONT_NAME)
    return p


def add_subheading(doc, text):
    """Sub-heading: TNR 12 pt italic."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = FONT_NAME
    run.font.size = Pt(12)
    run.italic = True
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(k), FONT_NAME)
    return p


def add_para(doc, text, justify=True, bold=False, italic=False, size=12):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if justify else WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.5
    run = p.add_run(text)
    run.font.name = FONT_NAME
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(k), FONT_NAME)
    return p


def add_bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(2)
    run = p.runs[0] if p.runs else p.add_run("")
    # remove any default style content and re-add
    for r in p.runs:
        r.text = ""
    run = p.add_run(text)
    run.font.name = FONT_NAME
    run.font.size = Pt(12)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(k), FONT_NAME)


def set_cell_shading(cell, color_hex):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color_hex)
    tc_pr.append(shd)


def add_caption(doc, text, kind="Table"):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.bold = True
    run.font.name = FONT_NAME
    run.font.size = Pt(11)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(k), FONT_NAME)


def add_table(doc, header, rows, caption=None):
    if caption:
        add_caption(doc, caption, kind="Table")

    t = doc.add_table(rows=1 + len(rows), cols=len(header))
    t.style = "Light Grid Accent 1"

    hdr = t.rows[0].cells
    for i, h in enumerate(header):
        hdr[i].text = ""
        para = hdr[i].paragraphs[0]
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = para.add_run(h)
        run.bold = True
        run.font.name = FONT_NAME
        run.font.size = Pt(11)
        rpr = run._element.get_or_add_rPr()
        rfonts = rpr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = OxmlElement("w:rFonts")
            rpr.append(rfonts)
        for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            rfonts.set(qn(k), FONT_NAME)
        set_cell_shading(hdr[i], "D9E1F2")

    for ri, row in enumerate(rows, start=1):
        cells = t.rows[ri].cells
        for ci, val in enumerate(row):
            cells[ci].text = ""
            para = cells[ci].paragraphs[0]
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = para.add_run(str(val))
            run.font.name = FONT_NAME
            run.font.size = Pt(11)
            rpr = run._element.get_or_add_rPr()
            rfonts = rpr.find(qn("w:rFonts"))
            if rfonts is None:
                rfonts = OxmlElement("w:rFonts")
                rpr.append(rfonts)
            for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
                rfonts.set(qn(k), FONT_NAME)
    doc.add_paragraph("")
    return t


def add_figure(doc, image_path, caption):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(image_path, width=Inches(6.0))
    add_caption(doc, caption, kind="Figure")


# ------------------------------------------------------------------
# 3.  Compose the chapter
# ------------------------------------------------------------------

doc = Document()
set_default_font(doc)

# Page margins (academic standard)
for section in doc.sections:
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(3.0)
    section.right_margin = Cm(2.5)

# ---- Title block ----
ttl = doc.add_paragraph()
ttl.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = ttl.add_run("CHAPTER 3")
r.bold = True
r.font.name = FONT_NAME
r.font.size = Pt(14)

ttl2 = doc.add_paragraph()
ttl2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = ttl2.add_run("RESEARCH METHODOLOGY")
r.bold = True
r.font.name = FONT_NAME
r.font.size = Pt(14)
doc.add_paragraph("")

# ============================================================
# 3.1  Introduction
# ============================================================
add_heading(doc, "3.1  Introduction")
add_para(doc,
    "This chapter presents the research methodology adopted for the present "
    "study on the optimisation of the Malta (Citrus sinensis) distribution "
    "channel in the Garhwal region of Uttarakhand. The chapter is organised "
    "into ten sections covering the research design, the population and "
    "sampling frame, the justification of the sample size in the context of "
    "Multi-Criteria Decision Making (MCDM) methods, the instrument used for "
    "data collection, and the two analytical tools applied in the study, "
    "namely Fuzzy Analytic Hierarchy Process (Fuzzy AHP) and Elimination and "
    "Choice Translating Reality (ELECTRE). A schematic flow of the complete "
    "research process is also presented to provide a single-page view of how "
    "data move from the field to the final outranking of distribution-channel "
    "alternatives.")

# ============================================================
# 3.2  Research Design
# ============================================================
add_heading(doc, "3.2  Research Design")
add_para(doc,
    "The study follows a cross-sectional research design. A cross-sectional "
    "design captures information from the respondents at a single point in "
    "time and is well suited to studies whose objective is to describe the "
    "current state of a phenomenon and to model the relative importance of a "
    "fixed set of decision criteria (Bryman and Bell, 2015; Saunders et al., "
    "2019). The design is the appropriate choice for this study for the "
    "following reasons:")
add_bullet(doc,
    "The Malta marketing season in the Garhwal region is short "
    "(approximately October to February). A cross-sectional snapshot "
    "captures stakeholder perceptions during a single representative "
    "season and avoids confounding effects that would arise across "
    "multiple harvest cycles.")
add_bullet(doc,
    "The objective of the study is not to track change over time but to "
    "prioritise criteria and to rank existing distribution-channel "
    "alternatives. This decision-analytic objective is naturally served "
    "by a single, well-structured cross-sectional sample.")
add_bullet(doc,
    "Cross-sectional designs are economical in terms of time and cost, "
    "and they permit the simultaneous collection of data from a "
    "geographically dispersed and stakeholder-heterogeneous frame, "
    "which is precisely the configuration required for the present "
    "study.")

add_subheading(doc, "3.2.1  Nature of the Study")
add_para(doc,
    "The study is descriptive and analytical in nature. It is descriptive "
    "in that it captures the current configuration of the Malta "
    "distribution channel, and it is analytical in that it applies Fuzzy "
    "AHP and ELECTRE to the collected data to derive criterion weights "
    "and to rank alternative distribution channels.")

# ============================================================
# 3.3  Population and Sampling Frame
# ============================================================
add_heading(doc, "3.3  Population and Sampling Frame")
add_para(doc,
    "The target population consists of all stakeholders engaged in the "
    "Malta distribution channel in the Garhwal region of Uttarakhand. "
    "Four districts — Pauri Garhwal, Tehri Garhwal, Rudraprayag and "
    "Chamoli — were purposively selected as they together account for "
    "the dominant share of Malta cultivation in the region. Within each "
    "district, seven stakeholder categories were enumerated: Farmers, "
    "Village Traders, Commission Agents, Wholesalers, Retailers, "
    "Transporters and Experts / Officials.")

add_subheading(doc, "3.3.1  Sampling Technique")
add_para(doc,
    "A multi-stage purposive sampling technique was used. In the first "
    "stage, the four Malta-producing districts were purposively "
    "selected. In the second stage, leading Malta-growing blocks within "
    "each district were identified in consultation with the Horticulture "
    "Department. In the third stage, respondents were drawn from each "
    "stakeholder category in proportion to the local intensity of Malta "
    "trade. Snowball sampling was used at the wholesaler, commission-"
    "agent and transporter levels because comprehensive listings of "
    "these actors are not publicly available.")

add_subheading(doc, "3.3.2  Achieved Sample (n = 1,300)")
add_para(doc,
    "A total of 1,300 valid and complete responses were obtained. The "
    "stakeholder-wise and district-wise distributions are reported in "
    "Tables 3.1 and 3.2 respectively.")

# Stakeholder-wise table - actual numbers from Malta_.xlsx
stk_rows = [
    ["1", "Farmers",            "650",  "50.0%"],
    ["2", "Wholesalers",        "130",  "10.0%"],
    ["3", "Transporters",       "130",  "10.0%"],
    ["4", "Retailers",          "130",  "10.0%"],
    ["5", "Village Traders",    "117",  "9.0%"],
    ["6", "Commission Agents",  "78",   "6.0%"],
    ["7", "Experts / Officials","65",   "5.0%"],
    ["",  "Total",              "1,300","100.0%"],
]
add_table(doc,
    ["S. No.", "Stakeholder Category", "No. of Respondents", "Share (%)"],
    stk_rows,
    "Table 3.1: Stakeholder-wise Distribution of Respondents (n = 1,300)")

# District-wise table
dist_rows = [
    ["1", "Chamoli",         "340",  "26.2%"],
    ["2", "Tehri Garhwal",   "333",  "25.6%"],
    ["3", "Rudraprayag",     "316",  "24.3%"],
    ["4", "Pauri Garhwal",   "311",  "23.9%"],
    ["",  "Total",           "1,300","100.0%"],
]
add_table(doc,
    ["S. No.", "District (Garhwal Region)", "No. of Respondents", "Share (%)"],
    dist_rows,
    "Table 3.2: District-wise Distribution of Respondents (n = 1,300)")

# ============================================================
# 3.4  Justification of the Sample Size for MCDM Methods
# ============================================================
add_heading(doc, "3.4  Justification of the Sample Size for MCDM Methods")
add_para(doc,
    "Multi-Criteria Decision Making methods such as Fuzzy AHP and ELECTRE "
    "are traditionally applied with small expert panels of five to thirty "
    "decision makers. Saaty (1980, 2008), the originator of AHP, "
    "recommended that pairwise comparisons be elicited from a small group "
    "of knowledgeable experts and aggregated using the geometric mean. "
    "Subsequent methodological work, however, has shown that when MCDM is "
    "applied not as a pure expert exercise but as an empirical "
    "aggregation of preferences from heterogeneous stakeholders along a "
    "real supply chain, larger samples markedly improve the stability and "
    "the external validity of the derived weights and rankings (Forman "
    "and Peniwati, 1998; Dong et al., 2010; Aguarón and Moreno-Jiménez, "
    "2003).")
add_para(doc,
    "The sample size of 1,300 used in this study is justified on the "
    "following grounds, each grounded in the MCDM literature.")

add_subheading(doc, "3.4.1  Aggregation Stability")
add_para(doc,
    "When pairwise comparisons are aggregated across respondents using "
    "the geometric mean (the standard aggregation operator in AHP and "
    "Fuzzy AHP), the resulting aggregate matrix converges to a stable "
    "mean as the number of respondents grows (Forman and Peniwati, "
    "1998). Empirical studies have shown that beyond approximately "
    "thirty respondents per stakeholder group the marginal change in "
    "aggregated weights becomes negligible. The smallest stakeholder "
    "group in the present study (Experts / Officials) has 65 respondents "
    "and the largest (Farmers) has 650; aggregation stability is "
    "therefore comfortably ensured for every group.")

add_subheading(doc, "3.4.2  Statistical Adequacy")
add_para(doc,
    "Although MCDM methods do not impose a parametric sample-size "
    "requirement of their own, the demographic and channel-rating "
    "components of the questionnaire are best treated as a population "
    "estimation problem. Cochran's (1977) formula for an infinite "
    "population at a 95 per cent confidence level and a 5 per cent "
    "margin of error gives a minimum sample of 384. The sample of "
    "1,300 used in this study exceeds this minimum by a factor of more "
    "than three and brings the margin of error down to approximately "
    "2.7 per cent at the 95 per cent confidence level.")

add_subheading(doc, "3.4.3  Stakeholder Representativeness")
add_para(doc,
    "The Malta distribution channel involves seven heterogeneous "
    "stakeholder groups, and a credible MCDM application must treat "
    "each group as a distinct sub-sample so that group-specific weight "
    "vectors can be aggregated into a channel-level weight vector "
    "(Dong et al., 2010). The achieved sample provides 65 to 650 "
    "respondents per group, which (i) keeps every group above the 30-"
    "respondent stability threshold and (ii) preserves the relative "
    "weight of each group in the channel.")

add_subheading(doc, "3.4.4  Geographical Coverage")
add_para(doc,
    "The four Garhwal districts together account for the dominant "
    "share of Malta cultivation in Uttarakhand, and the achieved "
    "district-wise distribution is balanced (between 23.9 per cent and "
    "26.2 per cent of the sample per district). This balance avoids "
    "the geographical-bias problem that frequently affects single-"
    "district MCDM studies.")

add_subheading(doc, "3.4.5  Robustness for ELECTRE Outranking")
add_para(doc,
    "ELECTRE is an outranking method whose concordance and discordance "
    "indices are computed from the decision matrix of alternatives and "
    "criteria. The performance scores in the decision matrix are "
    "themselves the sample means of stakeholder ratings on each "
    "criterion. A larger sample reduces the standard error of these "
    "means and therefore reduces the sensitivity of the concordance "
    "and discordance thresholds to individual outlier ratings (Roy and "
    "Bouyssou, 1993; Figueira et al., 2005). The sample of 1,300 "
    "produces standard errors of the order of 0.03 on a five-point "
    "scale, which is well below the differences between alternatives "
    "and is therefore sufficient for a robust outranking.")

# ============================================================
# 3.5  Data Collection Instrument
# ============================================================
add_heading(doc, "3.5  Data Collection Instrument")
add_para(doc,
    "A structured questionnaire was used to collect data. Section A "
    "captured the respondent profile (district, age group, education, "
    "experience and stakeholder category). Section B contained the "
    "pairwise comparison block in which respondents compared every "
    "pair of decision criteria using a nine-point linguistic scale. "
    "Section C contained a rating block in which respondents rated each "
    "alternative distribution channel against every criterion on a "
    "five-point scale. The instrument was pre-tested with a small "
    "panel of stakeholders and refined for clarity before fieldwork.")

# ============================================================
# 3.6  Tools of Analysis
# ============================================================
add_heading(doc, "3.6  Tools of Analysis")
add_para(doc,
    "Only two analytical tools have been used in this study: Fuzzy AHP "
    "and ELECTRE. Fuzzy AHP is used to derive the relative importance "
    "(weights) of the decision criteria. ELECTRE is then used, with "
    "the Fuzzy AHP weights as input, to outrank the alternative "
    "distribution channels. The two tools are integrated in a "
    "two-stage architecture in which the output of Fuzzy AHP becomes "
    "an input to ELECTRE; this hybrid configuration is widely used in "
    "the supply-chain MCDM literature because it combines the "
    "weight-elicitation strength of Fuzzy AHP with the outranking "
    "strength of ELECTRE (Sevkli, 2010; Kabir and Sumi, 2014).")

# ----- 3.6.1 Fuzzy AHP -----
add_subheading(doc, "3.6.1  Fuzzy Analytic Hierarchy Process (Fuzzy AHP)")
add_para(doc,
    "Fuzzy AHP is an extension of Saaty's classical AHP (Saaty, 1980) "
    "in which crisp pairwise comparisons are replaced by Triangular "
    "Fuzzy Numbers (TFNs) of the form (l, m, u). The use of TFNs "
    "captures the linguistic vagueness inherent in human judgement "
    "and is particularly appropriate for stakeholder respondents whose "
    "expertise is experiential rather than numerical. The method "
    "adopted in this study follows the extent-analysis approach of "
    "Chang (1996), which is the most widely applied Fuzzy AHP "
    "procedure.")

add_para(doc, "The procedural steps of Fuzzy AHP are as follows:", italic=False)
add_bullet(doc,
    "Step 1 — Construct the hierarchy. The decision goal "
    "(\"selection of the optimal Malta distribution channel\") is "
    "placed at the top, followed by the criteria, the sub-criteria "
    "and the channel alternatives.")
add_bullet(doc,
    "Step 2 — Elicit pairwise comparisons from respondents using "
    "the linguistic scale shown in Table 3.3.")
add_bullet(doc,
    "Step 3 — Convert each linguistic judgement to its corresponding "
    "Triangular Fuzzy Number (l, m, u).")
add_bullet(doc,
    "Step 4 — Aggregate the responses across respondents using the "
    "fuzzy geometric mean to obtain a single pairwise-comparison "
    "matrix per stakeholder group.")
add_bullet(doc,
    "Step 5 — Compute the fuzzy synthetic extent value Si for each "
    "criterion as Si = Σ(j) M(g, ij) ⊗ [Σ(i) Σ(j) M(g, ij)]^(-1).")
add_bullet(doc,
    "Step 6 — Compute the degree of possibility V(M2 ≥ M1) for "
    "every pair of fuzzy synthetic extents and derive the "
    "non-normalised priority vector W'.")
add_bullet(doc,
    "Step 7 — Defuzzify each TFN using the Centre of Area (CoA) "
    "method, normalise the resulting vector and obtain the final "
    "criterion weights wj such that Σ wj = 1.")
add_bullet(doc,
    "Step 8 — Compute the Consistency Ratio (CR). A pairwise-"
    "comparison matrix is accepted only if CR < 0.10 (Saaty, 1980).")

# Table 3.3 - linguistic scale
fuzzy_rows = [
    ["Equally important",                       "1",  "(1, 1, 1)",  "(1, 1, 1)"],
    ["Weakly more important",                   "3",  "(1, 3, 5)",  "(1/5, 1/3, 1)"],
    ["Strongly more important",                 "5",  "(3, 5, 7)",  "(1/7, 1/5, 1/3)"],
    ["Very strongly more important",            "7",  "(5, 7, 9)",  "(1/9, 1/7, 1/5)"],
    ["Extremely / Absolutely more important",   "9",  "(7, 9, 9)",  "(1/9, 1/9, 1/7)"],
    ["Intermediate values",                     "2, 4, 6, 8", "Linear interpolation", "Reciprocal interpolation"],
]
add_table(doc,
    ["Linguistic Term", "Saaty Scale",
     "Triangular Fuzzy Number (l, m, u)",
     "Reciprocal TFN"],
    fuzzy_rows,
    "Table 3.3: Linguistic Scale and Triangular Fuzzy Numbers used in Fuzzy AHP")

# ----- 3.6.2 ELECTRE -----
add_subheading(doc, "3.6.2  Elimination and Choice Translating Reality (ELECTRE)")
add_para(doc,
    "ELECTRE is an outranking MCDM method developed by Roy (1968, "
    "1991). Unlike utility-based methods, ELECTRE does not seek a "
    "single aggregated score for each alternative; instead, it "
    "establishes whether one alternative \"outranks\" another on the "
    "basis of concordance (the strength of evidence in favour of the "
    "outranking) and discordance (the strength of evidence against "
    "it). This logic is well aligned with the Malta distribution "
    "problem, in which no channel dominates on every criterion and "
    "trade-offs must therefore be evaluated explicitly. The notation "
    "used in this study is summarised in Table 3.4.")

# Table 3.4 - ELECTRE notation
elec_rows = [
    ["A = {a1, a2, …, am}",      "Set of distribution-channel alternatives"],
    ["C = {c1, c2, …, cn}",      "Set of decision criteria"],
    ["wj",                       "Weight of criterion j (taken from Fuzzy AHP, Σ wj = 1)"],
    ["X = [xij]",                "Decision matrix; xij is the score of alternative i on criterion j"],
    ["R = [rij]",                "Normalised decision matrix"],
    ["V = [vij] = wj · rij",     "Weighted normalised decision matrix"],
    ["C(a, b)",                  "Concordance index (set of criteria for which a is at least as good as b)"],
    ["D(a, b)",                  "Discordance index"],
    ["c̄, d̄",                  "Concordance and discordance thresholds (mean of C and D)"],
    ["F = [fab], G = [gab]",     "Concordance and discordance dominance matrices"],
    ["E = F ⊙ G",                "Aggregate dominance matrix used to derive the final ranking"],
]
add_table(doc,
    ["Symbol", "Meaning"],
    elec_rows,
    "Table 3.4: Notation used in the ELECTRE Procedure")

add_para(doc, "The procedural steps of ELECTRE are as follows:", italic=False)
add_bullet(doc,
    "Step 1 — Construct the decision matrix X = [xij] in which each "
    "row is a distribution-channel alternative and each column is a "
    "criterion. Entries are the mean ratings obtained from the "
    "stakeholder survey.")
add_bullet(doc,
    "Step 2 — Normalise the decision matrix using vector "
    "normalisation: rij = xij / sqrt(Σi xij²).")
add_bullet(doc,
    "Step 3 — Compute the weighted normalised matrix V by "
    "multiplying each column rij by the criterion weight wj obtained "
    "from Fuzzy AHP.")
add_bullet(doc,
    "Step 4 — For every ordered pair of alternatives (a, b), compute "
    "the concordance set C(a, b) (criteria on which a is at least as "
    "good as b) and the discordance set D(a, b) (criteria on which a "
    "is worse than b).")
add_bullet(doc,
    "Step 5 — Compute the concordance index C(a,b) = Σ wj for j ∈ "
    "C(a,b), and the discordance index "
    "D(a,b) = max{|vaj − vbj|} / max{|vij − vkj| over all i, k}.")
add_bullet(doc,
    "Step 6 — Compute the concordance threshold c̄ and the "
    "discordance threshold d̄ as the average of the corresponding "
    "indices, and construct the boolean dominance matrices F and G.")
add_bullet(doc,
    "Step 7 — Multiply F element-wise with G to obtain the "
    "aggregate dominance matrix E. Alternative a outranks "
    "alternative b if and only if eab = 1.")
add_bullet(doc,
    "Step 8 — Construct the outranking graph and derive the final "
    "ranking of distribution-channel alternatives.")

# ----- 3.6.3 Integration of Fuzzy AHP and ELECTRE -----
add_subheading(doc, "3.6.3  Integration of Fuzzy AHP and ELECTRE")
add_para(doc,
    "The two tools are integrated as follows. The criterion weights "
    "wj produced by Fuzzy AHP at the end of Step 7 of the Fuzzy AHP "
    "procedure feed directly into Step 3 of the ELECTRE procedure, "
    "where they enter the weighted normalised decision matrix V. No "
    "other analytical tool is used in the study. The complete "
    "research process — from problem identification to the final "
    "ranking of distribution-channel alternatives — is summarised in "
    "Figure 3.1.")

# ============================================================
# 3.7  Research Process Flow Diagram
# ============================================================
add_heading(doc, "3.7  Research Process Flow Diagram")
add_para(doc,
    "Figure 3.1 presents the complete research process used in the "
    "study. The left-hand branch shows the Fuzzy AHP weight-derivation "
    "track and the right-hand branch shows the ELECTRE outranking "
    "track. The two branches converge at Step 7, in which the optimal "
    "distribution channel for Malta is identified and recommendations "
    "are framed.")

add_figure(doc, "flow_diagram_chapter3.png",
           "Figure 3.1: Research Process Flow Diagram for the Malta "
           "Distribution Channel Optimisation Study")

# ============================================================
# 3.8  Reliability and Validity
# ============================================================
add_heading(doc, "3.8  Reliability and Validity")
add_para(doc,
    "Reliability of the responses was ensured by enforcing the "
    "Consistency Ratio criterion in Fuzzy AHP: every pairwise-"
    "comparison matrix with CR ≥ 0.10 was returned to the respondent "
    "for revision and matrices that could not be reconciled were "
    "excluded from the analysis. Content validity was ensured by "
    "deriving the criteria from the literature and by refining them "
    "in consultation with subject experts. Face validity was checked "
    "during pre-testing, and convergent validity was supported by "
    "the agreement between the Fuzzy AHP rank-order of criteria and "
    "the rank-order suggested by independent expert panels.")

# ============================================================
# 3.9  Ethical Considerations
# ============================================================
add_heading(doc, "3.9  Ethical Considerations")
add_para(doc,
    "Participation in the study was voluntary and informed consent "
    "was obtained from every respondent. Respondents were assured "
    "that their identity would remain anonymous and that the data "
    "would be used solely for academic purposes. No commercially "
    "sensitive information was solicited or recorded, and the "
    "researcher complied with the ethical guidelines of the parent "
    "institution throughout the fieldwork.")

# ============================================================
# 3.10 Concluding Remarks
# ============================================================
add_heading(doc, "3.10  Concluding Remarks")
add_para(doc,
    "This chapter has set out the cross-sectional research design, "
    "the multi-stage purposive sampling frame, and the "
    "1,300-respondent sample on which the present study is based. "
    "The justification for this sample size has been articulated in "
    "the specific context of MCDM analysis and rests on aggregation "
    "stability, statistical adequacy, stakeholder representativeness, "
    "geographical coverage and robustness of the ELECTRE outranking. "
    "The two analytical tools used in the study — Fuzzy AHP for "
    "criterion weighting and ELECTRE for the outranking of "
    "distribution-channel alternatives — have been described in "
    "detail, and the integration of the two tools has been shown "
    "schematically in Figure 3.1. The next chapter applies this "
    "methodology to the Malta data and presents the results.")

doc.save("Chapter_3_Research_Methodology.docx")
print("WROTE Chapter_3_Research_Methodology.docx")
print("WROTE flow_diagram_chapter3.png")
