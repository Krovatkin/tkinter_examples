from tkinter import PhotoImage
from tkinter import ttk
import tkinter as tk
root = tk.Tk()
from PIL import ImageTk, Image
myimg = ImageTk.PhotoImage(Image.open('cat.jpg'))

# tcl 8.6 only supports gif, pngs
# imgobj = PhotoImage(file='cat.jpg')
# use Pillow for more formats
# pip install Pillow
ttk.Label(root, text='Attention!', image=myimg, compound="left").grid()
print(root.winfo_rgb('red'))
root.mainloop()