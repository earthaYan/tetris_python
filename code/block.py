import pygame
from pygame.locals import *
from const import *

class Block(pygame.sprite.Sprite):
    def __init__(self,blockType,rowIdx,colIdx,width,height,relPos):
        super().__init__()
        self.blockType=blockType
        self.rowIdx=rowIdx
        self.colIdx=colIdx
        self.width=width
        self.height=height
        self.relPos=relPos
        self.loadImage()
        self.updateImagePos()
    def loadImage(self):
        self.img=pygame.image.load(BLOCK_RES[self.blockType])
        self.img=pygame.transform.scale(self.img,(self.width,self.height))
    def updateImagePos(self):
        self.rect=self.img.get_rect()
        self.rect.left=self.relPos[0]+self.width*self.colIdx   
        self.rect.top=self.relPos[1]+self.height*self.rowIdx
    def update(self):
        pressed=pygame.key.get_pressed()
        if pressed[K_LEFT]:
            self.rect.move_ip(-1,0)
        elif pressed[K_RIGHT]:
            self.rect.move_ip(1,0)
        elif pressed[K_UP]:
            self.rect.move_ip(0,-1)
        elif pressed[K_DOWN]:
            self.rect.move_ip(0,1)
    def draw(self,screen):
        screen.blit(self.img,self.rect)
        
