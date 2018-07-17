# -*- coding:utf-8 -*-
#  Author:aling
import queue
q = queue.Queue() # 先进先出
q.put('abc')
q.put('bed')
print(q.get(1))
q2 = queue.LifoQueue() # 后进先出
q2.put('abc')
q2.put('bed')
print(q2.get(1))
q3 = queue.PriorityQueue() # 优先级进出，值越小优先级越高
q3.put((10,'vip_abc'))
q3.put((-1,'bed'))
q3.put((6,'aling_vip'))
q3.put((-5,'alina_vip'))
print(q3.get(1))
print(q3.get(2))
print(q3.get(3))