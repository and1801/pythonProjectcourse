import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Выживание с астероидами")

# Установка начальных переменных
ship_size = 50
ship_x, ship_y = width // 2, height - ship_size
ship_speed = 5
asteroid_speed = 5
asteroids = []
score = 0
font = pygame.font.SysFont(None, 35)


def draw_window():
    win.fill((0, 0, 0))  # Очистка экрана

    # Рисуем основной корпус корабля
    pygame.draw.rect(win, (0, 0, 255), (ship_x, ship_y, ship_size, ship_size))

    # Рисуем хвост корабля
    tail_width = ship_size // 2
    pygame.draw.rect(win, (0, 0, 255),
                     (ship_x + ship_size - tail_width, ship_y + ship_size // 2, tail_width, ship_size // 2))

    for asteroid in asteroids:
        pygame.draw.rect(win, (255, 0, 0), (asteroid[0], asteroid[1], ship_size, ship_size))

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(text, (10, 10))
    pygame.display.update()


def main():
    global ship_x, ship_y, asteroids, score
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)  # Устанавливаем FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship_x - ship_speed > 0:
            ship_x -= ship_speed
        if keys[pygame.K_RIGHT] and ship_x + ship_speed < width - ship_size:
            ship_x += ship_speed

        # Создание астероидов
        if random.randint(1, 20) == 1:
            asteroid_x = random.randint(0, width - ship_size)
            asteroid_y = -ship_size
            asteroids.append([asteroid_x, asteroid_y])

        # Обновление позиции астероидов
        for i, asteroid in enumerate(asteroids):
            asteroid[1] += asteroid_speed
            if asteroid[1] > height:
                asteroids.pop(i)
                score += 1

        # Проверка на столкновение
        for asteroid in asteroids:
            if (ship_x < asteroid[0] + ship_size and
                    ship_x + ship_size > asteroid[0] and
                    ship_y < asteroid[1] + ship_size and
                    ship_y + ship_size > asteroid[1]):
                run = False

        draw_window()

    pygame.quit()


main()
