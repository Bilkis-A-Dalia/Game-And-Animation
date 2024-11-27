# in this program ball passes left to right to fast
bif = 'bg.bmp'
mif= 'ball.png'

import pygame,sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,340),0,32)
backgraound = pygame.image.load(bif).convert()
original_ball = pygame.image.load(mif).convert()
resized_ball = pygame.transform.scale(original_ball, (50, 50)) 

x=0
clock = pygame.time.Clock() #clock method --> used to get the current processor time
speed = 250


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(backgraound,(0,0))
    screen.blit(resized_ball,(x,160))
    
    milli = clock.tick()
    seconds = milli/1000.
    dm= seconds*speed
    x += dm #distance move-->dm


    if x>640:
        x=0
    pygame.display.update()


