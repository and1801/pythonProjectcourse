def common_elements(list1, list2):
    # Используем пересечение множеств для поиска общих элементов
    return list(set(list1) & set(list2))

# Заданные списки
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Получаем список общих элементов
result = common_elements(a, b)

# Выводим результат
print(f"Общие элементы: {result}")