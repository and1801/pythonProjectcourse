import tkinter as tk

# Конверсионные курсы
exchange_rates = {
    'USD': 1,
    'EUR': 0.85,
    'GBP': 0.75,
    'JPY': 110.0
}

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = combo_from.get()
    to_currency = combo_to.get()
    if from_currency != to_currency:
        converted_amount = amount * (exchange_rates[to_currency] / exchange_rates[from_currency])
    else:
        converted_amount = amount
    entry_result.delete(0, tk.END)
    entry_result.insert(tk.END, f"{converted_amount:.2f}")

# Создание основного окна
root = tk.Tk()
root.title("Конвертер валют")

# Ввод суммы
tk.Label(root, text="Сумма:").grid(row=0, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1)

# Выбор валют
tk.Label(root, text="Из валюты:").grid(row=1, column=0)
combo_from = tk.StringVar(root)
combo_from.set('USD')  # Значение по умолчанию
tk.OptionMenu(root, combo_from, *exchange_rates.keys()).grid(row=1, column=1)

tk.Label(root, text="В валюту:").grid(row=2, column=0)
combo_to = tk.StringVar(root)
combo_to.set('EUR')  # Значение по умолчанию
tk.OptionMenu(root, combo_to, *exchange_rates.keys()).grid(row=2, column=1)

# Кнопка для конвертации
tk.Button(root, text="Конвертировать", command=convert_currency).grid(row=3, column=0, columnspan=2)

# Результат
tk.Label(root, text="Результат:").grid(row=4, column=0)
entry_result = tk.Entry(root)
entry_result.grid(row=4, column=1)

# Запуск главного цикла приложения
root.mainloop()
