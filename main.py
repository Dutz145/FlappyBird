import pygame, sys
from game import Game, screen, s_width, s_height
from global_images import *

pygame.init()

def pause(flappy_bird, record, player, obstacles):
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        flappy_bird.pause(record, player, obstacles)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        pygame.display.update()

def main(record, flappy_type):
    run = True
    clock = pygame.time.Clock()

    flappy_bird = Game(flappy_type)
 
    obstacles = pygame.sprite.Group(flappy_bird.obstacle_1, flappy_bird.obstacle_2)
    player = pygame.sprite.GroupSingle(flappy_bird.flappy_bird)
    medals = pygame.sprite.GroupSingle( )

    while run:
        clock.tick(60)
        flappy_bird.update(screen, obstacles, player, record, medals)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if flappy_bird.game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if flappy_bird.menu_rect.collidepoint(event.pos):
                        run = False
                if event.type == pygame.KEYDOWN:                    
                    if event.key == pygame.K_RETURN:
                        run = False
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause(flappy_bird, record, player, obstacles)

        pygame.display.update()

    if flappy_bird.score > record:
        record = flappy_bird.score

    return record

def shop(record, flappy_type):
    run = True
    clock = pygame.time.Clock()

    menu_rect = menu.get_rect(topright = (s_width - 5, 5))

    yellow_flappy_rect = yellow_flappy_1.get_rect(topleft = (s_width/6, s_height/4))
    blue_flappy_rect = blue_flappy_1.get_rect(topleft = (s_width/6, s_height/2))
    red_flappy_rect = red_flappy_1.get_rect(topleft = (s_width/6, s_height - s_height/4))

    silver_medal_rect = silver_medal.get_rect(topleft = (yellow_flappy_rect.topright[0] + 25, yellow_flappy_rect.topright[1]))
    gold_medal_rect = gold_medal.get_rect(topleft = (blue_flappy_rect.topright[0] + 25, blue_flappy_rect.topright[1]))
    orange_medal_rect = orange_medal.get_rect(topleft = (red_flappy_rect.topright[0] + 25, red_flappy_rect.topright[1]))

    title = small_font.render('Shop', 0, (255,255,255))
    title_rect = title.get_rect(topleft = (5,5))

    record_text = small_font.render(f'Record: {record}', 0, (255,255,255))
    record_rect = record_text.get_rect(bottomleft = (5, s_height - 5))

    while run:
        clock.tick(60)
        screen.blit(bg_night, (0,0))

        screen.blit(yellow_flappy_1, yellow_flappy_rect)
        screen.blit(blue_flappy_2, blue_flappy_rect)
        screen.blit(red_flappy_1, red_flappy_rect)

        screen.blit(menu, menu_rect)
        screen.blit(title, title_rect)
        screen.blit(record_text, record_rect)

        screen.blit(silver_medal, silver_medal_rect)
        screen.blit(gold_medal, gold_medal_rect)
        screen.blit(orange_medal, orange_medal_rect) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if yellow_flappy_rect.collidepoint(event.pos):
                    flappy_type = 'Yellow'

                if blue_flappy_rect.collidepoint(event.pos) and record > 25:
                    flappy_type = 'Blue'

                if red_flappy_rect.collidepoint(event.pos) and record > 50:
                    flappy_type = 'Red'

                if menu_rect.collidepoint(event.pos):
                    run = False

        
        yellow_label = small_font.render('Unlocked', 0, (0,255,0))

        if record > 25:
            blue_label = small_font.render('Unlocked', 0, (0,255,0))
        else:
            blue_label = small_font.render('Locked', 0, (255,0,0))

        if record > 50:
            red_label = small_font.render('Unlocked', 0, (0,255,0))
        else:
            red_label = small_font.render('Locked', 0, (255,0,0))


        yellow_label_rect = yellow_label.get_rect(topleft = (yellow_flappy_rect.topright[0] + yellow_label.get_width() + 25, 
        yellow_flappy_rect.topright[1]))

        blue_label_rect = blue_label.get_rect(topleft = (blue_flappy_rect.topright[0] + yellow_label.get_width() + 25, 
        blue_flappy_rect.topright[1]))

        red_label_rect = red_label.get_rect(topleft = (red_flappy_rect.topright[0] + yellow_label.get_width() + 25, 
        red_flappy_rect.topright[1]))

        equipped_label = small_font.render('Equipped', 0, (233,218,9))
        if flappy_type == 'Yellow':
            screen.blit(equipped_label, yellow_label_rect)
            screen.blit(blue_label, blue_label_rect)
            screen.blit(red_label, red_label_rect)
        elif flappy_type == 'Blue':
            screen.blit(equipped_label, blue_label_rect)
            screen.blit(yellow_label, yellow_label_rect)
            screen.blit(red_label, red_label_rect)
        else:
            screen.blit(equipped_label, red_label_rect)
            screen.blit(yellow_label, yellow_label_rect)
            screen.blit(blue_label, blue_label_rect)

        pygame.display.update()

    return flappy_type

def main_menu():
    run = True
    clock = pygame.time.Clock()

    # importing text
    play_button = pygame.image.load('text/play_button.png').convert_alpha()
    play_rect = play_button.get_rect(topleft = (s_width/6, s_height/2 - 12))

    shop_text = pygame.image.load('text/shop_image.png').convert_alpha()
    shop_rect = shop_text.get_rect(topright = (s_width - s_width/6, s_height/2))

    record = 0
    flappy_type = 'Yellow'

    while run:
        clock.tick(60)
        # Background
        screen.fill((102,204,0))
        screen.blit(bg_day, (0,0))
        screen.blit(play_button, play_rect)

        # Intro texts
        welcome = big_font.render('Flappy Bird', 0, (255, 255, 255))
        welcome_rect = welcome.get_rect(center = (s_width/2, s_height/4))

        start = small_font.render('Press SPACE to begin', 0, (250,50,0))
        start_rect = start.get_rect(midtop = (welcome_rect.midbottom[0], welcome_rect.midbottom[1] + 5))

        screen.blit(welcome, welcome_rect)
        screen.blit(start, start_rect)

        # Shop
        screen.blit(shop_text, shop_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    record = main(record, flappy_type)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    record = main(record, flappy_type)

                if shop_rect.collidepoint(event.pos):
                    flappy_type = shop(record, flappy_type)

        pygame.display.update()

if __name__ == '__main__':
    main_menu()