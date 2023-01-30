import pygame
import matplotlib.colors
import time
import random

pygame.init()

display_width = 300
display_height = 200

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

block_color = (53, 115, 255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()



def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 15)
    TextSurf, TextRect = text_objects(text, largeText)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("verdana",12)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def oui():
    print("Danut donut")
def non():
    pass
a = oui()

def interruption():

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill("white")
        largeText = pygame.font.SysFont("verdana", 15)
        TextSurf, TextRect = text_objects("Voulez vous interrompre?", largeText)
        TextRect.center = ((150, 70))
        gameDisplay.blit(TextSurf, TextRect)

        button("Oui!", 65, 100, 70, 40, (34,139,34), (0,255,0), oui)
        button("Non", 165, 100, 70, 40, "blue", "turquoise", None)

        pygame.display.update()
        clock.tick(60)

interruption()