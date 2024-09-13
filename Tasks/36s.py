import tkinter as tk

# Функции для обработки нажатий кнопок
def click(button_text):
    current_text = str(entry.get())
    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Создаем основное окно
root = tk.Tk()
root.title("Калькулятор")

# Создаем текстовое поле для отображения ввода и результата
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Создаем кнопки калькулятора
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_value = 1
col_value = 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
              command=lambda b=button: click(b)).grid(row=row_value, column=col_value)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Запуск главного цикла приложения
root.mainloop()
