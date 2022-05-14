from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('300x200') # WxH+-X+-Y
n = ttk.Notebook(root)
n.grid(sticky=(N, W, S, E))
root.rowconfigure(index=0, weight=1)
root.columnconfigure(index=0, weight=1)
f1 = ttk.Frame(n)
f1.rowconfigure(index=0, weight=1)
f1.columnconfigure(index=0, weight=1)
f1.grid()
ttk.Label(f1, text='Page1', background='red').grid(sticky=(N, W, S, E))
f2 = ttk.Frame(n)
ttk.Label(f2, text='Page2', background='blue').grid(sticky=(N, W, S, E))
f2.rowconfigure(index=0, weight=1)
f2.columnconfigure(index=0, weight=1)
f2.grid()
n.add(f1, text='One')
n.add(f2, text='Two') # , state=['disabled']
n.select(1) # switch to the tab by index
n.select(n.select()) # switch to the sibwindow
print(n.select())
n.tab(0, text='OneOne')
n.bind("<<NotebookTabChanged>>", lambda args: print(F"Tab has changed {args}"))
root.mainloop()