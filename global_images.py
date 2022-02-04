import pygame

pygame.init()

red_flappy_1 = pygame.image.load('animation/red_flappy_bird_1.png').convert_alpha()
red_flappy_1 = pygame.transform.scale2x(red_flappy_1)

red_flappy_2 = pygame.image.load('animation/red_flappy_bird_2.png').convert_alpha()
red_flappy_2 = pygame.transform.scale2x(red_flappy_2)

red_flappy_3 = pygame.image.load('animation/red_flappy_bird_3.png').convert_alpha()
red_flappy_3 = pygame.transform.scale2x(red_flappy_3)

blue_flappy_1 = pygame.image.load('animation/blue_flappy_bird_1.png').convert_alpha()
blue_flappy_1 = pygame.transform.scale2x(blue_flappy_1)

blue_flappy_2 = pygame.image.load('animation/blue_flappy_bird_2.png').convert_alpha()
blue_flappy_2 = pygame.transform.scale2x(blue_flappy_2)

blue_flappy_3 = pygame.image.load('animation/blue_flappy_bird_3.png').convert_alpha()
blue_flappy_3 = pygame.transform.scale2x(blue_flappy_3)

yellow_flappy_1 = pygame.image.load('animation/flappy_bird_1.png').convert_alpha()
yellow_flappy_1 = pygame.transform.scale2x(yellow_flappy_1)

yellow_flappy_2 = pygame.image.load('animation/flappy_bird_2.png').convert_alpha()
yellow_flappy_2 = pygame.transform.scale2x(yellow_flappy_2)

yellow_flappy_3 = pygame.image.load('animation/flappy_bird_3.png').convert_alpha()
yellow_flappy_3 = pygame.transform.scale2x(yellow_flappy_3)

bg_day = pygame.image.load('bgs/bg_day.png').convert()
bg_night = pygame.image.load('bgs/bg_night.png').convert()

big_font = pygame.font.Font('text/Flappy-Bird.ttf', 75)
small_font = pygame.font.Font('text/Flappy-Bird.ttf', 50)

menu = pygame.image.load('text/menu.png').convert_alpha()

gold_medal = pygame.image.load('medals/gold_medal.png').convert_alpha()
silver_medal = pygame.image.load('medals/silver_medal.png').convert_alpha()
orange_medal = pygame.image.load('medals/orange_medal.png').convert_alpha()