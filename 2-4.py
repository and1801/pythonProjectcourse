def count_numbers_with_digit_3():
    count = 0
    for num in range(1, 2025):  # Перебираем числа от 1 до 2024
        if '3' in str(num):  # Проверяем, есть ли цифра 3 в строковом представлении числа
            count += 1
    return count

# Запускаем функцию и выводим результат
result = count_numbers_with_digit_3()
print(f"Количество чисел от 1 до 2024, содержащих хотя бы одну цифру 3: {result}")