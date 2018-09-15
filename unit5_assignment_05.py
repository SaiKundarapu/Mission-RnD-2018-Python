__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
import string
def prune_either_or(sentence):
    try:
        e=sentence.find(' either ')
        o=sentence.find(' or ')
        if e<1 or o<e:
            return sentence
        blah=list(sentence[0:e])
        if blah == []:
            return sentence
        something=list(sentence[(e+7):o])
        if something == []:
            return sentence
        return "".join(blah+something)
    except Exception:
        return sentence

def test_prune_either_or_student():
    assert "we could go to a movie"==prune_either_or("we could either go to a movie or a hotel")
    assert "I think the amazon great indian sale will be today"==prune_either_or("I think the amazon great indian sale will be either today or tomorrow")
    assert "we could go to a movie" == prune_either_or("we could go to a movie")
    assert "either go to a movie or a hotel" == prune_either_or("either go to a movie or a hotel")
    assert "He is neither student nor faculty" == prune_either_or("He is neither student nor faculty")
    assert "Take origin as 1" == prune_either_or("Take origin as either 1 or 3")
    assert None == prune_either_or(None)


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
