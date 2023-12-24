#!/usr/bin/python3
"""
This Interactive English Dictionary program is
built and developed by OGUNDARE OLAMIDE EMMANUEL
"""

import json
from difflib import get_close_matches

from models import data, DictionaryModel
from resources import error_messages
from resources import Base, engine, session


def create_table(engine=engine):
    Base.metadata.create_all(engine)


def insert_data(session=session, data=data):
    for word, meanings in data.items():
        new_word = DictionaryModel(word=word, meanings=json.dumps(meanings))
        session.add(new_word)

    session.commit()


def load_data_from_db(session=session):
    word = input("Enter a word: ").lower()
    result = session.query(DictionaryModel).filter_by(word=word).first()

    if result:
        meanings = json.loads(result.meanings)
        print(f"\n{word.upper()}:\n")
        for meaning in meanings:
            print(f"\t{meaning}\n")
        suggestions = get_close_matches(word, session.query(DictionaryModel))

    if suggestions:
        suggestion = suggestions[0]
        yes = ["y", "yes"]
        no = ["n", "no"]

        user_response = input(f"Do you mean {suggestion}? (y | n):  ")

        if user_response.lower() in yes:
            print(f"\n{suggestion.upper()}", ": \n")
            return data[suggestion]
        elif user_response.lower() in no:
            return error_messages[0]
        else:
            return error_messages[1]
    else:
        return error_messages[0]


if __name__ == "__main__":
    create_table()
    insert_data()
    load_data_from_db()

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
    # suggestions = get_close_matches(word, data.keys())

    # if suggestions:
    #     suggestion = suggestions[0]
    #     yes = ["y", "yes"]
    #     no = ["n", "no"]

    #     user_response = input(f"Do you mean {suggestion}? (y | n):  ")

    #     if user_response.lower() in yes:
    #         print(f"\n{suggestion.upper()}", ": \n")
    #         return data[suggestion]
    #     elif user_response.lower() in no:
    #         return error_messages[0]
    #     else:
    #         return error_messages[1]
    # else:
    #     return error_messages[0]
