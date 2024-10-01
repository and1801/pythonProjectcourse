class MyCustom(Exception):
    #базовый класс для пользовательских исключений и ошибок
    pass
def check_number(x):
    if x > 100:
        raise MyCustom('Число больше 100')
    elif x < 0:
        raise MyCustom('число меньше 0')
    else:
        print('число в диапазоне')
try:
    check_number(99)
except MyCustom as e:
    print(e)
