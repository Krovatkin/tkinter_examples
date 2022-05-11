from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()

root.after(5000, lambda: print("After 5s")) # this doesn't block timers after it
root.after(3000, lambda: print("After 3s")) # in other words, timers are concurrent
root.after(1000, lambda: print("After 1s")) # as long as they don't block the event loop
root.mainloop()