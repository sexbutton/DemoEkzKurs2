import tkinter as tk
from tkinter import ttk

def apply_discount(item):
    old_price = tree.set(item, "price")
    discount = tree.set(item, "discount")
    if discount:
        new_price = float(old_price) * (1 - float(discount))
        tree.set(item, "tags", ("discounted",))
        tree.set(item, "text", f"{old_price} -> {new_price:.2f}")
    else:
        tree.set(item, "tags", ())
        tree.set(item, "text", old_price)

root = tk.Tk()

tree = ttk.Treeview(root)
tree["columns"] = ("price", "discount")
tree.pack()

tree.heading("#0", text="Item")
tree.heading("price", text="Price")
tree.heading("discount", text="Discount")

item1 = tree.insert("", "end", text="Product 1", values=("100.00", "0.10"))
item2 = tree.insert("", "end", text="Product 2", values=("50.00", ""))
item3 = tree.insert("", "end", text="Product 3", values=("80.00", "0.20"))

tree.tag_configure("discounted", font=("Arial", 12, "overstrike"))

tree.bind("<<TreeviewSelect>>", lambda event: apply_discount(tree.selection()[0]))

root.mainloop()
