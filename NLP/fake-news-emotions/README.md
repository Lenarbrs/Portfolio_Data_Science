# The Emotional Loading of Fake News

> LLM-annotated anger, disgust and fear in 1,000 headlines: anger and disgust predict unreliable sources, fear does not.

| | |
|---|---|
| **Period** | 2025 |
| **Context** | Course project, Université PSL |
| **Team** | Bouzid Nélia, Rebours Léna |
| **Role** | Full project involvement: literature review, methodology, coding, data analysis, academic writing, and final presentation |
| **Stack** | Python, LLM annotation (Phi-4), logistic regression |

**Links:** [Code (full project repository)](https://github.com/Lenarbrs/Bouzid_Rebours_Exam_03)

> The code lives in a separate repository; this folder gives the overview.

## Research question

Do headlines from unreliable news sites express stronger negative emotions (**anger, disgust, fear**) than headlines from reliable sources?

## Data

Two datasets from fake news detection research: more than 20,000 articles, mostly 2016–2017, labelled truthful (Reuters) or unreliable (sites flagged by PolitiFact and Wikipedia). We sampled **1,000 headlines**: 500 truthful and 500 unreliable.

## Methods

- **LLM annotation:** Phi-4 scores each headline from 0 (not expressed) to 1 (very strong) for fear, anger and disgust, based on wording and framing, not factual content
- **Multiple logistic regression:** the three emotion scores predict whether a headline comes from a truthful or an unreliable source

## Key results

- **Anger** is significantly associated with unreliable headlines
- **Disgust** is also a significant predictor
- **Fear** does not significantly predict reliability

Not all negative emotions contribute equally to misinformation, which suggests emotional signals could help automated fake news detection.
