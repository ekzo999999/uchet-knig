# app_v1.py — Учёт книг (GUI версия 1)
# Регрессионное тестирование: базовая версия без возврата

from tkinter import *
from tkinter import ttk

# Переменная для хранения количества выданных книг
vyidano = 0

def accept_book():
    global vyidano
    vyidano = vyidano + 1
    label_count["text"] = vyidano

def show_count():
    # В GUI счётчик и так всегда виден на экране, 
    # но мы можем добавить всплывающее окно или просто обновить статус
    label_info["text"] = "Текущее состояние: " + str(vyidano) + " книг выдано"

def reset():
    global vyidano
    vyidano = 0
    label_count["text"] = vyidano
    label_info["text"] = "Счётчик сброшен"

def exit_app():
    window.destroy()

# Создание главного окна
window = Tk()
window.title("Учёт книг (v1)")
window.geometry("350x300")

label_title = Label(text="Выдано книг:", font=("Arial", 14))
label_title.pack(pady=10)

label_count = Label(text="0", font=("Arial", 24, "bold"), fg="blue")
label_count.pack(pady=10)

# Кнопки управления
btn_accept = ttk.Button(text="1. Выдать книгу", command=accept_book)
btn_accept.pack(pady=5)

btn_show = ttk.Button(text="2. Показать счётчик", command=show_count)
btn_show.pack(pady=5)

btn_reset = ttk.Button(text="3. Сбросить счётчик", command=reset)
btn_reset.pack(pady=5)

btn_exit = ttk.Button(text="0. Выход", command=exit_app)
btn_exit.pack(pady=5)

# Метка для вывода текста (вместо консоли)
label_info = Label(text="Готово к работе", fg="gray")
label_info.pack(pady=10)

window.mainloop()