#!/usr/bin/python3
from tkinter import *

root = Tk()

root.wm_title("EmyDictionary")

# Labels
keyword = Label(root, text="Keyword")
keyword.grid(row=0, column=0)

meaning = Label(root, text="Meaning")
meaning.grid(row=2, column=0)
# Entry
keyword_text = StringVar()
keyword_entry = Entry(root, border=2, textvariable=keyword_text)
keyword_entry.grid(row=0, column=1)

# Buttons
close = Button(root, text="Close", width=12, border=3, command=root.destroy)
close.grid(row=1, column=5)

search = Button(root, text="Search", width=12, border=3)
search.grid(row=0, column=5)

# ListBox
display = Listbox(root, height=6, width=35, border=2)
display.grid(row=1, column=2, columnspan=3, rowspan=5)

__copyright = Label(root, text="(C) EmyCodes 2024")
__copyright.grid(row=10, column=2, columnspan=2)

root.mainloop()