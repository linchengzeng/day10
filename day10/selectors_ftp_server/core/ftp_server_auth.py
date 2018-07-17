# -*- coding:utf-8 -*-
#  Author:aling
import os,sys,json,time
from selectors_ftp_server.conf import settings
from selectors_ftp_server.core import db_handler
base_dir = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
# print(base_dir) -> D:\python\day10\selectors_ftp_server
sys.path.append(base_dir)
def acc_auth(account,password):
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = '%s%s.json'%(db_path,account)
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['e']))
                if time.time() > exp_time_stamp:
                    print('\033[31;1m Account[%s] has expried,please')
                else:
                    return account_data
            else:
                print('\033[01;1mAccount ID or pasword is incorrect!\033[0m')

def acc_login(acc_data,log_obj):
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth(account,password)
        if auth: # 如果没有数据返回 not none
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count += 1
    else:
        log_obj.error('account [%s] too many attempts'%account)
        exit()

class Authencation_user(object):
    def __init__(self,username,password):
        self.username = username,
        self.password = password

    def auth_user(self):
        sql = 'select '