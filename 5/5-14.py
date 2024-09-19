sum_of_numbers = 0

while True:
    user_input = input("Введите число (или 'q' для выхода): ")

    if user_input.lower() == 'q':
        break

    try:
        number = float(user_input)
    except ValueError:
        print("Пожалуйста, введите действительное число.")
        continue

    if number < 0:
        print("Отрицательные числа игнорируются.")
        continue

    sum_of_numbers += number

print(f"Сумма введенных положительных чисел: {sum_of_numbers}")
if number == 0:
    pass
