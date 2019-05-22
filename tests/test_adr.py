# -*- coding: utf-8 -*-

import filecmp
import iranlowo as ránlọ
import os


def test_strip_accents_text():
    ca_fr = "Montréal, über, 12.89, Mère, Françoise, noël, 889"
    yo_0 = "ọjọ́ìbí 18 Oṣù Keje 1918 jẹ́ Ààrẹ Gúúsù Áfríkà"
    yo_1 = "Kí ó tó di ààrẹ"

    assert ránlọ.adr.strip_accents_text(ca_fr) == "Montreal, uber, 12.89, Mere, Francoise, noel, 889"
    assert ránlọ.adr.strip_accents_text(yo_0) == "ojoibi 18 Osu Keje 1918 je Aare Guusu Afrika"
    assert ránlọ.adr.strip_accents_text(yo_1) == "Ki o to di aare"


def test_strip_accents_file():
    cwd = os.getcwd()
    src_filepath = cwd + "/tests/testdata/src_file.txt"
    reference_stripped_filepath = cwd + "/tests/testdata/ref_proccessed_file.txt"
    processed_stripped_filepath = cwd + "/tests/testdata/processed_file.txt"

    assert(ránlọ.adr.strip_accents_file(src_filepath, processed_stripped_filepath) is True)  # job completed
    assert(filecmp.cmp(src_filepath, processed_stripped_filepath) is False)         # src & processed are different
    assert(filecmp.cmp(reference_stripped_filepath, processed_stripped_filepath))   # processed matches reference


def test_is_text_nfc():
    assert(ránlọ.adr.is_text_nfc("Kílódé, ṣèbí àdúrà le̩ fé̩ gbà nbẹ?") is False)  # NFD
    assert(ránlọ.adr.is_text_nfc("Kílódé, ṣèbí àdúrà le̩ fé̩ gbà nbẹ?") is True)   # NFC
    
    # cover diacritics that have both accents and underdots
    assert(ránlọ.adr.is_text_nfc("kòsí ǹǹkan tó le ń’bẹ̀ pé káa ṣẹ̀sìn-ìn ’dílé è") is False)  # NFD
    assert(ránlọ.adr.is_text_nfc("kòsí ǹǹkan tó le ń’bẹ̀ pé káa ṣẹ̀sìn-ìn ’dílé è") is True)   # NFC


def test_normalize_diacritics_file():
    cwd = os.getcwd()
    nfd_filepath = cwd + "/tests/testdata/nfd.txt"
    reference_nfc_filepath = cwd + "/tests/testdata/nfc.txt"
    processed_nfc_filepath = cwd + "/tests/testdata/processed_nfc.txt"

    assert(ránlọ.adr.normalize_diacritics_file(nfd_filepath, processed_nfc_filepath) is True)  # job completed
    assert(filecmp.cmp(nfd_filepath, processed_nfc_filepath) is False)              # src & processed are different
    assert(filecmp.cmp(reference_nfc_filepath, processed_nfc_filepath) is True)     # processed matches reference


def test_file_info():
    cwd = os.getcwd()
    reference_nfc_filepath = cwd + "/tests/testdata/nfc.txt"
    ránlọ.adr.file_info(reference_nfc_filepath)

    # reference_nfc_filepath

# def test_split_corpus_on_symbol():
#     cwd = os.getcwd()
#     multiline_filepath = "/tests/testdata/multiline.txt"
#     reference_multiline_split_filepath = "/tests/testdata/multiline.split.txt"
#     processed_multiline_split_filepath = "/tests/testdata/processed_multiline.split.txt"
#
#     assert(ránlọ.adr.split_out_corpus_on_symbol(multiline_filepath,
#                                                  reference_multiline_split_filepath, ',') is True)  # job completed
#     assert(filecmp.cmp(multiline_filepath, reference_multiline_split_filepath) is False)              # src & processed are different
#     assert(filecmp.cmp(reference_multiline_split_filepath, processed_multiline_split_filepath) is True)     # processed matches reference
#
#     # try different punctuation ',', ':', etc?


def test_diacritize_text():
    predictions = ránlọ.adr.diacritize_text("awon okunrin nse ise agbara bi ise ode")
    assert(predictions == "àwọn ọkùnrin nṣe iṣẹ́ agbára bí iṣẹ́ ọdẹ")   # generated matches reference
    assert(predictions != "awọn ọkùnrin nṣe iṣẹ́ agbára bí iṣẹ́ ọdẹ")   # generated does not match incorrect reference
