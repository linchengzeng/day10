# -*- coding:utf-8 -*-
#  Author:aling
import socket,time,hashlib,json
sock = socket.socket()
sock.connect(('localhost',8823))
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}
# while True:
retry_count = 0
while user_data['is_authenticated'] is not True and retry_count < 3:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    str_md5_obj = hashlib.md5()
    str_md5_obj.update(password.encode('utf-8'))
    pwd_md5_str = str_md5_obj.hexdigest()
    user_info = {"action":"login","user_info":{"username":username,"password":pwd_md5_str}}
    user_info_json = json.dumps(user_info)
    print(user_info_json)
    sock.send(user_info_json.encode('utf-8'))
    auth_result = sock.recv(1024)
    if auth_result == b'auth_error':
        print("用户名或密码错误!")
        retry_count += 1
    else:
        print(user_data)
        user_data = json.loads(auth_result)
        print("client:%s"%user_data)
        print("输出菜单")
        sock.send(json.dumps({"action":"get_menu"}).encode('utf-8'))
        ftp_menu = sock.recv(1024)
        while True:
            print(json.loads(ftp_menu))
            client_options = input("请选择您需要的操作：")
            if client_options == "exit":
                print("欢迎您再次使用aling select ftp，再见！")
                exit()
            print("client_options",client_options)
            sock.send(json.dumps({"action":client_options}).encode('utf-8'))
        # break
