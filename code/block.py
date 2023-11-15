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
        self.image=pygame.image.load(BLOCK_RES[self.blockType])
        self.image=pygame.transform.scale(self.image,(self.width,self.height))
    def updateImagePos(self):
        self.rect=self.image.get_rect()
        # 设置方块对象x轴的位置坐标
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
    def draw(self,surface):
        surface.blit(self.image,self.rect)
    def drop(self):
        self.rowIdx+=1
        self.updateImagePos()
    def getIndex(self):
        # 获取block当前的坐标
        return (int(self.rowIdx),int(self.colIdx))
    def getNextIndex(self):
        # 获取block下落之后的坐标
        return (int(self.rowIdx+1),int(self.colIdx))
    def isLeftBound(self):
        # 边界判断
        return self.colIdx==0
    def isRightBound(self):
        return self.colIdx==GAME_COL-1
    def doLeft(self):
        # 左右移动
        self.colIdx-=1
    def doRight(self):
        self.colIdx+=1