#!/usr/bin/python3
from resources import interpreter
from resources import error_messages
special_commands = ["Cancel -f", "Terminate -f", "Exit -f", "Quit -f",
                    "Cancel -F", "Terminate -F", "Exit -F", "Quit -F"]

iterate = True
while iterate:
    try:
        user = input("Enter a word: ")
        if user.capitalize() in special_commands:
            iterate = False
        else:
            meanings = interpreter(user)
            count = len(meanings)
            # if type(meanings) == str:
            for i in range(count):
                print(meanings)
    except TypeError:
            print("\n\tCheck your Input. It must be a string!\n")
    except KeyboardInterrupt:
        # print("\n\tCheck your Input. It must be a string!\n")
        print("\n\nExit with any of the folloiwing commands:\n")
        for i in range(len(special_commands)):
            if i < len(special_commands) -1:
                print(special_commands[i], end=", ")
            else:
                print(special_commands[i], end="\n")

# rain = input("Enter a word: ")
# print(interpreter(rain))