from msilib.schema import ListBox
from random import choices
from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()

choices = ['USA', 'Canada', 'Australia'] # use lists if you want to edit `choices`
choices.extend(f"Country {i}" for i in range(100))

countryvar = StringVar(value=choices)
"""
countryvar.set(choices) # resets if needed
"""

# selectmode = "browse" (single) | "extended" (multiple)
l = Listbox(root, listvariable=countryvar, selectmode="multiple") # note, not a ttk widget
l.grid(row=0, column=0)
l.insert('end', 'Line 101 of 100')
# synchronized with l.insert
print(countryvar.get())

"""
Every widget that can be scrolled vertically includes a method named
yview
"""

s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(row=0, column=1, sticky=(N,S))
l.configure(yscrollcommand=s.set)

idx = 2
l.selection_set(idx)
# make sure the selected item is visible
l.see(idx)

l.bind("<<ListboxSelect>>", lambda e: print(l.curselection()))
l.bind("<Double-1>", lambda e: print(l.curselection()))
root.mainloop()
