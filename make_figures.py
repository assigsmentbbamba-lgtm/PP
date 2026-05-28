"""
Generates 10 informative figures (flowcharts, framework diagrams, charts) for
the Research Methodology chapter of the Malta Distribution Channel study.

Figures created (saved into ./figures):
  3.1  Overall research process flowchart
  3.2  Three-phase data-collection timeline
  3.3  Malta supply-chain stakeholder map
  3.4  Resource-Based View (RBV) framework diagram
  3.5  Sources used for the initial pool of 144 factors
  3.6  Factor refinement funnel (144 -> 116 -> 94 -> 82)
  3.7  Stage- and dimension-wise factor distribution (initial vs final)
  3.8  Stratified sampling tree (n = 1,300)
  3.9  Cronbach's alpha across 15 sub-scales (horizontal bar)
  3.10 Two-stage MCDM analytical pipeline (Fuzzy AHP + ELECTRE)
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

os.makedirs("figures", exist_ok=True)

# -------- consistent style --------
PRIMARY = "#1f6f8b"
SECONDARY = "#e07b00"
ACCENT = "#2e7d32"
PURPLE = "#7b1fa2"
RED = "#c62828"
DARK = "#37474f"
LIGHT = "#eef3f7"
TEXT = "#1f2933"

plt.rcParams["font.family"] = "DejaVu Serif"
plt.rcParams["font.size"] = 10
plt.rcParams["axes.edgecolor"] = TEXT
plt.rcParams["axes.labelcolor"] = TEXT
plt.rcParams["xtick.color"] = TEXT
plt.rcParams["ytick.color"] = TEXT


def box(ax, x, y, w, h, text, color=PRIMARY, text_color="white",
        fontsize=10, bold=False, italic=False):
    fb = FancyBboxPatch((x, y), w, h,
                        boxstyle="round,pad=0.02,rounding_size=0.10",
                        linewidth=1.2, edgecolor=color, facecolor=color)
    ax.add_patch(fb)
    weight = "bold" if bold else "normal"
    style = "italic" if italic else "normal"
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            color=text_color, fontsize=fontsize, weight=weight, style=style,
            wrap=True)


def arrow(ax, x1, y1, x2, y2, color=DARK, lw=1.4, style="-|>", ms=14):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                        mutation_scale=ms, linewidth=lw, color=color)
    ax.add_patch(a)


# ============================================================
# Figure 3.1 - Overall Research Process Flowchart (vertical)
# ============================================================
def fig_3_1():
    fig, ax = plt.subplots(figsize=(8.5, 12))
    ax.set_xlim(0, 10); ax.set_ylim(0, 14.2); ax.axis("off")

    items = [
        ("Problem identification\nDistribution-channel inefficiencies in the Malta supply chain (Garhwal)",
         13.2, PRIMARY),
        ("Literature review  +  Expert consultation (15 experts)  +  Field observation",
         12.0, PRIMARY),
        ("Pilot study (n = 60) — instrument refinement and language check",
         10.8, PRIMARY),
        ("Initial pool of 144 factors  (5 stages × 3 dimensions: Cost / Time / Quality)",
         9.6, SECONDARY),
        ("Step 1 — Expert content validity (CVI ≥ 3.0; overlap check)   ⇒   116 items",
         8.4, SECONDARY),
        ("Step 2 — Cronbach's α  &  item-total correlation (≥ 0.30)   ⇒   94 items",
         7.2, SECONDARY),
        ("Step 3 — Inter-rater consistency (Cohen's κ ≥ 0.60)   ⇒   82 items",
         6.0, SECONDARY),
        ("Main survey: stratified random sample (n = 1,300; 5 Garhwal districts)",
         4.7, ACCENT),
        ("Fuzzy AHP — derive weights of the 82 factors (CR < 0.10)",
         3.4, ACCENT),
        ("ELECTRE — outranking & final priority ranking",
         2.1, ACCENT),
        ("Optimisation framework grounded in the Resource-Based View (RBV)",
         0.8, PURPLE),
    ]

    h = 0.95
    for txt, y, c in items:
        box(ax, 0.6, y - h/2, 8.8, h, txt, color=c, fontsize=10, bold=True)

    # arrows
    for i in range(len(items) - 1):
        y_top = items[i][1] - h/2
        y_bot = items[i+1][1] + h/2
        arrow(ax, 5, y_top, 5, y_bot)

    plt.title("Figure 3.1 — Overall Research Process Flowchart",
              fontsize=12, weight="bold", pad=8)
    plt.tight_layout()
    plt.savefig("figures/fig_3_1_research_process.png", dpi=200, bbox_inches="tight")
    plt.close()


# ============================================================
# Figure 3.2 - Three-phase Timeline (Gantt)
# ============================================================
def fig_3_2():
    fig, ax = plt.subplots(figsize=(12, 5.2))
    phases = [
        ("Phase I: Exploratory & Pilot",   0, 6, PRIMARY,
         "Lit review · 15 experts · pilot n=60 · 144 factors"),
        ("Phase II: Main Field Survey",    6, 6, SECONDARY,
         "Stratified sampling · n=1,300 · 5 districts · peak harvest"),
        ("Phase III: Validation & MCDM",  12, 4, ACCENT,
         "Reliability · Cohen's κ · Fuzzy AHP · ELECTRE · follow-ups"),
    ]
    for i, (name, start, dur, color, desc) in enumerate(phases):
        y = 2 - i
        ax.barh(y, dur, left=start, height=0.55, color=color,
                edgecolor="black", linewidth=0.8)
        ax.text(start + dur/2, y, name, ha="center", va="center",
                color="white", fontsize=11, weight="bold")
        ax.text(start + dur/2, y - 0.45, desc, ha="center", va="top",
                color=TEXT, fontsize=9, style="italic")

    months = ["Sep'24","Oct'24","Nov'24","Dec'24",
              "Jan'25","Feb'25","Mar'25","Apr'25","May'25","Jun'25",
              "Jul'25","Aug'25","Sep'25","Oct'25","Nov'25","Dec'25"]
    ax.set_xticks(np.arange(16) + 0.5)
    ax.set_xticklabels(months, rotation=45, fontsize=9)
    ax.set_yticks([])
    ax.set_xlim(0, 16); ax.set_ylim(-0.6, 3)
    ax.set_title("Figure 3.2 — Three-Phase Data-Collection Timeline (September 2024 – December 2025)",
                 fontsize=12, weight="bold", pad=12)
    for sp in ["top", "right", "left"]:
        ax.spines[sp].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.35)
    plt.tight_layout()
    plt.savefig("figures/fig_3_2_phases_timeline.png", dpi=200, bbox_inches="tight")
    plt.close()


# ============================================================
# Figure 3.3 - Malta Supply-Chain Stakeholder Map
# ============================================================
def fig_3_3():
    fig, ax = plt.subplots(figsize=(13, 6.5))
    ax.set_xlim(0, 13); ax.set_ylim(0, 7); ax.axis("off")

    nodes = [
        (0.3, 4.0, 2.0, 1.4, "Farmer /\nGrower",      "n = 540"),
        (2.7, 4.0, 2.0, 1.4, "Local Trader /\nCommission Agent", "n = 220"),
        (5.1, 4.0, 2.0, 1.4, "Wholesale /\nMandi Agent", "n = 180"),
        (7.5, 4.0, 2.0, 1.4, "Retailer",                "n = 230"),
        (9.9, 4.0, 2.0, 1.4, "End\nConsumer",           ""),
    ]
    for (x, y, w, h, t, sub) in nodes:
        box(ax, x, y, w, h, t, color=PRIMARY, fontsize=10, bold=True)
        if sub:
            ax.text(x + w/2, y - 0.25, sub, ha="center", va="top",
                    fontsize=10, color=SECONDARY, weight="bold")

    # forward flow arrows
    for i in range(4):
        x1 = nodes[i][0] + nodes[i][2]
        x2 = nodes[i+1][0]
        y  = nodes[i][1] + nodes[i][3]/2
        arrow(ax, x1 + 0.05, y, x2 - 0.05, y, lw=1.8, ms=18)

    # transporter strip below
    box(ax, 0.3, 1.6, 11.6, 1.0,
        "Transporter (n = 130) — vehicles, drivers, hill-route logistics, "
        "loading & unloading at every transition",
        color=SECONDARY, fontsize=10, bold=True)
    for (x, y, w, h, _, _) in nodes[:-1]:
        ax.plot([x + w/2, x + w/2], [y, 2.6],
                linestyle="--", color="#666", linewidth=1)

    ax.text(6.3, 6.4, "Malta (Citrus sinensis) Distribution Channel — Garhwal Region",
            ha="center", fontsize=12, weight="bold", color=DARK)
    ax.text(6.3, 0.7,
            "Each node assessed on three dimensions:  COST  •  TIME  •  QUALITY",
            ha="center", fontsize=10, style="italic", color=TEXT)
    plt.title("Figure 3.3 — Malta Supply-Chain Stakeholder Map (Achieved Sample = 1,300)",
              fontsize=11, weight="bold", pad=12)
    plt.tight_layout()
    plt.savefig("figures/fig_3_3_supply_chain.png", dpi=200, bbox_inches="tight")
    plt.close()


# ============================================================
# Figure 3.4 - RBV Framework Diagram
# ============================================================
def fig_3_4():
    fig, ax = plt.subplots(figsize=(12, 8.5))
    ax.set_xlim(0, 12); ax.set_ylim(0, 10); ax.axis("off")

    box(ax, 3.5, 8.7, 5, 0.9,
        "Resource-Based View (RBV)\nWernerfelt (1984)  •  Barney (1991)",
        color=PRIMARY, fontsize=11, bold=True)

    vrio = [("V — Valuable", 0.4),
            ("R — Rare", 3.4),
            ("I — Inimitable", 6.4),
            ("O — Organised", 9.4)]
    for txt, x in vrio:
        box(ax, x, 7.0, 2.3, 1.1, txt, color=SECONDARY, fontsize=10, bold=True)
        arrow(ax, 6, 8.7, x + 1.15, 8.1)

    box(ax, 0.4, 4.8, 5.2, 1.4,
        "TANGIBLE RESOURCES\nOrchards · vehicles · packing material · cold chain · mandi infra",
        color=ACCENT, fontsize=10, bold=False)
    box(ax, 6.4, 4.8, 5.2, 1.4,
        "INTANGIBLE RESOURCES\nFarmer skill · market information · trust networks · knowledge · brand",
        color=ACCENT, fontsize=10, bold=False)
    arrow(ax, 3, 7.0, 3, 6.2); arrow(ax, 9, 7.0, 9, 6.2)

    box(ax, 0.4, 2.6, 3.5, 1.3,
        "COST efficiency\n(financial + physical resources)",
        color=PRIMARY, fontsize=10, bold=True)
    box(ax, 4.25, 2.6, 3.5, 1.3,
        "TIME efficiency\n(coordination capability)",
        color=PRIMARY, fontsize=10, bold=True)
    box(ax, 8.1, 2.6, 3.5, 1.3,
        "QUALITY assurance\n(knowledge + infrastructure)",
        color=PRIMARY, fontsize=10, bold=True)

    arrow(ax, 3, 4.8, 2.15, 3.9)
    arrow(ax, 6, 4.8, 6.0, 3.9)
    arrow(ax, 9, 4.8, 9.85, 3.9)

    box(ax, 1.5, 0.5, 9.0, 1.2,
        "82 validated factors across 5 supply-chain stages\n"
        "(Farmer → Trader → Mandi → Retailer → Transporter)",
        color=DARK, fontsize=11, bold=True)
    for x in [2.15, 6.0, 9.85]:
        arrow(ax, x, 2.6, 6.0, 1.7)

    plt.title("Figure 3.4 — Resource-Based View (RBV) Framework Mapped to the Malta Chain",
              fontsize=12, weight="bold", pad=8)
    plt.tight_layout()
    plt.savefig("figures/fig_3_4_rbv_framework.png", dpi=200, bbox_inches="tight")
    plt.close()


# ============================================================
# Figure 3.5 - Sources -> Initial 144 Factors
# ============================================================
def fig_3_5():
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 13); ax.set_ylim(0, 8); ax.axis("off")

    sources = [
        (0.3, 6.4, "Literature review\n(ICAR, NIAM, APEDA reports; journal articles 2005+)"),
        (0.3, 4.9, "Expert consultation\n(15 experts: academia · mandi officials · growers · agents)"),
        (0.3, 3.4, "Pilot study\n(60 respondents across 5 stakeholder groups)"),
        (0.3, 1.9, "Stakeholder discussions\n(farmer collectives & mandi premises during peak weeks)"),
        (0.3, 0.4, "Field observations\n(orchard-to-retail walk-along; structured field diary)"),
    ]
    for (x, y, t) in sources:
        box(ax, x, y, 5.4, 1.1, t, color=PRIMARY, fontsize=10, bold=False)

    box(ax, 8.2, 2.8, 4.4, 2.2,
        "INITIAL POOL\n144  FACTORS\n(5 stages × 3 dimensions)",
        color=SECONDARY, fontsize=14, bold=True)

    for (x, y, _) in sources:
        arrow(ax, x + 5.4, y + 0.55, 8.2, 4.0)

    plt.title("Figure 3.5 — Five Sources Converging into the Initial Pool of 144 Factors",
              fontsize=12, weight="bold", pad=8)
    plt.tight_layout()
    plt.savefig("figures/fig_3_5_factor_sources.png", dpi=200, bbox_inches="tight")
    plt.close()


# ============================================================
# Figure 3.6 - Refinement Funnel (144 -> 116 -> 94 -> 82)
# ============================================================
def fig_3_6():
    fig, ax = plt.subplots(figsize=(13, 8.5))
    ax.set_xlim(0, 14); ax.set_ylim(0, 10); ax.axis("off")

    levels = [
        (144, 8.5, 7.0, 5.6, PRIMARY,   None,
         "Initial pool"),
        (116, 6.7, 5.6, 4.4, SECONDARY, "28 eliminated",
         "Step 1 — Expert content validity\n(CVI ≥ 3.0; overlap & redundancy check)"),
        (94,  4.9, 4.4, 3.4, ACCENT,    "22 eliminated",
         "Step 2 — Pilot reliability\n(Cronbach's α; corrected item-total ≥ 0.30)"),
        (82,  3.1, 3.4, 2.4, PURPLE,    "12 eliminated",
         "Step 3 — Inter-rater consistency\n(Cohen's κ ≥ 0.60; merge or drop)"),
    ]
    centre = 5
    for (n, yc, w_top, w_bot, color, removed, label) in levels:
        x_lt = centre - w_top/2; x_rt = centre + w_top/2
        x_lb = centre - w_bot/2; x_rb = centre + w_bot/2
        y_high = yc + 0.7; y_low = yc - 0.7
        poly = patches.Polygon(
            [(x_lt, y_high), (x_rt, y_high), (x_rb, y_low), (x_lb, y_low)],
            closed=True, facecolor=color, edgecolor="black",
            linewidth=1.3, alpha=0.92)
        ax.add_patch(poly)
        ax.text(centre, yc + 0.18, f"{n} factors",
                ha="center", va="center", color="white",
                fontsize=15, weight="bold")
        if removed:
            ax.text(centre, yc - 0.30, f"({removed})",
                    ha="center", va="center", color="white",
                    fontsize=10, style="italic")
        ax.text(10.0, yc, label, ha="left", va="center",
                fontsize=10.5, color=TEXT)

    # final
    box(ax, 3.6, 1.2, 2.8, 0.9,
        "FINAL : 82 factors", color=DARK, fontsize=12, bold=True)
    arrow(ax, 5, 2.4, 5, 2.1, lw=1.6)

    plt.title("Figure 3.6 — Three-Step Refinement Funnel (144 → 82 Factors)",
              fontsize=12, weight="bold", pad=8)
    plt.tight_layout()
    plt.savefig("figures/fig_3_6_refinement_funnel.png", dpi=200, bbox_inches="tight")
    plt.close()


# ============================================================
# Figure 3.7 - Stage x Dimension factor distribution
# ============================================================
def fig_3_7():
    fig, ax = plt.subplots(figsize=(11.5, 6))
    stages = ["Farm", "Trader", "Mandi", "Retail", "Transport"]
    initial = {"Cost":[12,11,10,10,11], "Time":[10,9,9,7,10], "Quality":[10,9,9,8,9]}
    final   = {"Cost":[7,6,6,6,6],     "Time":[6,5,5,4,5],   "Quality":[6,5,5,5,5]}
    colors  = {"Cost":PRIMARY, "Time":SECONDARY, "Quality":ACCENT}

    x = np.arange(len(stages)); w = 0.13
    for i, dim in enumerate(["Cost","Time","Quality"]):
        ax.bar(x + (i-1)*w*2 - w/2, initial[dim], w,
               color=colors[dim], alpha=0.45,
               label=f"{dim} (initial)", edgecolor="black", linewidth=0.5)
        ax.bar(x + (i-1)*w*2 + w/2, final[dim], w,
               color=colors[dim], alpha=1.0,
               label=f"{dim} (final)", edgecolor="black", linewidth=0.5)
    for i, dim in enumerate(["Cost","Time","Quality"]):
        for j in range(len(stages)):
            ax.text(j+(i-1)*w*2 - w/2, initial[dim][j]+0.18, str(initial[dim][j]),
                    ha="center", fontsize=8, color=colors[dim])
            ax.text(j+(i-1)*w*2 + w/2, final[dim][j]+0.18, str(final[dim][j]),
                    ha="center", fontsize=8, color=colors[dim], weight="bold")

    ax.set_xticks(x); ax.set_xticklabels(stages, fontsize=10)
    ax.set_ylabel("Number of factors", fontsize=10)
    ax.legend(loc="upper right", ncol=3, fontsize=8.5, frameon=False)
    ax.set_ylim(0, 14)
    ax.set_title("Figure 3.7 — Stage × Dimension Factor Distribution: Initial 144 vs Final 82",
                 fontsize=12, weight="bold", pad=10)
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    for sp in ["top","right"]: ax.spines[sp].set_visible(False)
    plt.tight_layout()
    plt.savefig("figures/fig_3_7_stage_dim_dist.png", dpi=200, bbox_inches="tight")
    plt.close()


# ============================================================
# Figure 3.8 - Sampling tree
# ============================================================
def fig_3_8():
    fig, ax = plt.subplots(figsize=(13.5, 8))
    ax.set_xlim(0, 14); ax.set_ylim(0, 9); ax.axis("off")

    box(ax, 5.5, 7.5, 3, 1, "TOTAL SAMPLE\nn = 1,300",
        color=PRIMARY, fontsize=12, bold=True)

    strata = [
        (0.2,  "Farmers\nn = 540"),
        (3.0,  "Local Traders /\nCommission Agents\nn = 220"),
        (5.8,  "Wholesale /\nMandi Agents\nn = 180"),
        (8.6,  "Retailers\nn = 230"),
        (11.4, "Transporters\nn = 130"),
    ]
    for (x, t) in strata:
        box(ax, x, 4.5, 2.4, 1.6, t, color=SECONDARY, fontsize=10, bold=True)
        arrow(ax, 7, 7.5, x + 1.2, 6.1)

    districts = ["Pauri Garhwal","Tehri Garhwal","Chamoli","Rudraprayag","Uttarkashi"]
    for i, d in enumerate(districts):
        x = 0.5 + i * 2.7
        box(ax, x, 1.3, 2.3, 0.95, d, color=ACCENT, fontsize=10, bold=False)

    ax.text(7, 3.5, "Stratified random selection across 5 Garhwal districts",
            ha="center", fontsize=10.5, style="italic", color=TEXT)
    arrow(ax, 7, 4.5, 7, 2.3, lw=1.6)

    plt.title("Figure 3.8 — Stratified Random Sampling Design (n = 1,300)",
              fontsize=12, weight="bold", pad=8)
    plt.tight_layout()
    plt.savefig("figures/fig_3_8_sampling_tree.png", dpi=200, bbox_inches="tight")
    plt.close()


# ============================================================
# Figure 3.9 - Cronbach's alpha bar chart
# ============================================================
def fig_3_9():
    fig, ax = plt.subplots(figsize=(11, 8))
    scales = [
        ("Farm – Cost",      0.917), ("Farm – Time",      0.897),
        ("Farm – Quality",   0.919), ("Trader – Cost",    0.899),
        ("Trader – Time",    0.847), ("Trader – Quality", 0.894),
        ("Mandi – Cost",     0.905), ("Mandi – Time",     0.861),
        ("Mandi – Quality",  0.886), ("Retail – Cost",    0.885),
        ("Retail – Time",    0.820), ("Retail – Quality", 0.875),
        ("Transport – Cost", 0.900), ("Transport – Time", 0.903),
        ("Transport – Quality", 0.870),
    ]
    names = [s[0] for s in scales]
    vals  = [s[1] for s in scales]
    stage_colors = {"Farm":PRIMARY, "Trader":SECONDARY,
                    "Mandi":ACCENT, "Retail":PURPLE, "Transport":RED}
    bar_colors = [stage_colors[n.split(" – ")[0]] for n in names]
    y = np.arange(len(names))
    ax.barh(y, vals, color=bar_colors, edgecolor="black", linewidth=0.6)
    for i, v in enumerate(vals):
        ax.text(v + 0.004, i, f"α = {v:.3f}", va="center", fontsize=9.5)
    ax.set_yticks(y); ax.set_yticklabels(names, fontsize=10)
    ax.invert_yaxis()
    ax.set_xlim(0.70, 1.0)
    ax.axvline(0.70, color="red", linestyle="--", linewidth=1.5, alpha=0.7,
               label="Acceptable ≥ 0.70 (Nunnally, 1978)")
    ax.axvline(0.80, color="green", linestyle=":", linewidth=1.4, alpha=0.7,
               label="Excellent ≥ 0.80")
    ax.set_xlabel("Cronbach's α  (n = 1,300)", fontsize=10)
    ax.legend(loc="lower right", fontsize=9.5)
    ax.set_title("Figure 3.9 — Reliability of the 15 Sub-Scales (Cronbach's α)",
                 fontsize=12, weight="bold", pad=10)
    for sp in ["top","right"]: ax.spines[sp].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.3)
    plt.tight_layout()
    plt.savefig("figures/fig_3_9_cronbach.png", dpi=200, bbox_inches="tight")
    plt.close()


# ============================================================
# Figure 3.10 - Two-stage MCDM Analytical Pipeline
# ============================================================
def fig_3_10():
    fig, ax = plt.subplots(figsize=(13.5, 7.5))
    ax.set_xlim(0, 14); ax.set_ylim(0, 8); ax.axis("off")

    ax.text(7, 7.4, "Two-Stage MCDM Analytical Pipeline",
            ha="center", fontsize=13, weight="bold", color=DARK)

    # input
    box(ax, 0.2, 3.6, 2.5, 1.6,
        "82 validated factors\n+\nn = 1,300\nrespondents",
        color=DARK, fontsize=10, bold=True)

    # Stage 1: Fuzzy AHP
    ax.text(0.4, 6.0, "Stage 1\nFuzzy AHP", fontsize=11,
            weight="bold", color=PRIMARY)
    fahp = [
        (3.0, 5.4, 2.4, 1.2, "Pair-wise\ncomparison matrices\n(linguistic terms)"),
        (5.7, 5.4, 2.4, 1.2, "Triangular fuzzy\nnumbers\n(l, m, u)"),
        (8.4, 5.4, 2.4, 1.2, "Extent analysis\n(Chang, 1996)"),
        (11.1, 5.4, 2.4, 1.2, "Defuzzified weights\nCR < 0.10"),
    ]
    for (x, y, w, h, t) in fahp:
        box(ax, x, y, w, h, t, color=PRIMARY, fontsize=9.5, bold=False)
    for i in range(len(fahp) - 1):
        arrow(ax, fahp[i][0]+fahp[i][2], fahp[i][1]+fahp[i][3]/2,
              fahp[i+1][0],              fahp[i+1][1]+fahp[i+1][3]/2)

    # Stage 2: ELECTRE
    ax.text(0.4, 3.0, "Stage 2\nELECTRE", fontsize=11,
            weight="bold", color=SECONDARY)
    electre = [
        (3.0, 2.3, 2.4, 1.2, "Weighted\ndecision matrix"),
        (5.7, 2.3, 2.4, 1.2, "Concordance &\nDiscordance matrices"),
        (8.4, 2.3, 2.4, 1.2, "Threshold-based\noutranking\n(Roy, 1991)"),
        (11.1, 2.3, 2.4, 1.2, "Net dominance &\nfinal ranking"),
    ]
    for (x, y, w, h, t) in electre:
        box(ax, x, y, w, h, t, color=SECONDARY, fontsize=9.5, bold=False)
    for i in range(len(electre) - 1):
        arrow(ax, electre[i][0]+electre[i][2], electre[i][1]+electre[i][3]/2,
              electre[i+1][0],                electre[i+1][1]+electre[i+1][3]/2)

    # input feeding both stages
    arrow(ax, 2.7, 4.8, 3.0, 5.4 + 0.6)
    arrow(ax, 2.7, 4.2, 3.0, 2.3 + 0.6)

    # weights flowing from FAHP into ELECTRE matrix
    arrow(ax, 12.3, 5.4, 12.3, 3.5, lw=1.6)
    ax.text(12.5, 4.45, "Weights",
            fontsize=9.5, color=TEXT, style="italic")

    # final output
    box(ax, 4.5, 0.4, 5, 1.1,
        "Prioritised list of 82 factors  →  optimisation framework",
        color=ACCENT, fontsize=10.5, bold=True)
    arrow(ax, 12.3, 2.3, 9.5, 1.5, lw=1.6)

    plt.tight_layout()
    plt.savefig("figures/fig_3_10_analytical_pipeline.png", dpi=200, bbox_inches="tight")
    plt.close()


def main():
    fig_3_1(); fig_3_2(); fig_3_3(); fig_3_4(); fig_3_5()
    fig_3_6(); fig_3_7(); fig_3_8(); fig_3_9(); fig_3_10()
    files = sorted(os.listdir("figures"))
    for f in files:
        sz = os.path.getsize(os.path.join("figures", f)) // 1024
        print(f"  {f:<40s} {sz:>5d} KB")


if __name__ == "__main__":
    main()
