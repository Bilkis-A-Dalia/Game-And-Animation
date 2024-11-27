bif = 'bg.bmp'
mif = 'ball.png'

import pygame, sys
from pygame.locals import *

pygame.init()

# Set up the screen and load assets
screen = pygame.display.set_mode((640, 360), 0, 32)
background = pygame.image.load(bif).convert()
mouse_c_original = pygame.image.load(mif).convert_alpha()
mouse_c = pygame.transform.scale(mouse_c_original, (50, 50)) 

# Initialize position and movement variables
x, y = 0, 0
movex, movey = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                movex = -1
            elif event.key == K_RIGHT:
                movex = 1
            elif event.key == K_UP:
                movey = -1
            elif event.key == K_DOWN:
                movey = 1

        if event.type == KEYUP:
            if event.key == K_LEFT:
                movex = 0
            elif event.key == K_RIGHT:
                movey = 0
            elif event.key == K_UP:
                movey = 0
            elif event.key == K_DOWN:
                movey = 0

    # Update position
    x += movex
    y += movey

    # Prevent movement outside screen boundaries
    x = max(0, min(x, screen.get_width() - mouse_c.get_width()))
    y = max(0, min(y, screen.get_height() - mouse_c.get_height()))

    # Draw the background and image
    screen.blit(background, (0, 0))
    screen.blit(mouse_c, (x, y))

    pygame.display.update()
