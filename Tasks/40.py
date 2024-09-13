import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Лабиринт")

# Настройки игры
player_size = 50
player_x, player_y = width // 2, height // 2
player_speed = 5
maze_size = 50

# Определение структуры лабиринта (1 - стена, 0 - пустое пространство)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def draw_maze():
    win.fill((0, 0, 0))  # Очистка экрана
    # Рисуем стены лабиринта
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                pygame.draw.rect(win, (255, 255, 255), (x * maze_size, y * maze_size, maze_size, maze_size))
    draw_player(player_x, player_y)
    pygame.display.update()


def draw_player(x, y):
    pygame.draw.rect(win, (0, 0, 255), (x, y, player_size, player_size))


def check_collision(x, y):
    # Проверяем, есть ли стена на следующей позиции
    maze_x = x // maze_size
    maze_y = y // maze_size
    if 0 <= maze_x < len(maze[0]) and 0 <= maze_y < len(maze):
        return maze[maze_y][maze_x] == 1
    return False


def main():
    global player_x, player_y
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)  # Устанавливаем FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        new_x, new_y = player_x, player_y

        if keys[pygame.K_LEFT]:
            new_x -= player_speed
        if keys[pygame.K_RIGHT]:
            new_x += player_speed
        if keys[pygame.K_UP]:
            new_y -= player_speed
        if keys[pygame.K_DOWN]:
            new_y += player_speed

        # Проверяем на столкновение перед перемещением
        if not check_collision(new_x, new_y):
            player_x, player_y = new_x, new_y

        draw_maze()

    pygame.quit()


main()
