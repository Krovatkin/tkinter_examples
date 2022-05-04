from tkinter import *
from tkinter import ttk # new themed widgets
root = Tk()
resultsContents = StringVar()
# text='Full.name:'
"""
use the compound configuration
option. The default value is none, meaning display only the image if present;
if there is no image, display the text specified by the text or textvariable
options. Other possible values for the compound option are: text (text only),
image (image only), center (text in the center of image), top (image above
text), left, bottom, and right.
"""
label = ttk.Label(root, compound='left') 
label['textvariable'] = resultsContents
resultsContents.set('New value to display')
image = PhotoImage(file='telegram.png')
label['image'] = image
label.grid()
root.mainloop()

# TkDefaultFont
# TkTextFont
# TkFixedFont
# TkMenuFont
# TkHeadingFont
# TkCaptionFont
# TkSmallCaptionFont
# TkIconFont
# TkTooltipFont
