# Such An Easy Task: Detecting Sarcasm in Text

> Three models compared on a unified sarcasm corpus: a simple Logistic Regression on global sentence embeddings beats a more elaborate pivot-based architecture (F1 0.60 vs 0.38).

| | |
|---|---|
| **Period** | 2026 |
| **Context** | Course project, Université PSL |
| **Status** | Completed (ACL style paper written) |
| **Team** | Éloïse Delerue, Lucile Lapray, Léna Rebours |
| **Role** | Literature review · Dataset collection & harmonization · Statistical testing pipeline · Manuscript writing & editing |
| **Stack** | Python, sentence embeddings, scikit-learn / MLP |

**Links:** [Code](https://github.com/Lenarbrs/2026_Sarcasm_Detection) · [Paper (PDF)](report/paper_sarcasm_detection.pdf)

> The code lives in a separate repository; this folder gives the overview and the paper.

## Research question

Sarcasm detection is hard because the literal and intended meanings diverge. Can explicitly modelling **local semantic shifts inside a sentence** help, compared with models using global sentence semantics?

## Data

A **unified corpus** built from three public sarcasm benchmarks:

- Sarcasm Corpus V2
- iSarcasmEval
- Conversational Sarcasm Corpus (CSC)

Binary classification, evaluated on a held-out test set.

## Models compared

1. **Logistic Regression** on sentence embeddings
2. **Multi-Layer Perceptron (MLP)** on global semantic features
3. **Pivot-based MLP**: a novel token-level pivot-splitting strategy designed to capture semantic shifts within sentences

## Key results

- **Logistic Regression: F1 ≈ 0.60**, the most balanced performance
- **Pivot-based MLP: F1 = 0.38**, with a severe collapse in recall
- Preserving **global** semantic information works better than isolating local contrasts, which strips away pragmatic cues needed to identify sarcasm
