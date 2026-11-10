# Predicting Next Year's Best-Rated Board Games

> Bayesian regression on BoardGameGeek data to find which characteristics (complexity, mechanics, domains, year) drive player ratings.

| | |
|---|---|
| **Period** | 2026 |
| **Context** | Course project, Université PSL |
| **Status** | Completed |
| **Team** | Lucile Lapray, Léna Rebours |
| **Role** | End-to-end project contribution: literature review, research design, data collection and preprocessing, coding, statistical analysis, paper writing, and final presentation |
| **Stack** | Python, PyMC, ArviZ, pandas, NumPy, scikit-learn, Matplotlib |

**Links:** [Code](https://github.com/Lenarbrs/2026_Board_Game_Prediction)

> The code lives in a separate repository; this folder gives the overview.

## Research question

Which characteristics are associated with highly rated board games, and can we predict the features of next year's best-rated games?

## Data

Board Games dataset from Kaggle (BoardGameGeek): more than **20,000 games** with ratings, complexity, mechanics, domains and publication year.

## Methods

- Data preprocessing and feature engineering
- Bayesian regression with PyMC
- MCMC sampling with NUTS
- Posterior analysis and convergence diagnostics

## Key results

- **Complexity is a strong predictor of player ratings:** A one-standard-deviation increase in game complexity is associated with a +0.363-point increase in expected ratings (94% HDI excludes zero).

- **Customizable Games lead among game domains:** They show the strongest positive baseline effect (+0.420 points), followed by Party Games (+0.267).

- **Some mechanics are particularly appreciated:** Card Drafting (+0.182), Dice Rolling (+0.148), and Variable Player Powers (+0.136) have credible positive associations with ratings.

- **Player preferences evolve over time:** Customizable Games show the strongest upward trend (+0.042 rating points per year), followed by Card Drafting (+0.008) and Dice Rolling (+0.007).

- **Some categories face significant penalties:** Roll / Spin and Move (-0.307), Children's Games (-0.280), and Abstract Games (-0.156) have the strongest negative baseline effects.

- **Complexity remains valuable but is no longer gaining momentum:** Its positive baseline effect is significant, while its annual trend is not.

All effects are assessed using 94% Highest Density Intervals (HDIs). The results identify associations rather than causal effects.
