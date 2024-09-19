import random


def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'Ничья'
    elif (player_choice == 'камень' and computer_choice == 'ножницы') or \
            (player_choice == 'ножницы' and computer_choice == 'бумага') or \
            (player_choice == 'бумага' and computer_choice == 'камень'):
        return 'Игрок'
    else:
        return 'Компьютер'


def play_game():
    player_score = 0
    computer_score = 0
    while player_score < 3 and computer_score < 3:
        player_choice = input("Введите 'камень', 'ножницы' или 'бумага': ").lower()
        if player_choice not in ['камень', 'ножницы', 'бумага']:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
            continue

        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)
        if winner == 'Игрок':
            player_score += 1
            print("Вы выиграли этот раунд!")
        elif winner == 'Компьютер':
            computer_score += 1
            print("Компьютер выиграл этот раунд.")
        else:
            print("Этот раунд закончился вничью.")

        print(f"Счет - Игрок: {player_score}, Компьютер: {computer_score}\n")

    if player_score == 3:
        print("Поздравляем! Вы выиграли игру.")
    else:
        print("К сожалению, компьютер выиграл игру.")


play_game()