# -*- coding: utf-8 -*-

import filecmp
import iranlowo.adr as ránlọ
import os


def test_strip_accents_text():
    ca_fr = "Montréal, über, 12.89, Mère, Françoise, noël, 889"
    yo_0 = "ọjọ́ìbí 18 Oṣù Keje 1918 jẹ́ Ààrẹ Gúúsù Áfríkà"
    yo_1 = "Kí ó tó di ààrẹ"

    assert ránlọ.strip_accents_text(ca_fr) == "Montreal, uber, 12.89, Mere, Francoise, noel, 889"
    assert ránlọ.strip_accents_text(yo_0) == "ojoibi 18 Osu Keje 1918 je Aare Guusu Afrika"
    assert ránlọ.strip_accents_text(yo_1) == "Ki o to di aare"


def test_strip_accents_file():
    cwd = os.getcwd()
    src_filepath = cwd + "/tests/testdata/src_file.txt"
    reference_stripped_filepath = cwd + "/tests/testdata/ref_proccessed_file.txt"
    processed_stripped_filepath = cwd + "/tests/testdata/processed_file.txt"

    assert(ránlọ.strip_accents_file(src_filepath, processed_stripped_filepath) is True)  # job completed
    assert(filecmp.cmp(src_filepath, processed_stripped_filepath) is False)         # src & processed are different
    assert(filecmp.cmp(reference_stripped_filepath, processed_stripped_filepath))   # processed matches reference


def test_is_file_nfc():
    cwd = os.getcwd()
    src_filepath_pass = cwd + "/testdata/nfc.txt"
    src_filepath_fail = cwd + "/testdata/nfc_fail.txt"
    assert (ránlọ.is_file_nfc(src_filepath_pass) is True)
    assert (ránlọ.is_file_nfc(src_filepath_fail) is False)


def test_is_text_nfc():
    assert(ránlọ.is_text_nfc("Kílódé, ṣèbí àdúrà le̩ fé̩ gbà nbẹ?") is False)  # NFD
    assert(ránlọ.is_text_nfc("Kílódé, ṣèbí àdúrà le̩ fé̩ gbà nbẹ?") is True)   # NFC
    
    # cover diacritics that have both accents and underdots
    assert(ránlọ.is_text_nfc("kòsí ǹǹkan tó le ń’bẹ̀ pé káa ṣẹ̀sìn-ìn ’dílé è") is False)  # NFD
    assert(ránlọ.is_text_nfc("kòsí ǹǹkan tó le ń’bẹ̀ pé káa ṣẹ̀sìn-ìn ’dílé è") is True)   # NFC


def test_normalize_diacritics_file():
    cwd = os.getcwd()
    nfd_filepath = cwd + "/tests/testdata/nfd.txt"
    reference_nfc_filepath = cwd + "/tests/testdata/nfc.txt"
    processed_nfc_filepath = cwd + "/tests/testdata/processed_nfc.txt"

    assert(ránlọ.normalize_diacritics_file(nfd_filepath, processed_nfc_filepath) is True)  # job completed
    assert(filecmp.cmp(nfd_filepath, processed_nfc_filepath) is False)              # src & processed are different
    assert(filecmp.cmp(reference_nfc_filepath, processed_nfc_filepath) is True)     # processed matches reference


def test_file_info():
    cwd = os.getcwd()
    reference_nfc_filepath = cwd + "/tests/testdata/nfc.txt"
    ránlọ.file_info(reference_nfc_filepath)

    # reference_nfc_filepath

# def test_split_corpus_on_symbol():
#     cwd = os.getcwd()
#     multiline_filepath = "/tests/testdata/multiline.txt"
#     reference_multiline_split_filepath = "/tests/testdata/multiline.split.txt"
#     processed_multiline_split_filepath = "/tests/testdata/processed_multiline.split.txt"
#
#     assert(ránlọ.split_out_corpus_on_symbol(multiline_filepath,
#                                                  reference_multiline_split_filepath, ',') is True)  # job completed
#     assert(filecmp.cmp(multiline_filepath, reference_multiline_split_filepath) is False)              # src & processed are different
#     assert(filecmp.cmp(reference_multiline_split_filepath, processed_multiline_split_filepath) is True)     # processed matches reference
#
#     # try different punctuation ',', ':', etc?


def test_diacritize_text():

    predictions = ránlọ.diacritize_text("leyin igba naa")
    assert(predictions == "lẹ́yìn ìgbà náà")   # generated matches reference
    assert(predictions != "lẹ́yìn igbà náà")   # generated does not match incorrect reference

    predictions = ránlọ.diacritize_text("obinrin")
    assert(predictions == "obìnrin")   # generated matches reference
    assert(predictions != "obinrin")   # generated does not match incorrect reference

    predictions = ránlọ.diacritize_text("okunrin")
    assert(predictions == "ọkùnrin")   # generated matches reference
    assert(predictions != "ọkunrin")   # generated does not match incorrect reference

    predictions = ránlọ.diacritize_text("orisirisi")
    assert(predictions == "oríṣiríṣi")   # generated matches reference
    assert(predictions != "orísiríṣi")   # generated does not match incorrect reference

    predictions = ránlọ.diacritize_text("nitori naa")
    assert(predictions == "nítorí náà")   # generated matches reference
    assert(predictions != "nitorí náà")   # generated does not match incorrect reference

    predictions = ránlọ.diacritize_text("leyin oro mi won ko tun soro mo")
    assert(predictions == "lẹ́yìn ọ̀rọ̀ mi wọn kò tún sọ̀rọ̀ mọ́")   # generated matches reference
    assert(predictions != "lẹ́yìn ọ̀rọ̀ mi won kò tún sọ̀rọ̀ mọ́")   # generated does not match incorrect reference

    # predictions = ránlọ.diacritize_text("awon okunrin nse ise agbara bi ise ode")
    # assert(predictions == "àwọn ọkùnrin nṣe iṣẹ́ agbára bí iṣẹ́ ọdẹ")   # generated matches reference
    # assert(predictions != "awọn ọkùnrin nṣe iṣẹ́ agbára bí iṣẹ́ ọdẹ")   # generated does not match incorrect reference

    predictions = ránlọ.diacritize_text("ati beebee lo")
    assert(predictions == "àti bẹ́ẹ̀bẹ́ẹ̀ lọ")   # generated matches reference
    assert(predictions != "ati bẹ́ẹ̀bẹ́ẹ̀ lọ")   # generated does not match incorrect reference

    predictions = ránlọ.diacritize_text("bee ni gbogbo ise ago naa ti ago ajo pari")
    assert(predictions == "bẹ́ẹ̀ ni gbogbo iṣẹ́ àgọ́ náà ti àgọ́ àjọ parí")   # generated matches reference
    assert(predictions != "bẹ́ẹ̀ ni gbogbo iṣẹ́ àgọ́ náà ti agọ́ àjọ parí")   # generated does not match incorrect reference

    # predictions = ránlọ.diacritize_text("bi ase nlo yii")
    # assert(predictions == "bí aṣe ńlọ yìí")   # generated matches reference
    # assert(predictions != "bí ase ńlọ yìí")   # generated does not match incorrect reference

    predictions = ránlọ.diacritize_text("o dabi pe")
    assert(predictions == "ó dàbí pé")   # generated matches reference
    assert(predictions != "ó dàbí pe")   # generated does not match incorrect reference

    predictions = ránlọ.diacritize_text("sugbon")
    assert(predictions == "ṣùgbọ́n")   # generated matches reference
    assert(predictions != "ṣugbọ́n")   # generated does not match incorrect reference

