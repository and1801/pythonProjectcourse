def sum_numbers():
    total = 0
    print("Введите числа для суммирования. Введите 0, чтобы закончить.")

    while True:
        number = int(input("Введите число: "))

        if number == 0:
            break  # Прерываем цикл, если введено 0

        total += number  # Добавляем введенное число к общей сумме

    print(f"Общая сумма введенных чисел: {total}")


# Запуск программы
sum_numbers()