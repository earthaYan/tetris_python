import pygame
from pygame.locals import *
from blockGroup import *
class Game(pygame.sprite.Sprite):
    def __init__(self,surface):
        super().__init__()
        self.surface=surface
        self.fixedBlockGroup=BlockGroup(BlockGroupType.FIXED,BLOCK_SIZE_W,BLOCK_SIZE_H,[],self.getRelPos())
        self.dropBlockGroup=None
    
    def generateDropBlockGroup(self):
        conf=BlockGroup.GenerateBlockGroupConfig(0,GAME_COL/2-1)
        self.dropBlockGroup=BlockGroup(BlockGroupType.DROP,BLOCK_SIZE_W,BLOCK_SIZE_H,conf,self.getRelPos())

    def update(self):
        # 执行两者的update
        self.fixedBlockGroup.update()
        if self.dropBlockGroup:
            self.dropBlockGroup.update()
        else :
            self.generateDropBlockGroup()
        if self.willCollide():
            blocks=self.dropBlockGroup.getBlocks()
            for blk in blocks:
                self.fixedBlockGroup.addBlocks(blk)
            self.dropBlockGroup.clearBlocks()
            self.dropBlockGroup=None
    
    def draw(self):
        self.fixedBlockGroup.draw(self.surface)
        if self.dropBlockGroup:
            self.dropBlockGroup.draw(self.surface)
            
    def getRelPos(self):
        return (240,50)
    
    def willCollide(self):
        # 碰撞检测函数
        hash={}
        allIndexes=self.fixedBlockGroup.getBlockIndexes()
        for idx in allIndexes:
            hash[idx]=1
        dropIndexes=self.dropBlockGroup.getNextBlockIndexes()
        for dropIdx in dropIndexes:
            if hash.get(dropIdx):
                return True
            if dropIdx[0]>=GAME_ROW:
                return True
        return False
            
        