# -*- coding:utf-8 -*-
#  Author:aling
import socket,time,hashlib
sock = socket.socket()
sock.connect(('localhost',8823))
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}
while True:
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        username = input('请输入用户名：')
        password = input('请输入密码：')
        str_md5_obj = hashlib.md5()
        str_md5_obj.update(password.encode('utf-8'))
        pwd_md5_str = str_md5_obj.hexdigest()
        user_info = (username,pwd_md5_str)
        sock.send(str(user_info).encode('utf-8'))
        auth_result = sock.recv(1024)
        print(auth_result.decode('utf-8'))
        if auth_result.decode('utf-8') == 'auth_success':
            print(sock.recv(1024).decode('utf-8'))
    retry_count += 1
