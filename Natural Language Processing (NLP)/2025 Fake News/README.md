# The Emotional Loading of Fake News

⚠️ **Note:** This project (scripts, notebooks, and data processing pipeline) lives in another GitHub repository.

🔗 **Code repository:**
[\[Link to the full project repository\]](https://github.com/Lenarbrs/Bouzid_Rebours_Exam_03)

This repository contains a short overview of the project.

---

## 🧪 Research Question

Fake news often spreads faster than real news, partly because it relies on **emotionally charged language**.

This project investigates whether **unreliable news headlines express stronger negative emotions than truthful news headlines**, focusing on three emotions frequently associated with misinformation:

- **Anger**
- **Disgust**
- **Fear**

More specifically, the project asks:

**Do headlines from unreliable news sites convey stronger negative emotions than those from reliable news sources?**

---

## 🧠 Project Idea

Many fake news headlines are designed to **trigger emotional reactions** and increase engagement on social media platforms.

By measuring the **emotional intensity** expressed in headlines, we aim to test whether certain emotions are **systematically associated with unreliable news sources**.

Understanding these patterns could help improve **automatic fake news detection systems**.

---

## 📊 Data

The analysis is based on two datasets previously used in fake news detection research.

Key characteristics of the data:

- Over **20,000 news articles**
- Published mainly between **2016 and 2017**
- Articles labeled as **truthful** or **unreliable**
- Sources include **Reuters** (truthful news) and websites flagged by **PolitiFact and Wikipedia**

For this project:

- **1,000 headlines were sampled**
- **500 truthful headlines**
- **500 unreliable headlines**

These headlines were then annotated for emotional intensity.

---

## 🤖 LLM-based Emotion Annotation

To evaluate the emotional tone of each headline, we used a **Large Language Model (Phi-4)**.

For every headline, the model estimated the intensity of three emotions:

- Fear
- Anger
- Disgust

Each emotion received a score between **0 and 1**, where:

- **0** = emotion not expressed
- **1** = very strong emotional expression

The annotation process relied on prompts asking the model to analyze the **wording and framing of headlines**, rather than their factual content.

---

## ⚙️ Method

To test the hypothesis, we performed a **multiple logistic regression analysis**.

The model estimates whether the intensity of each emotion predicts the **reliability of the news source**.

The regression model uses:

- **Anger score**
- **Disgust score**
- **Fear score**

to predict whether a headline comes from a **truthful or unreliable news source**.

---

## 📈 Results

The results show that:

- **Anger** is significantly associated with unreliable news headlines
- **Disgust** is also a significant predictor of unreliable news
- **Fear** does not significantly predict news reliability

These findings suggest that **not all negative emotions contribute equally to the spread of misinformation**.

---

## 🔍 Why This Project?

This project explores how **emotional language shapes misinformation**.

It contributes to research at the intersection of:

- **Natural Language Processing**
- **Computational Social Science**
- **Misinformation detection**

The findings also suggest potential applications for **automated fake news detection tools that incorporate emotional signals**.

---

## 🏷 Keywords

Fake News Detection • NLP • Emotional Analysis • LLM Annotation • Logistic Regression • Computational Social Science
