#!/usr/bin/python3
from difflib import get_close_matches
from tkinter import *

from models.db import dbModel


db = dbModel()


def get_matches(n):
    """
    function to get the closest matches to the word.
    Parameters:\n
        n (str): The word to be searched for in the database.
    Returns:\n
        str: The closest match to the word.
    """
    new_sug = []
    _sug = []
    _items = db.get_all(n)
    for i in _items:
        sug = get_close_matches(n, i)
        if len(sug) != 0:
            _sug.append(sug)
    for i in _sug:
        for j in i:
                new_sug.append(j)
    _check = get_close_matches(n, new_sug)[0]
    return _check


root = Tk()

def _search():
    """
    function to search for the word in the database.
    Returns:\n
        str: The meanings of the word if found,
             a suggestion if the word is not found,
             or "No records found." if the word is not found.
    """
    _text = keyword_text.get().lower()
    responses = db.get_meaning(_text)
    if responses is None:
        try:
            suggestion = get_matches(_text)
            if suggestion:
                return f"Do you mean '{suggestion}'?"
        except IndexError:
            return "No records found."
    elif not responses:
        pass
    else:
        meanings = responses[1].split('", ')
        return meanings


def search_command():
    """
    function to implement the search button.
    Returns:\n
        None
    """
    display.delete(0, END)
    meanings = _search()
    if meanings == "No records found.":
        display.insert(END, meanings)
        return
    if str(meanings).startswith("Do you mean"):
        display.insert(END, meanings)
        return
    for i in range(len(meanings)):
        meaning = "{}. {}\n".format(i+1,
                                  meanings[i].strip("[]").strip('"'))
        display.insert(END, meaning)

def close_command():
    """
    function to implement the close button.
    Returns:\n
        None
    """
    db.close_db()
    root.destroy()

def clear_command():
    """
    function to implement the clear button.
    Returns:\n
        None
    """
    keyword_entry.delete(0, END)
    display.delete(0, END)

root.wm_title("EmyDictionary")

# Labels
keyword = Label(root, text="Keyword")
keyword.grid(row=1, column=0)

meaning = Label(root, text="Meaning")
meaning.grid(row=2, column=0)
# Entry
keyword_text = StringVar()
keyword_entry = Entry(root, border=2, textvariable=keyword_text)
keyword_entry.grid(row=1, column=1)

# Buttons
search = Button(root, text="Search", width=12, border=3, command=search_command)
search.grid(row=2, column=9)

clear = Button(root, text="Clear", width=12, border=3, command=clear_command)
clear.grid(row=4, column=9)

close = Button(root, text="Close", width=12, border=3, command=close_command)
close.grid(row=6, column=9)

# ListBox
display = Listbox(root, height=6, width=35, border=2)
display.grid(row=2, column=1, columnspan=3, rowspan=5)

__copyright = Label(root, text="(C) EmyCodes 2024")
__copyright.grid(row=8, column=1, columnspan=3, rowspan=5)

root.mainloop()
