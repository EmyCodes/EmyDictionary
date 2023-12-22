#!/usr/bin/python3
"""
This Interactive English Dictionary program is
built and developed by OGUNDARE OLAMIDE EMMANUEL
"""

import json
from difflib import get_close_matches

special_commands = ["Cancel -f", "Terminate -f", "Exit -f", "Quit -f",
                    "Cancel -F", "Terminate -F", "Exit -F", "Quit -F"]

with open("data.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)


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


# Usage
iterate = True
while iterate:
    user = input("Enter a word: ")
    if user.capitalize() in special_commands:
        iterate = False
    else:
        meanings = translator(user)
        for meaning in meanings:
            print(f"\t{meaning} \n")
    
