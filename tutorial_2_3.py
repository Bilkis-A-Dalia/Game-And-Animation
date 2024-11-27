bif = 'bg.bmp'
mif= 'ball.png'

import pygame, sys
from pygame.locals import*

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)

background = pygame.image.load(bif).convert()
mouse_c_original = pygame.image.load(mif).convert_alpha()
mouse_c = pygame.transform.scale(mouse_c_original, (50, 50)) 

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    screen.blit(background,(0,0))

    x,y = pygame.mouse.get_pos()
    x -= mouse_c.get_width()
    y -= mouse_c.get_height()

    screen.blit(mouse_c,(x,y))

    pygame.display.update()

    