#!/usr/bin/python3
"""
This Interactive English Dictionary program is
built and developed by OGUNDARE OLAMIDE EMMANUEL
"""

import json
from difflib import get_close_matches

from models import load_data

def translator(word):
    """
    Translates the given word and returns its meanings.

    Parameters:
        word (str): The English word to be translated.

    Returns:
        list or str: A list of meanings if the word is found,
                    a string with suggestions if a close match is found,
                    or an error message if the word doesn't exist.
    """
    word = word.lower()

    data = load_data()
    if word in data:
        print(f"\n{word.upper()}", ": \n")
        return data[word]

    # Check for matches
    suggestions = get_close_matches(word, data.keys())

    if suggestions:
        suggestion = suggestions[0]
        yes = ["y", "yes"]
        no = ["n", "no"]
        user_response = input(f"Do you mean {suggestion}? (y | n):  ")
        # user = input(" ")
        if user_response.lower() in yes:
            print(f"\n{suggestion.upper()}", ": \n")
            return data[suggestion]
        elif user_response.lower() in no:
            return "This word doesn't exist. Please, double check it."
        else:
            return "Invalid Input. Please, try again with the right word."
    else:
        return "This word doesn't exist. Please, double check it."

