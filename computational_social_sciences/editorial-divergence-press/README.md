# Editorial Divergence and Tone in the French Press

> Topic modelling and CamemBERT sentiment on 5,821 French press articles: the further an article drifts from its category's usual topics, the more its tone changes, in different directions depending on the press type.

| | |
|---|---|
| **Period** | 2026 |
| **Context** | Computational Social Sciences course, Université PSL |
| **Status** | Completed (paper in French) |
| **Team** | Mélanie Barret, Nycia Pradel--Fernandes, Léna Rebours |
| **Role** | literature review, methodology, coding, data analysis, academic writing, and final presentation |
| **Stack** | Python, NLTK, LDA (topic modelling), CamemBERT, Jensen-Shannon distance, OLS, Spearman |

**Links:** [Paper (PDF, French)](report/paper_editorial_divergence_fr.pdf)

## Research question

Do articles that deviate from the typical editorial line of their media category also express a different emotional tone?

We define **editorial divergence**: how far an article's topic profile is from the average profile of its media category.

## Data

**5,821 French press articles** from **294 media sources**, 2010–2025, full text plus metadata, grouped into five categories: general, economic, specialized / professional, digital, magazines.

## Methods

1. **Preprocessing:** lowercasing, URL and non-alphabetic character removal, NLTK stopwords, removal of advertising tokens
2. **Representation:** bag-of-words with unigrams and bigrams, frequency filtering
3. **Topic modelling:** LDA
4. **Divergence:** Jensen-Shannon distance between each article's topic distribution and its category's mean distribution
5. **Tone:** CamemBERT positive/negative probabilities turned into a continuous valence score
6. **Statistics:** Spearman correlation and OLS, run separately per media category

## Key results

- **Specialized and economic press:** higher divergence goes with a **more negative** tone
- **Digital media:** higher divergence goes with a **more positive** tone
- **General press:** weak or slightly positive relationship
