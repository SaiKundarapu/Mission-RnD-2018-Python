__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys

def getPunctuation(s):
    if s[-1] == "," or s[-1] == ".":
        return (s[-1], s[:-1])
    return ("", s)

def pig_latin(word):
    import string
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = set(string.ascii_lowercase) - vowels
    isCapitalized = word[0].isupper()
    punctuation, word = getPunctuation(word)
    word = word.lower()

    for i in word:
        if i in consonants:
            word = word[1:]+word[0]
        else:
            word=word+"ay"
            break

    if isCapitalized:
        word= word.capitalize()

    word = word+punctuation

    return word

def main():
    while(True):
        words = sys.argv[1]
        result = []
        for word in words.split():
            result.append(pig_latin(word))

        print(" ".join(result))

if __name__ == "__main__":
    sys.exit(main())