import pygame,random
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
                'colIdx':colIdx+BLOCK_SHAPE[idx][x][1],
            }
            configList.append(config)
        return configList
    def __init__(self,width,height,blockConfigList,relPos):
        super().__init__()
        self.blocks=[]
        for config in blockConfigList:
            blk=Block(config['blockType'],config['rowIdx'],config['colIdx'],width,height,relPos)
            self.blocks.append(blk)
    def draw(self,screen):
        for b in self.blocks:
            b.draw(screen)