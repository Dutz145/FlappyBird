import pygame
from settings import *
from global_images import *
from flappy_bird import FlappyBird
from obstacles import Obstacle
from medal import Medal

pygame.init()

class Game:
    def __init__(self, flappy_type):
        # obstacle images
        self.obstacle_up = pygame.image.load('obstacles/obstacle_up.png').convert_alpha()
        self.obstacle_up = pygame.transform.scale2x(self.obstacle_up)
        self.obstacle_down = pygame.image.load('obstacles/obstacle_down.png').convert_alpha()
        self.obstacle_down = pygame.transform.scale2x(self.obstacle_down)

        # Medal atributes
        self.caught_gold_medal = False
        self.caught_silver_medal = False
        self.caught_orange_medal = False
        self.current_medal = silver_medal
        self.medal = None

        # ground image
        self.ground = pygame.image.load('bgs/ground.png').convert_alpha()
        self.ground = pygame.transform.scale(self.ground, (s_width, self.ground.get_height() * 2))
        self.ground_rect = self.ground.get_rect(midbottom = (s_width/2, s_height))

        # game over image
        self.game_over_text = pygame.image.load('text/game_over.png').convert_alpha()
        self.game_over_rect = self.game_over_text.get_rect(center = (s_width/2, s_height/4))
        self.game_over = False

        # score display image
        self.score_display = pygame.image.load('text/score_display.png').convert_alpha()
        self.score_display_rect = self.score_display.get_rect(midtop = (s_width/2, self.game_over_rect.midbottom[1] + 10))

        self.menu_rect = menu.get_rect(midtop = (s_width/2, self.score_display_rect.midbottom[1] + 5))

        # game speeed
        self.camera_vel = 2
        self.update_camera_count = 5

        # flappy bird and obstacles
        self.flappy_bird = FlappyBird(s_height, flappy_type)

        self.obstacle_1 = Obstacle(s_width, s_height, self.obstacle_up, 
        'obstacle up', self.camera_vel)

        self.obstacle_2 = Obstacle(s_width, s_height, self.obstacle_down, 
        'obstacle down', self.camera_vel)

        # score and fonts
        self.score = 0
        self.small_font = pygame.font.Font('text/Flappy-Bird.ttf', 40)
        self.big_font = pygame.font.Font('text/Flappy-Bird.ttf', 75)

        # New image
        self.new = pygame.image.load('text/new.png').convert_alpha()
        self.new = pygame.transform.scale2x(self.new)
        self.new_rect = self.new.get_rect(topright = (self.score_display_rect.topright[0] - 90, 
                self.score_display_rect.topright[1] + 125))

    # checking objects collisions
    def collision(self, obstacles, medals):
        if pygame.sprite.spritecollide(self.flappy_bird, obstacles, 0) \
            or self.flappy_bird.rect.colliderect(self.ground_rect):
            self.game_over = True

        if self.medal:
            if pygame.sprite.spritecollide(self.flappy_bird, medals, 0):
                self.medal.kill()
                if self.score >= 0:
                    self.current_medal = silver_medal
                    self.caught_silver_medal = True

                if self.score >= 24:
                    self.current_medal = gold_medal
                    self.caught_gold_medal = True
                
                if self.score >= 49:
                    self.current_medal = orange_medal
                    self.caught_orange_medal = True

    # Increasing the game speed
    def update_camera_vel(self):
        if self.score == self.update_camera_count:
            self.update_camera_count *= 2
            self.camera_vel += 1
    
    # creating the medals
    def create_medals(self, medals):
        if self.score in {0, 24, 49}:
            self.medal = Medal(self.current_medal, self.camera_vel)
            medals.add(self.medal)

    # Updating the medal of the current round
    def update_current_medal(self):
        if self.score >= 24:
            self.current_medal = gold_medal
        if self.score >= 49:
            self.current_medal = orange_medal

    # Creating the obstacles
    def create_obstacles(self, obstacles):
        for obstacle in obstacles:
            if self.flappy_bird.rect.left > obstacle.rect.right and len(obstacles) <= 2:
                obstacle_1 = Obstacle(s_width, s_height, self.obstacle_up, 'obstacle up', self.camera_vel)
                obstacle_2 = Obstacle(s_width, s_height, self.obstacle_down, 'obstacle down', self.camera_vel)
                    
                obstacles.add(obstacle_1, obstacle_2)
                self.score += 1

    def pause(self, record, player, obstacles):
        screen.blit(bg_day, (0,0))
        obstacles.draw(screen)
        screen.blit(self.ground, self.ground_rect)
        player.draw(screen)
        screen.blit(self.score_display, self.score_display_rect)
        screen.blit(menu, self.menu_rect)
        
        score_text = self.small_font.render(f'{self.score}', 0, (0,0,0))
        score_rect = score_text.get_rect(topright = (self.score_display_rect.topright[0] - 55, 
        self.score_display_rect.topright[1] + 55))
        screen.blit(score_text, score_rect)

        if self.score > record:
            best_text = self.small_font.render(f'{self.score}', 0, (0,0,0))
            screen.blit(self.new, self.new_rect)
        else:
            best_text = self.small_font.render(f'{record}', 0, (0,0,0))

        best_rect = score_text.get_rect(topright = (self.score_display_rect.topright[0] - 55, 
        self.score_display_rect.topright[1] + 125))
        screen.blit(best_text, best_rect)

        if self.caught_silver_medal or self.caught_gold_medal or self.caught_orange_medal:
            self.current_medal = pygame.transform.scale(self.current_medal, (92, 76))
            medal_rect = self.current_medal.get_rect(topleft = (self.score_display_rect.topleft[0] + 25, 
            self.score_display_rect.topleft[1] + 65))
            screen.blit(self.current_medal, medal_rect)

    def update(self, screen, obstacles, player, record, medals):
        screen.fill((102,204,0))
        if record > 50:
            screen.blit(bg_night, (0,0))
        else:
            screen.blit(bg_day, (0,0))

        if not self.game_over:
            # Updating game methods
            self.collision(obstacles, medals)
            self.create_obstacles(obstacles)
            self.create_medals(medals)
            self.update_current_medal()
            self.update_camera_vel()

            # Displaying the score
            score_text = self.big_font.render(f'{self.score}', 0, (255,255,255))
            score_rect = score_text.get_rect(center = (s_width/2, s_height/6))
            screen.blit(score_text, score_rect)

            # Bliting and updating player, obstacles, and medals
            self.flappy_bird.update()
            obstacles.update()
            if self.medal:
                medals.update()
                medals.draw(screen)

            player.draw(screen)
            obstacles.draw(screen)
        else:
            # drawing game over screen
            screen.blit(self.game_over_text, self.game_over_rect)
            screen.blit(self.score_display, self.score_display_rect)
            screen.blit(menu, self.menu_rect)

            score_text = self.small_font.render(f'{self.score}', 0, (0,0,0))
            score_rect = score_text.get_rect(topright = (self.score_display_rect.topright[0] - 55, 
            self.score_display_rect.topright[1] + 55))
            screen.blit(score_text, score_rect)

            if self.score > record:
                best_text = self.small_font.render(f'{self.score}', 0, (0,0,0))
                screen.blit(self.new, self.new_rect)
            else:
                best_text = self.small_font.render(f'{record}', 0, (0,0,0))

            best_rect = score_text.get_rect(topright = (self.score_display_rect.topright[0] - 55, 
            self.score_display_rect.topright[1] + 125))
            screen.blit(best_text, best_rect)

            if self.caught_silver_medal or self.caught_gold_medal or self.caught_orange_medal:
                self.current_medal = pygame.transform.scale(self.current_medal, (92, 76))
                medal_rect = self.current_medal.get_rect(topleft = (self.score_display_rect.topleft[0] + 25, 
                self.score_display_rect.topleft[1] + 65))
                screen.blit(self.current_medal, medal_rect)
        # drawing ground
        screen.blit(self.ground, self.ground_rect)