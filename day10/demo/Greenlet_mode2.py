# -*- coding:utf-8 -*-
#  Author:aling
from greenlet import greenlet
import gevent
def foo():
    print('running in foo')
    gevent.sleep(2)  # 卡2秒执行IO操作 gevent.sleep模拟IO操作
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(1) #卡1秒，执行IO操作
    print('Implicit context switch back to bar')

def foo3():
    print('running func3')
    gevent.sleep(0) # 不卡，仅IO操作
    print('running func3 again')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(foo3)
])