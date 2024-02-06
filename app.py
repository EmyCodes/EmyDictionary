#!/usr/bin/python3
from tkinter import *

from models.db import dbModel


db = dbModel()
root = Tk()

def _search():
    responses = db.get_meaning(keyword_text.get().lower())
    if not responses:
        return "No records found."
    else:
        # meaning = responses[1].split(", ")
        meanings = responses[1].split('", ')
        # print(meanings)
        return meanings


def search_command():
    display.delete(0, END)
    meanings = _search()
    if meanings == "No records found.":
        display.insert(END, meanings)
        return
    for i in range(len(meanings)):
        meaning = "{}. {}".format(i+1,
                                  {meanings[i].strip("[").strip("]").strip("'").strip('"')})
        # print(meaning)
        display.insert(END, meaning)

def close_command():
    db.close_db()
    root.destroy()

def clear_command():
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
