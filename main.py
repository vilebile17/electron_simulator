import pygame,sys
from constants import *
from electron import Electron, draw_star_lines
from shell import Shell

def main():
    if len(sys.argv) < 2:
        print("\n \n USAGE: python3 main.py <no. electrons> ['--star']")
        sys.exit(69)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0

    electrons = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Electron.containers = (updatable, drawable, electrons)
    Shell.containers = (updatable, drawable)

    electron_shell = Shell()
    electron_list = []

    # Game Loop
    while True:

        # This bit allows you to close the program by hitting the close button in the top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        # this rather overly-complicated part is what makes the electrons repel each other
        for first_electron in electrons:
            for second_electron in electrons:
                if first_electron != second_electron:
                    first_electron.repulsive_force(second_electron)

        if "--star" in sys.argv:
            draw_star_lines(electron_list,screen)
        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)
        
        if len(electron_list) < (float(sys.argv[1])//1): # the strange sytax is just incase some idiot tries to spawn fractions of an electron
            electron_list.append(Electron())
        
        pygame.display.flip()
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()
