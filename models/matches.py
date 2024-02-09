#!/usr/bin/python3
from difflib import get_close_matches

def get_matches(keyword, func):
    """
    function to get the closest matches to the word.
    Parameters:\n
        n (str): The word to be searched for.\n
        func (list): The list of words to be searched from.
    Returns:\n
        str: The closest match to the word.
    """
    _items = func   # stores the list of words from the database

    _sug = []   # a temporary list to store the suggestions (first iteration)
    new_sug = [] # a new list to store the suggestions from the temporary list above (second iteration)
    
    _check = ""  # the closest match to the word
    for item in _items:
        sug = get_close_matches(keyword, item)
        if len(sug) != 0:
            _sug.append(sug)
    for item in _sug:
        for j in item:
                new_sug.append(j)
    _check += get_close_matches(keyword, new_sug)[0]
    return _check
