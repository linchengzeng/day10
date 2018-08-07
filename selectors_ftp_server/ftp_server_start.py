# -*- coding:utf-8 -*-
#  Author:aling
import socket,select,time,queue
from selectors_ftp_server.core import logger,interactive,ftp_server_auth as auth

sock = socket.socket()
sock.bind(('localhost',8823))
sock.listen(100)
sock.setblocking(0)
data_dict = {}
# 将socket放入select监测，如果活动则表示有新连接
inputs = [sock,]
outputs = []
trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}
def account_info(user_data):
    print(user_data)

def repay(acc_data):
    print(acc_data)

while True:
    readable,writeable,exceptional = select.select(inputs,outputs,inputs)
    # readable,writeable,exceptional =select.select(inputs, outputs, inputs)
    for activity_sock in readable:
        if activity_sock is sock:
            # 新连接连入
            # activity 表示活动连接的socket
            conn,raddr = activity_sock.accept()
            # conn放入select监测，如果活动则表示有数据
            inputs.append(conn)
            data_dict[conn] = queue.Queue()
        else:
            # 有数据进来
            try:
                acc_input_data = activity_sock.recv(1024)
                print('收到用户名密码为：%s'%acc_input_data)
                acc_data = auth.acc_login(user_data,acc_input_data,logger)
                print("acc_data:",acc_data)
                if user_data['is_authenticated']:
                    user_data['account_data'] = acc_data
                    print('验证通过:',user_data)
                    data_dict[activity_sock].put(b'auth_success')# 返回的数据
                    interactive.Interactive_Service(user_data,activity_sock)
                    # data_dict[activity_sock].put(res)
                else:
                    data_dict[activity_sock].put(b'auth_error')  # 返回的数据
                outputs.append(activity_sock)
            except Exception as e:
                print('客户端%s断开连接。。。'%activity_sock)
                print(e)
                outputs.append(activity_sock)
                inputs.remove(activity_sock)
    # 发送数据
    for activity_sock in writeable:
        data_to_client = data_dict[activity_sock].get()
        activity_sock.send(data_to_client)
        outputs.remove(activity_sock)
    # 移除无用监测
    for activity_sock in exceptional:
        if activity_sock in outputs:
            outputs.remove(activity_sock)
        inputs.remove(activity_sock)
        del data_dict[activity_sock]
