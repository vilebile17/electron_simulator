import pygame,sys
from constants import *
from electron import Electron, draw_star_lines
from shell import Shell
from user_interface import no_electrons, move_speed

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    key_clicked = False

    # setting default values
    number_of_electrons = 5
    electron_speed = 25

    electrons = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Electron.containers = (updatable, drawable, electrons)
    Shell.containers = (drawable, )

    electron_shell = Shell()
    electron_list = []
    
    # This is for the top right corner which show the total number of electrons
    up_arrow = pygame.transform.smoothscale(pygame.image.load("assets/up_arrow.png"),(35,35))        
    down_arrow = pygame.transform.rotate(pygame.transform.smoothscale(pygame.image.load("assets/up_arrow.png"),(35,35)),180)
    up_arrow_rect = up_arrow.get_rect(topleft=(1180,32))
    down_arrow_rect = down_arrow.get_rect(topleft=(1080,32))
     # This is for the top right corner which show the total number of electrons
    e_button = pygame.transform.smoothscale(pygame.image.load("assets/E.png"),(35,35))        
    q_button = pygame.transform.smoothscale(pygame.image.load("assets/Q.png"),(35,35))  
    e_rect = e_button.get_rect(topleft=(190,32))
    q_rect = q_button.get_rect(topleft=(50,32))



    # Game Loop
    while True:

        # This bit allows you to close the program by hitting the close button in the top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if up_arrow_rect.collidepoint(event.pos):
                    number_of_electrons += 1
                elif down_arrow_rect.collidepoint(event.pos):
                    number_of_electrons -= 1
                elif e_rect.collidepoint(event.pos):
                    electron_speed += 5
                elif q_rect.collidepoint(event.pos):
                    electron_speed -= 5

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
            object.update(dt,electron_speed)
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
        elif keys[pygame.K_e]:
            if not key_clicked:
                if electron_speed < 90:
                    electron_speed += 5 
                    key_clicked = True
        elif keys[pygame.K_q]:
            if not key_clicked:
                if electron_speed > -90:
                    electron_speed -= 5
                    key_clicked = True
        else:
            key_clicked = False
 
        # This is for the top right corner which show the total number of electrons
        no_electrons(screen,number_of_electrons)
        screen.blit(up_arrow,up_arrow_rect)
        screen.blit(down_arrow,down_arrow_rect)
        move_speed(screen,electron_speed)
        screen.blit(e_button,e_rect)
        screen.blit(q_button,q_rect)


        pygame.display.flip()
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()
