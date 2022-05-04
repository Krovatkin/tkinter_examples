from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()
mainframe = ttk.Frame(root, padding="3 3 3 3") # left top right bottom
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1) # strech as the main window resizes
root.rowconfigure(0, weight=1)    # strech as the main window resizes


def calculate():
    feet.set("Yay!")
    meters.set("Woah!")

def toast(e):
    messagebox.showinfo("Title", "Header")

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=10, textvariable=feet)
feet_entry.grid(column=0, row=0, sticky=(W, E))
feet_entry.focus()


meters = StringVar()
meters.set("Initial value!")
lbl = ttk.Label(mainframe, textvariable=meters, text="Wot")
lbl.grid(column=0, row=1, sticky=(W, E))
btn = ttk.Button(mainframe, text="Calculate", command=calculate)
btn.grid(column=0, row=2, sticky=W)

#btn['text'] = 'goodbye'
#btn.configure(text='goodbye')
print(btn.configure())

for child in mainframe.winfo_children(): 
    # https://tcl.tk/man/tcl8.6/TkCmd/winfo.htm
    child.grid_configure(pady=5)


#lbl.bind("<Double-Button-1>", toast)
lbl.bind("<Control-Double-Button-1>", toast)

mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

print(btn) # .!frame.!button

root.bind("<Return>", calculate)
root.mainloop()