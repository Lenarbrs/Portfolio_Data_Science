## 💔 Predicting Divorce Themes in Film Overviews

The goal of the project is to predict whether a film contains a **divorce-related storyline** based solely on its textual overview.

### Text Representation

Film overviews were first converted into numerical representations suitable for machine learning models.
This included standard preprocessing steps such as:

- text cleaning and tokenization
- removal of stopwords
- vectorization of the text

In addition, **BERT-based representations** were explored using the HuggingFace Transformers library to capture richer semantic information from the summaries.

### Models

Several predictive models were implemented and compared:

- **Logistic Regression**
  Used as a baseline classification model for predicting the presence of divorce themes.

- **Neural Networks (MLPClassifier)**
  Multi-layer perceptron models with different architectures were tested, including networks with hidden layers such as `(100, 50)` neurons and smaller architectures `(50, 25)` to reduce variance.

- **Linear Models (Ridge / Lasso Regression)**
  These models were explored to analyze relationships between textual features and the target variable and to test regularization effects.

### Training and Evaluation

The dataset was split into **training and test sets** in order to evaluate model performance.

Models were trained to estimate the probability that a given film overview corresponds to a movie involving a **divorce narrative**.

Performance was evaluated using standard metrics such as:

- Accuracy
- Mean Squared Error (for regression-based experiments)
- Mean Absolute Error

The comparison of different models helps identify which approaches best capture **linguistic signals indicating divorce-related narratives** in film summaries.
