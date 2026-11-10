# Predicting Housing Prices

> Linear, regularized and tree-based regression models compared on residential sale prices.

| | |
|---|---|
| **Period** | 2024 |
| **Context** | Course exam, Université PSL |
| **Stack** | Python, scikit-learn (OLS, Ridge, Lasso, decision trees), pandas |

**Links:** [Notebook](house_price_prediction.ipynb) · [Data](data/housing_prices.csv)

## Goal

Predict the **sale price** of a house from its characteristics, and find which modelling approach is the most accurate.

## Data

[`housing_prices.csv`](data/housing_prices.csv): 545 properties, 12 features (area, bedrooms, bathrooms, stories, main road, guest room, basement, hot water heating, air conditioning, parking, preferred area, furnishing status) and the target `price`.

## Methods

- **Preparation:** missing values, feature selection, scaling of numerical variables, train / test split
- **Models:** Linear regression (baseline), **Ridge** (L2), **Lasso** (L1, automatic feature selection), **tree-based models** for non-linear relationships
- **Evaluation:** MSE and MAE


