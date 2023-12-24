#!/usr/bin/python3
"""
This Interactive English Dictionary program is
built and developed by OGUNDARE OLAMIDE EMMANUEL
"""

import json
import os
from difflib import get_close_matches

from resources.error import error_messages
from resources import Base, engine
from models import data, Dictionary


data = data
def create_table(engine=engine):
    Base.metadata.create_all(engine)

def insert_data(session, data):
    for word, meanings in data.items():
        new_word = Dictionary(word=word, meanings=json.dumps(meanings))
        session.add(new_word)

    session.commit()

# def translator(word):
#     """
#     Translates the given word and returns its meanings.

#     Parameters:
#         word (str): The English word to be translated.

#     Returns:
#         list or str: A list of meanings if the word is found,
#                     a string with suggestions if a close match is found,
#                     or an error message if the word doesn't exist.
#     """
#     word = word.lower()

#     data = data() # Load the data from the json file

#     if word in data:
#         print(f"\n{word.upper()}", ": \n")
#         return data[word]

#     # Check for matches
#     suggestions = get_close_matches(word, data.keys())

#     if suggestions:
#         suggestion = suggestions[0]
#         yes = ["y", "yes"]
#         no = ["n", "no"]

#         user_response = input(f"Do you mean {suggestion}? (y | n):  ")

#         if user_response.lower() in yes:
#             print(f"\n{suggestion.upper()}", ": \n")
#             return data[suggestion]
#         elif user_response.lower() in no:
#             return error_messages[0]
#         else:
#             return error_messages[1]
#     else:
#         return error_messages[0]
