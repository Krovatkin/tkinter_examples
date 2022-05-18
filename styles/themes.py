from tkinter import *
from tkinter import ttk # new themed widgets
root = Tk()
s = ttk.Style()
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
print(s.theme_names())
print(s.theme_use())
s.theme_use('winnative')

"""
https://sourceforge.net/projects/tcl-awthemes/. 
Download and unzip the awthemes-*.zip file somewhere. 
One of the files is named pkgIndex.tcl. 
This identifies it as a Tcl package, 
To use it, we need to tell Tcl where to find the package via `auto_path`
"""

#root.tk.call('lappend', 'auto_path', '/full/path/to/awthemes-9.3.1')
#root.tk.call('package', 'require', 'awdark') # awdark is theme's name

"If the theme is instead implemented as a single Tcl source file, without a pkgIndex.tcl"
#root.tk.call('source', '/full/path/to/themefile.tcl')


# !!!! Using themes

# Widget states: active, disabled, focus, 
# pressed, selected, background, readonly, alternate, and invalid.,

b = ttk.Button(root, text="Emergency")
b.grid()
print(b['style']) # ''
print(b.winfo_class()) # 'TButton'

# Prepending another name (Emergency) followed by a dot onto an existing
# style creates a new style derived from the existing one
s.configure('Emergency.TButton', font='helvetica.24', foreground='red', padding=10, anchor='e', highlightcolor='yellow')
b['style'] = 'Emergency.TButton'

# To see configure options, one needs to know which elements style's layout
# consists of and then query options for each element.
print(s.layout('TButton'))
print(s.element_options('Button.border'))
# option names are set on a STYLE and element's options inherit the style options
# if two elements use the same option name, they'll use the same value
print(s.lookup('Emergency.TButton', 'highlightcolor')) # yellow which we set via s.configure


# background, foreground and relief will be applied simultaneously
# relief has multiple state selectors e.g.
# 1. 'pressed', '!disabled'
# 2. 'pressed', 'disabled'
# the first one that matches button's states will be applied
s.map('TButton',
background=[('disabled','#d9d9d9'), ('active','#ececec')],
foreground=[('disabled','#a3a3a3')],
relief=[('pressed', '!disabled', 'sunken'), 
        ('pressed', 'disabled', 'flat')])

root.mainloop()
