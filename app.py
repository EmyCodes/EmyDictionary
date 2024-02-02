#!/usr/bin/python3
from resources import interpreter
from resources import error_messages
special_commands = ["Cancel -f", "Terminate -f", "Exit -f", "Quit -f",
                    "Cancel -F", "Terminate -F", "Exit -F", "Quit -F"]

iterate = True
# while iterate:
#     user = input("Enter a word: ")
#     if user.capitalize() in special_commands:
#         iterate = False
#     else:
#         meanings = interpreter(user)
#         if meanings in error_messages:
#             print(f"\n\t{meanings}\n")
#         # else:
#         #     word_count = len(meanings)
#         #     for word in range(word_count):
#         #         print(f"\t{word + 1}. {meanings[word]} \n")
rain = input("Enter a word: ")
print(interpreter(rain))