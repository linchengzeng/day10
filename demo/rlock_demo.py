# -*- coding:utf-8 -*-
#  Author:aling

import threading
def run1():
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num


def run2():
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2

def run3():
    lock.acquire()
    res = run1()
    print('between run1 and run2')
    res2 = run2()
    lock.release()
    print(res,res2)
lock = threading.RLock()
num,num2 = 1,0
for i in range(10):
    t = threading.Thread(target=run3)
    t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('---all threads done----')