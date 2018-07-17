# -*- coding:utf-8 -*-
#  Author:aling
import socket,gevent
s = socket.socket()
s.connect(('localhost',8823))
while True:
    inputs = input('>>')
    s.send(inputs.encode('utf-8'))
# data = s.recv(1024)
# print(data)