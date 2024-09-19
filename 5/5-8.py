command = input('введите команду: ')
if command == 'start':
    print('начинаем работу')
elif command == 'stop':
    print('стоп')
elif command == 'exit':
    print('выход')



match command:
    case 'start':
        print('начинаем работу')
    case 'stop':
        print('стоп')
    case 'exit':
        print('выход')

