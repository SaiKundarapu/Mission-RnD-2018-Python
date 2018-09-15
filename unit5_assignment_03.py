__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    if first is None or second is None:
        return False
    else:
        first=first.replace(" ","")
        second=second.replace(" ","")
        first=(first.lower())
        second=(second.lower())

        if(first.__len__()!=second.__len__()):
            return False
        for i in first:
            if first.count(i)!=second.count(i):
                return False
        else:
            return True


# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.
    assert False== are_anagrams(None,None)
    assert False==are_anagrams(None,"sai")
    assert True == are_anagrams("sai","ias")
    assert False == are_anagrams("sai","ksai")
    assert True == are_anagrams("Anna Madrigal", "a man and a girl")
    assert False==are_anagrams("Anna Madrigal", "man and girl")

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_are_anagrams(are_anagrams)
