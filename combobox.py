from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()

countryvar = StringVar()
country = ttk.Combobox(root, textvariable=countryvar)
country.grid()
country['values'] = ('USA', 'Canada', 'Australia')
def onselect(*args):
    print(f"{args}")
    print(f"country = {country.get()}")
    cur_index = country.current()
    cur_value = country.get()
    print(f"{cur_index}")
    print(f"{cur_value}")
    # country.set("new_value")


country.bind('<<ComboboxSelected>>', onselect)
# country.state(["readonly"]) we can make the widget readonly in addition to disabling it
# when the value changes in readonly mode call `selection_clear`
root.mainloop()