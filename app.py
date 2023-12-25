#!/usr/bin/python3
from models import data
from resources.interpreter import load_data_from_db
from resources import session

special_commands = ["Cancel -f", "Terminate -f", "Exit -f", "Quit -f",
                    "Cancel -F", "Terminate -F", "Exit -F", "Quit -F"]

iterate = True
while iterate:
    user = input("Enter a word: ")
    if user.capitalize() in special_commands:
        iterate = False
    else:
        meanings = load_data_from_db(user, session)
        for meaning in meanings:
            print(f"\t{meaning} \n")
