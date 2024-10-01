user_text = input("введите текст: ")
with open('user_data.txt', 'a', encoding='utf-8') as file:
    file.write(user_text + '\n')