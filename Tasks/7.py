def bank_deposit(a, years):
    for i in range(years):
        a += a * 0.10  # Увеличиваем вклад на 10% ежегодно
    return round(a, 2)  # Округляем до двух знаков после запятой

# Пример использования
initial_amount = float(input("Введите сумму вклада (в рублях): "))
years = int(input("Введите срок вклада (в годах): "))

final_amount = bank_deposit(initial_amount, years)
print(f"Сумма вклада через {years} лет: {final_amount} руб.")
