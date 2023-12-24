#!/usr/bin/python3

import json
import os

file_path = os.path.join(os.path.dirname(__file__), "data.json")
with open(file_path, mode="r", encoding="utf-8") as f:
    data = json.load(f)

# from resources import Base, engine
# from models import Dictionary

# file_path = os.path.join(os.path.dirname(__file__), "data.json")
# with open(file_path, mode="r", encoding="utf-8") as f:
#     data = json.load(f)

# def create_table(engine=engine):
#     Base.metadata.create_all(engine)

# def insert_data(session, data):
#     for word, meanings in data.items():
#         new_word = Dictionary(word=word, meanings=json.dumps(meanings))
#         session.add(new_word)

#     session.commit()