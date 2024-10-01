import math

print(math.ceil(2.01))
print(math.floor(2.9))
print(math.log(10, 100))
print(math.sqrt(9))
print(math.pow(9, 2))
print(math.pi)

radius = float(input('введите радиус круга '))
area = math.pi * radius ** 2
print(area)

a = float(input(' сторона а '))
b = float(input( ' сторона b '))
c = math.sqrt(math.pow(a,2) + math.pow(b,2))
print(f'гипо - {c}')