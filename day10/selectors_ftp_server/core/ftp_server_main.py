# -*- coding:utf-8 -*-
#  Author:aling

from selectors_ftp_server.core import ftp_server_auth,transaction,accounts,logger

trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}
def account_info(acc_data):
    print(user_data)

def repay(acc_data):
    '''

    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(account_data['account_id'])
    current_balance = '''------------BALANCE INFO-----
    Credit : %s
    Balance:%s'''%(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input('\033[33;1m Imput repay amount:\033[0m').strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,)
            if new_balance:
                print('''\033[42;1m New Blance:%s\033[0m''')%(new_balance['balance'])
        else:
            print('033\31;1s[%s] is not a valid amount,noly accept,iinteger!')

        if repay_amount == 'b':
            back_flag = True


def withdraw(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])# 加载当前余额信息
    current_balance = '''--------------------BALANCE INFO--------------
        Credit:%s
        Balance:%s
    '''%(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input('\033[33;1mInput repay amount:\033[0m')
        if len(repay_amount) > 0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay',repay_amount)
            if new_balance:
                print('\033[42;1mNew Balance:%s\033[0m'%(new_balance['balance']))
        else:
            print('abc')

def transfer(acc_data):
    pass

def pay_check(acc_data):
    pass

def logout(acc_data):
    pass

def interactive(acc_data)
    '''

    :param acc_data:
    :return:
    '''
    menu = u'''
    ------01dboy Bank----------
    \033[32;1m1.帐户信息
    2.还款
    3.取款
    4.转帐
    5.帐单
    6.退出
    \033[0m
    '''
    menu_dic = {
        '1':account_info,
        '2':repay,
        '3':withdraw,
        '4':transfer,
        '5':pay_check,
        '6':logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input('>>').strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)

def run():
    '''

    :return:
    '''
    acc_data = ftp_server_auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)