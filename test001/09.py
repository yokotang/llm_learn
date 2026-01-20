import time
ticks =1459996086.7115328
# ticks =time.time()
# print(ticks)
localtime=time.asctime(time.localtime(ticks))
print(localtime)