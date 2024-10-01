def divide_numbers():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        result = a / b
        print(f"Результат деления: {result}")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль невозможно.")
    except ValueError:
        print("Ошибка: Пожалуйста, введите числовые значения.")


# Запуск функции
divide_numbers()