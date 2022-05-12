from tkinter import *
from tkinter import ttk # new themed widgets
root = Tk()
t = Toplevel(root) # screen= to draw a window in

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

"""
!!! Screen Information
"""

print("color.depth=" + str(root.winfo_screendepth())+ " (" + root.winfo_screenvisual() + ")")
print("pixels.per.inch=" + str(root.winfo_pixels('1i')))
print("width=", str(root.winfo_screenwidth()) + ".height=", str(root.winfo_screenheight()))

# how big the entire display spanning multiple monitors
print(root.wm_maxsize())

# to determine which screen a window is on
print(root.winfo_screen())

# the default close button on `Toplevel`
# would still keep `root` running
t.protocol("WM_DELETE_WINDOW", close)
root.mainloop()

"""
If you ask for its position, it will be relative to the primary monitor. 
if you call `winfo_x` on a window positioned near the left edge of a monitor, 
it might return 100 if it’s on the primary monitor,
or -1820 if it’s on a monitor to the left of the primary
"""