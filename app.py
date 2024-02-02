#!/usr/bin/python3
from resources import interpreter
from resources import error_messages
special_commands = ["Cancel -f", "Terminate -f", "Exit -f", "Quit -f",
                    "Cancel -F", "Terminate -F", "Exit -F", "Quit -F"]

iterate = True
while iterate:
    user = input("Enter a word: ")
    if user.capitalize() in special_commands:
        iterate = False
    else:
        meanings = interpreter(user)
        count = len(meanings)
        # if type(meanings) == str:
        for i in range(count):
            print(meanings)
# rain = input("Enter a word: ")
# print(interpreter(rain))