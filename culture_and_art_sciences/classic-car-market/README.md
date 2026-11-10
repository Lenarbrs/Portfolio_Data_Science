# From Machine to Masterpiece: Pricing Classic Cars at Auction

> An original dataset of 584 classic cars and hedonic regressions showing that provenance, rarity and the auction event itself shape prices.

| | |
|---|---|
| **Context** | Academic research paper, Université PSL |
| **Status** | Paper in preparation for publication (report in French) |
| **Team** | Noam Chabot, Léna Rebours |
| **Role** | End-to-end project contribution: literature review, research design, data collection and preprocessing, coding, statistical analysis, paper writing, and final presentation |
| **Stack** | Python, statsmodels (OLS, fixed effects), LLM-based feature extraction |

**Links:** [Report (PDF, French)](report/report_classic_car_market_fr.pdf)

## Research question

How are the prices of classic cars formed at auction? What turns a technical object into a high-value collectible, and which technical, contextual and narrative factors affect its price?

## Data

Original dataset built from auction catalogs: **584 cars**, **11 auctions**, **6 auction houses**, cars built between **1901 and 1995**. **44 variables** extracted through manual annotation and NLP.

For each car: standardized price, brand and year, auction context, and the full text description. An **LLM** extracts structured features from the descriptions, keeping only explicitly stated information: pedigree / provenance, restoration, rarity wording ("unique", "exceptional"), technical details.

## Methods: hedonic regression

- **Model 1, full hedonic model (OLS on log price):** year, brand, auction fixed effects, contextual variables and LLM-extracted features
- **Model 2, event effect:** indicator for the Rétromobile sale, with brand fixed effects

## Key results

- **Year** has a positive, significant effect on price
- **Pedigree / provenance** significantly raises value
- **Rarity wording** is strongly associated with higher prices
- Descriptive features such as colour are **not significant**
- Cars sold at **Rétromobile** are significantly more expensive: an event / context effect
