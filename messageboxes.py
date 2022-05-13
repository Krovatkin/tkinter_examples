from tkinter import Tk, Toplevel
from tkinter import ttk
from tkinter import messagebox
root = Tk()
messagebox.showinfo(message='Have a good day')
answer = messagebox.askyesno(message='Are you sure you want to install SuperVirus?', icon='question', title='Install')
print(answer) # False, True

def dismiss ():
    dlg.grab_release()
    dlg.destroy()


dlg = Toplevel(root)
ttk.Button(dlg, text="Done", command=dismiss).grid()
dlg.protocol("WM_DELETE_WINDOW", dismiss) # intercept close button
dlg.transient(root)
# dialog window is related to main
dlg.wait_visibility() # can't grab until window appears, so we wait
dlg.grab_set()
# ensure all input goes to our window
dlg.wait_window()
# block until window is destroyed

"""
https://docs.python.org/3/library/tkinter.messagebox.html

Information message box
tkinter.messagebox.showinfo(title=None, message=None, **options)

Warning message boxes
tkinter.messagebox.showwarning(title=None, message=None, **options)
tkinter.messagebox.showerror(title=None, message=None, **options)

Question message boxes
tkinter.messagebox.askquestion(title=None, message=None, **options)
tkinter.messagebox.askokcancel(title=None, message=None, **options)
tkinter.messagebox.askretrycancel(title=None, message=None, **options)
tkinter.messagebox.askyesno(title=None, message=None, **options)
tkinter.messagebox.askyesnocancel(title=None, message=None, **options)
"""

# https://tcl.tk/man/tcl8.6/TkCmd/messageBox.htm

root.mainloop()
