import pygame, random

pygame.init()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, s_width, s_height, image, image_type, camera_vel):
        super().__init__()

        # all possible spawns for the obstacles
        position_choices = [
            {'obstacle up': (s_width + 25, s_height - 200), 'obstacle down':(s_width + 25, 100)},
            {'obstacle up': (s_width + 25, s_height - 275), 'obstacle down': (s_width + 25, 200)},
            {'obstacle up': (s_width + 25, s_height - 350), 'obstacle down': (s_width + 25, 50)},
            {'obstacle up': (s_width + 25, s_height - 175), 'obstacle down': (s_width + 25, 275)},
            {'obstacle up': (s_width + 25, s_height - 275), 'obstacle down': (s_width + 25, 275)},
            {'obstacle up': (s_width + 25, s_height - 315), 'obstacle down': (s_width + 25, 225)}
            ]

        self.image = image
        choice = random.choice(position_choices)
        if image_type == 'obstacle up':
            self.rect = self.image.get_rect(topleft = choice['obstacle up'])
        else:            
            self.rect = self.image.get_rect(bottomleft = choice['obstacle down'])

        self.camera_vel = camera_vel

    # moving obstacle
    def move(self):
        self.rect.x -= self.camera_vel
    
    # killing the obstacle after it passes the screen
    def kill_obstacle(self):
        if self.rect.right <= -25:
            self.kill()

    def update(self):
        self.move()
        self.kill_obstacle()