# Запрос курса и суммы у пользователя
exchange_rate = float(input('Введите курс валюты (например, курс доллара): '))
amount = float(input('Введите сумму в рублях: '))

# Конвертация валюты
converted_amount = amount / exchange_rate

# Вывод результата
print(f'Эквивалент в другой валюте: {converted_amount:.2f}')
