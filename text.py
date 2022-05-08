from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()

t = Text(root, width=40, height=10, wrap=WORD)
# txt['state'] = 'disabled'
t.grid(row=0, column=0)
s = ttk.Scrollbar(root, orient=VERTICAL, command=t.yview)
s.grid(row=0, column=1, sticky=(N,S))
t.configure(yscrollcommand=s.set)

# use `see` to make sure that a given line is visible.
# index is linenum.charnum; line idx is 1-based

t.bind("<Double-1>", lambda e: print(t.get('1.0', 'end')))

# the text is inserted before the given index
t.insert("3.0", "Rara") # 'start' , 'end' are valid
root.mainloop()