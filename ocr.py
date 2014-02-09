# -*- coding: utf-8 -*-

import doctest
import requests

def sortWord(word):
    """ Sorting Word
    >>> sortWord('ababac') == {'a': 3, 'b': 2, 'c': 1}
    True
    """
    sort_result = {}
    for char in word:
        if sort_result.has_key(char):
            sort_result[char] += 1
        else:
            sort_result[char] = 1
    return sort_result

def getSource(url):
    return requests.get(url).text

def findRare(sortedWord):
    rare_words = []
    for k, v in sortedWord.items():
        if v < 5:
            rare_words.append(k)
    return rare_words

if __name__ == "__main__":
    doctest.testmod()

    source = getSource('http://www.pythonchallenge.com/pc/def/ocr.html')
    start = source.rfind('<!--') + len('<!--')
    end = source.rfind('-->') - len('-->')
    cryptography = source[start:end]
    sortedWord = sortWord(cryptography)
    rare_words =  findRare(sortedWord)
    answer_list = []
    for rare in rare_words:
        indexing = cryptography.index(rare)
        answer_list.append(indexing)
    answer_list.sort()
    answer = []
    for answer_index in answer_list:
       answer.append( cryptography[answer_index])
    print ''.join(answer)
