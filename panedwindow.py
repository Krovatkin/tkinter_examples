from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()

p = ttk.Panedwindow(root, orient=VERTICAL)
p.grid(sticky=(N, S))
# two panes, each of which would get widgets gridded into it:
f1 = ttk.Labelframe(p, text='Pane1', width=100, height=100)
f2 = ttk.Labelframe(p, text='Pane2', width=100, height=100)

# also works with buttons
# note we overwrite f1, f2, so label frames never get drawn
f1 = ttk.Button(p, text="Button1")
f2 = ttk.Button(p, text="Button2")


# p.insert(2, f2) # if the pane is already a child it will be moved
# p.forget(f2)

p.add(f1)
p.add(f2)

root.rowconfigure(0, weight=1)
root.mainloop()