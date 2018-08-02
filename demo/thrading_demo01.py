# -*- coding:utf-8 -*-
#  Author:aling
import threading,time
def run(n,sleep_time):
    print('task',n)
    time.sleep(sleep_time)

statt_time = time.time()

p1 = threading.Thread(target=run,args=('aling',2,))
p2 = threading.Thread(target=run,args=('alina',4,))
p1.start()
p2.start()
p1.join()
p2.join()
end_time = time.time() - statt_time
print('cost time',end_time)
print(threading.current_thread())