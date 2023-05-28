import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
import random
from os import listdir
#code revue)

pygame.init()

# FPS = pygame.time.Clock()

screen = width, height = 800, 600


font = pygame.font.SysFont('Verdana', 20)

main_surface = pygame.display.set_mode(screen)


# player = pygame.Surface((30,30))
# player.fill((255,255,255))

player_imgs = [pygame.image.load('goose' + '/' + file).convert_alpha() for file in listdir('goose')]
player= player_imgs[0]
player_rect = player.get_rect()
player_speed = 5

pygame.time.set_timer(pygame.USEREVENT + 3, 125)
def create_enemy():
    # enemy = pygame.Surface((20, 20))
    # enemy.fill(RED)
    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy_rect = pygame.Rect(width - 15, random.randint(0,height - 30), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]

pygame.time.set_timer(pygame.USEREVENT + 1, 1500) #

def create_bonus():
    # bonus = pygame.Surface((20, 20))
    # bonus.fill(GREEN)
    bonus = pygame.image.load('bonus.png').convert_alpha()
    bonus_rect = pygame.Rect(random.randint(0, width),-bonus.get_height(), *bonus.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus, bonus_rect, bonus_speed]
pygame.time.set_timer(pygame.USEREVENT + 2, 1500)

bg = pygame.transform.scale(pygame.image.load('background.png').convert(), screen)
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3

img_index = 0
scores = 0
#
enemies = []
bonuses = []

is_working = True

while is_working:

    pygame.time.Clock().tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working=False#

        if event.type == pygame.USEREVENT + 1:
            enemies.append(create_enemy())#
        if event.type == pygame.USEREVENT + 2:
            bonuses.append(create_bonus())

        if event.type == pygame.USEREVENT + 3:
            img_index += 1
            if img_index == len(player_imgs):
                img_index = 0
            player = player_imgs[img_index]




    pressed_keys = pygame.key.get_pressed()

    bgX -= bg_speed
    bgX2 -= bg_speed

    if bgX < -bg.get_width():#
        bgX = bg.get_width()
    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()

    main_surface.blit(bg, (bgX, 0))
    main_surface.blit(bg, (bgX2, 0))

    main_surface.blit(player, player_rect)

    main_surface.blit(font.render(str(scores),True, 0,0,0), (width - 30, 0))


    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        if player_rect.colliderect(enemy[1]):
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom >= height:
            bonuses.pop(bonuses.index(bonus))
        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1

    if pressed_keys[K_DOWN] and not player_rect.bottom >= height:
        player_rect = player_rect.move(0, player_speed)
    elif pressed_keys[K_UP] and not player_rect.top <= 0:
        player_rect = player_rect.move(0, -player_speed)
    elif pressed_keys[K_RIGHT] and not player_rect.right >= width:
        player_rect = player_rect.move(player_speed, 0)
    elif pressed_keys[K_LEFT] and not player_rect.left <= 0:
        player_rect = player_rect.move(-player_speed, 0)




    #main_surface.fill((155,155,155))
    pygame.display.flip()




    # ball_speed[1] = -ball_speed[1]
    # ball.fill((255, 0, 0))

    # elif ball_rect.left >= width or ball_rect.right <= 0:
    # ball_speed[0] = -ball_speed[0]
    # ball.fill((0, 255, 0))