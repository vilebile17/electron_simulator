import pygame
from constants import SHELL_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT 

class Shell(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self.containers)
        self.radius = SHELL_RADIUS 
        self.position = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    def draw(self, screen):
        pygame.draw.circle(screen ,"white" ,self.position ,self.radius ,2)
