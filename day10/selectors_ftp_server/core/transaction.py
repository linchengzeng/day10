# -*- coding:utf-8 -*-
#  Author:aling
from  selectors_ftp_server.conf import settings
from selectors_ftp_server.core import accounts
def make_transaction(log_obj,account_data,tran_type,amount,**other):
    '''
    deal all the user transactions
    :param log_obj:
    :param account_data:user acount data
    :param tran_type:transaction type
    :param amount:transaction amount
    :param other:mainly for logging usage
    :return:
    '''
    amount = float(amount)
    if tran_type in settings.TRANSACTION_TYPE:# 交易类型
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']# 手续费 = 金额*手续费点数
        old_balance = account_data['balance']
        if settings.TRANSACTION_TYPE[tran_type]['action']== 'plus':
            new_balance = old_balance + amount + interest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            if new_balance < 0:# 额度不足
                print('''\033[31;1m Your credit [%s] is not enough for this transaction[%s],your current balance is
                [%s]'''%(account_data['credit'],(amount+interest),old_balance))
                return
        account_data['balance'] = new_balance
        accounts.dump_account(account_data)
        log_obj.info('account:%s   action:%s amount:%s interest:%s'%(account_data['id'],tran_type,amount,interest))
        return account_data
    else:
        print('\033[31;1mTransaction type[%s] is not exits!\033[0m'%tran_type)
