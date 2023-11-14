class BlockType:
    RED=0
    ORANGE=1
    YELLOW=2
    GREEN=3
    CYAN=4
    BLUE=5
    PURPLE=6
    BLOCKMAX=7

BLOCK_RES={
    BlockType.RED:'../pic/red.png',
    BlockType.ORANGE:'../pic/orange.png',
    BlockType.YELLOW:'../pic/yellow.png',
    BlockType.GREEN:'../pic/green.png',
    BlockType.CYAN:'../pic/cyan.png',
    BlockType.BLUE:'../pic/blue.png',
    BlockType.PURPLE:'../pic/purple.png',
}

GAME_ROW=17
GAME_COL=10

BLOCK_SHAPE=[
    [(0,0),(0,1),(1,0),(1,1)], #方形
    [(0,0),(0,1),(0,2),(0,3)], #长条
    [(0,0),(0,1),(1,1),(1,2)], #z字形
    [(0,1),(1,0),(1,1),(1,2)]  #飞机形
]

class BlockGroupType:
    FIXED=0
    DROP=1
    
BLOCK_SIZE_W=32
BLOCK_SIZE_H=32