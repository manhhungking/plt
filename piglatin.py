from itertools import filterfalse
import re
class PigLatin:

    def __init__(self, phrase):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        the_vowel = ["a", "e", "i", "o", "u"]

        words = re.split(r'(\s+|-)', self.phrase)
        after_words = []
        for word in words:
            if word in  ["-", " "]:
                after_words.append(word)
                continue

            if word.lower()[0] in the_vowel:
                if word.lower()[-1] == "y":
                    after_words.append(word + "nay")
                elif word.lower()[-1] in the_vowel:
                    after_words.append(word + "yay")
                else:
                    after_words.append(word + "ay")

            else:
                j = 0
                while j < len(word) and word[j].lower() not in the_vowel:
                    j += 1
                after_words.append(word[j:] + word[0:j] + "ay")

        final_word = ""
        for i in after_words:
            final_word = final_word + i
        return final_word

    def PigLatinTranslator(phrase):
        return PigLatin(phrase)