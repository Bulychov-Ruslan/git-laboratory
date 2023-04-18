import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Устанавливаем заголовок окна.
pygame.display.set_caption("First Game!")

# Задаем цвета в формате RGB.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

RED_BULLETSS = (158, 41, 74)
YELLOW_BULLETSS = (41, 158, 68)

# Создаем границу, разделяющую экран на две части.
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

# Загружаем звуковые файлы и создаем объекты звуковых эффектов.
BULLET_HIT_SOUND = pygame.mixer.Sound('Game/Assets/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Game/Assets/Gun+Silencer.mp3')

# Создаем шрифты для отображения информации на экране.
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
BULLET_NEW_VEL = 7
MAX_BULLETS = 5

MAX_double_BULLETS = 1

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# Жизнь
YELLOW_HIT = 1
RED_HIT = 2

YELLOW_double_HIT = 3
RED_double_HIT = 4

# Задаем размеры и загружаем изображения космических кораблей в формате PNG, используя модуль os.
# Далее поворачиваем и масштабируем их с помощью методов rotate() и scale().
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Game', 'Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Game', 'Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# Загружаем и масштабируем изображение космического пространства.
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Game', 'Assets', 'space.png')), (WIDTH, HEIGHT))



def draw_window(red, yellow, red_bullets, yellow_bullets, red_double_bullets, yellow_double_bullets, red_health, yellow_health):
    screen.blit(SPACE, (0, 0))
    pygame.draw.rect(screen, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)

    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)

    screen.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    screen.blit(yellow_health_text, (10, 10))

    screen.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    screen.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(screen, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(screen, YELLOW, bullet)

    for bul in red_double_bullets:
        pygame.draw.rect(screen, RED_BULLETSS, bul)

    for bul in yellow_double_bullets:
        pygame.draw.rect(screen, YELLOW_BULLETSS, bul)

    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def handle_bulletss(yellow_double_bullets, red_double_bullets, yellow, red):
    for bul in yellow_double_bullets:
        bul.x += BULLET_VEL
        if red.colliderect(bul):
            pygame.event.post(pygame.event.Event(RED_double_HIT))
            yellow_double_bullets.remove(bul)
        elif bul.x > WIDTH:
            yellow_double_bullets.remove(bul)


    for bul in red_double_bullets:
        bul.x -= BULLET_VEL
        if yellow.colliderect(bul):
            pygame.event.post(pygame.event.Event(YELLOW_double_HIT))
            red_double_bullets.remove(bul)
        elif bul.x < 0:
            red_double_bullets.remove(bul)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    screen.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))

    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_double_bullets = []
    yellow_double_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == pygame.KEYDOWN:
                # yellow_double_bullets
                if event.key == pygame.K_LSHIFT and len(yellow_double_bullets) < MAX_double_BULLETS:
                    bul = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_double_bullets.append(bul)
                    BULLET_FIRE_SOUND.play()

                # red_double_bullets
                if event.key == pygame.K_RSHIFT and len(red_double_bullets) < MAX_double_BULLETS:
                    bul = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_double_bullets.append(bul)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()


            if event.type == RED_double_HIT:
                red_health -= 2
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_double_HIT:
                yellow_health -= 2
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()

        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        handle_bulletss(yellow_double_bullets, red_double_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_double_bullets, yellow_double_bullets, red_health, yellow_health)


    main()


if __name__ == "__main__":
    main()
