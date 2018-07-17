# -*- coding:utf-8 -*-
#  Author:aling
import threading,time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('this is n%s'%n)
    semaphore.release() # 释放锁
semaphore = threading.BoundedSemaphore(5)  # 生成锁实例
statt_time = time.time()
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.start()
while threading.active_count() != 1:
    pass
else:
    print('--all threads done---')
