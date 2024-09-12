import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH = 800
HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Параметры игрока
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_COLOR = BLUE
PLAYER_GRAVITY = 0.8
PLAYER_SPEED = 5

# Параметры платформ
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLATFORM_COLOR = GREEN

# Параметры бонуса
BONUS_SIZE = 20
BONUS_COLOR = RED

# Создаем окно игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Платформер")

clock = pygame.time.Clock()


# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.vel_y = 0
        self.vel_x = 0
        self.is_jumping = False

    def update(self):
        self.vel_y += PLAYER_GRAVITY
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x

        # Границы экрана для движения влево и вправо
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        # Если игрок падает за экран, вернуть на платформу
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = 0
            self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.vel_y = -15  # Прыжок
            self.is_jumping = True

    def move_left(self):
        self.vel_x = -PLAYER_SPEED

    def move_right(self):
        self.vel_x = PLAYER_SPEED

    def stop(self):
        self.vel_x = 0


# Класс платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(PLATFORM_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Класс бонуса
class Bonus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BONUS_SIZE, BONUS_SIZE))
        self.image.fill(BONUS_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Основная функция игры
def game():
    player = Player()
    platforms = pygame.sprite.Group()
    bonuses = pygame.sprite.Group()

    # Создание платформ
    platform1 = Platform(100, 500)
    platform2 = Platform(300, 400)
    platform3 = Platform(500, 300)
    platforms.add(platform1, platform2, platform3)

    # Создание бонуса
    bonus = Bonus(600, 250)
    bonuses.add(bonus)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, platform1, platform2, platform3, bonus)

    running = True
    score = 0

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Управление движением и прыжками
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.move_left()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.move_right()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.stop()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.stop()

        # Обновление игрока
        player.update()

        # Проверка столкновения игрока с платформами
        hits = pygame.sprite.spritecollide(player, platforms, False)
        if hits:
            if player.vel_y > 0:  # Игрок падает сверху на платформу
                player.rect.bottom = hits[0].rect.top
                player.vel_y = 0
                player.is_jumping = False

        # Проверка на сбор бонусов
        bonus_hits = pygame.sprite.spritecollide(player, bonuses, True)
        if bonus_hits:
            score += 1
            print(f"Бонус собран! Ваш счёт: {score}")

        # Очистка экрана
        screen.fill(WHITE)

        # Отрисовка всех объектов
        all_sprites.draw(screen)

        # Обновление экрана
        pygame.display.flip()

    pygame.quit()


# Запуск игры
game()
