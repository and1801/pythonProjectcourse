def int_num():
    while True:
        try:
            user_in = input('введите целое число: ')
            user_num = int(user_in)
            print(f'Вы ввели число: {user_num}')
            break
        except ValueError:
            print('Неверное значение. Еще раз')
int_num()
