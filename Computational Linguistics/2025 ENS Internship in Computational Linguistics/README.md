# 🌐 Nestedness in Phonological Inventories

⚠️ **Note:** The full implementation of this project (data processing, simulations, and statistical analysis) lives in another GitHub repository.

🔗 **Code repository:**
[\[Link to the full project repository\]](https://github.com/alexeykosh/2025-nestedness-project)

This repository contains a short overview of the project.

---

## Research Question

Do phonological inventories across the world’s languages exhibit **nested structures**?

In other words:

👉 Do languages with rare phonemes also contain common phonemes, while smaller inventories only contain common ones?

---

## Project Idea

The concept of **nestedness**, originally from ecology, describes systems where:

- complex sets include both **common and rare elements**
- simpler sets contain only **common elements**

This project applies this concept to **phonology**, testing whether language sound systems follow similar structural patterns.

---

## 📊 Data

The analysis uses the **PHOIBLE database**:

- **3,020 phonological inventories**
- **2,186 languages**
- **3,183 phoneme types**

Languages are grouped into **70 language families** after filtering.

---

## ⚙️ Data Representation

For each language family:

- rows = languages
- columns = phonemes
- values = presence (1) / absence (0)

👉 This creates a **binary matrix equivalent to a bipartite graph**.

---

## 🤖 Modeling Approach

### Nestedness Metrics

Two complementary measures from ecology were used:

- **NODF (Nestedness based on Overlap and Decreasing Fill)**
- **Nestedness Temperature (NTC)**

👉 These quantify how much smaller inventories are subsets of larger ones

---

### Null Models (Simulation)

To test statistical significance, nestedness was compared to simulated random matrices:

- **r00 model**: random structure (no constraints)
- **c0 model**: preserves phoneme frequencies (more conservative)

👉 For each family:

- **10,000 simulations per model**
- **40,000 simulations total**

---

### Statistical Testing

- Nestedness scores compared to simulations using **Monte Carlo methods**
- p-values computed for each family
- significance threshold: **p < 0.005**

👉 Ensures robust identification of non-random structure

---

## Key Hypotheses

- Phonological inventories are **nested within language families**
- Nestedness persists even under conservative null models
- Nestedness may reflect:
  - cognitive constraints
  - cultural transmission
  - phonological structure

---

## 🏷 Keywords

Computational Linguistics • Phonology • Nestedness • Network Analysis • Simulation • Cross-Linguistic Data
