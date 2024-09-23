a = int(input('введите число 1: '))
b = int(input('введите число 2: '))
c = int(input('введите число 3: '))
if a < b and a < c:
    print (f'наименьшее число:{a}')
elif b < a and b < c:
    print(f'наименьшее число:{b}')
elif c < a and c < b:
    print(f'наименьшее число:{c}')
else:
    print("все числа равны")