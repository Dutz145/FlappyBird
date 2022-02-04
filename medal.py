import pygame, random
from settings import *

class Medal(pygame.sprite.Sprite):
    def __init__(self, current_medal, camera_vel):
        super().__init__()
        self.image = current_medal

        y_spawn = random.choice([s_height/2 - 75, s_height/2, s_height/2 + 25])
        self.rect = self.image.get_rect(midleft = (s_width + 10, y_spawn))
        self.camera_vel = camera_vel

    # moving the medal
    def move(self):
        self.rect.x -= self.camera_vel

    def update(self):
        self.move()
