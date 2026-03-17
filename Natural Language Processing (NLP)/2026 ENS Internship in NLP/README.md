# Recovering Text from Jabberwocky Distortions

---

## 🧪 Ongoing Research Project

This project is **currently in progress** as part of a research internship at **ENS Ulm (Paris)**, which began in **January 2026**.
The work is conducted in collaboration with **two researchers** and investigates the limits of large language models in reconstructing heavily distorted text.

---

## 🧠 Reconstructing Meaning from Distorted Text

Large Language Models are often very good at reconstructing missing information in text.
But **how far does this ability go?**

In this project, we investigate how well LLMs can reconstruct an original text when it has been heavily distorted using a **Jabberwocky-style masking method**, where many letters are replaced with the character **"x"**.

The challenge for the model is to **recover the most likely original text** while respecting strict structural constraints.

This setup allows us to test how far **contextual linguistic inference** can go when most of the surface form of a sentence has been removed.

---

## 🎯 Research Goal

The project explores:

- the **limits of contextual inference** in large language models
- how distortion affects **semantic reconstruction**
- whether models can recover meaning while respecting **strict structural constraints**

---

## 🧩 Jabberwocky Distortion

The distortion process replaces letters with the character **"x"**, while preserving the overall structure of the text.

Constraints include:

- each **"x" represents exactly one missing letter**
- word lengths remain unchanged
- punctuation and spacing remain identical
- capitalization remains identical

Example:

Original text:

```text
Before the emergence of transformer-based models in 2017...
```

Distorted text:

```text
Before the xxxxxxxxx of xxxxxxxxxxx-xxxxed xxxxxs in 2017...
```

The model must reconstruct the most plausible original text while respecting these structural constraints.

---

## ⚙️ Method

The experimental pipeline includes:

1. **Text collection and preprocessing**
   Wikipedia paragraphs are cleaned and prepared as source texts.

2. **Text distortion**
   The original text is transformed using a Jabberwocky-style masking algorithm.

3. **LLM reconstruction**
   Large Language Models attempt to reconstruct the original text under strict constraints.

4. **Evaluation**
   The reconstructed text is compared to the original to evaluate reconstruction quality.

---

## 🔍 Why This Project?

By pushing language models into extreme reconstruction tasks, this project helps explore:

- their **contextual reasoning abilities**
- their **limits in linguistic inference**
- their potential applications in **text restoration and error correction**

---

## 🏷 Keywords

Large Language Models • NLP • Computational Linguistics • Text Reconstruction • Language Modeling • LLM Evaluation
