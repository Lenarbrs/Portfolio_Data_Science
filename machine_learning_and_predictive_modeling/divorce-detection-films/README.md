# Predicting Divorce Storylines in Film Overviews

> Text classification of film synopses with classic vectorization and BERT embeddings, to detect divorce-related storylines.

| | |
|---|---|
| **Period** | 2024 |
| **Context** | Course project, Université PSL |
| **Stack** | Python, scikit-learn (Logistic Regression, MLP, Ridge, Lasso), HuggingFace Transformers, PyTorch, spaCy, NLTK |

**Links:** [Notebook](divorce_detection.ipynb) · [Annotated data](data/letterboxd_annotations.csv)

## Research question

Can we predict from its **text overview alone** whether a film has a divorce-related storyline?

## Data

About 2,300 film overviews from Letterboxd, manually annotated for divorce-related content.

## Methods

- **Text representation:** cleaning, tokenization, stopword removal, vectorization, plus **BERT embeddings** (HuggingFace Transformers) for richer semantics
- **Models compared:**
  - Logistic Regression (baseline)
  - Neural networks (`MLPClassifier`, architectures `(100, 50)` and smaller `(50, 25)` to reduce variance)
  - Ridge / Lasso regression to study regularization
- **Evaluation:** train / test split; accuracy, recall, MSE and MAE

