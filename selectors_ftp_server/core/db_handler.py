# -*- coding:utf-8 -*-
#  Author:aling
def file_db_handle(conn_params):
    '''

    :param conn_params:
    :return:
    '''
    print('file db:',conn_params)
    db_path = "%s%s"%(conn_params['path'],conn_params['name'])
    return db_path

def mysql_db_handle(conn_params):
    pass

def db_handle(conn_parms):
    '''

    :param conn_parms:v如果设置文件中写的是file_storage就调用file_db_handle
    :return:
    '''
    if conn_parms['engine'] == 'file_storage':
        return file_db_handle(conn_parms)
    elif conn_parms['engine'] == 'mysql':
        return mysql_db_handle(conn_parms)