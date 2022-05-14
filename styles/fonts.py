from tkinter import font, Label
from tkinter import ttk
import tkinter as tk
root = tk.Tk()

print(font.names())

f = font.nametofont('TkTextFont')
print(type(f).__name__)
print(type(f.actual()).__name__)
print(f.actual())

# Tk ensures the names: Courier, Times, and Helvetica are available
highlightFont = font.Font(family='Helvetica', name='appHighlightFont', size=12, weight='bold')
ttk.Label(root, text='Attention!', font=highlightFont).grid()
print(font.families())
root.mainloop()
"""
https://tcl.tk/man/tcl8.6/TkCmd/font.htm

STANDARD FONTS
    TkDefaultFont
    TkTextFont
    TkFixedFont
    TkMenuFont
    TkHeadingFont
    TkCaptionFont
    TkSmallCaptionFont
    TkIconFont
    TkTooltipFont
"""