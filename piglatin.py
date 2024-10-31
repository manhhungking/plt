from itertools import filterfalse
import re

from error import PigLatinError

def trans(word, case):
    if case == 0:
        return word
    if case == 1:
        return word[0].upper() + word[1:].lower()
    if case == 2:
        return word.upper()

class PigLatin:

    def __init__(self, phrase):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        the_vowel = ["a", "e", "i", "o", "u"]
        the_consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
        the_punctuation = [".", ",", ";", ":", "'", "?", "!", "(", ")", "-", " "]

        punctuation = r"[ -.,;:'?!()]"
        words_and_punctuation = re.split(f'({punctuation})', self.phrase)

        after_words = []
        for word in words_and_punctuation:
            case = 0 # case 0 is normal word, case 1 is upper-case word, case 2 is title-case word
            if word == "":
                continue
            if word in the_punctuation:
                after_words.append(word)
                continue
            if word.isupper():
                case = 2
            else:
                if word[0].isupper():
                    case = 1
                for i in range(1, len(word)):
                    if word[i].isupper():
                        raise PigLatinError("Not allowed word")
            if word.lower()[0] in the_vowel:
                if word.lower()[-1] == "y":
                    translated_word = word + "nay"
                    after_words.append(trans(translated_word, case))
                elif word.lower()[-1] in the_vowel:
                    translated_word = word + "yay"
                    after_words.append(trans(translated_word, case))
                else:
                    translated_word = word + "ay"
                    after_words.append(trans(translated_word, case))

            elif word.lower()[0] in the_consonant:
                j = 0
                while j < len(word) and word[j].lower() not in the_vowel:
                    j += 1
                translated_word = word[j:] + word[0:j] + "ay"
                after_words.append(trans(translated_word, case))
            else:
                raise PigLatinError("Unrecognized character")

        final_word = ""
        for i in after_words:
            final_word = final_word + i
        return final_word

    def PigLatinTranslator(phrase):
        return PigLatin(phrase)