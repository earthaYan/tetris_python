import time
import os
def getCurrentTime():
    # 获取毫秒级别的当前时间
    t=time.time()
    return int(t*1000)

def checkProgressFileIsExist():
    return os.path.exists("progress.json")