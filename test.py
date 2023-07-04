from tkinter import ttk
from tkinter import *

# Создание окна
window = Tk()

# Создание Treeview
tree = ttk.Treeview(window)
tree.pack()

# Создание изображений
image1 = PhotoImage(file="photo/error.png")
image2 = PhotoImage(file="photo/ipad.jpg")

# Добавление элементов в Treeview с изображениями
item1 = tree.insert("", "end", text="Элемент 1", image=image1)
item2 = tree.insert("", "end", text="Элемент 2", image=image2)

# Отображение окна
window.mainloop()
