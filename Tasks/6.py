def season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Некорректный номер месяца"

# Пример использования
month = int(input("Введите номер месяца (от 1 до 12): "))
print(f"Время года: {season(month)}")
