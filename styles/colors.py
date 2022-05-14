from tkinter import font, Label
from tkinter import ttk
import tkinter as tk
root = tk.Tk()

# https://www.tcl.tk/man/tcl/TkCmd/colors.html
ttk.Label(root, text='Attention!', foreground='#00ff00', background='red').grid()
print(root.winfo_rgb('red'))
root.mainloop()