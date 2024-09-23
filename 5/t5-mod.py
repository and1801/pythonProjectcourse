import random

pc_list = ('rock' , 'paper' , 'scissors')

user_win = 0
pc_win = 0

print('игра камень ножницы бумага началась')

while user_win < 3 and pc_win < 3:
    user = input(' выберите камень ножницы бумага')
    pc = random.choice(pc_list)

    if user == 'rock' and pc == 'scissors':
        print ('win')
        user_win += 1
    elif user == 'scissors' and pc == 'paper':
        print ('win')
        user_win += 1
    elif user == 'paper' and pc == 'rock':
        print ('win')
        user_win += 1
    elif user == pc:
        print('draw')
    else:
        print ('lose')
        pc_win += 1
if user_win == 3:
    print('user win')
else :
    print('user lose')