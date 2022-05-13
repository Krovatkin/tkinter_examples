from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()

ttk.Button(root, text="Button1").grid(row=0)
s = ttk.Separator(root, orient=HORIZONTAL).grid(row=1, sticky=(W, E))
ttk.Button(root, text="Button2").grid(row=2)
root.columnconfigure(0, weight=1)
root.mainloop()