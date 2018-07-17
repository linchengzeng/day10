# -*- coding:utf-8 -*-
#  Author:aling
from multiprocessing import Process,Pipe
def run(conn):
    conn.send([42,None,'hello from child1']) # 子进程Queue
    conn.send([42,None,'hello from child2']) # 子进程Queue
    conn.send([42,None,'hello from child4']) # 子进程Queue
    conn.close()
if __name__ =='__main__':
    parent_conn,child_conn = Pipe()
    p = Process(target = run,args=(child_conn,))   # 这里相当于克隆了一个Q，并序列化后给子进程，子进程反序列化之后再取出数据
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())