import pygame
from pygame.locals import *
from blockGroup import *
import json
class Game(pygame.sprite.Sprite):
    def __init__(self,surface):
        super().__init__()
        self.surface=surface
        self.gameOverImage=pygame.image.load('../pic/lose.png')
        self.isGameOver=False
        self.scoreFont=pygame.font.Font(None,60)
        self.score=0
        self.fixedBlockGroup=BlockGroup(BlockGroupType.FIXED,BLOCK_SIZE_W,BLOCK_SIZE_H,[],self.getRelPos())
        self.dropBlockGroup=None
        self.nextBlockGroup=None
        self.generateNextDropBlockGroup()

    
    def generateDropBlockGroup(self):
        self.dropBlockGroup=self.nextBlockGroup
        self.dropBlockGroup.setBaseIndexes(0,GAME_COL/2-1)
        self.generateNextDropBlockGroup()
        
    def generateNextDropBlockGroup(self):
        conf=BlockGroup.GenerateBlockGroupConfig(0,GAME_COL+3)
        self.nextBlockGroup=BlockGroup(BlockGroupType.DROP,BLOCK_SIZE_W,BLOCK_SIZE_H,conf,self.getRelPos())
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
            if self.fixedBlockGroup.processEliminate():
                self.score+=1
    
    def draw(self):
        self.fixedBlockGroup.draw(self.surface)
        if self.dropBlockGroup:
            self.dropBlockGroup.draw(self.surface)
        self.nextBlockGroup.draw(self.surface)
        if self.isGameOver:
            self.surface.fill((0,0,0))
            rect=self.gameOverImage.get_rect()
            rect.centerx=GAME_WIDTH_SIZE/2
            rect.centery=GAME_HEIGHT_SIZE/2
            self.surface.blit(self.gameOverImage,rect)
        scoreTextImage=self.scoreFont.render('Score:'+str(self.score),True,(255,255,255))
        self.surface.blit(scoreTextImage,(10,20))   
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
            
    def saveProgress(self):
        score=self.saveScore()
        progress={
            "score":score,
        }
        with open("progress.json","w") as file:
            json.dump(progress,file)

    def saveScore(self):
        return self.score   
    
    def loadProgress(self):
        try:
            with open("progress.json","r") as file:
                previousProgress=json.load(file)
            self.score=previousProgress['score']
        except FileNotFoundError:
            print("No previous progress found. Starting a new game...")
            