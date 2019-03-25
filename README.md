[![Build Status](https://travis-ci.com/ruohoruotsi/iranlowo.svg?token=DjfQAQyyoxFCdeCmWju3&branch=master)](https://travis-ci.com/ruohoruotsi/iranlowo)

# Ìrànlọ́wọ́
Ìrànlọ́wọ́ is a set of utilities to analyze &amp; process Yorùbá text for NLP tasks. The initial focus is on help for diacritic restoration or machine translation.

## Features

### ADR tools
* Find all variants of all word-type in a given corpus
* Compute a score of diacritic ambiguity in a given corpus
* Canonicalize a corpus (from MS Word or elsewhere as NFC)
* Convert corpora easily between NFC and NFD
* Strip all diacritics from word-types
* Partially strip diacritics from word-types
* Split long sentences on certain characters like `;`,`:`, etc

### Ready to use webpage scrapers
* Bíbélì Mímọ́
* Yoruba Bible - Bible Society of Nigeria
* Yorùbá Blog
* BBC Yorùbá

### Corpus analysis tools
* Dataset scoring (proximity to correctly diacritized text, lm perplexity, KL divergence)
* dataset character distribution
* dataset ambuiguity statistics &rarr; Lexdif, etc
