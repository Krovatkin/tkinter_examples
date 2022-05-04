from tkinter import *
from tkinter import ttk # new themed widgets
root = Tk()
phone = StringVar()
# Radiobutton selection doesn't generates any event
# One can use`trace` see an example with checkbutton above

def onchange():
    print (f"phone={phone.get()}")

home = ttk.Radiobutton(root, text='Home', variable=phone, value='home', command=onchange).grid(row=0, column=0)
office = ttk.Radiobutton(root, text='Office', variable=phone, value='office', command=onchange).grid(row=0, column=1)
cell = ttk.Radiobutton(root, text='Mobile', variable=phone, value='cell', command=onchange).grid(row=0, column=2)
root.mainloop()