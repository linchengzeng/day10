# -*- coding:utf-8 -*-
#  Author:aling


import gevent
from urllib import request
from gevent import monkey # 给urllib打上补丁，变成协程操作
monkey.patch_all() #把当前程序的所有IO操作给单独的做上标记
def f(url):
    print('GET:%s'%url)
    resp = request.urlopen(url)
    data = resp.read()
    f = open('index.html','wb')
    f.write(data)
    f.close()
    print('%d bytes received from %s.'%((len(data),url)))
# 下载一个页面
f('http://edu.51cto.com/')
#下载多个页面
gevent.joinall([  # gevent默认就是阻塞的，因为它检测不到IO操作，为解决这个问题，需为gevent补上monkey补丁
                                             # 这样它会把当前程序的所有IO操作给单独的做上标记
    gevent.spawn(f,'https://www.python.org/'),
    gevent.spawn(f,'http://edu.51cto.com/topiclist?edunav'),
    gevent.spawn(f,'http://edu.51cto.com/')
])