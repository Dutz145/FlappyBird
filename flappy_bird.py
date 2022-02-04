import pygame
from global_images import *

pygame.init()

class FlappyBird(pygame.sprite.Sprite):
    def __init__(self, s_height, flappy_type):
        super().__init__()

        # setting up the image
        if flappy_type == 'Yellow':
            animation_1 = yellow_flappy_1
            animation_2 = yellow_flappy_2
            animation_3 = yellow_flappy_3

        elif flappy_type == 'Blue':
            animation_1 = blue_flappy_1
            animation_2 = blue_flappy_2
            animation_3 = blue_flappy_3
        else:
            animation_1 = red_flappy_1
            animation_2 = red_flappy_2
            animation_3 = red_flappy_3                   

        self.images = [animation_1, animation_2, animation_3]
        self.image = animation_1
        self.rect = self.image.get_rect(topleft = (50, s_height/2 - 10))

        self.animation_counter = 0
        self.vel = 50
        self.gravity = 0
        self.cooldown_counter = 0

    # creating cooldown for jump
    def cooldown(self):
        if self.cooldown_counter > 0:
            self.cooldown_counter += 1
        if self.cooldown_counter > 10:
            self.cooldown_counter = 0

    # animating
    def animate(self):
        if self.animation_counter >= 3:
            self.animation_counter = 0

        self.image = self.images[int(self.animation_counter)]
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
        
        self.animation_counter += 0.15

    # getting the player input
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.rect.top - self.vel > 0 and self.cooldown_counter == 0:
            self.cooldown_counter = 1
            self.gravity = -10

    # applying the gravity of the game
    def apply_gravity(self):
        self.gravity += 0.5
        self.rect.y += self.gravity

        if self.rect.bottom >= 650:
            self.rect.bottom = 650

    # updating player methods
    def update(self):
        self.animate()
        self.get_input()
        self.apply_gravity()
        self.cooldown()
