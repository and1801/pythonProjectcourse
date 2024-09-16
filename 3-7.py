import requests


# Функция для получения актуального курса валют
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if target_currency in data['rates']:
        return data['rates'][target_currency]
    else:
        print("Ошибка: Валюта не найдена.")
        return None


# Функция конвертации валют
def currency_converter():
    base_currency = input("Введите код валюты, из которой вы хотите конвертировать (например, USD): ").upper()
    target_currency = input("Введите код валюты, в которую вы хотите конвертировать (например, EUR): ").upper()
    amount = float(input(f"Введите сумму в {base_currency}: "))

    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate:
        converted_amount = amount * exchange_rate
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Не удалось получить курс валют.")


# Запуск программы
currency_converter()
