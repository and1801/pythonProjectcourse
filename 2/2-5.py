def compress_string(s):
    if not s:  # Если строка пуста, возвращаем пустую строку
        return ""

    compressed = []  # Список для хранения сжатой версии строки
    count = 1  # Счетчик повторяющихся символов

    # Проходим по строке, начиная со второго символа
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  # Если символ совпадает с предыдущим
            count += 1
        else:
            # Добавляем предыдущий символ и его количество к результату
            compressed.append(s[i - 1] + str(count))
            count = 1  # Сбрасываем счетчик

    # Не забываем добавить последний символ и его количество
    compressed.append(s[-1] + str(count))

    return ''.join(compressed)  # Объединяем список в строку

# Пример использования
input_string = "aabcccccaaa"
result = compress_string(input_string)
print(f"Сжатая строка: {result}")