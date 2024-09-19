name = input('введите свое имя - ')
height = float(input('введите свой рост - '))
weight = int(input('введите свой вес - '))

result = weight / (height ** 2)
print(f'{name} ваш индекс массы тела - {result}')