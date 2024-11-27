import pygame,sys
from pygame.locals import*

pygame.init()
screen = pygame.display.set_mode((640, 360), 0, 32)

color = (0,255,255)
position1 = (20,20)
position2 = (150,143)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.lock()
    pygame.draw.line(screen,color,position1,position2,10)
    screen.unlock()
    

    pygame.display.update()

