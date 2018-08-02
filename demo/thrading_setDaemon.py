# -*- coding:utf-8 -*-
#  Author:aling
import threading,time
def run(n,sleep_time):
    print('task',n)
    time.sleep(sleep_time)

statt_time = time.time()
for i in range(50):
    p1 = threading.Thread(target=run,args=('aling%s'%i,2,))
    p1.setDaemon(True) #r把当前线程设置为守护线程
    p1.start()

print('cost:%s'%(time.time()-statt_time))