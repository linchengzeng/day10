# -*- coding:utf-8 -*-
#  Author:aling
import json
from selectors_ftp_server.core import db_handler
from selectors_ftp_server.conf import settings
def dump_account(account_data):
    db_path = db_handler.db_handle(settings.DATABASE)
    account_file = '%s%s.json'%(db_path,account_data['id'])
    with open(account_file,'w') as f:
        acc_data = json.dump(account_data,f)
    return  True
def load_current_balance(account_id):
    db_path = db_handler.db_handle(settings.DATABASE)
    account_file = "%s%s.json"%(db_path,account_id)
    with open(account_file) as f:
        acc_data = json.load(f)

def dump_account(account_data):
    '''
    :param account_data:
    :return:
    '''
    pass