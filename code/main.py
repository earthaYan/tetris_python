import pygame
from pygame.locals import *
import sys
from const import *
from block import *
import random
from blockGroup import *

pygame.init()
DISPLAYSURF=pygame.display.set_mode((800,600))

blockGroups=[]
for x in range(5):
    print(x)
    conf=BlockGroup.GenerateBlockConfig(x*4,x)
    blockGroups.append(BlockGroup(32,32,conf,(240,50)))
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill((0,0,0))
    for i in blockGroups:
       i.draw(DISPLAYSURF)
    pygame.display.update()