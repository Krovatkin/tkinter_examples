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




root.mainloop()