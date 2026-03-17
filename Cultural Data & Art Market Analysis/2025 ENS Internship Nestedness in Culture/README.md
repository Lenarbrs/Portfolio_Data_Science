# 🌍 Nestedness in Cultural Data: A Comparative and Methodological Analysis

⚠️ **Note:** The full implementation of this project (data processing, simulations, and statistical analysis) lives in another GitHub repository.

🔗 **Code repository:**
[\[Link to the full project repository\]](https://github.com/Lenarbrs/2025_Global_Nestedness_Analysis)

---

## Research Questions

Is **nestedness** a general property of cultural data?

This project investigates:

- whether nestedness is **pervasive across cultural domains**
- how results depend on **metrics and null models**
- whether structural properties (matrix size, density) influence nestedness

---

## Project Idea

Nestedness describes a structure where:

-> rare elements appear only in **large repertoires**
-> small repertoires contain mostly **common elements**

While widely studied in ecology, its role in **cultural data** remains unclear due to inconsistent methodologies.

This project proposes a **systematic and standardized reassessment** of nestedness across multiple cultural domains.

---

## Data (Large-Scale Comparative Analysis)

The study compiles **122 binary matrices** from diverse cultural domains:

- 🎬 movie collections (Netflix, MovieLens)
- 🧠 knowledge datasets (trivia)
- 🗣 phonological inventories (PHOIBLE)
- 🌿 ethnobotanical knowledge
- 🏺 archaeological assemblages

-> Some matrices contain **millions of observations**, making this a **large-scale comparative study**.

Each dataset is represented as a **binary matrix**:

- rows = repertoires (e.g. users, languages, individuals)
- columns = cultural elements (e.g. movies, phonemes, traits)
- values = presence (1) / absence (0)

---

## Modeling Approach

### Nestedness Metrics

Two complementary measures were used:

- **NODF (Nestedness based on Overlap and Decreasing Fill)**
- **Nestedness Temperature (NTC)**

---

### Null Models

A key contribution of the project is the **systematic comparison of multiple baselines**:

- r00, r0, r1, r2
- c0, c1
- swap, curveball

👉 Each model preserves different structural properties (row sums, column sums, probabilities).

This allows a **robust and comparative evaluation** of nestedness.

---

### Simulation Framework

For each matrix:

- **1,000 simulations per null model**
- **8 baselines → 8,000 simulations per matrix**
- comparison of empirical vs simulated nestedness

👉 Enables statistical testing via **bootstrapped p-values**.

---

## 🏷 Keywords

Nestedness • Simulation • Network Analysis • Cultural Data • Statistics
