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