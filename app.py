#!/usr/bin/python3
"""
This Interactive English Dictionary program is
built and developed by OGUNDARE OLAMIDE EMMANUEL
"""

import json
from difflib import get_close_matches

special_commands = ["Cancel", "Terminate", "Exit"]

with open("data.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)

def translator(word):
    """ To be updated """
    word = word.lower()
    if word in data:
        return data[word]

    # Check for matches
    suggestions = get_close_matches(word, data.keys())

    if suggestions:
        suggestion = suggestions[0]
        yes =["y", "yes"]
        no = ["n", "no"]
        user_response = input(f"Do you mean {suggestion}? (y | n):  ")
        # user = input(" ")
        if user_response.lower() in yes:
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
    print(translator(user))
    if user.capitalize() in special_commands:
        iterate = False
