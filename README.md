# Ìrànlọ́wọ́
[![Build Status](https://travis-ci.com/ruohoruotsi/iranlowo.svg?token=DjfQAQyyoxFCdeCmWju3&branch=master)](https://travis-ci.com/ruohoruotsi/iranlowo)
[![PyPI](https://img.shields.io/pypi/v/iranlowo.svg)](https://pypi.org/project/iranlowo)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/iranlowo.svg)
[![License](https://black.readthedocs.io/en/stable/_static/license.svg)](https://github.com/ruohoruotsi/iranlowo/blob/master/LICENSE)
[![Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Ìrànlọ́wọ́ is a set of utilities to analyze &amp; process Yorùbá text for NLP tasks. The focus is on *helping software developers* build large, clean text datasets for (further) diacritic restoration and machine translation tasks.

## Features

### ADR tools
* [X] Strip all diacritics from word-types
* [X] Verify that text is NFC or NFD
* [X] Canonicalize a corpus (from MS Word or elsewhere) &rarr; NFC
* [X] Split long sentences on certain characters like `;`,`:`, etc
* [X] Automatically restore correct diacritics using a pre-trained model
* [X] Find all variants of all word-type in a given corpus
* [ ] Partially strip diacritics from word-types

### Ready to use webpage scrapers
* [X] Bíbélì Mímọ́
* [X] Yoruba Bible - Bible Society of Nigeria
* [ ] Yorùbá Blog
* [ ] BBC Yorùbá

### Corpus analysis tools
* [X] Dataset character distribution
* [X] Dataset ambuiguity statistics &rarr; Lexdif, etc for a given corpus
* [ ] Dataset scoring (proximity to correctly diacritized text, LM perplexity, KL divergence)

## Installation
Obtainable from the [Python Package Index (PyPI)](https://pypi.org/project/iranlowo/) &rarr;  `pip install iranlowo`

## Example

* Show computing environment and installation process

<img src="https://raw.githubusercontent.com/ruohoruotsi/iranlowo/master/docs/install.gif" width="700">

* Diacritize a phrase
```
$ python
Python 3.7.3 (default, Mar 27 2019, 16:54:48)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import iranlowo.adr as ránlọ
>>> ránlọ.diacritize_text("lootoo ni pe ojo gbogbo ni ti ole")
PRED AVG SCORE: -0.0037, PRED PPL: 1.0037
'lóòtóọ́ ni pé ọjọ́ gbogbo ni ti olè' 
```

* Diacritize phrases, note we use `ipython` only because it renders nicer, easy-to-read text-colours in the terminal!

<img src="https://raw.githubusercontent.com/ruohoruotsi/iranlowo/master/docs/adr.gif" width="700">

## Disclaimer

This is beta software, if you pass the diacritizer [out-of-domain text](https://www.quora.com/What-is-in-domain-out-domain-and-open-domain-data), English, pidgin or any other non-Yorùbá text, you will experience very marvelous, black-box results. 

Since this a work-in-progress and we are steadily improving, if you encounter any problems with correctness or performance, please submit [pull-requests](https://github.com/ruohoruotsi/iranlowo/pulls) with corrections or file an [issue](https://github.com/ruohoruotsi/iranlowo/issues).

## License
 
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).