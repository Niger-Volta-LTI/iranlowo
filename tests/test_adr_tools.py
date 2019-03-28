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
    src_file = cwd + "/tests/testdata/file1.txt"
    target_file = cwd + "/tests/testdata/file2.txt"
    test_target_file = cwd + "/tests/testdata/file3.txt"

    assert(ránlọ.adr_tools.strip_accents_from_file(src_file, test_target_file) is True)
    assert(filecmp.cmp(src_file, test_target_file) is False)
    assert(filecmp.cmp(target_file, test_target_file))


def test_is_text_nfc():
    assert(ránlọ.adr_tools.is_text_nfc("Kílódé, ṣèbí àdúrà le̩ fé̩ gbà nbẹ?") is False)  # NFD
    assert(ránlọ.adr_tools.is_text_nfc("Kílódé, ṣèbí àdúrà le̩ fé̩ gbà nbẹ?") is True)  # NFC

#
# def test_convert_to_nfc():
#     nfd_file = "./testdata/nfd.txt"
#     target_file = "./testdata/file3.txt"
#
#     assert(iranlowo.adr_tools.convert_to_NFC(nfd_file, target_file) == True)
#     # assert(target_file meets specs for NFD or matches a previously validated NFC file)
