# -*- coding:utf-8 -*-
#  Author:aling
import socket,select,time,queue,json,os
from selectors_ftp_server.core import logger,interactive,ftp_server_auth as auth
from selectors_ftp_server.conf import settings
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
    print("等待客户端信息输入~")
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
                print('收到信息为：%s'%acc_input_data)
                print(acc_input_data.split(" "))
                client_input_info = json.loads(acc_input_data.split(" "))
                client_action = client_input_info[0]
                # if client_input_info is dict:
                if client_action == "login":
                    acc_data = auth.acc_login(client_input_info["user_info"],logger)
                    print("acc_data_auth:",acc_data['is_authenticated'])
                    if acc_data['is_authenticated']:
                        user_data = acc_data
                        print('验证通过:', user_data)
                        data_dict[activity_sock].put(json.dumps('auth_success').encode('utf-8'))# 返回的数据
                    else:#登录信息错误
                        data_dict[activity_sock].put(json.dumps('auth_error').encode('utf-8'))  # 返回的数据
                elif client_action == "get_menu":#非登录操作
                    data_dict[activity_sock].put(json.dumps(settings.FTP_MAIN_MENU_INFO).encode('utf-8'))
                elif client_action == "get":
                    print(json.dumps(client_input_info))
                    data_dict[activity_sock].put(json.dumps(settings.FTP_MAIN_MENU_INFO).encode('utf-8'))
                elif client_action == "put":
                    data_dict[activity_sock].put(json.dumps(settings.FTP_MAIN_MENU_INFO).encode('utf-8'))
                outputs.append(activity_sock)
            except Exception as e:
                print('客户端%s断开连接。。。'%activity_sock)
                print(e)
                outputs.append(activity_sock)
                inputs.remove(activity_sock)
    # 发送数据
    for activity_sock in writeable:
        data_to_client = data_dict[activity_sock].get()
        print("data_to_client",data_to_client)
        activity_sock.send(data_to_client)
        outputs.remove(activity_sock)
    # 移除无用监测
    for activity_sock in exceptional:
        if activity_sock in outputs:
            outputs.remove(activity_sock)
        inputs.remove(activity_sock)
        del data_dict[activity_sock]

# 文件下载
def get_file(user_home, user_in_path,get_file_name):
    # print('this is ftp server line 72')
    print('当前所在目录：', user_in_path)
    f_name = get_file_name
    print('从客户端发过来的请求下载的文件名称：%s' % f_name.decode('utf-8'))
    file_path = user_in_path + '/' + f_name.decode('utf-8')
    print(file_path)
    if os.path.exists(file_path):
        f_size = os.path.getsize(file_path)  # 文件大小
        print('被请求文件大小', f_size)
        conn.send(str(f_size).encode('utf-8'))  # 发送file_exist 表示文件存在并开始传送文件
        send_break = conn.recv(204800).decode('utf-8')  # 接收到send_break表示客户端文件存在
        print('send_break:', send_break)
        if send_break == 'send_break':
            print('客户端出错')
            return None
        sended_size = 0  # 已发送文件大小
        # conn.send('abcdefg'.encode('utf-8'))
        i = 0
        with open(file_path, 'rb') as f:
            while f_size - sended_size >= 204800:
                print('文件大小：', f_size)
                # print('未发送文件大小：', f_size - sended_size)
                # print('读取前光标句柄所在位置：', f.tell())
                if f_size - sended_size > 204800:
                    contest = f.read(204800)
                else:
                    contest = f.read(f_size - sended_size)
                # print('将要发送的内容大小：', len(contest))
                conn.send(contest)  # 发送本次读取到的信息
                sended_size += len(contest)
                f.seek(sended_size)  # 将光标句柄移至已发送的位置（即从光标开始往后都是未发送的内容)
                # print('光标句柄所在位置：', f.tell())
                i += 1
                print('发送了:', i, '次')
                print('已发送文件大小：', sended_size)
            else:
                print('准备发送最后一次')
                print('读取前光标句柄所在位置：', f.tell())
                print('剩余文件大小', f_size - sended_size)
                contest = f.read(f_size - sended_size)
                print('contest len:', len(contest))
                conn.sendall(contest)
                # conn.send(b'send_session')
                print('文件发送完毕！')
                # conn.send(b'send_session')
                # return self.start()
    else:
        conn.send('file_error'.encode('utf-8'))
        return None