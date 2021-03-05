import pygame
import sys

pygame.init()

res = (1000,800)

guiDisplay = pygame.display.set_mode(res)
width = guiDisplay.get_width() 
height = guiDisplay.get_height() 


font = pygame.font.SysFont('Merriweather',35)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

guiDisplay.fill(BLACK)

buttonWidth = 100
buttonHeight = 50

driving_mode_button = pygame.Rect(200,300,buttonWidth,buttonHeight)
pygame.draw.rect(guiDisplay, RED,(700,300,buttonWidth,buttonHeight))

pygame.display.update()
driving_mode_button_Tracker = 0


running = True
pygame.draw.rect(guiDisplay, GREEN, driving_mode_button)


while running:
    mouseClicked = False
    if driving_mode_button_Tracker % 2:
        driving_mode_button_Color = BLUE
    else:
        driving_mode_button_Color = GREEN

    pygame.draw.rect(guiDisplay, driving_mode_button_Color, driving_mode_button)

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseClicked = True

        if driving_mode_button.collidepoint(pos) and mouseClicked == False:
            pygame.draw.rect(guiDisplay, driving_mode_button_Color, driving_mode_button)
        elif driving_mode_button.collidepoint(pos) and mouseClicked:
            driving_mode_button_Tracker += 1

        pygame.display.update()
        



    