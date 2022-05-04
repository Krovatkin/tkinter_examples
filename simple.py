import tkinter as tk
from tkinter import Label
from tkinter import Entry
app = tk.Tk()


frame = tk.Frame(
    master=app,
    relief=tk.RAISED,
    borderwidth=1
)

frame.pack()

_url_label = Label(frame, text="URL:")
_url_label.grid(column=0, row=0)
_url_field = Entry(frame, width=100)
_url_field.grid(column=0, row=1)
#_url_field['value'] = "Rara"
_url_field.insert(0, "Python")
app.mainloop()