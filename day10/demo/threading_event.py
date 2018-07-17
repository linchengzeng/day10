# -*- coding:utf-8 -*-
#  Author:aling
import threading,time
event = threading.Event()
def lighter():
    count = 0
    event.set() #标志位初始化
    while True:
        if  count > 5 and count < 11: # 改成红灯
            event.clear()  # 把标志位清了
            print('\033[41;1mred light is on ...\033[0m%s'%count)
        elif count >10:
            event.set() # 变绿灯
            print('清空标志位，表示清空绿灯，变红灯%s'%count)
            count = 0 # 表示开始重新计数
        else:
            print('\033[42;1mgreen light is on ...\033[0m%s'%count)
        time.sleep(1)
        count += 1

def cars():
    i = 0
    while True:
        i += 1
        if event.is_set():# 如果为真，表示设置了标志位，为绿灯
            print('running car:%s '%i )
            time.sleep(1)
        else:
            print('sees red light is on,waiting....')
            event.wait()
            print('\033[34;1m green light is on ,start going...\033[1m')
hight = threading.Thread(target=lighter,)
hight.start()

car = threading.Thread(target=cars,)
car.start()
# event.wait()
# 等待标志位被设置，未被设置的时候，不允许通行（未被设置成绿灯的时候）
# 如果标志位被设置，代表绿灯了，可以通行，如果标志位被清空，则代表红灯，变成阻塞状态，等待变绿灯
# 多个线程可以使用同一个标志位
# count = 0
# while True:
#     if count <30:
#         print('red')

