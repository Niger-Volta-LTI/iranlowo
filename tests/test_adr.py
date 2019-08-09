# -*- coding: utf-8 -*-

import filecmp
import iranlowo.adr as ránlọ
from iranlowo import utils
from iranlowo import preprocessing
import unittest

from tests.utils import datapath


class IranlowoADRTest(unittest.TestCase):

    def test_strip_accents_text(self):
        ca_fr = "Montréal, über, 12.89, Mère, Françoise, noël, 889"
        yo_0 = "ọjọ́ìbí 18 Oṣù Keje 1918 jẹ́ Ààrẹ Gúúsù Áfríkà"
        yo_1 = "Kí ó tó di ààrẹ"

        self.assertEqual(utils.strip_accents_text(ca_fr), "Montreal, uber, 12.89, Mere, Francoise, noel, 889")
        self.assertEqual(utils.strip_accents_text(yo_0), "ojoibi 18 Osu Keje 1918 je Aare Guusu Afrika")
        self.assertEqual(utils.strip_accents_text(yo_1), "Ki o to di aare")

    def test_strip_accents_file(self):
        src_filepath = datapath('src_file.txt')
        reference_stripped_filepath = datapath('ref_proccessed_file.txt')
        processed_stripped_filepath = datapath('processed_file.txt')

        self.assertTrue(preprocessing.strip_accents_file(src_filepath, processed_stripped_filepath))
        self.assertFalse(filecmp.cmp(src_filepath, processed_stripped_filepath))
        self.assertTrue(filecmp.cmp(reference_stripped_filepath, processed_stripped_filepath))

    def test_is_file_nfc(self):
        src_filepath_pass = datapath('nfc.txt')
        src_filepath_fail = datapath('nfc_fail.txt')

        self.assertTrue(utils.is_file_nfc(src_filepath_pass))
        self.assertFalse(utils.is_file_nfc(src_filepath_fail))

    def test_is_text_nfc(self):
        self.assertFalse(utils.is_text_nfc("Kílódé, ṣèbí àdúrà le̩ fé̩ gbà nbẹ?"))
        self.assertFalse(utils.is_text_nfc("Kílódé, ṣèbí àdúrà le̩ fé̩ gbà nbẹ?"))

        self.assertTrue(utils.is_text_nfc('kòsí ǹǹkan tó le ń’bẹ̀ pé káa ṣẹ̀sìn-ìn ’dílé è'))
        self.assertFalse(utils.is_text_nfc('kòsí ǹǹkan tó le ń’bẹ̀ pé káa ṣẹ̀sìn-ìn ’dílé è'))

    def test_normalize_diacritics_file(self):
        nfd_filepath = datapath('nfd.txt')
        reference_nfc_filepath = datapath('nfc.txt')
        processed_nfc_filepath = datapath('processed_nfc.txt')

        self.assertTrue(preprocessing.normalize_diacritics_file(nfd_filepath, processed_nfc_filepath))
        self.assertFalse(filecmp.cmp(nfd_filepath, processed_nfc_filepath))  # src & processed are different
        self.assertTrue(filecmp.cmp(reference_nfc_filepath, processed_nfc_filepath))  # processed matches reference

    def test_file_info(self):
        reference_nfc_filepath = datapath('nfc.txt')
        utils.file_info(reference_nfc_filepath)

        # reference_nfc_filepath

    # def test_split_corpus_on_symbol(self):
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

    def test_diacritize_text(self):
        predictions = ránlọ.diacritize_text("leyin igba naa")
        self.assertEqual(predictions, "lẹ́yìn ìgbà náà")  # generated matches reference
        self.assertNotEqual(predictions, "lẹ́yìn igbà náà")  # generated does not match incorrect reference

        predictions = ránlọ.diacritize_text("obinrin")
        self.assertEqual(predictions, "obìnrin")  # generated matches reference
        self.assertNotEqual(predictions, "obinrin")  # generated does not match incorrect reference

        predictions = ránlọ.diacritize_text("okunrin")
        self.assertEqual(predictions, "ọkùnrin")  # generated matches reference
        self.assertNotEqual(predictions, "ọkunrin")  # generated does not match incorrect reference

        predictions = ránlọ.diacritize_text("orisirisi")
        self.assertEqual(predictions, "oríṣiríṣi")  # generated matches reference
        self.assertNotEqual(predictions, "orísiríṣi")  # generated does not match incorrect reference

        predictions = ránlọ.diacritize_text("nitori naa")
        self.assertEqual(predictions, "nítorí náà")  # generated matches reference
        self.assertNotEqual(predictions, "nitorí náà")  # generated does not match incorrect reference

        predictions = ránlọ.diacritize_text("leyin oro mi won ko tun soro mo")
        self.assertEqual(predictions, "lẹ́yìn ọ̀rọ̀ mi wọn kò tún sọ̀rọ̀ mọ́")  # generated matches reference
        self.assertNotEqual(predictions, "lẹ́yìn ọ̀rọ̀ mi won kò tún sọ̀rọ̀ mọ́")  # generated does not match incorrect reference

        # predictions = ránlọ.diacritize_text("awon okunrin nse ise agbara bi ise ode")
        # assert(predictions , "àwọn ọkùnrin nṣe iṣẹ́ agbára bí iṣẹ́ ọdẹ")   # generated matches reference
        # assert(predictions , "awọn ọkùnrin nṣe iṣẹ́ agbára bí iṣẹ́ ọdẹ")   # generated does not match incorrect reference

        predictions = ránlọ.diacritize_text("ati beebee lo")
        self.assertEqual(predictions, "àti bẹ́ẹ̀bẹ́ẹ̀ lọ")  # generated matches reference
        self.assertNotEqual(predictions, "ati bẹ́ẹ̀bẹ́ẹ̀ lọ")  # generated does not match incorrect reference

        predictions = ránlọ.diacritize_text("bee ni gbogbo ise ago naa ti ago ajo pari")
        self.assertEqual(predictions, "bẹ́ẹ̀ ni gbogbo iṣẹ́ àgọ́ náà ti àgọ́ àjọ parí")  # generated matches reference
        self.assertNotEqual(predictions, "bẹ́ẹ̀ ni gbogbo iṣẹ́ àgọ́ náà ti agọ́ àjọ parí")  # generated does not match incorrect reference

        # predictions = ránlọ.diacritize_text("bi ase nlo yii")
        # assert(predictions , "bí aṣe ńlọ yìí")   # generated matches reference
        # assert(predictions , "bí ase ńlọ yìí")   # generated does not match incorrect reference

        predictions = ránlọ.diacritize_text("o dabi pe")
        self.assertEqual(predictions, "ó dàbí pé")  # generated matches reference
        self.assertNotEqual(predictions, "ó dàbí pe")  # generated does not match incorrect reference

        predictions = ránlọ.diacritize_text("sugbon")
        self.assertEqual(predictions, "ṣùgbọ́n")  # generated matches reference
        self.assertNotEqual(predictions, "ṣugbọ́n")  # generated does not match incorrect reference


