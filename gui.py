#!/usr/bin/python3
from tkinter import *

root = Tk()

# Labels
keyword = Label(root, text="Keyword")
keyword.grid(row=0, column=0)

entry = Entry(root, border=2)
entry.grid(row=0, column=1)


root.mainloop()