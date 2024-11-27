import pygame,sys
from pygame.locals import*

pygame.init()

screen = pygame.display.set_mode((640, 360), 0, 32)
color = (230,170,0)

# position
position = (300,176)
radius = (60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.lock()
    pygame.draw.circle(screen,color,position,radius)
    screen.unlock()
    

    pygame.display.update()