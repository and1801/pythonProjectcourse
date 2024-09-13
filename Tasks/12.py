def calculate(a, b):
    product = a * b
    sum_ab = a + b
    if sum_ab >= 1000:
        return product
    else:
        return sum_ab

# Ввод чисел
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = calculate(a, b)
    print("Результат:", result)
except ValueError:
    print("Пожалуйста, введите корректные числовые значения.")
