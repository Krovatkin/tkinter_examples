from tkinter import *
from tkinter import ttk
from tkinter import messagebox # new themed widgets
root = Tk()

t = Text(root, width=40, height=10, wrap=WORD) # WORD, "none"
# foreground, background, padx, borderwidth, relief

# txt['state'] = 'disabled'
ys = ttk.Scrollbar(root, orient = 'vertical', command = t.yview)
xs = ttk.Scrollbar(root, orient = 'horizontal', command = t.xview)
t['yscrollcommand'] = ys.set
t['xscrollcommand'] = xs.set

t.grid(column = 0, row = 0, sticky = 'nwes')
xs.grid(column = 0, row = 1, sticky = 'we')
ys.grid(column = 1, row = 0, sticky = 'ns')
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)

# use `t.see` to make sure that a given line is visible.
t.see('1.0')

t.bind("<Double-1>", lambda e: print(t.get('1.0', 'end')))

# the text is inserted before the given index
t.insert("3.0", "abcd\nnefgh") # 'start' , 'end' are valid
print(t.get('1.0', 'end'))

t.index('end') # determine a canonical position


# each cmd starts with the initial text:  "abcd\nnefgh"
t.delete('1.2') # "abd\nefgh"
t.delete('1.1', '1.2') # "acd\nefgh"
t.delete('1.0', '2.0') # "efgh"
t.delete('1.2', '2.1') # "abfgh"

t.replace('1.1', '1.2', "Rara!")

"""
With long lines and wrapping enabled, one logical
line may represent multiple display lines. 
you can specify this as, e.g., `1.0 + 2 display lines`
"""

# Valid operators are ==, !=, <, <=, >, and >=
print(t.compare('end', "==", 'end'))

# !!!! Tags !!!!

t.tag_add('highlightline', '1.0', '1.5')
t.tag_configure('highlightline', background='yellow', font='TkFixedFont', relief='raised')
# tag formatting options:
"""
background, bgstipple, borderwidth, elide, fgstipple, font, foreground, justify, lmargin1, 
lmargin2, offset, overstrike, relief, rmargin, spacing1, spacing2, spacing3, tabs, 
tabstyle, underline, and wrap
"""

print(t.tag_cget("highlightline", "background"))
t.tag_delete('tag1', 'tag2')
# keeps the tag for chars outside the remove range
t.tag_remove('highlightline', '1.0', '1.2')
print(t.tag_ranges('highlightline')) # (<string object: '1.2'>, <string object: '1.5'>)
print(t.tag_nextrange('highlightline', '1.3', '1.5'))
print(t.tag_names()) # returns list of tags

# elide hides the text
#t.tag_configure('highlightline', elide=True)

# tagname.first or tagname.last can be used in lieu indices
t.tag_bind('highlightline', '<1>', lambda x: messagebox.showinfo("Hi", f"Clicked on {x}"))
t.bind('<<Modified>>', lambda x: print(f"Modified {x}")) # doesn't seem to work very well


# Text Selection

def show_sel_ranges(x):
    r = t.tag_ranges('sel')
    print(f"selection = {r[0]} {r[1]}")

t.tag_add('sel', '1.0', '1.2') # this doesn't seem to visually highlight text?
t.bind('<<Selection>>', show_sel_ranges)

# !!! Marks
# marks are always in between chars
# default marks: current, insert

t.mark_set('mark1', '1.1')

# marks can be used as indices

mark_name = t.mark_next('1.0')
print(mark_name)
t.mark_gravity('mark1', 'left') # which way the mark moves after insertion
t.mark_unset('mark1', '1.1')

# !!!! Images, Widgets

# setting w/h doesn't resize the image, but just cuts it off at those values
flowers = PhotoImage(file='telegram.png', width=30, height=30)
t.image_create('end', image=flowers)

b = ttk.Button(t, text='Push.Me')
t.window_create('1.0', window=b)

# !!! Search, Modifications, Undo, Redo

print(t.search('ara', '1.0'))
print(f"edit_modified = {t.edit_modified()}")
print(t.edit_undo()) # t.edit_redo()

# !!! Introspection 

print(f"debug={t.debug(True)}")
print(f"dlineinfo = {t.dlineinfo('1.0')}") # gives the bounding box for a char

# Valid counting options are "chars", "displaychars", "displayindices", 
# "displaylines", "indices", "lines", "xpixels" and "ypixels"
print(f"bbox= {t.bbox('1.0')} count={t.count('1.0', '1.2', 'displaychars')}")
# 'all', 'image', 'mark', 'tag', 'text', or 'window'
print(f"dump={t.dump('1.0', '1.2', 'text')}")
root.mainloop()




"""
The Tk text widget allows the same underlying text data structure 
(containing all the text, marks, tags, images, etc.) to be shared 
between two or more different text widgets. This is known as peering 
"""

"""

1 0 + 3 chars: Three characters past the start of line 1
2 end -1 chars: The last character before the new line in line 2
end -1 chars: The newline that Tk always adds at the end of the text
end -2 chars: The actual last character of the text
end -1 lines: The start of the last actual line of text
2 2 + 2 lines: The third character (index 2) of the fourth line of text
2 5 linestart: The first character of line 2
2 5 lineend: The position of the newline at the end of line 2
2 5 wordstart: First char  of the word with the char  at index 2 5
2 5 wordend: First char  after the word with the char  at index 2 5

The term can be abbreviated as `c` and `l`.
"""