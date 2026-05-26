# Malta (Citrus) Post-Harvest Supply Chain — Fuzzy AHP & Fuzzy ELECTRE I

This repository contains a complete Fuzzy Multi-Criteria Decision-Making (FMCDM) analysis of the malta (sweet lime, *Citrus sinensis*) post-harvest supply chain in four districts of Uttarakhand. It applies **Buckley's Fuzzy AHP** to derive criterion weights from a 1 300-respondent survey and **Fuzzy ELECTRE I** to rank the five supply-chain stages (Farm, Trader, Mandi, Retail, Transport).

## Headline result

| | Cost | Quality | Time |
|---|---:|---:|---:|
| Fuzzy AHP weight | **0.519** | **0.308** | **0.173** |

Consistency ratio **CR = 0.0079** ≪ 0.10.

> Final stage ranking: **Farm ≻ Mandi ≻ Transport ≻ Trader ≻ Retail**.
>
> The ranking is invariant under ±30 % perturbation of every criterion weight.

## Repository layout

```
PP/
├─ Malta_.xlsx                          ← raw survey data (1 300 respondents, 82 items)
├─ Thesis_Chapter_FAHP_FELECTRE.md      ← PhD thesis chapter (methodology, calculations, results, discussion)
├─ code/
│  └─ fuzzy_mcdm.py                     ← full pipeline (TFN class, Buckley AHP, Fuzzy ELECTRE I, sensitivity, plots)
├─ outputs/                             ← 21 CSVs of intermediate matrices and summary.json
└─ figures/                             ← 15 PNGs (boxplot, heatmaps, fuzzy weights, ranking, sensitivity, radar, …)
```

## Reproducing the analysis

```bash
pip install --quiet openpyxl pandas numpy matplotlib seaborn
python code/fuzzy_mcdm.py
```

The script regenerates everything under `outputs/` and `figures/`.

## Key figures

* `figures/fig02_decision_matrix_heatmap.png` — crisp 5×3 stage·criterion mean matrix.
* `figures/fig05_fuzzy_weights_TFN.png` — Buckley fuzzy AHP weights with TFN whiskers.
* `figures/fig08_concordance_heatmap.png` and `fig09_discordance_heatmap.png` — Fuzzy ELECTRE I concordance and discordance.
* `figures/fig10_dominance_aggregate_heatmap.png` — outranking matrix (Farm dominates everyone).
* `figures/fig12_final_ranking_bars.png` — final ranking.
* `figures/fig13_sensitivity_analysis.png` — rank stability under ±30 % weight perturbation.

## Citation

If you use the framework or the figures, please cite the thesis chapter `Thesis_Chapter_FAHP_FELECTRE.md` and reference the foundational works of Saaty (1980), Buckley (1985), Roy (1968), and Hatami-Marbini & Tavana (2011).
