import pygame,sys
from pygame.locals import*

pygame.init()

screen = pygame.display.set_mode((640, 360), 0, 32)

# corners
points = [(20,120),(140,140),(110,30)] 
color = (255,255,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.lock()
    pygame.draw.polygon(screen,color,points)
    screen.unlock()
    

    pygame.display.update()