# -*- coding: utf-8 -*-

import filecmp
import iranlowo as ránlọ
import os


def test_strip_accents():
    ca_fr = "Montréal, über, 12.89, Mère, Françoise, noël, 889"
    yo_0 = "ọjọ́ìbí 18 Oṣù Keje 1918 jẹ́ Ààrẹ Gúúsù Áfríkà"
    yo_1 = "Kí ó tó di ààrẹ"

    assert ránlọ.adr_tools.strip_accents(ca_fr) == "Montreal, uber, 12.89, Mere, Francoise, noel, 889"
    assert ránlọ.adr_tools.strip_accents(yo_0) == "ojoibi 18 Osu Keje 1918 je Aare Guusu Afrika"
    assert ránlọ.adr_tools.strip_accents(yo_1) == "Ki o to di aare"


def test_strip_accents_from_file():
    cwd = os.getcwd()
    src_filepath = cwd + "/tests/testdata/src_file.txt"
    reference_stripped_filepath = cwd + "/tests/testdata/ref_proccessed_file.txt"
    processed_stripped_filepath = cwd + "/tests/testdata/processed_file.txt"

    assert(ránlọ.adr_tools.strip_accents_from_file(src_filepath, processed_stripped_filepath) is True)  # job completed
    assert(filecmp.cmp(src_filepath, processed_stripped_filepath) is False)  # src & processed are different
    assert(filecmp.cmp(reference_stripped_filepath, processed_stripped_filepath))  # processed matches reference


def test_is_text_nfc():
    assert(ránlọ.adr_tools.is_text_nfc("Kílódé, ṣèbí àdúrà le̩ fé̩ gbà nbẹ?") is False)  # NFD
    assert(ránlọ.adr_tools.is_text_nfc("Kílódé, ṣèbí àdúrà le̩ fé̩ gbà nbẹ?") is True)  # NFC


def test_convert_file_to_nfc():
    cwd = os.getcwd()
    nfd_filepath = cwd + "/tests/testdata/nfd.txt"
    reference_nfc_filepath = cwd + "/tests/testdata/nfc.txt"
    processed_nfc_filepath = cwd + "/tests/testdata/processed_nfc.txt"

    assert(ránlọ.adr_tools.convert_file_to_nfc(nfd_filepath, processed_nfc_filepath) == True)  # job completed
    # assert(filecmp.cmp(nfd_filepath, processed_nfc_filepath) is False)  # src & processed are different
    # assert(filecmp.cmp(reference_nfc_filepath, processed_nfc_filepath))  # processed matches reference

