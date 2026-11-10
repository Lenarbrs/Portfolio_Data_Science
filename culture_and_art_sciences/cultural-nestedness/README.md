# Nestedness in Cultural Data

> A standardized reassessment of nestedness across 122 cultural datasets, testing how much the conclusion depends on the metric and the null model.

| | |
|---|---|
| **Period** | January – July 2025 |
| **Context** | Research internship (UROP), ENS-PSL |
| **Status** | Paper in preparation (methodology report available) |
| **Role** | Data compilation, simulation pipeline and analysis |
| **Stack** | Python, NODF and nestedness temperature, null-model simulations |

**Links:** [Code (full project repository)](https://github.com/Lenarbrs/2025_Global_Nestedness_Analysis) · [Methodology report (PDF)](report/report_global_nestedness.pdf)

> The code lives in a separate repository; this folder gives the overview and the report.

## Research question

Is nestedness a general property of cultural data? The literature claims it is, but uses different metrics and baselines, which makes results hard to compare. We apply the **same toolkit to all datasets** and ask:

- Is nestedness pervasive, and against which baselines does it appear?
- Do matrix size and fill influence nestedness?
- Does it vary across types of datasets?
- Do the two metrics (NODF and temperature) agree?

## Data

**122 binary matrices** (rows = repertoires such as users, languages or individuals; columns = cultural items such as movies, phonemes or traits) from:

- movie collections (Netflix, MovieLens)
- knowledge datasets (trivia)
- phonological inventories (PHOIBLE)
- ethnobotanical knowledge
- archaeological assemblages

Some matrices contain millions of observations.

## Methods

- **Metrics:** NODF and nestedness temperature
- **8 null models:** `r00`, `r0`, `r1`, `r2`, `c0`, `c1`, `swap`, `curveball`, each preserving different margins
- **Simulation:** 1,000 simulations per null model, i.e. 8,000 per matrix, to get simulation-based p-values

## Key results

The report in this folder documents the methodology and data structure. Final results are in preparation. 
