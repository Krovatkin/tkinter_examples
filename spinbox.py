from tkinter import *
from tkinter import ttk # new themed widgets
root = Tk()

spinval = StringVar()
s = Spinbox(root, from_=1.0, to=50.0, increment=.5, textvariable=spinval)
s.grid(row=0)
spinval2 = StringVar()
# s.state(['readonly'])
s2 = Spinbox(root, textvariable=spinval2, values=["Mon", "Tue", "Wed"])
s2.grid(row=1)
def show_val(*args):
    print(args)
s.bind("<<Increment>>", show_val)
s.bind("<<Decrement>>", show_val)
root.mainloop()