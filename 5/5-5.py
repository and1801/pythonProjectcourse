truePass = '12345dfs'
emailTru = "zer@gmall.com"
password = input('введите пароль: ')
if password == truePass:
    print('Верный пароль')
    print('теперь введите почту: ')
    email = input('введите почту: ')
    if email == emailTru:
        print('вы вошли в аккаунт')
    else:
        print('неверная почта')

else:
    print('неверный пароль')