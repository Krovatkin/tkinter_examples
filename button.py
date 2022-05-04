from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()

def show_message():
    messagebox.showinfo("Title", "Message")

resultsContents = StringVar()
# text='Full.name:'
"""
use the compound configuration
option. The default value is none, meaning display only the image if present;
if there is no image, display the text specified by the text or textvariable
options. Other possible values for the compound option are: text (text only),
image (image only), center (text in the center of image), top (image above
text), left, bottom, and right.
"""
label = ttk.Button(root, compound='left', command=show_message) 
label['textvariable'] = resultsContents
resultsContents.set('New value to display')
image = PhotoImage(file='telegram.png')
label['image'] = image
label.grid()
root.mainloop()