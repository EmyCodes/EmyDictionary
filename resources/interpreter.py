#!/usr/bin/python3
"""
This Interactive English Dictionary program is
built and developed by OGUNDARE OLAMIDE EMMANUEL
"""

from models.dictionary import DictionaryModel
from app import Base

def create_table(engine):
    Base.metadata.create_all(engine)


def insert_data(session, data):
    for word, meanings in data.items():
        new_word = DictionaryModel(word=word, meanings=json.dumps(meanings))
        session.add(new_word)

    session.commit()


def load_data_from_db(word, session):
    result = session.query(DictionaryModel).filter_by(word=word).first()

    if result:
        meanings = json.loads(result.meanings)
        print(f"\n{word.upper()}:\n")
        for meaning in meanings:
            print(f"\t{meaning}\n")
        suggestions = get_close_matches(word, [entry.word for entry in session.query(DictionaryModel)])

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
    import json
    from difflib import get_close_matches

    from models import data
    from resources.error import error_messages
    from resources.base import Base, engine, session
    from resources.interpreter import load_data_from_db, insert_data
    # create_table(engine)
    insert_data(session, data)
    word = input("Enter a word: ").lower()
    load_data_from_db(word)

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
