# Culture, Environment and Fear of Failure

> Multiple regression on 220 countries linking economic, health and disease conditions to a cultural attitude, fear of failure.

| | |
|---|---|
| **Period** | 2025 |
| **Context** | Course project, Université PSL |
| **Stack** | Python (pandas, statsmodels, SciPy, seaborn), Jupyter |

**Links:** [Notebook](fear_of_failure.ipynb)

## Research question

To what extent is human culture shaped by social and environmental conditions? I test whether economic development, health and environmental risk influence **fear of failure**.

## Data

Ecology-Culture Dataset (ECD): **220 countries**, 1950–2020, with ecological variables (GDP, disease, etc.) and cultural indicators (fear of failure, values, well-being).

> The ECD file is not included in this repository. The notebook expects `ECD Data v3.csv`.

## Methods

Data cleaning, exploratory analysis, then a multiple linear regression (OLS):

`Fear of failure ~ GDP + Life expectancy + Disease + Unemployment`

Hypotheses: higher GDP and life expectancy lower fear of failure; higher disease threat and unemployment raise it.

## Key results

- Economic and health factors are strong predictors of cultural attitudes
- Environmental constraints such as disease play a significant role
- Cultural traits appear systematically linked to structural conditions
