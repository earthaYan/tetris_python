import pygame
from pygame.locals import *
from blockGroup import *
class Game(pygame.sprite.Sprite):
    def __init__(self,surface):
        super().__init__()
        self.surface=surface
        self.gameOverImage=pygame.image.load('../pic/lose.png')
        self.isGameOver=False
        self.fixedBlockGroup=BlockGroup(BlockGroupType.FIXED,BLOCK_SIZE_W,BLOCK_SIZE_H,[],self.getRelPos())
        self.dropBlockGroup=None
    
    def generateDropBlockGroup(self):
        conf=BlockGroup.GenerateBlockGroupConfig(0,GAME_COL/2-1)
        self.dropBlockGroup=BlockGroup(BlockGroupType.DROP,BLOCK_SIZE_W,BLOCK_SIZE_H,conf,self.getRelPos())

    def update(self):
        if self.isGameOver:
            return
        self.checkGameOver()
        # 执行两者的update
        self.fixedBlockGroup.update()
        if self.fixedBlockGroup.IsEliminating():
            return 
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
            self.fixedBlockGroup.processEliminate()
    
    def draw(self):
        self.fixedBlockGroup.draw(self.surface)
        if self.dropBlockGroup:
            self.dropBlockGroup.draw(self.surface)
        if self.isGameOver:
            self.surface.fill((0,0,0))
            rect=self.gameOverImage.get_rect()
            rect.centerx=GAME_WIDTH_SIZE/2
            rect.centery=GAME_HEIGHT_SIZE/2
            self.surface.blit(self.gameOverImage,rect)
            
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
    def checkGameOver(self):
        allIndexes=self.fixedBlockGroup.getBlockIndexes()
        for idx in allIndexes:
            if idx[0]<2:
                self.isGameOver=True
            
        