from tkinter import Tk
from tkinter import filedialog
from tkinter import colorchooser

root = Tk()
filename = filedialog.askopenfilename(filetypes=[("Images", ".gif .png")])
print(filename)
filename = filedialog.askopenfiles() # multiple filenames
print(filename)
color = colorchooser.askcolor(initialcolor='#ff0000')
print(color) # ((84.328125, 171.66796875, 142.5546875), '#54ab8e')

def font_changed(font):
    print(font) 

root.tk.call('tk', 'fontchooser', 'configure', '-font', 'helvetica␣24', '-command', root.register(font_changed))
root.tk.call('tk', 'fontchooser', 'show')
# root.tk.call('tk', 'fontchooser', 'hide')
'If the font dialog is closed, "<<TkFontchooserVisibility>>" is generated'
root.mainloop()




# options (all have default values):
#
# - defaultextension: added to filename if not explicitly given
#
# - filetypes: sequence of (label, pattern) tuples.  the same pattern
#   may occur with several patterns.  use "*" as pattern to indicate
#   all files.
#
# - initialdir: initial directory.  preserved by dialog instance.
#
# - initialfile: initial file (ignored by the open dialog).  preserved
#   by dialog instance.
#
# - parent: which window to place the dialog on top of
#
# - title: dialog title
#
# - multiple: if true user may select more than one file
#
# options for the directory chooser:
#
# - initialdir, parent, title: see above
#
# - mustexist: if true, user must pick an existing directory