import pygame
from pygame.locals import *
import sys
from const import *
from block import *
from blockGroup import *
from game import *

pygame.init()
DISPLAYSURF=pygame.display.set_mode((800,600))
game=Game(DISPLAYSURF)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    game.update() #逻辑帧
    DISPLAYSURF.fill((0,0,0))
    game.draw() #渲染帧
    pygame.display.update()