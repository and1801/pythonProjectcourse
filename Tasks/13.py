def longest_common_prefix(words):
    if not words:
        return ""

    # Определяем минимальную длину слова в массиве
    min_length = min(len(word) for word in words)

    # Проверяем каждую подстроку от начала до минимальной длины
    for i in range(min_length):
        # Текущая подстрока
        prefix = words[0][:i + 1]

        # Проверяем, является ли подстрока общим началом для всех слов
        if all(word.startswith(prefix) for word in words):
            common_prefix = prefix
        else:
            break

    return common_prefix


# Ввод слов
words = input("Введите слова, разделенные пробелами: ").split()

# Нахождение максимально длинного общего начала
result = longest_common_prefix(words)
print("Максимально длинное общее начало:", result)
