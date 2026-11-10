# Recovering Semantics from Syntactic Scaffolding

> Can large language models recover semantic information from heavily redacted text using syntactic cues alone? Which linguistic features contribute most to successful reconstruction?

| **Period** | January 2026 – present |
| **Context** | Research internship at ENS-PSL (Paris), in collaboration with researchers from ENS and the University of Cambridge |
| **Status** | First-authored paper submitted to ACL |
| **Stack** | Python, pandas, Gemini 3.1 Pro, spaCy, LemmInflect, text-embedding-3-large, mixed-effects models |

**Links:** Code (private repository) · [OSF pre-registration](https://osf.io/dxq63/overview) · Manuscript not publicly available

## Research question

Large language models (LLMs) can reconstruct parts of heavily redacted text, even when most content words are replaced with `BLANK` tokens. But how much semantic information can they actually recover from the remaining linguistic structure?

We investigate the contribution of five linguistic cues:
- **Closed-class words** (function words such as articles, pronouns and prepositions)
- **Inflectional morphology** (grammatical suffixes such as `-ed` and `-ing`)
- **Punctuation**
- **Numbers**
- **Proper nouns**

Using a Jabberwocky-style redaction approach, we systematically manipulate which cues remain visible while asking an LLM to reconstruct the original passages.

## Method

1. **Corpus preparation:** We collect 150 English-language news passages from *The Guardian*, published between February 2025 and January 2026. Each passage contains at least one proper noun and one numerical expression and exceeds 200 tokens.

2. **Text redaction:** We replace content words with `BLANK` tokens while selectively preserving five linguistic features: closed-class words, inflectional morphology, punctuation, numbers and proper nouns. This produces 31 experimental conditions per passage.

3. **LLM reconstruction:** We submit each redacted passage individually to Gemini 3.1 Pro, using a consistent reconstruction prompt and positional markup tags to align predicted words with their original counterparts.

4. **Baseline construction:** We generate grammatically well-formed but semantically nonsensical passages by replacing masked words with randomly sampled words matching their fine-grained part-of-speech categories. This allows us to measure semantic recovery beyond what grammatical information alone would predict.

5. **Evaluation:** We compare reconstructions against the original passages using three metrics:
   - Paragraph embedding cosine similarity (`text-embedding-3-large`)
   - Mean word embedding cosine similarity on fully redacted positions
   - METEOR

6. **Statistical analysis:** We calculate normalized gain over the baseline, fit linear mixed-effects regression models, compute Shapley values to estimate the contribution of each linguistic feature, and perform paired Monte Carlo permutation tests (10,000 iterations), with Benjamini–Hochberg correction for multiple comparisons.

## Key results

- **Syntactic cues alone enable significant semantic recovery:** Combining closed-class words, morphology and punctuation yields a 19.4% normalized gain in mean word embedding similarity over the baseline.

- **Semantic cues alone are insufficient for word-level recovery:** Numbers and proper nouns together produce almost no improvement in word similarity (-0.4%) or METEOR (2.6%).

- **Combining syntactic and semantic cues substantially improves reconstruction:** Adding proper nouns to syntactic cues increases normalized gain to 40.7% in mean word embedding similarity. Adding numbers instead yields a 24.6% gain.

- **Closed-class words are the strongest syntactic cue:** They make the largest contribution to word-level similarity and METEOR, according to both regression coefficients and Shapley values.

- **Proper nouns are particularly informative:** They contribute most to paragraph-level similarity, although this metric is sensitive to exact matches of rare terms.

- **Less than one-third of the original text is needed:** Even when all five features are preserved, only 30.90% of the original non-whitespace characters remain visible to the model.