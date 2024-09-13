def first_digit(number):
    # Преобразуем число в строку и удаляем возможный знак "-"
    num_str = str(abs(number))
    # Возвращаем первую цифру
    return num_str[0]

# Ввод числа
try:
    number = int(input("Введите число: "))
    result = first_digit(number)
    print("Первая цифра числа:", result)
except ValueError:
    print("Пожалуйста, введите корректное целое число.")
