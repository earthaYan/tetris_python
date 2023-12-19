import pygame
from pygame.locals import *
import sys
from const import *
from block import *
from blockGroup import *
from game import *
import json
pygame.init()
DISPLAYSURF=pygame.display.set_mode((GAME_WIDTH_SIZE,GAME_HEIGHT_SIZE))
game=Game(DISPLAYSURF)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            confirm = input("Do you want to save the progress? (y/n) ")
            if confirm.lower() == 'y':
                game.saveProgress()
            elif confirm.lower()=='n':
                game.clearProgress()
            pygame.quit()
            sys.exit()
    game.update() #逻辑帧
    DISPLAYSURF.fill((0,0,0))
    game.draw() #渲染帧
    pygame.display.update()