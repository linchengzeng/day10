# -*- coding:utf-8 -*-
#  Author:aling
from multiprocessing import Process,Queue
def run(n):
    print('task',n)
    n.put([42,None,'hello']) # 子进程Queue
if __name__ =='__main__':
    q = Queue()  # 主进程Queue
    p = Process(target = run,args=(q,))   # 这里相当于克隆了一个Q，并序列化后给子进程，子进程反序列化之后再取出数据
    p.start()
    print(q.get())
    p.join()