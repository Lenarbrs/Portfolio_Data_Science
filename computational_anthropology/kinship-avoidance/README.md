
# Kinship Avoidance and Social Structure Across Societies

> Cross-cultural statistical analysis of kinship avoidance practices across societies: investigating how family size and marital residence patterns interact, while accounting for linguistic, geographical and phylogenetic relationships.

| | |
|---|---|
| **Period** | 2026 |
| **Context** | Cultural Evolution and Kinship project, Université PSL |
| **Status** | Completed (data processing, statistical and phylogenetic analysis) |
| **Team** | Bernard Titien, Levi Mazloum Sacha, Rebours Léna |
| **Role** | Data integration, variable construction, data cleaning, geospatial analysis, statistical modelling and phylogenetic analysis |
| **Stack** | Python, pandas, NumPy, matplotlib, seaborn, GeoPandas, scikit-learn (K-Means), statsmodels, Biopython |


**Links:** [Code (full project repository)](https://github.com/Lenarbrs/2026_Avoidance_Project) · [Analysis plan (PDF)](Analysis_Plan.pdf)

> The code and Jupyter notebooks are hosted in a separate repository; this folder provides an overview of the project and its research methodology.

## Research question

Why do some societies develop avoidance customs between specific in-laws (e.g. mother-in-law and son-in-law, father-in-law and daughter-in-law)?

We investigate whether avoidance practices are associated with the interaction between **small family sizes** and **strong lineal affiliation structures**, approximated through patterns of marital residence.

Building on anthropological research, we examine whether avoidance customs can serve to reinforce narrow community and kinship ties when these relationships are threatened by marriage.

## Data

We combine several cross-cultural anthropological datasets:

- **Standard Cross-Cultural Sample (SCCS):** family size, community size and kinship-related variables.
- **Ethnographic Atlas (EA):** prevailing patterns of marital residence and community marriage organization.
- **Glottolog:** linguistic classification and language family identifiers.
- **Geographical data:** latitude and longitude of societies.
- **Phylogenetic supertree:** evolutionary relationships between societies, based on shared ancestry.

We enrich the original avoidance dataset by integrating these sources, harmonizing society identifiers and constructing additional variables for statistical analysis.

## Methods

1. **Data integration and feature engineering:** Merge SCCS and Ethnographic Atlas variables with linguistic and geographical information. Construct an ordinal family-size variable and categorical marital residence groups.

2. **Exploratory data analysis:** Examine the distribution of avoidance practices, family structures and marital residence patterns through descriptive statistics and visualizations.

3. **Geospatial analysis:** Standardize latitude and longitude coordinates and apply K-Means clustering (6 clusters) to account for geographical proximity between societies.

4. **OLS regression models:** Estimate the relationship between family size, marital residence and their interaction for four in-law avoidance relationships:
   - Mother-in-law / Son-in-law (MiL/SiL)
   - Mother-in-law / Daughter-in-law (MiL/DiL)
   - Father-in-law / Son-in-law (FiL/SiL)
   - Father-in-law / Daughter-in-law (FiL/DiL)

   Include linguistic family and geographical cluster controls.

5. **Phylogenetic analysis:** Construct a covariance matrix from shared evolutionary branch lengths and fit Generalized Least Squares (GLS) models to account for phylogenetic dependence between societies.

## Key results

- **Three out of four phylogenetic GLS models are statistically significant overall:** MiL/SiL (p = 0.0008), MiL/DiL (p = 0.0016) and FiL/SiL (p = 0.0293). The FiL/DiL model is not significant at the 5% level (p = 0.091).

- **Marital residence patterns matter:** Some residence categories show significant associations with avoidance outcomes, particularly matrilocal/uxorilocal residence in the FiL/SiL model.

- **Family size and marital residence interact:** Significant interaction terms appear in selected models, suggesting that the association between family size and avoidance may vary across residence patterns.

- **Phylogenetic relationships are explicitly accounted for:** The GLS approach incorporates shared evolutionary history rather than treating all societies as fully independent observations.

*Note: These findings are exploratory associations, not evidence of causality. The models use relatively small samples (26–44 societies per relationship), so results should be interpreted cautiously.*
