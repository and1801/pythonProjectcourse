from random import randint, choice, random, uniform, randrange, shuffle

from Tasks.c1 import result

# Генерация случайного числа от 1 до 10
random_number = randint(1, 10)
print(f"Случайное число от 1 до 10: {random_number}")

# Список элементов
elements = ['яблоко', 'банан', 'вишня', 'груша', 'персик']

# Выбор случайного элемента из списка
random_element = choice(elements)
print(f"Случайный фрукт из списка: {random_element}")

ranndom = uniform(6, 5)
print(ranndom)

result = randrange(0, 100, 23)
print((result))

shuffle(elements)
print(elements)

print(dir(random))