# Nestedness in Phonological Inventories

> Do the sound systems of the world's languages follow a nested structure, where rare phonemes only appear in languages that also have the common ones?

| | |
|---|---|
| **Period** | January – July 2025 |
| **Context** | Research internship (UROP), ENS-PSL, Institut Jean Nicod |
| **Status** | First-authored paper in preparation; analysis pre-registered on OSF (7 April 2025) |
| **Supervision** | Alexey Koshevoy, Olivier Morin |
| **Role** | Conceptualization, methodology, software, formal analysis, first draft |
| **Stack** | Python, NODF and nestedness temperature, null-model simulations |

**Links:** [Code (full project repository)](https://github.com/alexeykosh/2025-nestedness-project) · [Pre-registration (PDF)](report/preregistration_phonological_nestedness.pdf)

> The code lives in another repository; this folder gives the overview and the pre-registration.

## Research question

Do phonological inventories exhibit **nested structures**? Do languages with rare phonemes also contain the common ones, while small inventories contain only common phonemes?

*Nestedness* comes from ecology: an island's species are usually a subset of the mainland's, mostly common ones. We test whether language sound systems follow the same pattern.

## Data

[PHOIBLE](https://phoible.org/) database: **3,020 phonological inventories**, **2,186 languages**, **3,183 phoneme types**, grouped into **70 language families** after filtering.

For each family, a binary matrix (rows = languages, columns = phonemes, 1 = present), equivalent to a bipartite graph.

## Methods

- **Metrics:** NODF (Nestedness based on Overlap and Decreasing Fill) and nestedness temperature
- **Null models:** `r00` (unconstrained random) and `c0` (preserves phoneme frequencies, more conservative), with **10,000 simulations per model and family**
- **Inference:** Monte Carlo p-values per family, significance threshold p < 0.005

## Hypotheses

- Inventories are nested within language families
- Nestedness persists under the conservative null model
- Possible explanations: cognitive constraints, cultural transmission, phonological structure (markedness, dispersion)

## Key results

Results are in the paper in preparation. 
