# 🎬 CinéLingua — Cultural Recommendation System for Language Learning

⚠️ **Note:** The full implementation of this project (code, data pipeline, and web app) lives in another GitHub repository.

🔗 **Code repository:**
[\[Link to the full project repository\]](https://github.com/Lenarbrs/CineLingua)

[\[Link to the website I created\]](https://rebours-lena-website.onrender.com)

---

## 🍿 Overview

**CinéLingua** is a movie recommendation system designed for language learners.

It helps users discover films that match both their **cinematic tastes** and their **language-learning goals**, making immersion enjoyable and engaging.

👉 Grab some popcorn and your favorite pillow:
**400,000 movies across 52 languages are available to explore.**

---

## 📊 Data (Large-Scale Pipeline)

The project is built on **large-scale movie data**:

- 🎥 **1,000,000+ movies initially collected via the TMDB API**
- 🧹 cleaned and filtered to **~400,000 high-quality films**
- 🌍 covering **52 languages**
- rich metadata:
  - genres
  - overviews
  - release dates
  - ratings
  - original language

The dataset was carefully processed to ensure:

- reliable language information (critical for learning use case)
- removal of noisy or low-quality entries
- consistency across multilingual data

👉 This results in a **robust and scalable recommendation base**.

---

## 🧠 Project Idea

Most recommendation systems reinforce existing habits.

CinéLingua instead aims to:

👉 recommend content in a **target language**
👉 maintain **user taste consistency**
👉 promote **cultural discovery and immersion**

---

## 🤖 Modeling Approach

### 🎯 Content-Based Recommendation

- similarity between movies based on:
  - genres
  - themes
  - textual descriptions

- filtering by **target language**

👉 Generates recommendations aligned with both **taste and learning goals**.

---

### 🔍 Feature Engineering

Key features include:

- genre similarity
- language filtering
- movie metadata
- user-defined preferences

---

## ⚙️ Tech Stack

### 🐍 Data & Backend

- **Python** (pandas, numpy, scikit-learn)
- API integration (**TMDB API**)
- large-scale data cleaning and processing

### 🗄️ Database

- **SQL** for structured storage and querying

### 🌐 Web Application

- **HTML / CSS** for interface
- **JavaScript** for interactivity
- dynamic recommendation display

---

## 🧪 Features

- selection of a **target language**
- personalized recommendations
- interactive interface
- large multilingual catalog

---

## 🔍 Why This Project?

This project demonstrates:

- handling of **large-scale datasets (1M+ → 400k cleaned)**
- **API-based data engineering (TMDB)**
- **recommendation systems**
- **full-stack development (Python + SQL + Web)**

---

## 🧩 Key Insight

👉 Language learning tools become significantly more effective when they combine **personalization, scale, and cultural immersion**.

---

## 🏷 Keywords

Recommendation System • Machine Learning • Large-Scale Data • TMDB API • Python • SQL • Web Development • Language Learning
