from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()

lf = ttk.Labelframe(root, text='Label')
lf.grid()
ttk.Button(lf, text="Button1").grid(row=0)
ttk.Button(lf, text="Button2").grid(row=1)
root.columnconfigure(0, weight=1)
root.mainloop()