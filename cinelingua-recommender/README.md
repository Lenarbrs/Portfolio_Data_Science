# CinéLingua: Film Recommendations for Language Learners

> A web platform that recommends films matching both your taste and the language you want to learn, built on a catalog of about 400,000 films in 52 languages.

| | |
|---|---|
| **Period** | 2025 |
| **Context** | Personal project, Université PSL |
| **Status** | Live |
| **Stack** | Python (pandas, NumPy, scikit-learn), TMDB API, SQL, HTML / CSS / JavaScript |

**Links:** [Live demo](https://rebours-lena-website.onrender.com) · [Code](https://github.com/Lenarbrs/CineLingua)

> The code lives in a separate repository; this folder gives the overview. The demo is hosted on a free tier and may take a moment to wake up.

## Idea

Unlike traditional recommendation systems that reinforce existing habits, **CinéLingua** introduces users to new films in their **target language** while preserving their **personal taste**, making language immersion both enjoyable and engaging.

## Data

- More than **1,000,000 films** collected through the TMDB API
- Cleaned and filtered to about **400,000 films** covering **52 languages**
- Metadata: genres, overviews, release dates, ratings, original language
- Cleaning focused on reliable language information, removal of noisy or low-quality entries, and consistency across multilingual data

## Approach

- **Content-based recommendation:** similarity between films from genres, themes and textual descriptions, filtered by target language
- **Features:** genre similarity, language filtering, film metadata, user preferences
- **Web app:** target language selection, personalized recommendations, interactive interface

## What it demonstrates

Large-scale data cleaning, API-based data engineering, recommender systems and end-to-end development (Python, SQL, web front end, deployment).
