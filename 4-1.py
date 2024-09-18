def main():
    # Получаем ввод от пользователя
    numbers = input("Введите числа, разделенные пробелами: ")

    # Преобразуем строку в список чисел
    numbers_list = [float(num) for num in numbers.split()]

    # Проверяем, что список не пуст
    if not numbers_list:
        print("Вы не ввели ни одного числа.")
        return

    # Вычисляем сумму, среднее, максимум и минимум
    total_sum = sum(numbers_list)
    average = total_sum / len(numbers_list)
    maximum = max(numbers_list)
    minimum = min(numbers_list)

    # Выводим результаты
    print(f"Сумма: {total_sum}")
    print(f"Среднее: {average}")
    print(f"Максимум: {maximum}")
    print(f"Минимум: {minimum}")


if __name__ == "__main__":
    main()