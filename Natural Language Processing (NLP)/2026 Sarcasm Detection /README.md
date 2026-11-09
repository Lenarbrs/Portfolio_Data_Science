# Such An Easy Task: Detecting Sarcasm in Text

This project explores sarcasm detection in English text using Natural Language Processing (NLP) and machine learning techniques.

3 approaches are compared:
- **Logistic Regression** using sentence embeddings.
- **Multi-Layer Perceptron (MLP)** using global semantic features.
- **Pivot-Based MLP**, designed to capture semantic shifts within sentences.

The models are trained and evaluated on a unified dataset combining three public sarcasm corpora:
- Sarcasm Corpus V2
- iSarcasmEval
- Conversational Sarcasm Corpus (CSC)

The experiment shows that Logistic Regression achieves the best overall performance, with an F1-score of approximately **0.60**. The results suggest that preserving global semantic information is more effective than focusing only on local semantic contrasts.

## Code

The complete source code and implementation are available in a separate repository:

[2026_Sarcasm_Detection – GitHub](https://github.com/Lenarbrs/2026_Sarcasm_Detection)