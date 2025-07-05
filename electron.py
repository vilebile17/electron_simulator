import pygame, random, math
from constants import ELECTRON_RADIUS, SHELL_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, STATIC_CONSTANT

class Electron(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self.containers)
        self.radius = ELECTRON_RADIUS
        self.velocity = pygame.Vector2(0,0)
        self.random_location()
            
    def random_location(self):
        angle = random.uniform(0, math.tau)
        height = (math.sin(angle) * SHELL_RADIUS) + (SCREEN_HEIGHT / 2)
        width = (math.cos(angle) * SHELL_RADIUS) + (SCREEN_WIDTH / 2)
        self.position = pygame.Vector2(width,height)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"cyan",self.position,self.radius,10)
    
    def update(self,dt):
        self.position += self.velocity

    def repulsive_force(self, other):
        # F = Q/d² where Q is a constant
        distance = self.position.distance_to(other.position)
        angle_from_self_to_other = math.asin((self.position.x-other.position.x)/ distance)

        
