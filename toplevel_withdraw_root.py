from tkinter import *
from tkinter import ttk # new themed widgets
root = Tk()
t = Toplevel(root)
# this hides root
root.withdraw()
def close():
    print("Closing a window!")
    root.destroy()

# the default close button on `Toplevel`
# would still keep `root` running
t.protocol("WM_DELETE_WINDOW", close)
root.mainloop()