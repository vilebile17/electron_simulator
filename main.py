import pygame,sys
from constants import *
from electron import Electron
from shell import Shell

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Electron.containers = (updatable, drawable)
    Shell.containers = (updatable, drawable)

    first_electron = Electron()
    noice_shell = Shell()

    test = []

    # Game Loop
    while True:

        # This bit allows you to close the program by hitting the close button in the top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)

        test.append(Electron())
        
        pygame.display.flip()
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()
