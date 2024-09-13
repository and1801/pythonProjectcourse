import random

matrix = [
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
]
new_row = [random.randint(1, 100) for _ in range(len(matrix[0]))]
matrix.append(new_row)
print("Матрица с добавленным случайным рядом:", matrix)
