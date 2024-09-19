import random

true_number = random.randint(1, 100)
while True:
    answer = int(input('какое число загадал компьютер: '))
    if answer < true_number:
        print('more')
    elif answer > true_number:
        print('less')
    else:
        print('bingo')
        break
