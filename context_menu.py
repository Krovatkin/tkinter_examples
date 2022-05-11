from tkinter import *
root = Tk()
# otherwise menus will look super weird
# and can be detached
root.option_add('*tearOff', FALSE)
menu = Menu(root)
for i in ('One', 'Two', 'Three'):
    menu.add_command(label=i)

if (root.tk.call('tk', 'windowingsystem')=='aqua'): # macos
    root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
    root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
else:
        root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))
root.mainloop()