from tkinter import *
from tkinter import ttk
root = Tk()

tree = ttk.Treeview(root, columns=('name', 'size'))
tree['columns'] = ('name', 'size', 'owner')

# anchor == alignment
tree.column('size', width=100, anchor='center')
tree.column('owner', anchor='center')
tree.column('name', anchor='e')
tree.heading('size', text='Size')
tree.heading('name', text='Name')
tree.heading('owner', text='Owner')



tree.grid()

# Inserted at the root, program chooses id:
tree.insert('', 'end', 'widgets', text='Widget.Tour')
# set the size property for `widgets` row
tree.set('widgets', 'size', '12KB')
size = tree.set('widgets', 'size')
# Same thing, but inserted as first child:
tree.insert('', 0, 'gallery', text='Applications')
# Treeview chooses the id:
id = tree.insert('', 'end', text='Tutorial')
# Inserted underneath an existing node:
tree.insert('widgets', 'end', text='Canvas')
tree.insert(id, 'end', text='Tree')
# move widgets under gallery
tree.move('widgets', 'gallery', 'end')

list_id = tree.insert('', 'end', text='Listbox', values=('Listbox', '777kb', 'John'))
print(list_id)



# removes from the tree
# can be reinserted with move
# tree.detach('widgets')

tree.item('gallery', open=TRUE)
isopen = tree.item('gallery', 'open')


# !!!! Appearance

"""
Like the text and canvas widgets, the treeview widget uses tags to modify
the appearance of items in the tree.
"""

def itemClicked(e):
    print(tree.focus())

tree.item('gallery', tags=("ttk",))
tree.insert('', 'end', text='button', tags=('ttk', 'simple'))
tree.tag_configure('ttk', background='yellow')
tree.tag_bind('ttk', '<1>', itemClicked)

# !!!! Virtual Events

tree.bind("<<TreeviewSelect>>", lambda x : print(f"TreeviewSelect={x}" + str(tree.selection())))
tree.bind("<<TreeviewOpen>>", lambda x : print(f"TreeviewOpen={x}"))
tree.bind("<<TreeviewClose>>", lambda x : print(f"TreeviewClose={x}"))

root.mainloop()