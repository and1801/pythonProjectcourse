def longest_chain(filename):
    # Допустимые символы
    allowed_chars = {'A', 'C', 'D', 'F', 'O'}

    # Открываем файл и считываем его содержимое
    with open(filename, 'r') as file:
        data = file.read().strip()

    # Проверяем, содержит ли файл недопустимые символы
    for char in data:
        if char not in allowed_chars:
            raise ValueError(f"Ошибка: обнаружен недопустимый символ '{char}'. Допустимы только символы A, C, D, F, O.")

    longest_chain = ''  # Переменная для хранения самой длинной цепочки
    current_chain = ''  # Текущая цепочка символов

    i = 0
    while i < len(data):
        if data[i] == 'D':  # Если символ D найден
            current_chain = 'D'  # Начинаем новую цепочку
            i += 1
            o_count = 0  # Счетчик букв O

            while i < len(data):
                current_chain += data[i]

                if data[i] == 'O':
                    o_count += 1
                elif data[i] == 'D':  # Если это конец цепочки
                    if o_count <= 2:  # Проверяем, чтобы не было более 2 O между D
                        if len(current_chain) > len(longest_chain):  # Проверяем длину
                            longest_chain = current_chain  # Обновляем самую длинную цепочку
                    break

                i += 1
        else:
            i += 1

    return longest_chain

# Пример использования
filename = 'input.txt'  # Имя текстового файла
try:
    chain = longest_chain(filename)

    # Выводим самую длинную цепочку и её длину
    if chain:
        print(f"Самая длинная цепочка: {chain}, длина: {len(chain)}")
    else:
        print("Подходящих цепочек не найдено.")

except ValueError as e:
    print(e)