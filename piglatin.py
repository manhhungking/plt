class PigLatin:

    def __init__(self, phrase):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"

    def PigLatinTranslator(phrase):
        return PigLatin(phrase)