## 安装 python

## 安装游戏环境

```bash
pip install pygame
# 测试，如果成功会运行示例游戏
py -m pygame.examples.aliens
```

## 建立对应文件夹/code 和/pic

## 初始化 pygame

```py
# 整个pygame模块导入到当前的命名空间中
import pygame
# 从pygame.locals模块中导入了所有内容，并将其直接导入当前的命名空间，无需通过模块前缀访问
from pygame.locals import *
# 游戏初始化
pygame.init()
```

## 主循环

```py
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() //此处报错
```

## 创建游戏窗口

```py
DISPLAYSURF=pygame.display.set_mode((800,600))
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
```

## 显示图片

```py
Image=pygame.image.load('../pic/yellow.png')
Rect=Image.get_rect()
Rect.center=(400,300)

DISPLAYSURF.blit(Image,Rect)
```

## 图片移动

```py
while True:
    for event in pygame.event.get():
        # 注释
        Rect.centerx+=random.randint(-1,1)
```

## 去除阴影

解决方案：每次渲染之前先把屏幕涂黑

```py
    DISPLAYSURF.fill((0,0,0))
    DISPLAYSURF.blit(Image,Rect)
```

## 控制移动

通过左右按键控制方块移动

```py
pressed=pygame.key.get_pressed()
if pressed[K_LEFT]:
    Rect.move_ip(-1,0) # move_ip代表根据当前的位置进行移动
elif pressed[K_RIGHT]:
    Rect.move_ip(1,0)
```

## 增加上下方向

## 实现方块类

## 多实例

## 拆分文件
