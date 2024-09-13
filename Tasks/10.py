def print_even_until_237(numbers):
    for num in numbers:
        if num == 237:
            print(num)
            break
        if num % 2 == 0:
            print(num)

# Пример использования
numbers_list = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953,
    345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949
]

print_even_until_237(numbers_list)
