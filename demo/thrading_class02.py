# -*- coding:utf-8 -*-
#  Author:aling
import threading,time
class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyThread,self).__init__()#继承父类的init方法
        self.n = n
        self.sleep_time =sleep_time

    def run(self): #必须写成run
        print('runnint task',self.n)
        time.sleep(2)

start_time = time.time()
p1 = MyThread('p1',2)
p2 = MyThread('p1',4)
p1.start()
p1.join()
p2.start()

print('task done ...:',time.time()-start_time)