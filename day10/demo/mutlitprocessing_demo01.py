# -*- coding:utf-8 -*-
#  Author:aling
import multiprocessing,time,os
def run(n):
    print('task',n)
    print(os.getppid())  #获得父进程号
    print(os.getpid())  #获得自身进程号

if __name__ =='__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run,args=('bob',))
        p.start()

