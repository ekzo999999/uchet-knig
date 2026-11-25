# app_v2.py — Учёт книг (GUI версия 2)
# Добавлена команда 4 — Вернуть книгу

from tkinter import *
from tkinter import ttk

vyidano = 0

def accept_book():
    global vyidano
    vyidano = vyidano + 1
    label_count["text"] = vyidano
    label_info["text"] = "Книга выдана."

def show_count():
    label_info["text"] = "Текущее состояние: " + str(vyidano) + " книг выдано"

def reset():
    global vyidano
    vyidano = 0
    label_count["text"] = vyidano
    label_info["text"] = "Счётчик сброшен"

def return_book():
    global vyidano
    if vyidano > 0:
        vyidano = vyidano - 1
        label_count["text"] = vyidano
        label_info["text"] = "Книга возвращена."
    else:
        # Если счётчик 0, выводим сообщение как требовалось
        label_info["text"] = "Нет выданных книг"

def exit_app():
    window.destroy()

window = Tk()
window.title("Учёт книг (v2)")
window.geometry("350x350")

label_title = Label(text="Выдано книг:", font=("Arial", 14))
label_title.pack(pady=10)

label_count = Label(text="0", font=("Arial", 24, "bold"), fg="blue")
label_count.pack(pady=10)

btn_accept = ttk.Button(text="1. Выдать книгу", command=accept_book)
btn_accept.pack(pady=5)

btn_show = ttk.Button(text="2. Показать счётчик", command=show_count)
btn_show.pack(pady=5)

btn_reset = ttk.Button(text="3. Сбросить счётчик", command=reset)
btn_reset.pack(pady=5)

# НОВАЯ КНОПКА (для v2)
btn_return = ttk.Button(text="4. Вернуть книгу", command=return_book)
btn_return.pack(pady=5)

btn_exit = ttk.Button(text="0. Выход", command=exit_app)
btn_exit.pack(pady=5)

label_info = Label(text="Готово к работе", fg="gray")
label_info.pack(pady=10)

window.mainloop()