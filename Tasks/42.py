import json


# Функция для проведения опроса
def conduct_survey():
    questions = [
        "Как вас зовут?",
        "Сколько вам лет?",
        "Какой ваш любимый цвет?",
        "Какой ваш любимый фильм?"
    ]

    responses = []

    print("Проведение опроса. Пожалуйста, ответьте на следующие вопросы.")

    for question in questions:
        answer = input(question + " ")
        responses.append(answer)

    return responses


# Функция для сохранения результатов в файл
def save_responses(responses):
    with open('responses.json', 'a') as file:
        json.dump(responses, file)
        file.write('\n')  # Каждая запись в новой строке


# Функция для просмотра результатов опроса
def view_responses():
    try:
        with open('responses.json', 'r') as file:
            print("\nРезультаты опросов:")
            for line in file:
                responses = json.loads(line.strip())
                print(f"Ответы: {responses}")
    except FileNotFoundError:
        print("Нет сохраненных результатов.")


def main():
    while True:
        print("\nМеню:")
        print("1. Провести опрос")
        print("2. Просмотреть результаты опроса")
        print("3. Выход")

        choice = input("Введите ваш выбор (1/2/3): ")

        if choice == '1':
            responses = conduct_survey()
            save_responses(responses)
            print("Ваши ответы сохранены.")
        elif choice == '2':
            view_responses()
        elif choice == '3':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
