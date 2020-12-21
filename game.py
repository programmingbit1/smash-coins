import pygame
import random

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()

background = pygame.image.load('bg.png')
user = pygame.image.load('user.png')
coin = pygame.image.load('coin.png')


def display_score(score):
    font = pygame.font.SysFont('BIG JOHN', 32)
    score_text = 'Your score: ' + str(score)
    text_img = font.render(score_text, True, (0, 255, 0))
    screen.blit(text_img, [20, 10])


def random_offset():
    return 1*random.randint(100, 1500)


coin_y = [random_offset(), random_offset(), random_offset()]
user_x = 150
score = 0


def crashed(idx):
    global score
    global keep_alive
    score = score -100
    coin_y[idx] = random_offset()
    if score < -500:
        keep_alive = False


def update_coin_pos(idx):
    global score
    if coin_y[idx] > 600:
        coin_y[idx] = random_offset()
        score = score + 50
        print('score', score)
    else:
        coin_y[idx] = coin_y[idx] + 5


keep_alive = True
clock = pygame.time.Clock()
while keep_alive:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x < 280:
        user_x = user_x + 10
    elif keys[pygame.K_LEFT] and user_x > 0:
        user_x = user_x - 10

    update_coin_pos(0)
    update_coin_pos(1)
    update_coin_pos(2)

    screen.blit(background, [0, 0])
    screen.blit(user, [user_x, 520])
    screen.blit(coin, [0, coin_y[0]])
    screen.blit(coin, [150, coin_y[1]])
    screen.blit(coin, [280, coin_y[2]])

    if coin_y[0] > 500 and user_x < 70:
        crashed(0)

    if coin_y[1] > 500 and user_x > 80 and user_x < 200:
        crashed(1)

    if coin_y[2] > 500 and user_x > 220:
        crashed(2)

    display_score(score)

    pygame.display.update()
    clock.tick(60)

