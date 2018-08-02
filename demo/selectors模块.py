# -*- coding:utf-8 -*-
#  Author:aling
import socket,selectors
sel = selectors.DefaultSelector()# selectors封装了select,poll,epoll默认用epoll，和select.select()类似



def accept(sock,mask):
    conn,addr = sock.accept()
    print('conn:%s,addr:%s,mask:%s'%(conn,addr,mask))
    conn.setblocking(False) # 把链接设置为非阻塞模式
    sel.register(conn,selectors.EVENT_READ,read)# 新连接注册到sel当中，read回调函数（如果有数据过来就调用read)，如果新连接活动，就代表有数据进来

# 接收数据
def read(conn,mask):
    data = conn.recv(1024)
    if data:# 如果有数据
        print('echoing:%s'%data)
        conn.send(data)
    else:# 如果没有数据就代表客户端断开
        print('closing:%s'%conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost',8823))
sock.listen(100)
sock.setblocking(False)
sel.register(sock,selectors.EVENT_READ,accept)# 注册事件，将当前的socket注册到sel去监听。只要来了一个新链接，就调用accept函数
while True:
    events = sel.select() # 在这里看到的是select,但程序封装后台有可能调用的是epoll，有可能调用的是select,主要看系统支持啥。
    # 默认它是阻塞的，只要阻塞了，就代表肯定有活动的数据，有活动连接就返回活动的连接列表
    # 假如100个链接里面有返回了，它返回的就是一个列表
    for key,mask in events:
        callable = key.data # accept,就是回调函数 ，callable现在是函数内存地址
        callable(key.fileobj,mask)# fileobj = 文件描述符   # 函数内存地址加上括号就是去执行它。对比select它是还没建议好连接的R

'''
#列表生成式'''
# sockets = [socket.socket(socket.AF_INET,socket.SOCK_STREAM) for i in range(300)]