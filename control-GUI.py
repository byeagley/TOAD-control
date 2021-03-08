import pygame
import sys

pygame.init()

res = (1000,800)
guiDisplay = pygame.display.set_mode(res)
width = guiDisplay.get_width() 
height = guiDisplay.get_height() 

font = pygame.font.SysFont('Merriweather',35)

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (128,128,128)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Background Color
guiDisplay.fill(BLACK)

# Power Button
power_button = pygame.Rect(100,50,70,50)
currentColor = RED
previousColor = GREEN
pygame.draw.rect(guiDisplay, currentColor, power_button)
onText = font.render('ON', True, BLACK)
offText = font.render('OFF', True, BLACK)

# Driving Mode Buttons 
ackermannButton = pygame.Rect(res[0]/2 - 325,200,250,50)
tankButton = pygame.Rect(res[0]/2 + 75,200,250,50)
alt1Color = WHITE
alt2Color = GREY
ackermannText = font.render('Ackermann steering', True, BLACK)
tankText = font.render('Tank mode', True, BLACK)

# Speed Slider
speed = 0



# Steering Angle Slider
steering_angle = 0


running = True
pygame.display.update()
while running:
    mouseClicked = False

    pygame.draw.rect(guiDisplay, currentColor, power_button)
    if currentColor == RED:
        guiDisplay.blit(offText, (120, 75))
    else:
        guiDisplay.blit(onText, (120, 75))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Left and right arrow keys change the steering angle (temporary)
        # Up and down arrows change the speed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if steering_angle > -30:
                    steering_angle -= 5
            if event.key == pygame.K_RIGHT:
                if steering_angle < 30:
                    steering_angle += 5
            if event.key == pygame.K_UP:
                if speed < 100:
                    speed += 10
            if event.key == pygame.K_DOWN:
                if speed > 0:
                    speed -= 10
            
        pygame.draw.rect(guiDisplay, alt1Color, ackermannButton)
        pygame.draw.rect(guiDisplay, alt2Color, tankButton)
        guiDisplay.blit(ackermannText, (185, 210))
        guiDisplay.blit(tankText, (610, 210))

        pygame.draw.rect(guiDisplay, BLACK, (400, 500, 300,300))
        angleDisplay = font.render('Steering angle: ' + str(steering_angle), True, WHITE)
        guiDisplay.blit(angleDisplay, (400, 600))

        speedDisplay = font.render('Speed: ' + str(speed), True, WHITE)
        guiDisplay.blit(speedDisplay, (400, 630))

        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseClicked = True

        if power_button.collidepoint(pos) and mouseClicked:
            temp = currentColor
            currentColor = previousColor
            previousColor = temp

        if ackermannButton.collidepoint(pos) and mouseClicked:
            if alt1Color == WHITE:
                pass
            else:
                alt1Color = WHITE
                alt2Color = GREY

        if tankButton.collidepoint(pos) and mouseClicked:
            if alt2Color == WHITE:
                pass
            else:
                alt1Color = GREY
                alt2Color = WHITE



        pygame.display.update()
        



    