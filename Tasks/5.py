import math

def square(side_length):
    perimeter = 4 * side_length
    area = side_length ** 2
    diagonal = math.sqrt(2) * side_length
    return (perimeter, area, diagonal)

# Пример использования
side = float(input("Введите длину стороны квадрата: "))
result = square(side)
print(f"Периметр: {result[0]}, Площадь: {result[1]}, Диагональ: {result[2]}")
