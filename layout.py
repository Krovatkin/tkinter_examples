from tkinter import *
from tkinter import ttk
root = Tk()
content = ttk.Frame(root, padding=(3, 3, 12, 12))
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
l00 = ttk.Label(content, anchor="ne", text="This is a cell 00", background="yellow")
l10 = ttk.Label(content, anchor="sw", text="This is a cell 10", background="red")
l01_11 = ttk.Label(content, anchor="center", text="This is a cell 01_11", background="blue")
l20_21_22 = ttk.Label(content, text="This is a cell 20_21_22", background="orange")
l00.grid(column=0, row=0, sticky=(N, S, E, W))
l10.grid(column=0, row=1, sticky=(N, S, E, W))
l01_11.grid(column=1, row=0, rowspan=2, columnspan=2, sticky=(E, W))
l20_21_22.grid(column=0, row=2, columnspan=3, sticky=(N, S))

content.grid(column=0, row=0, sticky=(N, S, E, W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)


for w in content.grid_slaves(): print(w) # row=, col=
print(content.grid_info())
#content.grid_configure(sticky=(E,W))

"""
l01_11.grid_remove() # removes the widget from the grid, but remembers the options
l20_21_22.forget() # removes the widget from the grid
"""
root.mainloop()