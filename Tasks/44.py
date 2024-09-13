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
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Параметры игрока
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_COLOR = BLUE
PLAYER_SPEED = 5

# Параметры врагов
ENEMY_WIDTH = 40
ENEMY_HEIGHT = 40
ENEMY_COLOR = RED
ENEMY_SPEED = 2

# Параметры пули
BULLET_WIDTH = 10
BULLET_HEIGHT = 20
BULLET_COLOR = GREEN
BULLET_SPEED = -10

# Параметры игры
score = 0
wave = 1
enemy_count = 5

# Создаем окно игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра на выживание")
clock = pygame.time.Clock()


# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - PLAYER_HEIGHT // 2)
        self.speed = PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed


# Класс врагов
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - ENEMY_WIDTH)
        self.rect.y = random.randint(-100, -40)
        self.speed = ENEMY_SPEED + wave  # Скорость увеличивается с каждой волной

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


# Класс пуль
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
        self.image.fill(BULLET_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


# Основная функция игры
def game():
    global score, wave, enemy_count

    player = Player()
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    all_sprites.add(player)

    # Создание врагов
    def spawn_enemies(count):
        for _ in range(count):
            enemy = Enemy()
            enemies.add(enemy)
            all_sprites.add(enemy)

    spawn_enemies(enemy_count)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Стрельба
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    bullets.add(bullet)
                    all_sprites.add(bullet)

        # Обновление спрайтов
        all_sprites.update()

        # Проверка попадания пули во врага
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 1
            print(f"Очки: {score}")

        # Если все враги уничтожены, начинаем новую волну
        if len(enemies) == 0:
            wave += 1
            enemy_count += 5  # Увеличиваем количество врагов с каждой волной
            spawn_enemies(enemy_count)

        # Проверка столкновения игрока с врагом
        if pygame.sprite.spritecollideany(player, enemies):
            print(f"Игра окончена! Вы набрали: {score} очков.")
            running = False

        # Очистка экрана
        screen.fill(BLACK)

        # Отрисовка всех спрайтов
        all_sprites.draw(screen)

        # Обновление экрана
        pygame.display.flip()

    pygame.quit()


# Запуск игры
game()
