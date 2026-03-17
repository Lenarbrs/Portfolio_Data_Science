# 🚗 From Machine to Masterpiece: Pricing Classic Cars

## Research Question

How are the prices of **classic cars formed at auctions**?

This project investigates how a technical object, a car, becomes a **high-value collectible**, and which factors (technical, contextual, and narrative) influence its price.

---

## Project Idea

The value of collectible cars is not determined solely by their physical characteristics.

This project explores how prices are shaped by:

- **observable features** (year, brand, condition)
- **contextual factors** (auction house, events like Rétromobile)
- **narrative elements** embedded in textual descriptions

The project combines **quantitative modeling and qualitative analysis** to understand how value is constructed in this market.

---

## 📊 Data

The dataset was built manually from auction catalogs and includes:

- **584 vehicles**
- **11 auctions**
- **6 auction houses**
- cars produced between **1901 and 1995**

For each car, the dataset includes:

- price (adjusted and standardized)
- brand and year
- auction context
- detailed textual descriptions

Additional features were extracted using a **Large Language Model (LLM)** from the descriptions.

---

## Feature Extraction with LLMs

A Large Language Model was used to extract structured information from auction descriptions.

This includes variables such as:

- presence of **pedigree / provenance**
- mention of **restoration**
- **rarity indicators** (e.g. "unique", "exceptional")
- technical details (engine, configuration)

Only explicitly stated information was retained, ensuring **high-quality structured features**.

---

## 📈 Predictive Modeling (Hedonic Regression)

To analyze price formation, the project uses **hedonic regression models**, a standard method in economics to explain prices based on product characteristics.

---

### Model 1 — Full Hedonic Model (OLS)

A **linear regression model (OLS)** was used to explain the **log of the price**.

The model includes:

- car characteristics (year, brand)
- auction-level effects (fixed effects)
- contextual variables
- features extracted from text (LLM variables)

This model captures how different attributes contribute to price variation.

👉 Key findings:

- **Year** has a positive and significant effect on price
- **Pedigree / provenance** significantly increases value
- **Rarity indicators** (e.g. “unique”) are strongly associated with higher prices
- descriptive features (e.g. color) are **not significant**

---

### Model 2 — Event Effect (Rétromobile)

A second regression focuses on the effect of **auction context**, particularly the Rétromobile event.

This model includes:

- an indicator variable for **Rétromobile**
- brand fixed effects

👉 Key finding:

- cars sold at **Rétromobile are significantly more expensive**, suggesting a strong **event / context effect**

---

## 🏷 Keywords

Econometrics • Hedonic Regression • Cultural Economics • NLP • LLM Feature Extraction • Auction Data • Art Market
