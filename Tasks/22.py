numbers = [1, 2, 3, 4, 5]
modified_list = [num for num in numbers for _ in (0, 1) if num < 10]
print("Список после вставки однозначных чисел:", modified_list)
