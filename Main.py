import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os
from DataBase import rows

# Массив кортежей из БД
data = rows

# Функция для проверки наличия файла по указанному пути
def check_image_path(image_path):
    if os.path.isfile(image_path):
        return image_path
    else:
        # Установка альтернативного пути к изображению
        return "photo/error.png"

def sort_products(event):
    selected_sort = dropdown.get()

    if selected_sort == "Все диапазоны":
        tree.delete(*tree.get_children())

        arr = data

        for item in arr:
            photo = tk.PhotoImage(item[3])
            tree.insert("", tk.END, open=True, image=photo, text="", values=item)
        for i in tree.get_children(""):
            if tree.item(i)["values"][6] != "None" and float(tree.item(i)["values"][6]) >= 15:
                tree.item(i, tags=("#7fff00",))
                tree.tag_configure("#7fff00", background="#7fff00")
        
        myvar2.set("Количество всей продукции: " + str(len(arr)))

    if selected_sort == "0 - 9.99%":
        tree.delete(*tree.get_children())
        
        count = 0
        arr = data

        for item in arr:
            if item[6] is not None and 0 <= item[6] <= 9.99:
                photo = tk.PhotoImage(item[3])
                tree.insert("", tk.END, open=True, image=photo, text="", values=item)
                count += 1
        for i in tree.get_children(""):
            if tree.item(i)["values"][6] != "None" and float(tree.item(i)["values"][6]) >= 15:
                tree.item(i, tags=("#7fff00",))
                tree.tag_configure("#7fff00", background="#7fff00")
        
        myvar2.set("Количество всей продукции: " + str(count))

    if selected_sort == "10 - 14.99%":
        tree.delete(*tree.get_children())

        arr = data
        count = 0

        for item in arr:
            if item[6] is not None and 10 <= item[6] <= 14.99:
                photo = tk.PhotoImage(item[3])
                tree.insert("", tk.END, open=True, image=photo, text="", values=item)
                count += 1
        for i in tree.get_children(""):
            if tree.item(i)["values"][6] != "None" and float(tree.item(i)["values"][6]) >= 15:
                tree.item(i, tags=("#7fff00",))
                tree.tag_configure("#7fff00", background="#7fff00")
        
        myvar2.set("Количество всей продукции: " + str(count))

    if selected_sort == "15 и более":
        tree.delete(*tree.get_children())

        arr = data
        count = 0

        for item in arr:
            if item[6] is not None and item[6] >= 15:
                photo = tk.PhotoImage(item[3])
                tree.insert("", tk.END, open=True, image=photo, text="", values=item)
                count += 1
        for i in tree.get_children(""):
            if tree.item(i)["values"][6] != "None" and float(tree.item(i)["values"][6]) >= 15:
                tree.item(i, tags=("#7fff00",))
                tree.tag_configure("#7fff00", background="#7fff00")
        
        myvar2.set("Количество всей продукции: " + str(count))

def treeview_sort_column(treeview, column, reverse=False):
    # Получаем все элементы Treeview
    elements = [(treeview.set(item, column), item) for item in treeview.get_children()]

    # Сортируем элементы по значению столбца
    elements.sort(reverse=reverse)

    # Перемещаем элементы в отсортированном порядке
    for index, (_, item) in enumerate(elements):
        treeview.move(item, "", index)

def sort_price(event):
    sort = dropdown2.get()

    if sort == "По возрастанию":
        treeview_sort_column(tree, "Цена", reverse=False)

    if sort == "По убыванию":
        treeview_sort_column(tree, "Цена", reverse=True)

# Создание окна приложения
window = tk.Tk()

# Создаем выпадающий список
dropdown = ttk.Combobox(window, values=["Все диапазоны", "0 - 9.99%", "10 - 14.99%", "15 и более"])
dropdown.set("Все диапазоны")
dropdown.pack()

# Отображение количества всей продукции
myvar = tk.StringVar()
label = tk.Label(window, textvariable=myvar)
myvar.set("Количество всей продукции: " + str(len(data)))
label.pack()

# Отображение количества продукции по текущему фильтру
myvar2 = tk.StringVar()
label2 = tk.Label(window, textvariable=myvar2)
label2.pack()

dropdown2 = ttk.Combobox(window, values=["По возрастанию", "По убыванию"])
dropdown2.pack()

# Назначаем обработчик события выбора элемента
dropdown.bind("<<ComboboxSelected>>", sort_products)

# Назначаем обработчик события выбора элемента
dropdown2.bind("<<ComboboxSelected>>", sort_price)

# Создание виджета Treeview
tree = ttk.Treeview(window)

# Добавление столбцов к Treeview
tree["columns"] = ("ID", "Название", "Описание", "Фото", "Цена", "Производитель", "Налог", "Цена по скидке")

# Настройка заголовков столбцов
tree.heading("#0", text="")
tree.heading("ID", text="ID")
tree.heading("Название", text="Название")
tree.heading("Описание", text="Описание")
tree.heading("Фото", text="Фото")
tree.heading("Цена", text="Цена")
tree.heading("Производитель", text="Производитель")
tree.heading("Налог", text="Скидка")
tree.heading("Цена по скидке", text="Цена по скидке")


# Добавление данных в Treeview
for item in data:
    photo = tk.PhotoImage(item[3])
    print(type(photo))
    tree.insert("", tk.END, open=True, image=photo, text="", values=item)

for i in tree.get_children(""):
    if tree.item(i)["values"][6] != "None" and float(tree.item(i)["values"][6]) >= 15:
        tree.item(i, tags=("#7fff00",))
        tree.tag_configure("#7fff00", background="#7fff00")
    
    if tree.item(i)["values"][6] != "None" and float(tree.item(i)["values"][6]) > 0:
        pass

myvar2.set("Количество всей продукции: " + str(len(data)))

# Установка стиля вывода данных в виде таблицы
tree["show"] = "headings"

# Отображение Treeview на окне
tree.pack()

# Запуск основного цикла обработки событий
window.mainloop()