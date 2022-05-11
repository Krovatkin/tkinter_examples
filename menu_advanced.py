from re import sub
from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()

# otherwise menus will look super weird
# and can be detached
root.option_add('*tearOff', FALSE)
menubar = Menu(root) # can also be created for TopLevel
root['menu'] = menubar

def newFile():
    print("New File")

def openFile():
    print("Open File")

menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menu_radio = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')
menubar.add_cascade(menu=menu_radio, label='Radio')

submenu = Menu(menu_edit)
menu_edit.add_cascade(menu=submenu, label='Submenu')
submenu.add_command(label='Item1')

"""
Mac
"""

# Tk will add the standard items (preferences and onward)
# onto the end of any items you have added
# appmenu = Menu(menubar, name='apple')
"If no help menu needed don't add menu with the name=help"
# root.createcommand('tk::mac::ShowPreferences', showMyPreferencesDialog)
# helpmenu = Menu(menubar, name='help')
# menubar.add_cascade(menu=helpmenu, label='Help')
# root.createcommand('tk::mac::ShowHelp', ...)
"Other Mac commands"
# https://tcl.tk/man/tcl8.6/TkCmd/tk_mac.htm

"""
Windows
"""

# "Close", "Minimize". if you create a system menu, you can add
# new items that will appear below the standard items.
sysmenu = Menu(menubar, name='system')
menubar.add_cascade(menu=sysmenu)
sysmenu.add_command(label='Not Much')

image = PhotoImage(file='telegram.png')
menu_file.add_command(label='New', compound='left', image=image, command=newFile, accelerator="Ctrl+N", underline=2) # underline is 0-based
menu_file.add_separator()
menu_file.add_command(label='Open...', command=openFile)
menu_file.add_command(label='Close', command=lambda : None)

# note focus_get()
menu_edit.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))


check = StringVar()
menu_radio.add_checkbutton(label='Check', variable=check, onvalue=1, offvalue=0)
radio = StringVar()
menu_radio.add_radiobutton(label='One', variable=radio, value=1)
menu_radio.add_radiobutton(label='Two', variable=radio, value=2)

print(menu_file.entrycget(0, 'label')) # get label of top entry in menu
print(menu_file.entryconfigure(0)) # show all options for an item

menu_file.entryconfigure('Close', state='disabled')

menu_file.entryconfigure(2, label="Open!!!")

root.bind("<Control-n>", newFile)



# figure out which platform we are running
print(root.tk.call('tk', 'windowingsystem')) # returns x11, win32 or aqua
root.mainloop()

"""
https://www.tcl.tk/man/tcl/TkCmd/event.html
PREDEFINED VIRTUAL EVENTS
<<AltUnderlined>>
<<Invoke>>
<<ListboxSelect>>
<<MenuSelect>>
<<Modified>>
<<Selection>>
<<ThemeChanged>>
<<TraverseIn>>
<<TraverseOut>>
<<UndoStack>>
<<WidgetViewSync>>
<<Clear>>
<<Copy>>
<<Cut>>
<<LineEnd>>
<<LineStart>>
<<NextChar>>
<<NextLine>>
<<NextPara>>
<<NextWord>>
<<Paste>>
<<PasteSelection>>
<<PrevChar>>
<<PrevLine>>
<<PrevPara>>
<<PrevWindow>>
<<PrevWord>>
<<Redo>>
<<SelectAll>>
<<SelectLineEnd>>
<<SelectLineStart>>
<<SelectNextChar>>
<<SelectNextLine>>
<<SelectNextPara>>
<<SelectNextWord>>
<<SelectNone>>
<<SelectPrevChar>>
<<SelectPrevLine>>
<<SelectPrevPara>>
<<SelectPrevWord>>
<<ToggleSelection>>
<<Undo>>
"""