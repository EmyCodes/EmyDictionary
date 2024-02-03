#!/usr/bin/python3
from tkinter import *

root = Tk()

label = Label(root, text="Keyword")
label.grid(row=0, column=0)

entry = Entry(root, border=2)
entry.grid(row=0, column=1)


root.mainloop()