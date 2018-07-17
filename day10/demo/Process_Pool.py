# -*- coding:utf-8 -*-
#  Author:aling
from multiprocessing import Process,Pool
import time,os

def Foo(i):
    time.sleep(2)
    print('in process->%s'%i)
    return i+100

def Bar(args):
    print('-->', args,os.getpid())#获取子进程IP，用于确认是否是回调函数

if __name__ == '__main__':
    '''
    在windows中启用多进程 就必须加这句话，
    它的作用是为了区分是主动执行这个脚本，还是它是当做模块被调用
    如果它是主动执行这个脚本，则执行下面这个内容,
    如果它是模块，就不会执行下面的内容，如下面的内容是测试内容，在执行的时候不会去启用下面这段代码
    模块导入__name__的值为模块名
    '''
    pool = Pool(5)#允许进程池时面时放入五个进程processes = 5
    for num in range(10):#启动了10个进程，但是没交给CPU去运行，只同时提交5个给CPU去运行
        pool.apply(func=Foo,args=(num,))
        # pool.apply_async(func=Foo,args=(num,),callback=Bar(num))
        '''
        apple就是串行，劳军apply_async就是并行，执行完后再去执行callback回调函数
        应用场景，备份完数据后写一条记录
        这个bar输出的PID是一致，的是因为调用时，不用多个备份操作都要去写一次日志，
        可以在程序执行完后写一条日志。减轻CPU操作计算
        '''

    print('end')
    pool.close() #先close再join
    pool.join() # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭