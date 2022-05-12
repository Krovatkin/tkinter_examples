from tkinter import *
from tkinter import ttk # new themed widgets
root = Tk()
t = Toplevel(root)

# until a window is redrawn `print(t.geometry())`
# gives the old value 
# use `t.update_idletasks()` to update the geometry
t.geometry('300x200-5+40') # WxH+-X+-Y
t.resizable(TRUE,TRUE)
t.minsize(200,100) # WxH
t.maxsize(500,500) # WxH

#Wondering how large it would be if you didn’t specify its geometry,

print(t.winfo_reqwidth()) # or winfo_reqheight

"""
!!! Attributes !!!
"""

#https://wiki.tcl-lang.org/page/wm+attributes
t.attributes("-alpha", 0.5)
#t.attributes("-fullscreen", 1)
#-notify to bounce an icon in macOS dock
"the lower numbers are on top"
# t.attributes("-topmost", 1)

"""
!!! States !!!
"""
thestate = t.state()
print(thestate)
# t.state('normal')
# t.iconify() # minimizes into the start bar
# t.deiconify() # deminimize
# t.withdraw() # hide

# this hides root
root.withdraw()
def close():
    print("Closing a window!")
    root.destroy()

oldtitle = t.title()
print(oldtitle)
t.title('New.title')

def minimize(_):
    print("Minimize")
    t.iconify()

t.bind("<Button-1>", minimize)


"""
!!! Stack order !!!

t.lift() # raise to the top
t.lift(root) # raise over
t.lower()
t.lower(root)

print(root.tk.eval('wm stackorder '+str(t)+' isabove '+str(root)))
"""
print(root.tk.eval('wm stackorder '+str(root)))

# Stacking order applies for any sibling widgets

# the default close button on `Toplevel`
# would still keep `root` running
t.protocol("WM_DELETE_WINDOW", close)
root.mainloop()