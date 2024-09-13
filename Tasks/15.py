def second_last_char(s):
    # Проверяем, что строка содержит более одного символа
    if len(s) > 1:
        # Возвращаем предпоследний символ
        return s[-2]
    else:
        return "Строка слишком короткая."

# Ввод строки
s = input("Введите строку: ")
result = second_last_char(s)
print("Предпоследний символ строки:", result)
