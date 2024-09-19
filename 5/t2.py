a = float(input('введите первое число: '))
act = input('введите действие (+, -, *, /): ')
b = float(input('введите второе число: '))
if act == '+':
    print(a + b)
elif act == '-':
    print(a - b)
elif act == '*':
    print (a * b)
elif act == '/' and b != 0:
    print (a / b)
else:
    print('невозможное действие')

