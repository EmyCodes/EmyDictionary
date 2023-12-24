#!/usr/bin/python3

from resources import interpreter

special_commands = ["Cancel -f", "Terminate -f", "Exit -f", "Quit -f",
                    "Cancel -F", "Terminate -F", "Exit -F", "Quit -F"]

iterate = True
while iterate:
    user = input("Enter a word: ")
    if user.capitalize() in special_commands:
        iterate = False
    else:
        meanings = interpreter(user)
        for meaning in meanings:
            print(f"\t{meaning} \n")
