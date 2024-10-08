def is_even_digit_string(s):
    # Проверяем, что все символы в строке являются четными цифрами
    return all(c in '02468' for c in s)

# Ввод строки
s = input("Введите строку: ")

# Проверка и вывод результата
if is_even_digit_string(s):
    print("Строка состоит только из четных цифр.")
else:
    print("Строка содержит нечетные цифры или недопустимые символы.")
