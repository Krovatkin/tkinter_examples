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

# tagname.first or tagname.last can be used in lieu indices
root.mainloop()

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