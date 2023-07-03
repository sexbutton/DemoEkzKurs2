import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from DataBase import rows

def set_cell_font(tree, row, column, font):
    tree.tag_configure(f'font_{row}_{column}', font=font)
    tree.item(row, tags=(f'font_{row}_{column}',))

# Создаем стиль шрифта с перечеркиванием
font_with_strike = Font(name='font_with_strike')
font_with_strike.configure(overstrike=True)

# Создание окна приложения
window = tk.Tk()

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

# Массив кортежей из БД
data = rows

# Добавление данных в Treeview
for item in data:
    tree.insert("", tk.END, text="", values=item)

for i in tree.get_children(""):
    if tree.item(i)["values"][6] != "None" and float(tree.item(i)["values"][6]) >= 15:
        tree.item(i, tags=("#7fff00",))
        tree.tag_configure("#7fff00", background="#7fff00")
    
    if tree.item(i)["values"][6] != "None" and float(tree.item(i)["values"][6]) > 0:

    


# Установка стиля вывода данных в виде таблицы
tree["show"] = "headings"

# Отображение Treeview на окне
tree.pack()

# Запуск основного цикла обработки событий
window.mainloop()