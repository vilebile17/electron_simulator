import pygame, random, math
from constants import ELECTRON_RADIUS, SHELL_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, STATIC_CONSTANT, DEGREES_PER_FRAME 

class Electron(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self.containers)
        self.radius = ELECTRON_RADIUS
        self.active_forces = []
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
        self.velocity = self.find_resultant_force() + self.find_momentum()
        self.position += self.velocity * dt
        self.stay_on_circle()
        self.active_forces = []

    def repulsive_force(self, other):
        self_to_other = pygame.Vector2(other.position.x - self.position.x, other.position.y - self.position.y)
        length = self_to_other.length() # the length of the self_to_other Vector
        # F = k/d² where k is a constant
        magnitude = STATIC_CONSTANT / (length**2) # the length of the vector that we want
        scalar = (magnitude * -1)/ length # it is multiplied by -1 in order to make them repel
        force = pygame.Vector2(self_to_other.x * scalar, self_to_other.y * scalar)
        self.active_forces.append(force)
         
    def find_resultant_force(self):
        resultant_x, resultant_y = 0, 0
        x_components, y_components = [],[]
        if len(self.active_forces) != 0:
            for force in self.active_forces:
                x_components.append(force.x) 
                y_components.append(force.y)
            return pygame.Vector2( sum(x_components) / len(self.active_forces) , sum(y_components) / len(self.active_forces))
        return pygame.Vector2(0,0)

    def stay_on_circle(self):
        circle_centre = pygame.Vector2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self_to_circle_centre = pygame.Vector2(circle_centre.x - self.position.x, circle_centre.y - self.position.y)
        if self_to_circle_centre.length() != 300:
            distance_needed_to_travel = self_to_circle_centre.length() - SHELL_RADIUS
            scalar = distance_needed_to_travel / self_to_circle_centre.length() 
            self.position += self_to_circle_centre * scalar

    def find_momentum(self): # Technically it isn't momentum, it's just the natural movement around the circle.
        circle_centre = pygame.Vector2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self_to_circle_centre = pygame.Vector2(circle_centre.x - self.position.x, circle_centre.y - self.position.y)
        target_point = self_to_circle_centre.rotate(DEGREES_PER_FRAME)
        return pygame.Vector2(target_point.x - self_to_circle_centre.x, target_point.y - self_to_circle_centre.y)


