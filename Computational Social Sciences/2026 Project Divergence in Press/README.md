# 📰 Editorial Divergence and Tone in French Media

## Research Question

How do media outlets differ in the way they **cover topics and express tone**?

This project investigates whether articles that deviate from their **typical editorial line** also exhibit different **emotional tones**.

---

## 🧠 Project Idea

Media outlets do not only differ in _what_ they cover, but also in _how_ they frame topics.

This project introduces the concept of **editorial divergence**:

_How far is an article from the typical thematic profile of its media category?_

We then study whether this divergence is associated with changes in **sentiment (tone)**.

---

## 📊 Data

The dataset includes:

- **5,821 French press articles**
- **294 media sources**
- Time period: **2010–2025**
- Full article text + metadata (source, category, etc.)

Articles were grouped into editorial categories such as:

- general press
- economic press
- specialized/professional press
- digital media
- magazines

---

## ⚙️ NLP Pipeline

### Text Preprocessing

- lowercasing
- removal of URLs and non-alphabetic characters
- stopword filtering (NLTK)
- removal of advertising-related tokens

### Text Representation

- **Bag-of-Words (BoW)**
- inclusion of **unigrams and bigrams**
- frequency filtering to remove rare and overly common terms

---

## 🤖 Modeling Approach

### Topic Modeling — LDA

A **Latent Dirichlet Allocation (LDA)** model was used to extract latent topics from the corpus.

This allows us to capture the **thematic structure of the media corpus**.

---

### 📏 Editorial Divergence — Jensen-Shannon Distance

To quantify how atypical an article is:

- each article’s topic distribution is compared to the **average distribution of its category**
- divergence is measured using **Jensen-Shannon distance**

Higher divergence = article is further from its editorial “norm”

---

### 💬 Sentiment Analysis — CamemBERT

To estimate tone, we used a **CamemBERT-based model**:

- outputs probability of **positive vs negative sentiment**
- transformed into a continuous **valence score**:

---

### Statistical Modeling

To test the relationship between divergence and tone:

- **Spearman correlation** (non-parametric)
- **Linear regression (OLS)**

These analyses were performed **separately for each media category** to capture heterogeneous effects.

---

## Results

Key findings:

- In **specialized and economic press**, higher divergence is associated with **more negative tone**
- In **digital media**, divergence is associated with **more positive tone**
- In **general press**, the relationship is weak or slightly positive

---

## 🏷 Keywords

NLP • Topic Modeling • LDA • Sentiment Analysis • CamemBERT • Computational Social Science • Media Studies
