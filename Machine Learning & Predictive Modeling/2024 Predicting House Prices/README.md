# 🏠 Predicting Housing Prices with Machine Learning

---

## Project Goal

The goal of this project is to **predict housing prices based on property characteristics** using machine learning models.

By analyzing structural and environmental features of houses, I aim to estimate their **market value** and evaluate which modeling approaches provide the most accurate predictions.

---

## 📊 Data

The dataset contains information about residential properties and their sale prices.

Typical variables include:

- house size
- number of rooms
- location-related features
- construction characteristics

The target variable is the **sale price of the property**.

---

## ⚙️ Data Preparation

Before training predictive models, the data was prepared using standard preprocessing steps:

- handling missing values
- feature selection
- normalization or scaling of numerical variables
- train–test split for model evaluation

These steps ensure that the models learn meaningful patterns from the data.

---

## 🤖 Predictive Modeling

Several machine learning models were implemented and compared to predict housing prices.

### Linear Regression

Linear regression was used as a **baseline model** to estimate housing prices from the available features.

It assumes a linear relationship between the predictors and the target variable and provides a simple and interpretable benchmark.

---

### Ridge Regression

Ridge regression introduces **L2 regularization**, which penalizes large coefficients and helps prevent overfitting.

This model is particularly useful when:

- many features are correlated
- the model risks becoming too complex

---

### Lasso Regression

Lasso regression applies **L1 regularization**, which can shrink some coefficients to zero.

This allows the model to perform **automatic feature selection**, helping identify which variables are most relevant for predicting housing prices.

---

### Tree-based Models

Tree-based models were also explored to capture **non-linear relationships** between housing features and price.

Decision trees allow the model to split the data into regions based on feature thresholds, enabling more flexible predictions than purely linear models.

---

## 📉 Model Evaluation

The performance of the models was evaluated using regression metrics such as:

- **Mean Squared Error (MSE)**
- **Mean Absolute Error (MAE)**

These metrics measure how close the predicted prices are to the actual housing prices.

Comparing multiple models helps determine which approach best captures the underlying structure of the housing market data.

---

## 🏷 Keywords

Machine Learning • Regression • Housing Prices • Predictive Modeling • Data Analysis
