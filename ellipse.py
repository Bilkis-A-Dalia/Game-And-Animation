import pygame,sys
from pygame.locals import*

pygame.init()

screen = pygame.display.set_mode((640, 360), 0, 32)

color = (0,255,255)
rectangle = (40,80,150,90)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.lock()
    pygame.draw.ellipse(screen, color, rectangle)
    screen.unlock()
    

    pygame.display.update()