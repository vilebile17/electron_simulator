import pygame
from constants import *

def no_electrons(screen,number_of_electrons):
    # Draws a rectangle in the background which seperates the text and makes it stand out
    background_rect = pygame.Rect(1000,-200,300,275)
    pygame.draw.rect(screen,(100,100,100),background_rect,border_radius=20)
    
    # Shows the text in the topright which says "number of electrons"
    small_text = pygame.font.Font(FONT,SMALL_FONT_SIZE)
    no_electrons_text = small_text.render("number of electrons",True, "white")
    text_rect1 = no_electrons_text.get_rect(topright=(SCREEN_WIDTH-25,0))
    screen.blit(no_electrons_text,text_rect1)
    
    # Shows the text in the topright that actually shows the number of electrons
    large_text = pygame.font.Font(FONT,LARGE_FONT_SIZE)
    no_electrons_text = large_text.render(f"{number_of_electrons}",True, "white")
    text_rect2 = no_electrons_text.get_rect(center=(SCREEN_WIDTH - 135,50))
    screen.blit(no_electrons_text,text_rect2)
    
    
def move_speed(screen,electron_speed):
    # Draws a rectangle in the background which seperates the text and makes it stand out
    background_rect = pygame.Rect(-200,-200,500,275)
    pygame.draw.rect(screen,(100,100,100),background_rect,border_radius=20)

     # Shows the text in the topleft which says "electron speed"
    small_text = pygame.font.Font(FONT,SMALL_FONT_SIZE)
    no_electrons_text = small_text.render("electron speed",True, "white")
    text_rect1 = no_electrons_text.get_rect(topright=(230,0))
    screen.blit(no_electrons_text,text_rect1)

    # Shows the text in the topright that actually shows the speed of the electrons
    large_text = pygame.font.Font(FONT,LARGE_FONT_SIZE)
    no_electrons_text = large_text.render(f"{electron_speed//5}",True, "white")
    text_rect2 = no_electrons_text.get_rect(center=(135,50))
    screen.blit(no_electrons_text,text_rect2)
    

