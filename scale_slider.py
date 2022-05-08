from distutils import command
from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()

def update(val):
    num.set(f"value is {val}")

s = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=1.0, to=100.0, command=update)
s.grid(row=0, column=0, sticky='we')
# s.configure(value=100.0)

# s.state(['disabled'])
num = StringVar()
l = ttk.Label(root, textvariable=num)
l.grid(column=0, row=1, sticky='we')



root.mainloop()

# To implement discrete steps
# https://stackoverflow.com/a/25745136

"""
valuelist = [0,10,30,60,100,150,210,270]

def valuecheck(value):
    newvalue = min(valuelist, key=lambda x:abs(x-float(value)))
    slider.set(newvalue)

root = tk.Tk()

slider = tk.Scale(root, from_=min(valuelist), to=max(valuelist), command=valuecheck, orient="horizontal")
"""
