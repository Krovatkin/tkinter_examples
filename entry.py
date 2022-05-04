from distutils import command
from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()
username = StringVar()

# Entry has no command=, but one can use trace
def onchange(*args):
    print(f"name.get()={name.get()}")
    print(f"{args}")
    print(f"username(StringVar)={username.get()}")
    # name.delete(0,'end')
    # name.insert(0, 'your.name') # insert new text

username.trace_add("write", onchange)

# validate='key' validate on any keystroke
# validate='all' all events include focusout and key
def validate_all(newval, op):
    if op == 'key':
        print("Validating a key")
    else: #elif op == 'focusout'
        print("Validating on {op}") 
    return True

# more % substitutions and op events
# https://www.pythontutorial.net/tkinter/tkinter-validation/
validate_all_args = (root.register(validate_all), '%P', '%V')

name = ttk.Entry(root, width=20, textvariable=username, validate='key', validatecommand=validate_all_args) # show="*" for pass
name.grid(column=0)

def make_readonly():
    name.state(['readonly'])    
    print(name.instate(['readonly']))

btn = ttk.Button(text='Set to ReadOnly', command=make_readonly)
btn.grid(row=1)
root.mainloop()