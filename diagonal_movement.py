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

x,y= 0,0
clock = pygame.time.Clock() #clock method --> used to get the current processor time
speedx,speedy = 150, 170 #for both axis


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

#blit() — blit stands for Block Transfer—and 
# it's going to copy the contents of one Surface onto another Surface
    screen.blit(backgraound,(0,0))
    screen.blit(resized_ball,(x,y))
    
    milli = clock.tick()
    seconds = milli/1000.
    dmx = seconds*speedx
    dmy = seconds*speedy

    x += dmx #distance move-->dm
    y += dmy 

#640-->screen size
    if x>640:
        x = 0
    if y>640:
        y = 0

    pygame.display.update()


