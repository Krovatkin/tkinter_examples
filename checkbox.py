from tkinter import *
from tkinter import ttk # new themed widgets
root = Tk()
def metricChanged():
    print(f"metricChanged {measureSystem.get()}")


measureSystem = StringVar()
print(f"measureSystem = {measureSystem}")
def on_field_change(index, value, op):
    print(f"combobox updated to {index} {value} {op}") # value is empty for some reason
    print(f"measureSystem.get()={measureSystem.get()}")
measureSystem.trace('w', on_field_change)

check = ttk.Checkbutton(root, text='Use.Metric', command=metricChanged, variable=measureSystem, onvalue='metric', offvalue='imperial')
check.state(['alternate']) # enable unknown state
print(f"{measureSystem}=")
check.grid()
root.mainloop()