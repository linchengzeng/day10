# -*- coding:utf-8 -*-
#  Author:aling
import threading,time,queue
q = queue.Queue(maxsize=10) #maxsize表示 最多生产10个包子
'''
  生产包子函数
'''
def Producer(name):
    i = 0
    while True:
        i +=1
        q.put('包子%s'%i)
        print('生产包子%s'%i)
        time.sleep(3) #三秒生产一个

'''
  消费包子函数
'''
def Consumer(name):
    while True:  #表示有包子，不能使用q.qsize()>0 否则当队列中数据不够时，这个部分就跳出去不再执行了
        print('开始吃包子了')
        print('%s 取到 %s 并吃了它...'%(name,q.get()))
        time.sleep(1)

if __name__ == '__main__':
    p = threading.Thread(target=Producer,args=('aling',)) # 一个生产者
    c = threading.Thread(target=Consumer,args=('alina',)) # 一个消费者
    c2 = threading.Thread(target=Consumer,args=('aping',)) # 第二个消费者
    p.start()
    c.start()
    c2.start()