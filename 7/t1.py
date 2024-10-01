def safe_divide():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        result = a / b
        print(f"Результат деления: {result}")
    except ZeroDivisionError:
        return None
    except ValueError:
        print("Ошибка: Пожалуйста, введите числовые значения.")

print(safe_divide())