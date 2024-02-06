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
        meanings = responses[1].split(", ")
        print(meanings)
        return meanings


def search_command():
    display.delete(0, END)
    meaning = _search()
    display.insert(END, meaning)

def close_command():
    db.close_db()
    root.destroy()

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
close = Button(root, text="Close", width=12, border=3, command=close_command)
close.grid(row=3, column=9)


# ListBox
display = Listbox(root, height=6, width=35, border=2)
display.grid(row=2, column=1, columnspan=3, rowspan=5)

__copyright = Label(root, text="(C) EmyCodes 2024")
__copyright.grid(row=10, column=2, columnspan=2)

root.mainloop()
