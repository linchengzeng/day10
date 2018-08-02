# -*- coding:utf-8 -*-
#  Author:aling
import logging,os
BASE_DIR =os.path.dirname(os.path.dirname(__file__))
DATABASE = {
    'engine':'file_storage',
    'name':'accounts',
    'path':"%s/db/"%BASE_DIR
}
LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction':'transactions.log',
    'access':'access.log'
}
TRANSACTION_TYPE = {
    'repay':{'action':'plus','interest':0},
    'withdraw':{'action':'minus','interest':0.05},
    'transfer':{'action':'minus','interest':0.05},
    'consume':{'action':'minus','interest':0}
}

FTP_MAIN_MENU_INFO = '''
    get_file:下载文件
    show_files：显示当前文件夹
    put_file：上传文件
    cd_files：切换目录
    editor_info：修改个人信息
    exits：退出程序
'''