import unittest
from idlelib.pyparse import trans

from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):
    def test_input_phrase(self):
        # Initialize a translator with a phrase
        translator = PigLatin.PigLatinTranslator("hello world")
        # Get the phrase
        phrase = translator.get_phrase()

        self.assertEqual("hello world", phrase)

    def test_translating_empty_phrase(self):
        translator = PigLatin.PigLatinTranslator("")
        translate = translator.translate()
        self.assertEqual("nil", translate)

    def test_translating_word_start_with_a_vowel_0(self):
        translator = PigLatin.PigLatinTranslator("any")
        translate = translator.translate()
        self.assertEqual("anynay", translate)

    def test_translating_word_start_with_a_vowel_1(self):
        translator = PigLatin.PigLatinTranslator("apple")
        translate = translator.translate()
        self.assertEqual("appleyay", translate)

    def test_translating_word_start_with_a_vowel_2(self):
        translator = PigLatin.PigLatinTranslator("ask")
        translate = translator.translate()
        self.assertEqual("askay", translate)

    def test_translating_word_start_with_a_single_consonant(self):
        translator = PigLatin.PigLatinTranslator("hello")
        translate = translator.translate()
        self.assertEqual("ellohay", translate)

    def test_translating_word_start_with_more_consonants(self):
        translator = PigLatin.PigLatinTranslator("known")
        translate = translator.translate()
        self.assertEqual("ownknay", translate)

    def test_translating_a_phrase_with_more_words_0(self):
        translator = PigLatin.PigLatinTranslator("hello world")
        translate = translator.translate()
        self.assertEqual("ellohay orldway", translate)

    def test_translating_a_phrase_with_more_words_1(self):
        translator = PigLatin.PigLatinTranslator("well-being")
        translate = translator.translate()
        self.assertEqual("ellway-eingbay", translate)

    def test_translating_a_phrase_containing_punctuations_0(self):
        translator = PigLatin.PigLatinTranslator("hello world!")
        translate = translator.translate()
        self.assertEqual("ellohay orldway!", translate)

    def test_translating_a_phrase_containing_punctuations_1(self):
        translator = PigLatin.PigLatinTranslator("hello world!@")
        self.assertRaises(PigLatinError, translator.translate)
