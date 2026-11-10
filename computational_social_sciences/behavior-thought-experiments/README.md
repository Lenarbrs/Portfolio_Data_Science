# Predicting Behavior from Individual Profiles

> Do personal characteristics predict how people answer moral dilemmas, and does thought-experiment behavior reflect real-life behavior?

| | |
|---|---|
| **Period** | 2024 |
| **Context** | Individual project, Université PSL |
| **Status** | Completed |
| **Stack** | Multivariate logistic regression, χ² tests, survey design |

**Links:** [Report (PDF)](report/report.pdf) · [Slides (PDF)](report/slides.pdf)

## Research question

Can we predict an individual's **theoretical** and **real** behavior from gender, economic status, religious beliefs, familiarity with philosophy and age? Inspired by philosophical thought experiments (Thomson, Nozick) and the work of Ruwen Ogien.

## Data

A **questionnaire I designed**: **114 respondents**, with demographic variables and answers to theoretical dilemmas (the violinist, the experience machine) and real-life questions (opinion on abortion, reaction to lying).

## Methods

- Data cleaning and variable selection, exploratory analysis
- **Multivariate logistic regression**, one model per behavior:
  `Y ~ Gender + Religion + Economic status + Philosophy + Age`
- **χ² tests** between thought-experiment answers and real-life answers

## Key results

- **Gender** and **economic status** significantly predict answers in some theoretical scenarios
- Most profile variables **do not predict behavior consistently**
- **No significant relationship** between theoretical and real-life behavior
