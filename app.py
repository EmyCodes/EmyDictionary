#!/usr/bin/python3
"""
This Interactive English Dictionary program is
built and developed by OGUNDARE OLAMIDE EMMANUEL
"""

import json

special_commands = ["Cancel", "Terminate", "Exit"]
with open("data.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)

def translator(word):
    """ To be updated """
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "This word doesn't exist. Please, double check"

