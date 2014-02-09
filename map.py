# -*- coding: utf-8 -*-

import doctest

def __remapAlphabet__(char):
    """
    >>> __remapAlphabet__('a')
    'c'
    >>> __remapAlphabet__('x')
    'z'
    >>> __remapAlphabet__('y')
    'a'
    >>> __remapAlphabet__('z')
    'b'
    >>> __remapAlphabet__(' ')
    ' '
    """
    remap_char = ""
    alphabet = ['a', 'b', 'c', 'd',
                'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p',
                'q', 'r', 's', 't',
                'u', 'v', 'w', 'x',
                'y', 'z']
    try:
        order = alphabet.index(char)
        if order < 24:
            remap = order + 2
            remap_char = alphabet[remap]
        elif 24 <= order < len(alphabet):
            remap = order + 2 - len(alphabet)
            remap_char = alphabet[remap]
    except:
        remap_char = char
    return remap_char

def wordRemap(word):
    """ Word Remapping
    >>> wordRemap('koe')
    'mqg'
    >>> wordRemap('abc')
    'cde'
    """
    remap_word = map(__remapAlphabet__, word)
    return ''.join(remap_word)

if __name__ == "__main__":
    doctest.testmod()
