__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.
 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.
 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.
 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.
 Do not modify the input file, the same constraints for processing input hold as for unit4_assignment_01
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.
 With in an anagram group, order them in case insensitive ascending sorting order.
 If 2 anagram groups have same count, then set with smaller starting word comes first.
 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.
 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.
 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils

def grouping(words):
    import string
    letter=list(string.ascii_lowercase)
    return letter.index(words[0].lower())

def anagram(words):
    anagrams=[]
    for x in words:
        l=[]
        for y in words:
            if(len(x)!=len(y)):
                continue
            for letter in x:
                if letter.upper() not in y and letter.lower() not in y:
                    break
            else:
                l.append(y)
        l.sort(key=grouping)
        anagrams.append(l)
        for x in l:
            words.remove(x)
    for x in words:
        anagrams.append([x])
    return anagrams

def AnagramLen(wlist):
    return -len(wlist),grouping(wlist[0])

def anagram_sort(source, destination):
    words = []
    with open(source, 'rt') as s:
        for word in s:
            if not (word[0] is '#' or word[0] is ' ' or word[0] is '\n'):
                words.append(word.strip())
    anagrams=anagram(words)
    anagrams.sort(key=AnagramLen)
    with open(destination,"wt") as d:
        for x in anagrams:
            for word in x:
                d.write(word+"\n")

def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
