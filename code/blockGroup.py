import random
import pygame,sys
from pygame.locals import *
from const import *
from block import *

class BlockGroup(object):
    def GenerateBlockGroupConfig(rowIdx,colIdx):
        idx=random.randint(0,len(BLOCK_SHAPE)-1)
        bType=random.randint(0,BlockType.BLOCKMAX-1)
        configList=[]
        for x in range(len(BLOCK_SHAPE[idx])):
            config={
                'blockType':bType,
                'rowIdx':rowIdx+BLOCK_SHAPE[idx][x][0],
                'colIdx':colIdx+BLOCK_SHAPE[idx][x][1]
            }
            configList.append(config)
        return configList
    
    def __init__(self,blockGroupType,width,height,blockConfigList,relPos):
        super().__init__()
        self.blocks=[]
        self.time=0
        self.blockGroupType=blockGroupType
        for config in blockConfigList:
            blk=Block(config['blockType'],config['rowIdx'],config['colIdx'],width,height,relPos)
            self.blocks.append(blk)
            
    def draw(self,surface):
        for b in self.blocks:
            b.draw(surface)

    def update(self):
        self.time+=1
        if self.blockGroupType==BlockGroupType.DROP:
            if self.time>=1000:
                self.time=0
                for b in self.blocks:
                    b.drop()
                    
    def getBlockIndexes(self):
        return [block.getIndex() for block in self.blocks]
    def getNextBlockIndexes(self):
        return [block.getNextIndex() for block in self.blocks]
    def getBlocks(self):
        return self.blocks
    def clearBlocks(self):
        self.blocks=[]
    def addBlocks(self,blk):
        self.blocks.append(blk)