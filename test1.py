x = 0
y = 0

while True:
    user_input = input("введите направление а расстояние (или 'stop' для завершения): ")

    if user_input.lower() == 'stop':
        print(f'{x} {y}')
        break

    direction, distance = user_input.split()
    distance = int(distance)

    if direction == 'N':
        y += distance
    elif direction == 'S':
        y -= distance
    elif direction == 'E':
        x += distance
    elif direction == 'W':
        x -= distance


