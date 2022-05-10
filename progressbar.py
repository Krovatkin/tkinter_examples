from tkinter import *
from tkinter import ttk # new themed widgets
root = Tk()
pval = StringVar()
# this sets progress in percentages
pval.set(50)
# The length represents the width of a horizontal progress bar or the height of a vertical progressbar
p = ttk.Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate', variable=pval).grid()
root.mainloop()