import random

#возможные выборы
choices = ['камень', 'ножницы', 'бумага']

#счетчики побед
user_wins = 0
computer_wins = 0

print('игра до 3 побед')
print('введите ваш выбор: камень, ножницы, бумага')

while user_wins < 3 and computer_wins < 3:
    user_choice = input('ваш выбор:').lower()
    if user_choice not in choices:
        print('неправильный ввод. пожалуйста выберите снова')
        continue
    computer_choice = random.choice(choices)
    print(f'компьютер выбрал :{computer_choice}')

    if user_choice == computer_choice:
        print('ничья')
    elif(user_choice ==  "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        user_wins += 1
        print("Вы выиграли раунд!")
    else:
        computer_wins += 1
        print("Компьютер выиграл раунд!")

    print(f"Счёт: Вы {user_wins} - Компьютер {computer_wins}\n")

if user_wins == 3:
    print("Поздравляем! Вы выиграли игру!")
else:
    print("К сожалению, компьютер выиграл игру.")