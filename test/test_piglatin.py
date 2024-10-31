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
