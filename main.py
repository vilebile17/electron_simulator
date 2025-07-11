import pygame,sys
from constants import *
number_of_electrons = NO_ELECTRONS
from electron import Electron, draw_star_lines
from shell import Shell

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    global number_of_electrons
    key_clicked = False

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

        # Draws and updates most of the important stuff
        if "--star" in sys.argv:
            draw_star_lines(electron_list,screen)
        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)
       
        # Deals with adding and subtracting electrons
        if len(electron_list) < number_of_electrons: 
            electron_list.append(Electron())
        elif len(electron_list) > number_of_electrons:
            if len(electron_list) != 0:
                electron_list[-1].kill()
                electron_list.pop()
       
        # Handles key inputs from the user
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if not key_clicked:
                number_of_electrons += 1
                key_clicked = True
        elif keys[pygame.K_DOWN]:
            if not key_clicked:
                if number_of_electrons > 0:
                    number_of_electrons -= 1
                    key_clicked = True
        else:
            key_clicked = False

        # Shows the text in the topright which says "number of electrons"
        small_text = pygame.font.Font(FONT,SMALL_FONT_SIZE)
        no_electrons_text = small_text.render("number of electrons",True, "white")
        text_rect1 = no_electrons_text.get_rect(topright=(SCREEN_WIDTH - 5,5))
        screen.blit(no_electrons_text,text_rect1)
        # Shows the text in the topright that actually shows the number of electrons
        large_text = pygame.font.Font(FONT,LARGE_FONT_SIZE)
        no_electrons_text = large_text.render(f"{number_of_electrons}",True, "white")
        text_rect2 = no_electrons_text.get_rect(topright=(SCREEN_WIDTH - 100,30))
        screen.blit(no_electrons_text,text_rect2)



        pygame.display.flip()
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()
