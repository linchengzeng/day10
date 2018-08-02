# -*- coding:utf-8 -*-
#  Author:aling
from multiprocessing import Process,Lock

def f(l,i):
    l.acquire()
    print('hello world',i)
    l.release()

if __name__ == '__main__':
    lock = Lock() # 这个锁的作用就是在屏幕输出的时候，不会乱，比如说输出hello world，不会说打成hellhelloo worworldld
    for num in range(10):
        Process(target=f,args=(lock,num)).start()