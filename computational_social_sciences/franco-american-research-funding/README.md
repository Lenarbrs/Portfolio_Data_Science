# Mapping Research Funding in Franco-American Science

> Econometric analysis of funding structures in 351,765 France–US co-authored articles (OpenAlex, 1990–2025): more funders, more hybrid public/private funding, growing non-Western sources.

| | |
|---|---|
| **Period** | 2026 |
| **Context** | Computational Social Sciences course, Université PSL |
| **Status** | Completed (report in French) |
| **Team** | Elsa Bidant, Eloïse Delerue, Lucile Lapray, Alice N'Gbesso, Léna Rebours |
| **Role** | literature review, methodology, coding, data analysis, academic writing, and final presentation |
| **Stack** | Python, OpenAlex API, pandas, statsmodels (logit, OLS), Spearman / Kendall |

**Links:** [Code (full project repository)](https://github.com/lucile40lpy/2025-26_sciences_sociales_computationnelles-financement_cooperation_fr_us) · [Report (PDF, French)](report/report_franco_american_funding_fr.pdf)

> The code lives in another repository; this folder gives the overview and the report.

## Research question

How is scientific funding structured in Franco-American collaborations, across institutions, fields, time and geographic origin?

## Data

[OpenAlex](https://openalex.org/): **351,765 articles**, 1990–2025, restricted to France + US collaborations, with authors, institutions, topics, funders and citations.

Processing: filtering on France–US collaborations, number of funders, binary funding indicator, one-hot encoding of scientific domains, dimensionality reduction.

## Methods

- **Logistic regression:** probability that an article is funded, by year, field and year × field interaction
- **OLS models:** (1) number of funders → citation impact (FWCI); (2) number of distinct funders over time; (3) share of hybrid public + private funding over time
- **Spearman / Kendall correlations** for temporal and geographic trends

## Key results

- Funding mentions rise significantly over time
- Strong growth in funded work in AI, biotechnology and quantum physics
- Rise of **hybrid public + private** funding and of the number of funding institutions
- Growing role of **non-Western (especially Asian)** funders
- More funding sources are associated with slightly higher citation impact
