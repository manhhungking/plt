class PigLatin:

    def __init__(self, phrase):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        the_vowel = ["a", "e", "i", "o", "u"]
        if self.phrase.lower()[0] in the_vowel:
            if self.phrase.lower()[-1] == "y":
                return self.phrase + "nay"
            elif self.phrase.lower()[-1] in the_vowel:
                return self.phrase + "yay"
            else:
                return self.phrase + "ay"


    def PigLatinTranslator(phrase):
        return PigLatin(phrase)