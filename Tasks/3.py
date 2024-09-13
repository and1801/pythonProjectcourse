def arithmetic(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Деление на ноль невозможно"
    else:
        return "Неизвестная операция"

# Запрос данных у пользователя
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /): ")

    # Вывод результата
    result = arithmetic(a, b, operation)
    print(f"Результат: {result}")
except ValueError:
    print("Ошибка ввода: пожалуйста, введите корректные числа.")