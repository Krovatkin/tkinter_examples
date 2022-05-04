from tkinter import *
from tkinter import ttk # new themed widgets
root = Tk()
mainframe = ttk.Frame(root, padding="3 3 12 12", relief="sunken") # left top right bottom
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1) # strech as the main window resizes
root.rowconfigure(0, weight=1)    # strech as the main window resizes
ttk.Button(mainframe, text="Hello.World").grid(column=0, row=0, sticky=(N, W, E))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
root.mainloop()