# -*- coding:utf-8 -*-
#  Author:aling
import threading,time

def run(n):
    lock.acquire()  # 获得一把锁
    global num
    time.sleep(1)
    num += 1
    print(num)
    lock.release() # 释放锁
lock = threading.Lock()  # 生成锁实例
num = 0
statt_time = time.time()
t_objs = []
for i in range(5):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.start()
    t_objs.append(t)
#
for t in t_objs:
    t.join()

print('cost:%s'%(time.time()-statt_time))
print(num)