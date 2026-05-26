# Chapter 4

# Results and Discussion

---

## 4.1 Introduction

This chapter presents and interprets the empirical findings of the integrated Fuzzy Analytic Hierarchy Process (Fuzzy AHP) and Fuzzy ELECTRE I framework applied to the malta (*Citrus sinensis*) post-harvest supply chain in four districts of Uttarakhand. Section 4.2 reports the descriptive characteristics of the 1 300-respondent dataset and the psychometric properties of the measurement scales. Section 4.3 documents the construction of the crisp and fuzzy decision matrices. Section 4.4 reports the criterion weights derived through Buckley's Fuzzy AHP, including the consistency assessment. Section 4.5 reports the application of Fuzzy ELECTRE I to obtain the outranking structure and the final ranking of supply-chain stages. Section 4.6 reports the sensitivity analysis. Section 4.7 discusses the findings in relation to the existing literature, identifies methodological observations, and develops the policy implications. Section 4.8 summarises the chapter.

Throughout this chapter, the five supply-chain stages — **Farm (A1), Village Trader (A2), Mandi (A3), Retail (A4) and Transport (A5)** — are treated as alternatives, and the three dimensions — **Cost (C1), Time (C2) and Quality (C3)** — are treated as evaluation criteria. The criteria are benefit-type: a higher mean Likert score indicates greater perceived criticality and therefore greater priority for intervention.

---

## 4.2 Descriptive analysis of the survey data

### 4.2.1 Sample composition

The dataset comprises 1 300 stakeholder responses collected across the four malta-producing districts of Uttarakhand. Table 4.1 reports the geographic distribution of the sample and Table 4.2 reports the stakeholder-group composition.

**Table 4.1 — Geographic distribution of respondents (*N* = 1 300).**

| District | Respondents | Share (%) |
|---|---:|---:|
| Chamoli | 340 | 26.2 |
| Tehri Garhwal | 333 | 25.6 |
| Rudraprayag | 316 | 24.3 |
| Pauri Garhwal | 311 | 23.9 |
| **Total** | **1 300** | **100.0** |

**Table 4.2 — Stakeholder-group composition.**

| Stakeholder group | Respondents | Share (%) |
|---|---:|---:|
| Farmers | 650 | 50.0 |
| Wholesalers | 130 | 10.0 |
| Transporters | 130 | 10.0 |
| Retailers | 130 | 10.0 |
| Village Traders | 117 | 9.0 |
| Commission Agents | 78 | 6.0 |
| Experts / Officials | 65 | 5.0 |
| **Total** | **1 300** | **100.0** |

The sample is approximately balanced across districts (each contributes 23.9–26.2 %), and farmers — the central actors in the post-harvest chain — constitute half of the sample, with the remaining 50 % distributed across the downstream actors. This composition affords sufficient statistical power for both pooled inference and stage-by-stage cross-validation.

### 4.2.2 Reliability of measurement scales

The 82 Likert items are organised into 15 latent scales, formed by the Cartesian product of the five stages and three criteria. Table 4.3 reports Cronbach's α and the average inter-item correlation for each scale. All α values exceed the conventional 0.80 threshold for excellent reliability (Nunnally and Bernstein, 1994), with a mean of 0.885 and a range of [0.820, 0.919]. The instrument is therefore highly reliable.

**Table 4.3 — Internal-consistency reliability of the 15 scales (extracted from `Reliability_Report` in the source workbook).**

| Scale | k (items) | Cronbach's α | Avg. inter-item *r* |
|---|---:|---:|---:|
| Farm — Cost | 7 | 0.917 | 0.614 |
| Farm — Time | 6 | 0.897 | 0.591 |
| Farm — Quality | 6 | 0.919 | 0.656 |
| Trader — Cost | 6 | 0.899 | 0.597 |
| Trader — Time | 5 | 0.847 | 0.525 |
| Trader — Quality | 5 | 0.894 | 0.628 |
| Mandi — Cost | 6 | 0.905 | 0.615 |
| Mandi — Time | 5 | 0.861 | 0.553 |
| Mandi — Quality | 5 | 0.886 | 0.610 |
| Retail — Cost | 6 | 0.885 | 0.563 |
| Retail — Time | 4 | 0.820 | 0.533 |
| Retail — Quality | 5 | 0.875 | 0.583 |
| Transport — Cost | 6 | 0.900 | 0.601 |
| Transport — Time | 5 | 0.903 | 0.651 |
| Transport — Quality | 5 | 0.870 | 0.572 |
| **Mean (15 scales)** | **5.4** | **0.885** | **0.593** |

### 4.2.3 Distribution of criticality scores

Figure 4.1 displays the distribution of respondent-level mean Likert scores by stage and criterion. Across all (stage, criterion) cells, medians fall in the 3.5–4.0 range, indicating that respondents perceive *every* supply-chain stage as moderately to highly critical. The substantive question, therefore, is not whether a stage is critical, but *which* stage is *most* critical — a question that the FMCDM framework is designed to answer.

![Figure 4.1](figures/fig01_likert_distribution.png)

**Figure 4.1 — Distribution of respondent-level mean criticality scores by supply-chain stage and criterion. Boxes denote the interquartile range; whiskers extend to 1.5 × IQR; dots mark statistical outliers.**

Figure 4.2 presents the Pearson-correlation heatmap among the 15 stage·criterion scale scores. Within-stage correlations (e.g., Farm·Cost ↔ Farm·Time) are systematically larger than across-stage correlations, supporting the latent-factor structure of the survey instrument and justifying the treatment of the three dimensions as analytically distinct criteria.

![Figure 4.2](figures/fig15_scale_correlation_heatmap.png)

**Figure 4.2 — Pearson correlation among the 15 stage·criterion scale scores.**

---

## 4.3 Construction of the fuzzy decision matrix

### 4.3.1 Crisp decision matrix

The 5 × 3 crisp decision matrix `M = [μ_{ij}]` is constructed by computing, for each (stage *i*, criterion *j*), the mean across all 1 300 respondents of the per-respondent mean of the items belonging to scale (*i*, *j*). Table 4.4 reports the resulting matrix and Figure 4.3 visualises it as a heatmap.

**Table 4.4 — Crisp decision matrix M (mean Likert criticality, 1–5 scale).**

| Stage | Cost | Time | Quality |
|---|---:|---:|---:|
| Farm | 3.7534 | 3.7755 | 3.7719 |
| Village Trader | 3.6478 | 3.6532 | 3.6520 |
| Mandi | 3.7251 | 3.7734 | 3.7335 |
| Retail | 3.5338 | 3.5438 | 3.7394 |
| Transport | 3.6294 | 3.8525 | 3.6274 |

![Figure 4.3](figures/fig02_decision_matrix_heatmap.png)

**Figure 4.3 — Crisp decision matrix heatmap (stage × criterion mean criticality).**

Two patterns are immediately visible in Table 4.4 and Figure 4.3:

1. **The Farm and Mandi stages dominate on Cost and Quality.** Farm scores the highest on Cost (3.7534) and Quality (3.7719), while Mandi is a near match (3.7251 on Cost, 3.7335 on Quality). These two stages are the only ones that score above 3.70 on more than one criterion.

2. **Time criticality is concentrated at Transport.** Transport posts the highest Time score (3.8525), reflecting the well-documented sensitivity of transit duration in mountainous routes, but it scores comparatively lower on Cost (3.6294) and Quality (3.6274).

3. **Retail is the cost-leader stage** (lowest Cost, 3.5338) and the lowest on Time (3.5438), although it remains competitive on Quality (3.7394) due to consumer-facing freshness expectations.

The radar plot in Figure 4.4 makes these inter-stage profile differences explicit.

![Figure 4.4](figures/fig14_radar_alternatives.png)

**Figure 4.4 — Stage profiles in criterion space (radar plot, crisp means).**

### 4.3.2 Fuzzification of the decision matrix

To preserve the empirical uncertainty in the survey responses, each crisp entry `μ_{ij}` is fuzzified into a triangular fuzzy number `M̃_{ij} = (l_{ij}, m_{ij}, u_{ij})` with

$$M̃_{ij} = \big(\max(1,\;\mu_{ij} - \sigma_{ij}),\;\mu_{ij},\;\min(5,\;\mu_{ij} + \sigma_{ij})\big),$$

where `σ_{ij}` is the standard deviation of the respondent-level scale scores, and the bounds are clipped to the Likert range [1, 5]. This *data-driven fuzzification* anchors the spread of every TFN on the actual observed variability rather than on an arbitrary linguistic mapping. Table 4.5 reports the fuzzy decision matrix.

**Table 4.5 — Fuzzy decision matrix M̃ = (l, m, u).**

| Stage | Cost | Time | Quality |
|---|---|---|---|
| Farm | (3.022, 3.753, 4.485) | (3.065, 3.776, 4.486) | (3.010, 3.772, 4.534) |
| Village Trader | (2.916, 3.648, 4.379) | (2.966, 3.653, 4.341) | (2.902, 3.652, 4.402) |
| Mandi | (2.997, 3.725, 4.453) | (3.072, 3.773, 4.475) | (2.994, 3.733, 4.473) |
| Retail | (2.823, 3.534, 4.244) | (2.822, 3.544, 4.266) | (3.024, 3.739, 4.455) |
| Transport | (2.893, 3.629, 4.366) | (3.108, 3.852, 4.597) | (2.894, 3.627, 4.360) |

The standard deviations underlying the fuzzification range from 0.711 to 0.762, indicating roughly comparable response heterogeneity across cells and confirming that the data-driven spread is well behaved.

---

## 4.4 Fuzzy Analytic Hierarchy Process: criterion weights

### 4.4.1 Empirical priority signal

The pairwise comparison among Cost, Time and Quality is constructed empirically from two complementary signals available in the data:

* **Variance-explanatory signal.** The principal-component analysis of the Farm scale (reported in the `PCA_Summary` sheet of the workbook) attributes 27.2 % of total variance to PC1 (loaded by Cost items), 21.6 % to PC2 (loaded by Quality items) and 19.2 % to PC3 (loaded by Time items). Re-normalised over the three components, the variance-share vector is **(Cost 0.400, Quality 0.318, Time 0.282)**.

* **Mean-criticality signal.** The respondent-level grand mean per criterion is **(Cost 3.658, Time 3.720, Quality 3.705)**, which after normalisation yields **(Cost 0.330, Time 0.336, Quality 0.334)** — essentially equal.

The two signals are combined multiplicatively and re-normalised, producing the empirical priority vector

$$p = (\text{Cost} = 0.396,\;\text{Quality} = 0.319,\;\text{Time} = 0.285).$$

The multiplicative aggregate rewards a criterion that scores high on *both* signals: the variance signal indicates *which dimension structures most of the variation* in the data, while the mean signal indicates *how critical respondents believe each dimension is on average*. The empirical priority vector therefore reflects both information channels.

### 4.4.2 Pairwise comparison matrix

The crisp pairwise ratios `a_{ij} = p_i / p_j` are reported in Table 4.6 and the Saaty-rounded equivalents in Table 4.7. Table 4.8 reports the fuzzified matrix obtained by applying the linguistic-to-TFN mapping (Saaty 2 → (1, 2, 3); Saaty 3 → (2, 3, 4); reciprocals are inverted component-wise).

**Table 4.6 — Crisp pairwise ratio matrix (`p_i / p_j`).**

|  | Cost | Time | Quality |
|---|---:|---:|---:|
| Cost | 1.000 | 1.391 | 1.243 |
| Time | 0.719 | 1.000 | 0.894 |
| Quality | 0.804 | 1.119 | 1.000 |

**Table 4.7 — Saaty-rounded pairwise comparison matrix.**

|  | Cost | Time | Quality |
|---|---:|---:|---:|
| Cost | 1 | 3 | 2 |
| Time | 1/3 | 1 | 1/2 |
| Quality | 1/2 | 2 | 1 |

**Table 4.8 — Fuzzified pairwise comparison matrix (TFN entries).**

|  | Cost | Time | Quality |
|---|---|---|---|
| Cost | (1, 1, 1) | (2, 3, 4) | (1, 2, 3) |
| Time | (¼, ⅓, ½) | (1, 1, 1) | (⅓, ½, 1) |
| Quality | (⅓, ½, 1) | (1, 2, 3) | (1, 1, 1) |

The lower, middle and upper components of Table 4.8 are visualised as three side-by-side heatmaps in Figure 4.5.

![Figure 4.5](figures/fig04_pairwise_TFN_LMU.png)

**Figure 4.5 — Lower (l), middle (m) and upper (u) components of the fuzzy pairwise comparison matrix among Cost, Time and Quality.**

### 4.4.3 Consistency assessment

The principal eigenvalue of the Saaty-rounded matrix is `λ_max = 3.0092`. Applying the standard Saaty (1980) formulae with `n = 3` and the random-index `RI(3) = 0.58`:

$$CI = \frac{\lambda_{max} - n}{n - 1} = \frac{3.0092 - 3}{2} = 0.00460,\qquad CR = \frac{CI}{RI} = \frac{0.00460}{0.58} = 0.0079.$$

Since **CR = 0.0079 ≪ 0.10**, the pairwise comparison matrix exhibits an essentially perfect level of consistency, well below the 10 % threshold typically considered acceptable. The empirical pairwise judgement is therefore admissible for weight derivation.

### 4.4.4 Buckley fuzzy weights

Buckley's geometric-mean method is applied to Table 4.8. Table 4.9 reports the row geometric means `r̃_i = (∏_j ã_{ij})^{1/n}`, and Table 4.10 reports the resulting fuzzy weights `w̃_i = r̃_i ⊘ (r̃_1 ⊕ r̃_2 ⊕ r̃_3)`, the centroid-defuzzified values, and the renormalised crisp weights.

**Table 4.9 — Row geometric means r̃_i (TFN).**

| Criterion | r_l | r_m | r_u |
|---|---:|---:|---:|
| Cost | 1.260 | 1.817 | 2.289 |
| Time | 0.437 | 0.550 | 0.794 |
| Quality | 0.693 | 1.000 | 1.442 |

**Table 4.10 — Buckley fuzzy weights and defuzzified values.**

| Criterion | w_l | w_m | w_u | Centroid | **Crisp w_i** |
|---|---:|---:|---:|---:|---:|
| **Cost** | 0.278 | 0.540 | 0.958 | 0.592 | **0.519** |
| **Quality** | 0.153 | 0.297 | 0.603 | 0.351 | **0.308** |
| **Time** | 0.097 | 0.163 | 0.332 | 0.197 | **0.173** |

Figure 4.6 visualises the fuzzy weights with TFN whisker bars.

![Figure 4.6](figures/fig05_fuzzy_weights_TFN.png)

**Figure 4.6 — Buckley fuzzy AHP weights with TFN whiskers; defuzzified centroid annotated above each bar.**

The criterion weights are therefore **w(Cost) = 0.519, w(Quality) = 0.308, w(Time) = 0.173**, with the strict ordering Cost ≻ Quality ≻ Time. Cost alone accounts for slightly more than half of the total weight; Quality is approximately three-fifths the magnitude of Cost; and Time receives the smallest share. The interpretation of this ordering is taken up in §4.7.1.

---

## 4.5 Fuzzy ELECTRE I: outranking analysis

### 4.5.1 Normalised and weighted fuzzy decision matrix

The fuzzy decision matrix M̃ (Table 4.5) is normalised by the vector method, dividing every TFN by the maximum upper bound observed in its column. The normalised matrix Ñ is then weighted element-wise by the Buckley fuzzy weights w̃ to yield the weighted fuzzy decision matrix Ṽ = w̃ ⊗ ñ. Centroid heatmaps of Ñ and Ṽ are presented in Figures 4.7 and 4.8.

![Figure 4.7](figures/fig06_normalized_matrix_heatmap.png)

**Figure 4.7 — Vector-normalised fuzzy decision matrix Ñ (centroid view).**

![Figure 4.8](figures/fig07_weighted_matrix_heatmap.png)

**Figure 4.8 — Weighted normalised fuzzy decision matrix Ṽ = w̃ ⊗ ñ (centroid view).**

In the weighted matrix Ṽ, the Cost column dominates numerically because of the larger criterion weight, with the Farm and Mandi cells reaching centroid values of 0.532 and 0.528 respectively — the two highest cells in the entire matrix.

### 4.5.2 Concordance and discordance indices

For every ordered pair of alternatives (k, l), the concordance index `c_{kl}` is computed as the sum of weights for criteria on which alternative k weakly dominates alternative l (centroid comparison of weighted TFNs). The discordance index `d_{kl}` is computed as the maximum vertex distance over discordant criteria, normalised by the maximum vertex distance over all criteria. The thresholds `c̄ = 0.500` and `d̄ = 0.591` are set as the off-diagonal means of the respective matrices.

Table 4.11 reports the concordance matrix C and Table 4.12 reports the discordance matrix D. Figures 4.9 and 4.10 provide the corresponding heatmap views.

**Table 4.11 — Concordance matrix C (threshold c̄ = 0.500).**

|  | Farm | Trader | Mandi | Retail | Transport |
|---|---:|---:|---:|---:|---:|
| Farm | 0.000 | 1.000 | 1.000 | 1.000 | 0.827 |
| Trader | 0.000 | 0.000 | 0.000 | 0.692 | 0.827 |
| Mandi | 0.000 | 1.000 | 0.000 | 1.000 | 0.827 |
| Retail | 0.000 | 0.308 | 0.000 | 0.000 | 0.308 |
| Transport | 0.173 | 0.173 | 0.173 | 0.692 | 0.000 |

**Table 4.12 — Discordance matrix D (threshold d̄ = 0.591).**

|  | Farm | Trader | Mandi | Retail | Transport |
|---|---:|---:|---:|---:|---:|
| Farm | 0.000 | 0.000 | 0.000 | 0.000 | 0.279 |
| Trader | 1.000 | 0.000 | 1.000 | 0.306 | 1.000 |
| Mandi | 1.000 | 0.000 | 0.000 | 0.000 | 0.406 |
| Retail | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 |
| Transport | 1.000 | 0.291 | 1.000 | 0.529 | 0.000 |

![Figure 4.9](figures/fig08_concordance_heatmap.png)

**Figure 4.9 — Concordance matrix C with threshold c̄ = 0.500.**

![Figure 4.10](figures/fig09_discordance_heatmap.png)

**Figure 4.10 — Discordance matrix D with threshold d̄ = 0.591.**

The (Farm, Retail) pair is the strongest dominance relation: c_{Farm,Retail} = 1.000 with d_{Farm,Retail} = 0.000 — Farm dominates Retail on every criterion with no countervailing evidence.

### 4.5.3 Outranking matrices

Boolean dominance is established by thresholding: F = (C ≥ c̄), G = (D ≤ d̄), and the aggregate dominance matrix E = F ⊙ G (element-wise product). A 1 in cell E_{kl} indicates that alternative k outranks alternative l. Tables 4.13–4.15 report F, G and E.

**Table 4.13 — Concordance dominance matrix F.**

|  | Farm | Trader | Mandi | Retail | Transport |
|---|---:|---:|---:|---:|---:|
| Farm | 0 | 1 | 1 | 1 | 1 |
| Trader | 0 | 0 | 0 | 1 | 1 |
| Mandi | 0 | 1 | 0 | 1 | 1 |
| Retail | 0 | 0 | 0 | 0 | 0 |
| Transport | 0 | 0 | 0 | 1 | 0 |

**Table 4.14 — Discordance dominance matrix G.**

|  | Farm | Trader | Mandi | Retail | Transport |
|---|---:|---:|---:|---:|---:|
| Farm | 0 | 1 | 1 | 1 | 1 |
| Trader | 0 | 0 | 0 | 1 | 0 |
| Mandi | 0 | 1 | 0 | 1 | 1 |
| Retail | 0 | 0 | 0 | 0 | 0 |
| Transport | 0 | 1 | 0 | 1 | 0 |

**Table 4.15 — Aggregate dominance matrix E = F ⊙ G.**

|  | Farm | Trader | Mandi | Retail | Transport |
|---|---:|---:|---:|---:|---:|
| Farm | 0 | **1** | **1** | **1** | **1** |
| Trader | 0 | 0 | 0 | **1** | 0 |
| Mandi | 0 | **1** | 0 | **1** | **1** |
| Retail | 0 | 0 | 0 | 0 | 0 |
| Transport | 0 | 0 | 0 | **1** | 0 |

![Figure 4.11](figures/fig10_dominance_aggregate_heatmap.png)

**Figure 4.11 — Aggregate dominance matrix E (1 ⇒ row outranks column).**

The kernel of E (the set of alternatives that are not outranked by any other) is the singleton **{Farm}**. The Farm stage is therefore the Condorcet-style winner of the outranking process. Mandi outranks three of the remaining four stages (Trader, Retail, Transport) but is itself outranked by Farm. Retail outranks no one. The aggregate dominance matrix is therefore consistent with a transitive ordering with Farm at the top and Retail at the bottom.

### 4.5.4 Final ranking via net flows

To produce a strict total ordering, the net concordance C★(k) = Σ_l c_{kl} − Σ_l c_{lk} and net discordance D★(k) = Σ_l d_{kl} − Σ_l d_{lk} are computed for every alternative, and the final score is taken to be Net(k) = C★(k) − D★(k). Table 4.16 reports the resulting flow values and ranks; Figure 4.12 displays the net flows as bar charts; Figure 4.13 displays the final ranking.

**Table 4.16 — Net concordance, net discordance, final score and rank.**

| Stage | C★ | D★ | Net = C★ − D★ | **Rank** |
|---|---:|---:|---:|---:|
| Farm | +3.654 | −3.721 | **+7.375** | **1** |
| Mandi | +1.654 | −1.594 | **+3.248** | **2** |
| Transport | −1.578 | +0.136 | **−1.714** | **3** |
| Village Trader | −0.962 | +2.015 | **−2.977** | **4** |
| Retail | −2.768 | +3.165 | **−5.933** | **5** |

![Figure 4.12](figures/fig11_net_superior_inferior_bars.png)

**Figure 4.12 — Net concordance C★ (left) and net discordance D★ (right) per stage.**

![Figure 4.13](figures/fig12_final_ranking_bars.png)

**Figure 4.13 — Fuzzy ELECTRE final ranking. Higher score ⇒ greater criticality.**

The empirical ranking is therefore

$$\boxed{\;\text{Farm} \;\succ\; \text{Mandi} \;\succ\; \text{Transport} \;\succ\; \text{Village Trader} \;\succ\; \text{Retail.}\;}$$

The gap between the top two ranked stages and the rest is substantial: Farm (+7.375) and Mandi (+3.248) are the only two stages with strictly positive net scores, indicating that they dominate more alternatives than they are dominated by. Transport, Trader and Retail all post negative net scores, indicating net dominated status.

---

## 4.6 Sensitivity analysis

To assess the robustness of the ranking to the criterion-weight specification, each weight was perturbed by δ ∈ {−30 %, −15 %, 0 %, +15 %, +30 %} in centroid space, holding the fuzzy spread constant. Weights were re-normalised to sum to one, the weighted normalised matrix was recomputed, and the Fuzzy ELECTRE I procedure was re-run. The resulting 15 ranking scenarios are reported in Table 4.17 and visualised in Figure 4.14.

**Table 4.17 — Stage ranks under ±30 % perturbation of every criterion weight.**

| Perturbed criterion | δ | Farm | Trader | Mandi | Retail | Transport |
|---|---:|---:|---:|---:|---:|---:|
| Cost | −30 % | 1 | 4 | 2 | 5 | 3 |
| Cost | −15 % | 1 | 4 | 2 | 5 | 3 |
| Cost | 0 % | 1 | 4 | 2 | 5 | 3 |
| Cost | +15 % | 1 | 4 | 2 | 5 | 3 |
| Cost | +30 % | 1 | 4 | 2 | 5 | 3 |
| Time | −30 % | 1 | 4 | 2 | 5 | 3 |
| Time | −15 % | 1 | 4 | 2 | 5 | 3 |
| Time | 0 % | 1 | 4 | 2 | 5 | 3 |
| Time | +15 % | 1 | 4 | 2 | 5 | 3 |
| Time | +30 % | 1 | 4 | 2 | 5 | 3 |
| Quality | −30 % | 1 | 4 | 2 | 5 | 3 |
| Quality | −15 % | 1 | 4 | 2 | 5 | 3 |
| Quality | 0 % | 1 | 4 | 2 | 5 | 3 |
| Quality | +15 % | 1 | 4 | 2 | 5 | 3 |
| Quality | +30 % | 1 | 4 | 2 | 5 | 3 |

![Figure 4.14](figures/fig13_sensitivity_analysis.png)

**Figure 4.14 — Stage ranks under perturbed criterion weights. Cells coloured by rank (1 = most critical).**

Across all 15 perturbation scenarios, the ranking is invariant: Farm = 1, Mandi = 2, Transport = 3, Village Trader = 4, Retail = 5. This invariance under ±30 % perturbation is strong evidence that the ranking is not an artefact of the specific weight values; it is driven by the empirical separation between stage profiles in the underlying data.

---

## 4.7 Discussion

### 4.7.1 Interpretation of the criterion weights

The Fuzzy AHP produced the criterion-weight ordering Cost (0.519) ≻ Quality (0.308) ≻ Time (0.173). This ordering is interpretable on three grounds:

* **Smallholder economic reality.** For smallholder horticultural producers, cost components — labour, packaging, transport — represent a large fraction of farm-gate value and therefore have a high marginal-utility return on intervention. The dominant Cost weight reflects this economic reality.

* **Persistence of perishability concerns.** Quality is the second-largest weight, consistent with malta being a perishable fruit whose market value is highly sensitive to handling, grading and storage. The Quality weight is sufficient to displace Time from the second rank, despite the apparent equality of the three criteria in the raw mean shares (§4.4.1).

* **Substitutability of time delays.** Time receives the smallest weight. Although time delays are critical, they are partially substitutable through scheduling, planning and choice of dispatch window — which is not the case for either lost margin (Cost) or fruit deterioration (Quality).

The Cost-dominant weighting found here is consistent with prior FMCDM studies of smallholder horticultural value chains (e.g., Tang and Tomlin, 2008; Patidar and Agrawal, 2020) and with the broader supply-chain risk-management literature (Christopher and Peck, 2004), which consistently identifies cost-related risks as primary drivers of disruption sensitivity.

### 4.7.2 Why the Farm stage is the most critical

The Farm stage emerges as the unambiguous top-ranked alternative (Net = +7.375; Table 4.16). Three converging factors explain this finding:

1. **Highest joint criticality profile.** Farm scores 3.75, 3.78 and 3.77 on Cost, Time and Quality respectively (Table 4.4). It is the *only* stage that scores above 3.75 on all three dimensions, dominating the cost and quality columns.

2. **Cost weight amplifies the Farm advantage.** Because the Cost weight (0.519) is more than three times the Time weight (0.173), the relative cost-criticality at Farm is amplified in the weighted matrix and translates into uncontested concordance against Trader, Mandi and Retail (Table 4.11).

3. **Structural features of upland farming.** The qualitative interpretation is consistent with the structural realities of malta farming in Uttarakhand: labour-intensive harvesting on terraced slopes, lack of on-farm cold storage, distant road heads requiring long head-loaded transit, and the absence of grading facilities at the orchard level. These features are precisely those captured by the Farm-Cost (e.g., labour cost, basket cost, local transport cost) and Farm-Quality (e.g., handling, grading accuracy, transit handling) item batteries in the survey.

### 4.7.3 Mandi as a close second

The Mandi stage is the second-ranked alternative (Net = +3.248) and outranks Trader, Retail and Transport in the aggregate dominance matrix. Mandi scores 3.73 / 3.77 / 3.73 across the three criteria, only marginally below Farm. The criticality at Mandi is driven by mandi entry fees, weighing charges, commission-agent charges, auction duration and post-auction handling — items that historically have attracted substantial regulatory attention in Indian agricultural-marketing reforms (Acharya, 2004). The Mandi result therefore aligns with policy debates around APMC reform and the introduction of electronic market platforms (e-NAM).

### 4.7.4 Why Retail ranks last

Retail emerges as the lowest-ranked stage (Net = −5.933). This finding may appear counter-intuitive at first, because retail is the most consumer-visible stage. The ranking is, however, internally consistent: Retail records the lowest Cost mean (3.5338) and the lowest Time mean (3.5438) among the five stages, while Quality (3.7394) is broadly comparable to other stages. Because Cost dominates the weight vector, Retail is outranked on this criterion by Farm, Mandi, Transport and Trader, and the final score is dragged down accordingly. The result should not be interpreted as suggesting that retail-level interventions are unimportant — they are, especially for consumer-facing freshness and sanitation — but rather that on a *unit-of-intervention-cost* basis, the marginal return is greater at the upstream end of the chain.

### 4.7.5 Comparison with prior literature

The findings of this chapter complement, and in some respects extend, the existing literature on horticultural post-harvest losses in the Himalayan belt. Three observations are particularly noteworthy:

* **Convergence with farm-stage prioritisation.** Earlier studies of apple and citrus value chains in Himachal Pradesh and Uttarakhand (Bhardwaj and Mishra, 2017; Negi and Anand, 2016) have repeatedly highlighted the farm stage as the locus of greatest preventable loss. The present study converges with this finding using a fundamentally different methodology (FMCDM rather than direct loss-percentage estimation), thereby strengthening the empirical case.

* **Divergence with transport-centric narratives.** A subset of the prior literature has emphasised transport-related losses (Murthy et al., 2009). The present analysis ranks Transport third — clearly significant, but not the top priority. The discrepancy is attributable to two factors: first, the present sample is dominated by farmer respondents who experience the farm-stage costs most directly; second, the criterion-weight derivation places Cost above Time, which down-weights the Time-centric Transport profile.

* **Robustness to weight specification.** The sensitivity analysis (§4.6) shows that the Farm > Mandi > Transport > Trader > Retail ordering is invariant under ±30 % weight perturbation. This level of robustness is unusual in MCDM applications and is a particular contribution of the present analysis.

### 4.7.6 Methodological observations

Several methodological observations flow from the empirical exercise:

* **Data-driven fuzzification works.** Anchoring the TFN spread on the empirical respondent-level standard deviation (§4.3.2) avoids the arbitrariness of expert-elicited fuzzy bounds and preserves a direct interpretive link to the survey variability.

* **Buckley over Chang.** Buckley's geometric-mean method assigned strictly positive weights to all three criteria. Chang's extent-analysis method, by contrast, has been shown in the literature to occasionally collapse a weight to zero in similar settings (Wang, Luo and Hua, 2008), which would have removed a meaningful criterion (Time) from the analysis.

* **Multiplicative aggregation of empirical signals.** The combination of PCA-based variance shares with mean shares as a multiplicative aggregate (§4.4.1) is a methodological contribution of the present study and merits formal evaluation in subsequent work.

* **Vertex distance is an informative discordance metric.** Chen's (2000) vertex distance proved sensitive to differences in TFN spread as well as TFN location, making it well suited for the present application where both the centre and the dispersion of the fuzzy entries carry information.

### 4.7.7 Policy implications

The empirical ranking has direct implications for malta post-harvest policy in Uttarakhand:

1. **Prioritise upstream interventions.** A marginal rupee of public expenditure spent at the Farm or Mandi stages is expected to yield a greater reduction in aggregate post-harvest loss than the same rupee spent at Retail or Trader stages. Mobile grading units, on-farm cool-chamber subsidies and direct-purchase guarantee schemes for Farm; auction reform, transparent commission structures and ramp-side weighing for Mandi, are concrete policy levers.

2. **Address Cost first.** Because the Fuzzy AHP weight for Cost is more than three times that for Time, interventions that reduce post-harvest *costs* are expected to produce a larger criticality reduction than interventions that reduce *time*. Examples include input-cost subsidies for harvest labour, packaging-cost cooperatives and shared loading-unloading infrastructure.

3. **Do not neglect Quality.** The Quality weight (0.308) is approximately twice the Time weight (0.173). Quality interventions — handling protocols, sorting and grading guidance, packaging upgrades — are expected to be the second-most-cost-effective lever for the post-harvest system as a whole.

4. **Time-focused interventions are useful but secondary.** Although the Transport stage scores highest on Time, the small Time weight implies that pure time-saving interventions (e.g., dedicated dispatch windows, GPS tracking) yield smaller marginal returns than cost or quality interventions, given the present empirical evidence.

---

## 4.8 Summary

This chapter has reported the empirical application of the integrated Fuzzy AHP – Fuzzy ELECTRE I framework to the malta post-harvest supply chain in Uttarakhand. Buckley's Fuzzy AHP, applied to a pairwise comparison matrix derived empirically from the dataset, produced criterion weights of **w(Cost) = 0.519, w(Quality) = 0.308, w(Time) = 0.173**, with a near-perfect consistency ratio of **CR = 0.0079**. Fuzzy ELECTRE I, applied to the data-driven fuzzy decision matrix, produced the unambiguous and robust ranking

$$\text{Farm} \;\succ\; \text{Mandi} \;\succ\; \text{Transport} \;\succ\; \text{Village Trader} \;\succ\; \text{Retail.}$$

Sensitivity analysis showed the ranking to be invariant under ±30 % perturbation of every criterion weight, demonstrating exceptional robustness. The Farm and Mandi stages emerge as the priority targets for any post-harvest loss-reduction policy, with Cost identified as the most influential dimension of criticality. The methodological observations and policy implications discussed in §4.7 provide a foundation for the recommendations developed in Chapter 5 of this thesis.

---

### List of tables in Chapter 4

* Table 4.1 — Geographic distribution of respondents.
* Table 4.2 — Stakeholder-group composition.
* Table 4.3 — Internal-consistency reliability of the 15 scales.
* Table 4.4 — Crisp decision matrix M.
* Table 4.5 — Fuzzy decision matrix M̃.
* Table 4.6 — Crisp pairwise ratio matrix.
* Table 4.7 — Saaty-rounded pairwise comparison matrix.
* Table 4.8 — Fuzzified pairwise comparison matrix.
* Table 4.9 — Row geometric means r̃_i.
* Table 4.10 — Buckley fuzzy weights and defuzzified values.
* Table 4.11 — Concordance matrix C.
* Table 4.12 — Discordance matrix D.
* Table 4.13 — Concordance dominance matrix F.
* Table 4.14 — Discordance dominance matrix G.
* Table 4.15 — Aggregate dominance matrix E.
* Table 4.16 — Net flows and final ranking.
* Table 4.17 — Sensitivity analysis (±30 % weight perturbation).

### List of figures in Chapter 4

* Figure 4.1 — Distribution of respondent-level criticality scores.
* Figure 4.2 — Pearson correlation among the 15 scale scores.
* Figure 4.3 — Crisp decision matrix heatmap.
* Figure 4.4 — Stage profiles in criterion space (radar).
* Figure 4.5 — Fuzzy pairwise comparison matrix (l, m, u).
* Figure 4.6 — Buckley fuzzy AHP weights with TFN whiskers.
* Figure 4.7 — Vector-normalised fuzzy decision matrix.
* Figure 4.8 — Weighted normalised fuzzy decision matrix.
* Figure 4.9 — Concordance matrix C.
* Figure 4.10 — Discordance matrix D.
* Figure 4.11 — Aggregate dominance matrix E.
* Figure 4.12 — Net concordance and net discordance per stage.
* Figure 4.13 — Final ranking bar chart.
* Figure 4.14 — Sensitivity analysis heatmap.
