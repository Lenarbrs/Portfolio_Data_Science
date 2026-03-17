# 🔬 Mapping Research Funding in Franco-American Science

**Note:** The full implementation of this project (data extraction, notebooks, and statistical analysis) lives in another GitHub repository.

🔗 **Code repository:**
[\[Link to the full project repository\]](https://github.com/lucile40lpy/2025-26_sciences_sociales_computationnelles-financement_cooperation_fr_us)

This repository contains a short overview of the project.

---

## Research Question

How is scientific funding structured in **Franco-American research collaborations**?

This project analyzes how funding is distributed across:

- institutions
- scientific fields
- time
- geographic origins

---

## 📊 Data

The dataset was built using **OpenAlex**, a large-scale open database of scientific publications.

- **351,765 articles**
- Time period: **1990–2025**
- Franco-American collaborations only
- Rich metadata: authors, institutions, topics, funding sources, citations

---

## ⚙️ Data Processing

Key steps:

- filtering articles with **France + US collaborations**
- feature engineering:
  - number of funding institutions
  - binary funding indicator

- one-hot encoding of **scientific domains**
- cleaning and reduction of high-dimensional data

---

## 🤖 Modeling Approach

### Logistic Regression

Used to model the probability that an article is **funded or not**:

- dependent variable: funding presence (binary)
- predictors:
  - publication year
  - scientific field
  - interaction terms (year × field)

Allows us to measure how funding evolves **over time and across disciplines**

---

### Linear Regression (OLS)

Several OLS models were implemented:

#### 1. Funding Diversity → Scientific Impact

- dependent variable: **FWCI (citation impact)**
- predictor: number of funding institutions

Result: more funding sources → slightly higher impact

---

#### 2. Institutional Diversity Over Time

- dependent variable: number of distinct funding institutions
- predictor: year

---

#### 3. Hybrid Funding Dynamics

- dependent variable: proportion of **public + private funding**
- predictor: year

---

### 🔗 Correlation Analysis

- **Spearman / Kendall correlations** used to analyze:
  - temporal trends
  - geographic shifts in funding sources

---

## Key Results

- 📈 Funding mentions increase significantly over time
- 🧬 Strong growth in funding for:
  - AI
  - biotechnology
  - quantum physics

- 🤝 Rise of **hybrid funding (public + private)**
- 🏢 Increasing number of funding institutions
- 🌍 Growing role of **non-Western (especially Asian) funding**

---

## 🏷 Keywords

Data Science • Econometrics • Regression • OpenAlex • Science Policy • Research Funding • Computational Social Science
