# What Makes a Language Sound Attractive?

> A survey of French speakers testing whether perceived language attractiveness follows linguistic proximity and phonetic diversity.

| | |
|---|---|
| **Period** | 2024 |
| **Context** | Course project, Université PSL |
| **Stack** | Python (pandas, SciPy, seaborn), Jupyter |

**Links:** [Notebook](language_attractiveness.ipynb) · [Survey data](data/language_attractiveness_survey.csv)

## Research question

Which linguistic and phonetic features influence **French speakers' perceptions of language attractiveness**? Inspired by *"Do some languages sound more beautiful than others?"* (Anikin et al.).

## Hypotheses

- **P1, linguistic comfort zone:** languages from the speaker's own subfamily (Romance) are perceived as more attractive
- **P2, phonetic diversity:** languages with fewer vowels are perceived as less attractive

## Data

A **survey I designed**: attractiveness ratings of several languages by French speakers, combined with linguistic features of each language. The CSV is the raw (French-language, semicolon-separated) export of the survey.

## Methods

- **OLS regression** explaining attractiveness scores
- **t-tests**: Romance vs non-Romance languages (P1), different levels of vowel diversity (P2)
- Significance tests on regression coefficients

## Key results

- French speakers tend to prefer languages closer to their linguistic background
- Phonetic features such as vowel diversity influence perception
- Attractiveness judgments show systematic patterns, not purely subjective ones
