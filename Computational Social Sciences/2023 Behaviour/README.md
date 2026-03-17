# 🧠 Predicting Behavior from Individual Profiles

---

## Research Question

Can we predict an individual’s behavior, both **theoretical and real**, from their personal characteristics?

This project explores whether variables such as:

- gender
- economic status
- religious beliefs
- familiarity with philosophy

can explain how people respond to **moral dilemmas and real-life situations**.

---

## Project Idea

The project is inspired by **philosophical thought experiments** (Thomson, Nozick).

It investigates:

👉 whether theoretical moral reasoning reflects real-world behavior
👉 whether individual profiles can predict both types of responses

---

## 📊 Data

The dataset comes from a questionnaire I created with:

- **114 respondents**
- demographic variables (gender, religion, economic status, age, etc.)
- answers to:
  - **theoretical dilemmas** (e.g. violinist, experience machine)
  - **real-life questions** (e.g. abortion opinion, reaction to lying)

---

## ⚙️ Data Analysis Pipeline

- data cleaning and variable selection
- exploratory analysis (distributions, visualizations)
- statistical modeling
- hypothesis testing

---

## 🤖 Modeling Approach

### Multivariate Logistic Regression

To predict responses to both **theoretical and real behaviors**, multiple logistic regression models were used.

General form:

$$
Y_i \sim \beta_0 + \beta_1 Gender + \beta_2 Religion + \beta_3 Economic + \beta_4 Philosophy + \beta_5 Age
$$

Models estimated:

- prediction of **theoretical behavior** (violinist, experience machine)
- prediction of **real behavior** (abortion, reaction to lying)

---

### 📊 Statistical Testing

To test whether theoretical behavior reflects real behavior:

- **Chi-square (χ²) tests** were performed between:
  - thought experiment responses
  - real-life answers

---

## 📊 Key Results

- Some variables (notably **gender and economic status**) significantly predict responses in certain theoretical scenarios
- Most profile variables **do not consistently predict behavior**
- No significant relationship between:
  - theoretical responses
  - real-life behavior

---

## 🏷 Keywords

Logistic Regression • Causal Inference • DAG • Behavioral Data • Philosophy • Statistical Testing • Social Science
