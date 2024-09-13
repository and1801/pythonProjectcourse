import cmath

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Находим дискриминант
d = b**2 - 4*a*c

# Находим корни
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

print("Корни квадратного уравнения:", root1, root2)
