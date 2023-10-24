import pygame,sys,random
from pygame.locals import *
from block import *
from const import *
from blockGroup import *
screen=pygame.display.set_mode((800,600))

pygame.init()
blockGroups=[]
for x in range(5):
    conf=BlockGroup.GenerateBlockGroupConfig(x*4,x)
    blockGroups.append(BlockGroup(32,32,conf,[240,50]))
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    for bg in blockGroups:
        bg.draw(screen)
    pygame.display.flip()