"""
Fuzzy AHP & Fuzzy ELECTRE I implementation for the Malta (citrus) post-harvest
supply-chain criticality study.

Author: PhD thesis support module
Inputs : ../Malta_.xlsx
Outputs: ../outputs/*.csv  and  ../figures/*.png

References
----------
- Saaty, T. L. (1980). The Analytic Hierarchy Process.
- Buckley, J. J. (1985). Fuzzy hierarchical analysis. Fuzzy Sets and Systems, 17(3), 233-247.
- Chang, D. Y. (1996). Applications of the extent analysis method on fuzzy AHP.
- Roy, B. (1968). Classement et choix en presence de points de vue multiples (la methode ELECTRE).
- Hatami-Marbini, A., & Tavana, M. (2011). An extension of the ELECTRE I method for group
  decision-making under a fuzzy environment. Omega, 39(4), 373-386.
"""

from __future__ import annotations

import os
import json
from itertools import combinations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from matplotlib import cm

# ------------------------------------------------------------------ paths
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
DATA_FILE = os.path.join(BASE, "Malta_.xlsx")
OUT_DIR = os.path.join(BASE, "outputs")
FIG_DIR = os.path.join(BASE, "figures")
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

plt.rcParams.update({
    "figure.dpi": 120,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titleweight": "bold",
})
sns.set_style("whitegrid")

STAGES = ["Farm", "Trader", "Mandi", "Retail", "Transport"]
STAGE_PREFIX = {"Farm": "F", "Trader": "T", "Mandi": "M", "Retail": "R", "Transport": "TR"}
CRITERIA = ["Cost", "Time", "Quality"]
CRIT_TOKEN = {"Cost": "COST", "Time": "TIME", "Quality": "QUAL"}


# ============================================================ TFN helpers
class TFN:
    """Triangular fuzzy number (l, m, u) with l <= m <= u."""

    __slots__ = ("l", "m", "u")

    def __init__(self, l: float, m: float, u: float):
        # accept slight numerical drift but force ordering for safety
        l, m, u = float(l), float(m), float(u)
        if not (l <= m <= u):
            l, m, u = sorted([l, m, u])
        self.l, self.m, self.u = l, m, u

    # ---- arithmetic (fuzzy) ------------------------------------
    def __add__(self, o: "TFN") -> "TFN":
        return TFN(self.l + o.l, self.m + o.m, self.u + o.u)

    def __mul__(self, o):
        if isinstance(o, TFN):
            return TFN(self.l * o.l, self.m * o.m, self.u * o.u)
        return TFN(self.l * o, self.m * o, self.u * o)

    def __truediv__(self, o):
        if isinstance(o, TFN):
            # standard fuzzy division for positive TFNs (Buckley)
            return TFN(self.l / o.u, self.m / o.m, self.u / o.l)
        return TFN(self.l / o, self.m / o, self.u / o)

    def reciprocal(self) -> "TFN":
        return TFN(1.0 / self.u, 1.0 / self.m, 1.0 / self.l)

    def power(self, p: float) -> "TFN":
        return TFN(self.l ** p, self.m ** p, self.u ** p)

    # ---- defuzzification ---------------------------------------
    def centroid(self) -> float:
        return (self.l + self.m + self.u) / 3.0

    def bnp(self) -> float:
        # Best Non-fuzzy Performance value (Tsaur 2002)
        return ((self.u - self.l) + (self.m - self.l)) / 3.0 + self.l

    # ---- distance ----------------------------------------------
    def vertex_distance(self, o: "TFN") -> float:
        # Chen 2000 vertex distance for TFN
        return np.sqrt(((self.l - o.l) ** 2 + (self.m - o.m) ** 2 + (self.u - o.u) ** 2) / 3.0)

    def __repr__(self):
        return f"TFN({self.l:.4f}, {self.m:.4f}, {self.u:.4f})"

    def to_tuple(self):
        return (self.l, self.m, self.u)


def tfn_geometric_mean(tfns):
    n = len(tfns)
    prod = TFN(1, 1, 1)
    for t in tfns:
        prod = prod * t
    return prod.power(1.0 / n)


# ============================================================ data load
def load_data():
    df = pd.read_excel(DATA_FILE, sheet_name="Data_for_jamovi")
    cb = pd.read_excel(DATA_FILE, sheet_name="Codebook")
    return df, cb


def build_scale_columns():
    """Return dict {stage: {criterion: [item_columns,...]}} from variable names."""
    out = {s: {c: [] for c in CRITERIA} for s in STAGES}
    df = pd.read_excel(DATA_FILE, sheet_name="Data_for_jamovi", nrows=0)
    for col in df.columns:
        if "_" not in col or col in ("Questionnaire_ID",):
            continue
        parts = col.split("_")
        prefix = parts[0]
        token = parts[1] if len(parts) >= 2 else ""
        for s, p in STAGE_PREFIX.items():
            if prefix == p:
                for c, t in CRIT_TOKEN.items():
                    if token == t:
                        out[s][c].append(col)
                        break
                break
    return out


# ============================================================ Step 1 - decision matrix
def build_decision_matrix(df: pd.DataFrame, cols_map: dict):
    """Compute the 5 (stage) x 3 (criterion) crisp decision matrix and a
    fuzzy decision matrix grounded in observed response variability.

    For each (stage, criterion) cell:
       crisp m = mean of all items in that scale, across all respondents
       l, u   = m - sigma, m + sigma   (clipped to [1, 5])
    where sigma is the std dev of respondent-level scale means.
    """
    crisp = pd.DataFrame(index=STAGES, columns=CRITERIA, dtype=float)
    fuzzy = {s: {} for s in STAGES}
    sigma_tab = pd.DataFrame(index=STAGES, columns=CRITERIA, dtype=float)
    n_items = pd.DataFrame(index=STAGES, columns=CRITERIA, dtype=int)

    for s in STAGES:
        for c in CRITERIA:
            cols = cols_map[s][c]
            if not cols:
                continue
            sub = df[cols].apply(pd.to_numeric, errors="coerce")
            resp_mean = sub.mean(axis=1)            # one score per respondent
            m = resp_mean.mean()
            sigma = resp_mean.std(ddof=1)
            l = max(1.0, m - sigma)
            u = min(5.0, m + sigma)
            crisp.loc[s, c] = m
            sigma_tab.loc[s, c] = sigma
            n_items.loc[s, c] = len(cols)
            fuzzy[s][c] = TFN(l, m, u)

    return crisp.astype(float), fuzzy, sigma_tab.astype(float), n_items.astype(int)


# ============================================================ Step 2 - Fuzzy AHP
SAATY_TFN = {
    1: TFN(1, 1, 1),
    2: TFN(1, 2, 3),
    3: TFN(2, 3, 4),
    4: TFN(3, 4, 5),
    5: TFN(4, 5, 6),
    6: TFN(5, 6, 7),
    7: TFN(6, 7, 8),
    8: TFN(7, 8, 9),
    9: TFN(8, 9, 9),
}


def crisp_to_saaty(ratio: float) -> int:
    """Map a positive ratio to a signed Saaty integer in {±1,…,±9}.
    Sign indicates direction (positive = i preferred to j).

    Thresholds based on Saaty's original verbal anchors translated to
    multiplicative bands (1.10, 1.25, 1.40 …) so that a ~10% difference is
    already detectable as a 'weak' preference.
    """
    if ratio < 1.0:
        return -crisp_to_saaty(1.0 / ratio)
    bands = [(1.10, 1), (1.25, 2), (1.45, 3), (1.70, 4),
             (2.00, 5), (2.40, 6), (2.90, 7), (3.50, 8)]
    for cutoff, s in bands:
        if ratio < cutoff:
            return s
    return 9


def derive_priority_signal(df, cols_map):
    """Combine two empirical signals to derive a priority vector among the
    three criteria (Cost, Time, Quality) suitable for AHP pairwise comparison:

      (a) PCA variance contribution per criterion taken from the workbook
          PCA_Summary sheet (Cost=27.2 %, Quality=21.6 %, Time=19.2 %).
      (b) Respondent-level mean criticality per criterion computed across all
          stages from the raw Likert data.

    The two signals are combined as a multiplicative aggregate so that a
    criterion that is both more 'variance-explanatory' (PCA) and more
    'critical' (mean) gets the higher priority. The aggregate is normalised
    to sum to one and used to populate the pairwise comparison matrix.
    """
    # --- (a) PCA variance shares from the workbook ---------------------
    pca = pd.read_excel(DATA_FILE, sheet_name="PCA_Summary")
    # Robust parse: find the rows for PC1/PC2/PC3 and read the % string
    def _row(label):
        row = pca[pca.iloc[:, 0].astype(str).str.strip() == label]
        return row.iloc[0]
    pc1 = _row("PC1"); pc2 = _row("PC2"); pc3 = _row("PC3")
    def _pct(v):
        return float(str(v).replace("%", "").strip())
    pca_var = {
        "Cost":    _pct(pc1.iloc[1]),       # PC1 -> Cost
        "Quality": _pct(pc2.iloc[1]),       # PC2 -> Quality
        "Time":    _pct(pc3.iloc[1]),       # PC3 -> Time
    }

    # --- (b) respondent-level criterion means --------------------------
    means = {}
    for c in CRITERIA:
        cols = []
        for s in STAGES:
            cols += cols_map[s][c]
        means[c] = float(df[cols].apply(pd.to_numeric, errors="coerce").mean().mean())

    # --- normalise each signal to share-of-total -----------------------
    pca_share = {c: pca_var[c] / sum(pca_var.values()) for c in CRITERIA}
    mean_share = {c: means[c] / sum(means.values()) for c in CRITERIA}

    # multiplicative aggregate (unnormalised)
    agg = {c: pca_share[c] * mean_share[c] for c in CRITERIA}
    z = sum(agg.values())
    priority = {c: agg[c] / z for c in CRITERIA}
    return priority, pca_share, mean_share


def build_pairwise_from_priority(priority: dict):
    """Build crisp ratio matrix and fuzzified TFN matrix among criteria."""
    n = len(CRITERIA)
    crisp = np.ones((n, n))
    saaty = np.ones((n, n))
    fuzzy = [[TFN(1, 1, 1) for _ in range(n)] for _ in range(n)]

    for i, ci in enumerate(CRITERIA):
        for j, cj in enumerate(CRITERIA):
            if i == j:
                continue
            r = priority[ci] / priority[cj]
            crisp[i, j] = r
            s = crisp_to_saaty(r)
            saaty[i, j] = s if s > 0 else 1.0 / abs(s)
            tfn = SAATY_TFN[abs(s)]
            fuzzy[i][j] = tfn if s > 0 else tfn.reciprocal()
    return crisp, saaty, fuzzy


def consistency_ratio(saaty: np.ndarray) -> tuple[float, float, float]:
    n = saaty.shape[0]
    eigvals = np.linalg.eigvals(saaty)
    lam_max = float(np.real(eigvals[np.argmax(np.real(eigvals))]))
    CI = (lam_max - n) / (n - 1) if n > 1 else 0.0
    RI = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}.get(n, 1.49)
    CR = CI / RI if RI > 0 else 0.0
    return lam_max, CI, CR


def buckley_fuzzy_weights(fuzzy_matrix):
    """Buckley's fuzzy AHP weight derivation."""
    n = len(fuzzy_matrix)
    # row geometric means
    r = [tfn_geometric_mean(fuzzy_matrix[i]) for i in range(n)]
    s_l = sum(t.l for t in r)
    s_m = sum(t.m for t in r)
    s_u = sum(t.u for t in r)
    sum_r_recip = TFN(1.0 / s_u, 1.0 / s_m, 1.0 / s_l)
    fuzzy_w = [ri * sum_r_recip for ri in r]
    crisp_w = np.array([w.centroid() for w in fuzzy_w])
    crisp_w = crisp_w / crisp_w.sum()           # normalise centroids
    return r, fuzzy_w, crisp_w


# ============================================================ Step 3 - Fuzzy ELECTRE
def normalize_fuzzy(decision_fuzzy: dict, benefit: list[bool]):
    """Vector normalisation for fuzzy decision matrix (Hatami-Marbini)."""
    norm = {s: {} for s in STAGES}
    for j, c in enumerate(CRITERIA):
        u_max = max(decision_fuzzy[s][c].u for s in STAGES)
        for s in STAGES:
            t = decision_fuzzy[s][c]
            if benefit[j]:
                norm[s][c] = TFN(t.l / u_max, t.m / u_max, t.u / u_max)
            else:                                # cost-type: invert
                l_min = min(decision_fuzzy[ss][c].l for ss in STAGES)
                norm[s][c] = TFN(l_min / t.u, l_min / t.m, l_min / t.l)
    return norm


def weighted_fuzzy(norm_fuzzy: dict, fuzzy_weights):
    """Multiply normalised TFN by fuzzy weight TFN element-wise."""
    out = {s: {} for s in STAGES}
    for j, c in enumerate(CRITERIA):
        for s in STAGES:
            out[s][c] = norm_fuzzy[s][c] * fuzzy_weights[j]
    return out


def fuzzy_electre(weighted: dict, fuzzy_weights):
    """Compute concordance, discordance, dominance, net flows."""
    A = STAGES
    n = len(A)
    crit = CRITERIA
    nC = len(crit)

    # crisp weight defuzzified for concordance
    w_crisp = np.array([w.centroid() for w in fuzzy_weights])
    w_crisp = w_crisp / w_crisp.sum()

    C = np.zeros((n, n))                        # concordance index
    D = np.zeros((n, n))                        # discordance index

    # vertex distance helper (Chen 2000)
    def vd(a: TFN, b: TFN) -> float:
        return a.vertex_distance(b)

    # max distance per criterion (used as denominator for discordance)
    for k in range(n):
        for l in range(n):
            if k == l:
                continue
            conc_set, disc_set = [], []
            disc_distances = []
            for j, c in enumerate(crit):
                xk = weighted[A[k]][c]
                xl = weighted[A[l]][c]
                # decision rule: use centroid (BNP) of weighted TFN
                if xk.centroid() >= xl.centroid():
                    conc_set.append(j)
                else:
                    disc_set.append(j)
                disc_distances.append((j, vd(xk, xl), xk.centroid() < xl.centroid()))

            # concordance index = sum of weights of concordant criteria
            C[k, l] = sum(w_crisp[j] for j in conc_set)

            # discordance index
            num = max((d for j, d, is_disc in disc_distances if is_disc), default=0.0)
            den = max(d for j, d, _ in disc_distances) or 1e-12
            D[k, l] = num / den

    # thresholds = mean of off-diagonal entries
    off = ~np.eye(n, dtype=bool)
    c_bar = C[off].mean()
    d_bar = D[off].mean()

    # boolean dominance matrices
    F = (C >= c_bar).astype(int)
    G = (D <= d_bar).astype(int)
    np.fill_diagonal(F, 0)
    np.fill_diagonal(G, 0)
    E = F * G                                   # aggregate dominance

    # net concordance / discordance
    C_sup = C.sum(axis=1) - C.sum(axis=0)
    D_inf = D.sum(axis=1) - D.sum(axis=0)
    net_score = C_sup - D_inf                   # higher = better (more dominant)

    return dict(C=C, D=D, F=F, G=G, E=E,
                c_bar=c_bar, d_bar=d_bar,
                C_sup=C_sup, D_inf=D_inf,
                net=net_score, w_crisp=w_crisp)


# ============================================================ Sensitivity analysis
def sensitivity(weighted_norm_fuzzy_factory, fuzzy_weights_base, deltas=(-0.3, -0.15, 0.0, 0.15, 0.3)):
    """Vary each criterion weight by delta (additive in centroid space) and
    recompute final ranking. Returns DataFrame of ranks per scenario."""
    rows = []
    base_centroids = np.array([w.centroid() for w in fuzzy_weights_base])
    for j, c in enumerate(CRITERIA):
        for d in deltas:
            new = base_centroids.copy()
            new[j] = max(0.01, base_centroids[j] * (1 + d))
            new = new / new.sum()
            # rebuild fuzzy weights with same spread but rescaled m
            new_fw = []
            for k, fw in enumerate(fuzzy_weights_base):
                scale = new[k] / fw.centroid()
                new_fw.append(TFN(fw.l * scale, fw.m * scale, fw.u * scale))
            weighted = weighted_norm_fuzzy_factory(new_fw)
            res = fuzzy_electre(weighted, new_fw)
            order = np.argsort(-res["net"])
            ranks = np.empty(len(STAGES), dtype=int)
            for r, idx in enumerate(order):
                ranks[idx] = r + 1
            rows.append({"criterion": c, "delta_pct": int(d * 100),
                         **{stage: ranks[i] for i, stage in enumerate(STAGES)},
                         "net_score": ",".join(f"{v:+.3f}" for v in res["net"])})
    return pd.DataFrame(rows)


# ============================================================ Plotting
def fig_likert_distribution(df, cols_map):
    rows = []
    for s in STAGES:
        for c in CRITERIA:
            cols = cols_map[s][c]
            if not cols:
                continue
            mean_per_resp = df[cols].apply(pd.to_numeric, errors="coerce").mean(axis=1)
            for v in mean_per_resp.dropna():
                rows.append({"Stage": s, "Criterion": c, "Score": v})
    plot_df = pd.DataFrame(rows)
    fig, ax = plt.subplots(figsize=(11, 6))
    sns.boxplot(data=plot_df, x="Stage", y="Score", hue="Criterion",
                palette="Set2", ax=ax, fliersize=2)
    ax.set_title("Distribution of Respondent-Level Criticality Scores\nby Supply-Chain Stage and Criterion")
    ax.set_ylabel("Mean Likert Score (1 = Not critical … 5 = Extremely critical)")
    ax.set_ylim(1, 5)
    ax.legend(title="Criterion", loc="lower right")
    fig.savefig(os.path.join(FIG_DIR, "fig01_likert_distribution.png"))
    plt.close(fig)


def fig_decision_heatmap(crisp):
    fig, ax = plt.subplots(figsize=(7.2, 5.5))
    sns.heatmap(crisp, annot=True, fmt=".3f", cmap="YlOrRd",
                cbar_kws={"label": "Mean criticality (1-5)"}, ax=ax,
                vmin=crisp.values.min() - 0.05, vmax=crisp.values.max() + 0.05,
                linewidths=0.5, linecolor="white")
    ax.set_title("Crisp Decision Matrix\n(stage × criterion mean criticality)")
    ax.set_xlabel("Criterion")
    ax.set_ylabel("Supply-chain stage")
    fig.savefig(os.path.join(FIG_DIR, "fig02_decision_matrix_heatmap.png"))
    plt.close(fig)


def fig_membership_functions():
    fig, ax = plt.subplots(figsize=(10, 5))
    levels = [("Equal (1)", SAATY_TFN[1], "#888"),
              ("Weak (2)", SAATY_TFN[2], "#1f77b4"),
              ("Moderate (3)", SAATY_TFN[3], "#2ca02c"),
              ("Mod-plus (4)", SAATY_TFN[4], "#d62728"),
              ("Strong (5)", SAATY_TFN[5], "#9467bd"),
              ("Strong-plus (6)", SAATY_TFN[6], "#8c564b"),
              ("Very strong (7)", SAATY_TFN[7], "#e377c2"),
              ("V-strong-plus (8)", SAATY_TFN[8], "#bcbd22"),
              ("Extreme (9)", SAATY_TFN[9], "#17becf")]
    x = np.linspace(0, 10, 1000)
    for label, t, color in levels:
        y = np.where(x <= t.m,
                     np.where(x >= t.l, (x - t.l) / max(t.m - t.l, 1e-9), 0),
                     np.where(x <= t.u, (t.u - x) / max(t.u - t.m, 1e-9), 0))
        ax.plot(x, y, label=label, color=color, lw=2)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("Saaty intensity")
    ax.set_ylabel("Membership μ(x)")
    ax.set_title("Triangular Fuzzy Numbers used to fuzzify the Saaty 1-9 Scale")
    ax.legend(ncol=3, fontsize=9, loc="upper right")
    fig.savefig(os.path.join(FIG_DIR, "fig03_linguistic_membership.png"))
    plt.close(fig)


def fig_pairwise_LMU(fuzzy_pw):
    L = np.array([[t.l for t in row] for row in fuzzy_pw])
    M = np.array([[t.m for t in row] for row in fuzzy_pw])
    U = np.array([[t.u for t in row] for row in fuzzy_pw])
    fig, axes = plt.subplots(1, 3, figsize=(13, 4))
    for ax, mat, title in zip(axes, [L, M, U], ["Lower (l)", "Middle (m)", "Upper (u)"]):
        sns.heatmap(mat, annot=True, fmt=".2f", cmap="coolwarm",
                    xticklabels=CRITERIA, yticklabels=CRITERIA, ax=ax, cbar=False, center=1.0)
        ax.set_title(f"Pairwise TFN — {title}")
    fig.suptitle("Fuzzy Pairwise Comparison Matrix among Criteria (TFN components)", y=1.04)
    fig.savefig(os.path.join(FIG_DIR, "fig04_pairwise_TFN_LMU.png"))
    plt.close(fig)


def fig_fuzzy_weights(fuzzy_w, crisp_w):
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.arange(len(CRITERIA))
    lo = [w.l for w in fuzzy_w]
    mid = [w.m for w in fuzzy_w]
    up = [w.u for w in fuzzy_w]
    err = np.array([[m - l for m, l in zip(mid, lo)],
                    [u - m for m, u in zip(mid, up)]])
    bars = ax.bar(x, mid, yerr=err, capsize=8,
                  color=["#1f77b4", "#2ca02c", "#d62728"], alpha=0.85,
                  edgecolor="black")
    for i, (b, c) in enumerate(zip(bars, crisp_w)):
        ax.text(b.get_x() + b.get_width() / 2, mid[i] + (up[i] - mid[i]) + 0.01,
                f"w = {c:.3f}", ha="center", fontsize=10, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(CRITERIA)
    ax.set_ylabel("Fuzzy weight (TFN)")
    ax.set_title("Fuzzy AHP Criterion Weights (Buckley method)\nTFN with whiskers; defuzzified centroid annotated")
    ax.set_ylim(0, max(up) * 1.25)
    fig.savefig(os.path.join(FIG_DIR, "fig05_fuzzy_weights_TFN.png"))
    plt.close(fig)


def fig_matrix_heatmap(matrix_dict, title, fname, fmt=".3f", cmap="YlGnBu", vmin=None, vmax=None):
    arr = np.array([[matrix_dict[s][c].centroid() for c in CRITERIA] for s in STAGES])
    fig, ax = plt.subplots(figsize=(7.2, 5.2))
    sns.heatmap(arr, annot=True, fmt=fmt, cmap=cmap,
                xticklabels=CRITERIA, yticklabels=STAGES, ax=ax,
                linewidths=0.5, linecolor="white", vmin=vmin, vmax=vmax,
                cbar_kws={"label": "Defuzzified centroid"})
    ax.set_title(title)
    fig.savefig(os.path.join(FIG_DIR, fname))
    plt.close(fig)


def fig_concordance_heatmap(C, c_bar):
    fig, ax = plt.subplots(figsize=(7.2, 5.5))
    sns.heatmap(C, annot=True, fmt=".3f", cmap="Greens",
                xticklabels=STAGES, yticklabels=STAGES, ax=ax,
                linewidths=0.5, linecolor="white",
                cbar_kws={"label": "Concordance index"})
    ax.set_title(f"Concordance Matrix C (threshold c̄ = {c_bar:.3f})")
    ax.set_xlabel("Compared with (alt l)")
    ax.set_ylabel("Alt k")
    fig.savefig(os.path.join(FIG_DIR, "fig08_concordance_heatmap.png"))
    plt.close(fig)


def fig_discordance_heatmap(D, d_bar):
    fig, ax = plt.subplots(figsize=(7.2, 5.5))
    sns.heatmap(D, annot=True, fmt=".3f", cmap="Reds",
                xticklabels=STAGES, yticklabels=STAGES, ax=ax,
                linewidths=0.5, linecolor="white",
                cbar_kws={"label": "Discordance index"})
    ax.set_title(f"Discordance Matrix D (threshold d̄ = {d_bar:.3f})")
    ax.set_xlabel("Compared with (alt l)")
    ax.set_ylabel("Alt k")
    fig.savefig(os.path.join(FIG_DIR, "fig09_discordance_heatmap.png"))
    plt.close(fig)


def fig_dominance_heatmap(E):
    fig, ax = plt.subplots(figsize=(7.2, 5.5))
    sns.heatmap(E, annot=True, fmt="d", cmap="Blues",
                xticklabels=STAGES, yticklabels=STAGES, ax=ax,
                linewidths=0.5, linecolor="white", cbar=False)
    ax.set_title("Aggregate Dominance Matrix E = F · G\n(1 ⇒ row dominates column)")
    fig.savefig(os.path.join(FIG_DIR, "fig10_dominance_aggregate_heatmap.png"))
    plt.close(fig)


def fig_net_flows(C_sup, D_inf):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    axes[0].bar(STAGES, C_sup, color="#2ca02c", edgecolor="black", alpha=0.85)
    axes[0].set_title("Net Concordance  C★(k) = ΣC_kl − ΣC_lk")
    axes[0].axhline(0, color="black", lw=0.7)
    axes[0].set_ylabel("Net concordance")

    axes[1].bar(STAGES, D_inf, color="#d62728", edgecolor="black", alpha=0.85)
    axes[1].set_title("Net Discordance  D★(k) = ΣD_kl − ΣD_lk")
    axes[1].axhline(0, color="black", lw=0.7)
    axes[1].set_ylabel("Net discordance")
    fig.savefig(os.path.join(FIG_DIR, "fig11_net_superior_inferior_bars.png"))
    plt.close(fig)


def fig_final_ranking(net_score):
    order = np.argsort(-net_score)
    fig, ax = plt.subplots(figsize=(9, 5))
    colors = sns.color_palette("viridis", len(STAGES))
    sorted_stages = [STAGES[i] for i in order]
    sorted_scores = net_score[order]
    bars = ax.bar(sorted_stages, sorted_scores, color=colors, edgecolor="black")
    for r, b in enumerate(bars):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.02,
                f"#{r + 1}\n{b.get_height():+.3f}", ha="center", fontweight="bold")
    ax.axhline(0, color="black", lw=0.6)
    ax.set_title("Fuzzy ELECTRE — Final Ranking of Supply-Chain Stages\n(Net score = C★ − D★, larger ⇒ more critical)")
    ax.set_ylabel("Net ranking score")
    fig.savefig(os.path.join(FIG_DIR, "fig12_final_ranking_bars.png"))
    plt.close(fig)


def fig_sensitivity(sens_df):
    fig, ax = plt.subplots(figsize=(11, 5.5))
    sens_df = sens_df.copy()
    sens_df["scenario"] = sens_df["criterion"] + " " + sens_df["delta_pct"].map(lambda x: f"{x:+d}%")
    rank_mat = sens_df[STAGES].values.astype(int)
    sns.heatmap(rank_mat, annot=True, fmt="d", cmap="RdYlGn_r",
                xticklabels=STAGES, yticklabels=sens_df["scenario"].tolist(),
                ax=ax, cbar_kws={"label": "Rank (1 = most critical)"},
                linewidths=0.4, linecolor="white", vmin=1, vmax=5)
    ax.set_title("Sensitivity Analysis — Ranks under Perturbed Criterion Weights")
    ax.set_xlabel("Stage")
    fig.savefig(os.path.join(FIG_DIR, "fig13_sensitivity_analysis.png"))
    plt.close(fig)


def fig_radar(crisp):
    fig = plt.figure(figsize=(8.5, 8.5))
    ax = fig.add_subplot(111, polar=True)
    angles = np.linspace(0, 2 * np.pi, len(CRITERIA), endpoint=False).tolist()
    angles += angles[:1]
    palette = sns.color_palette("husl", len(STAGES))
    for i, s in enumerate(STAGES):
        vals = crisp.loc[s].tolist()
        vals += vals[:1]
        ax.plot(angles, vals, color=palette[i], lw=2, label=s)
        ax.fill(angles, vals, color=palette[i], alpha=0.10)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(CRITERIA, fontsize=12)
    ax.set_ylim(crisp.values.min() - 0.1, crisp.values.max() + 0.1)
    ax.set_title("Stage Profiles across Criteria (crisp means)", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.18, 1.05))
    fig.savefig(os.path.join(FIG_DIR, "fig14_radar_alternatives.png"))
    plt.close(fig)


def fig_correlation_heatmap(df, cols_map):
    """Pearson correlation heatmap among the 15 stage-criterion scale scores."""
    cols = []
    labels = []
    for s in STAGES:
        for c in CRITERIA:
            scale_cols = cols_map[s][c]
            scale_score = df[scale_cols].apply(pd.to_numeric, errors="coerce").mean(axis=1)
            cols.append(scale_score)
            labels.append(f"{s}·{c}")
    score_df = pd.concat(cols, axis=1)
    score_df.columns = labels
    corr = score_df.corr()
    fig, ax = plt.subplots(figsize=(9.5, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="vlag", vmin=-1, vmax=1,
                ax=ax, square=True, cbar_kws={"label": "Pearson r"})
    ax.set_title("Pearson Correlation among 15 Stage·Criterion Scale Scores")
    fig.savefig(os.path.join(FIG_DIR, "fig15_scale_correlation_heatmap.png"))
    plt.close(fig)


# ============================================================ MAIN
def main():
    df, _ = load_data()
    cols_map = build_scale_columns()

    # 1. Decision matrix
    crisp_dm, fuzzy_dm, sigma_tab, n_items_tab = build_decision_matrix(df, cols_map)
    crisp_dm.to_csv(os.path.join(OUT_DIR, "01_decision_matrix_crisp.csv"))
    sigma_tab.to_csv(os.path.join(OUT_DIR, "01b_decision_matrix_sigma.csv"))
    n_items_tab.to_csv(os.path.join(OUT_DIR, "01c_items_per_scale.csv"))
    fuzzy_dm_records = []
    for s in STAGES:
        for c in CRITERIA:
            t = fuzzy_dm[s][c]
            fuzzy_dm_records.append({"Stage": s, "Criterion": c,
                                     "l": round(t.l, 4), "m": round(t.m, 4), "u": round(t.u, 4)})
    pd.DataFrame(fuzzy_dm_records).to_csv(os.path.join(OUT_DIR, "01d_decision_matrix_fuzzy.csv"), index=False)

    # 2. Derive criterion priority from PCA variance + respondent-level mean
    priority, pca_share, mean_share = derive_priority_signal(df, cols_map)
    pd.DataFrame({"Criterion": CRITERIA,
                  "PCA_share": [pca_share[c] for c in CRITERIA],
                  "Mean_share": [mean_share[c] for c in CRITERIA],
                  "Priority": [priority[c] for c in CRITERIA]}).to_csv(
        os.path.join(OUT_DIR, "02_priority_signal.csv"), index=False)
    crisp_pw, saaty_pw, fuzzy_pw = build_pairwise_from_priority(priority)
    pd.DataFrame(crisp_pw, index=CRITERIA, columns=CRITERIA)\
        .to_csv(os.path.join(OUT_DIR, "02a_pairwise_crisp_ratio.csv"))
    pd.DataFrame(saaty_pw, index=CRITERIA, columns=CRITERIA)\
        .to_csv(os.path.join(OUT_DIR, "02b_pairwise_saaty.csv"))
    fuzzy_pw_records = []
    for i, ci in enumerate(CRITERIA):
        for j, cj in enumerate(CRITERIA):
            t = fuzzy_pw[i][j]
            fuzzy_pw_records.append({"i": ci, "j": cj,
                                     "l": round(t.l, 4), "m": round(t.m, 4), "u": round(t.u, 4)})
    pd.DataFrame(fuzzy_pw_records).to_csv(os.path.join(OUT_DIR, "02c_pairwise_TFN.csv"), index=False)

    # 3. Consistency check (on Saaty matrix)
    lam_max, CI, CR = consistency_ratio(saaty_pw)
    pd.DataFrame({"lambda_max": [lam_max], "CI": [CI], "RI": [0.58], "CR": [CR],
                  "Acceptable_(<0.10)": [CR < 0.10]}).to_csv(
        os.path.join(OUT_DIR, "03_consistency_ratio.csv"), index=False)

    # 4. Buckley fuzzy weights
    r_values, fuzzy_w, crisp_w = buckley_fuzzy_weights(fuzzy_pw)
    pd.DataFrame({"Criterion": CRITERIA,
                  "r_l": [r.l for r in r_values],
                  "r_m": [r.m for r in r_values],
                  "r_u": [r.u for r in r_values]}).to_csv(
        os.path.join(OUT_DIR, "04a_geometric_means.csv"), index=False)
    pd.DataFrame({"Criterion": CRITERIA,
                  "w_l": [w.l for w in fuzzy_w],
                  "w_m": [w.m for w in fuzzy_w],
                  "w_u": [w.u for w in fuzzy_w],
                  "centroid": [w.centroid() for w in fuzzy_w],
                  "normalised_crisp_w": crisp_w}).to_csv(
        os.path.join(OUT_DIR, "04b_fuzzy_weights.csv"), index=False)

    # 5. Fuzzy ELECTRE - normalisation
    benefit = [True, True, True]   # we treat each rated criticality as benefit-type
    norm_fuzzy = normalize_fuzzy(fuzzy_dm, benefit)
    pd.DataFrame([{"Stage": s, "Criterion": c,
                   "l": norm_fuzzy[s][c].l, "m": norm_fuzzy[s][c].m, "u": norm_fuzzy[s][c].u}
                  for s in STAGES for c in CRITERIA])\
        .to_csv(os.path.join(OUT_DIR, "05a_normalized_fuzzy_matrix.csv"), index=False)

    # 6. Weighted normalised fuzzy matrix
    weighted = weighted_fuzzy(norm_fuzzy, fuzzy_w)
    pd.DataFrame([{"Stage": s, "Criterion": c,
                   "l": weighted[s][c].l, "m": weighted[s][c].m, "u": weighted[s][c].u,
                   "centroid": weighted[s][c].centroid()}
                  for s in STAGES for c in CRITERIA])\
        .to_csv(os.path.join(OUT_DIR, "05b_weighted_fuzzy_matrix.csv"), index=False)

    # 7. Concordance / Discordance / Dominance
    res = fuzzy_electre(weighted, fuzzy_w)
    pd.DataFrame(res["C"], index=STAGES, columns=STAGES)\
        .to_csv(os.path.join(OUT_DIR, "06a_concordance_matrix.csv"))
    pd.DataFrame(res["D"], index=STAGES, columns=STAGES)\
        .to_csv(os.path.join(OUT_DIR, "06b_discordance_matrix.csv"))
    pd.DataFrame(res["F"], index=STAGES, columns=STAGES)\
        .to_csv(os.path.join(OUT_DIR, "06c_concordance_dominance_F.csv"))
    pd.DataFrame(res["G"], index=STAGES, columns=STAGES)\
        .to_csv(os.path.join(OUT_DIR, "06d_discordance_dominance_G.csv"))
    pd.DataFrame(res["E"], index=STAGES, columns=STAGES)\
        .to_csv(os.path.join(OUT_DIR, "06e_aggregate_dominance_E.csv"))
    pd.DataFrame({"Stage": STAGES,
                  "C_sup": res["C_sup"],
                  "D_inf": res["D_inf"],
                  "Net": res["net"],
                  "Rank": (-res["net"]).argsort().argsort() + 1}).to_csv(
        os.path.join(OUT_DIR, "07_final_ranking.csv"), index=False)

    # 8. Sensitivity analysis
    def factory(new_fw):
        return weighted_fuzzy(norm_fuzzy, new_fw)
    sens_df = sensitivity(factory, fuzzy_w)
    sens_df.to_csv(os.path.join(OUT_DIR, "08_sensitivity_analysis.csv"), index=False)

    # ---------- figures ----------
    fig_likert_distribution(df, cols_map)
    fig_decision_heatmap(crisp_dm)
    fig_membership_functions()
    fig_pairwise_LMU(fuzzy_pw)
    fig_fuzzy_weights(fuzzy_w, crisp_w)
    fig_matrix_heatmap(norm_fuzzy,
                       "Normalised Fuzzy Decision Matrix\n(centroid of TFN cells)",
                       "fig06_normalized_matrix_heatmap.png")
    fig_matrix_heatmap(weighted,
                       "Weighted Normalised Fuzzy Decision Matrix\n(centroid of w·v TFN cells)",
                       "fig07_weighted_matrix_heatmap.png", cmap="PuBu")
    fig_concordance_heatmap(res["C"], res["c_bar"])
    fig_discordance_heatmap(res["D"], res["d_bar"])
    fig_dominance_heatmap(res["E"])
    fig_net_flows(res["C_sup"], res["D_inf"])
    fig_final_ranking(res["net"])
    fig_sensitivity(sens_df)
    fig_radar(crisp_dm)
    fig_correlation_heatmap(df, cols_map)

    # ---------- summary print ----------
    summary = {
        "n_respondents": int(df.shape[0]),
        "criterion_priority": priority,
        "pca_share": pca_share,
        "mean_share": mean_share,
        "fuzzy_weights": [{"crit": c, "l": fuzzy_w[i].l, "m": fuzzy_w[i].m,
                            "u": fuzzy_w[i].u, "centroid": fuzzy_w[i].centroid(),
                            "normalised": float(crisp_w[i])}
                           for i, c in enumerate(CRITERIA)],
        "lambda_max": lam_max, "CI": CI, "CR": CR,
        "c_bar": float(res["c_bar"]), "d_bar": float(res["d_bar"]),
        "ranking": [{"stage": STAGES[i],
                     "C_sup": float(res["C_sup"][i]),
                     "D_inf": float(res["D_inf"][i]),
                     "net": float(res["net"][i])}
                    for i in (-res["net"]).argsort()],
    }
    with open(os.path.join(OUT_DIR, "00_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
