# -*- coding:utf-8 -*-
#  Author:aling
import socket,time,hashlib
sock = socket.socket()
sock.connect(('localhost',8823))
while True:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    str_md5_obj = hashlib.md5()
    str_md5_obj.update(password.encode('utf-8'))
    pwd_md5_str = str_md5_obj.hexdigest()
    user_info = (username,pwd_md5_str)
    sock.send(str(user_info).encode('utf-8'))
    auth_result = sock.recv(1024)
