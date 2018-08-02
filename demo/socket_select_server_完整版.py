# -*- coding:utf-8 -*-
#  Author:aling
import socket,select,time,sys,queue
'''单线程下的多路复用'''
server = socket.socket()

server_addres = ('localhost',8823)
server.bind(server_addres)
server.listen(1000)
server.setblocking(0)# 设置成非阻塞模式 0 就是false 就是非阻塞模式
msg_dic={}
inputs = [server,] # 用于select监测使用，只要是想监测的就给它，初始没有链接时，程序自己本身就是一个链接，如果自己活动了，那就表示有人连我了
#第一次是server,第二次里面的值则为server,conn
outputs = [] # 下一次select的时候，就会把output里面的数据返回
# outputs = [r1] #
while True:# 循环接收select数据
    # 第一个Inputs是你要让select监测的内容
    # 第二个Inputs 是如果第一个inputs其中有部分链接断了，那就有问题放到第二个Inputs当中
    readable , writeable,exceptional = select.select(inputs,outputs,inputs)# 在此阻塞，监测是否有用户连接进来或是否有数据进来，如果活动则表示有数据或用户连接进来
    # readable 可读列表,用于保存用户连接，即conn（仅第一次保存）
    # writable 可写列表
    # exceptional 异常列表
    print('readable:',readable,
          '\nwriteable:',writeable,
          '\nexceptional:',exceptional)
    for r in readable:
        print(type(r))
        print('r:',r)
        print('server:',server)
        if r is server:#代表来了一个新链接,当来的是数据时，socket里面的fd值变了(上下文变了），此时的socket连接是带着数据的，所以会跳开这个if
            conn,addr = r.accept()# 没数据不阻塞，没有链接就报错
            print('来了个新链接：',addr)
            # 如果马上conn.recv(1024)会报错，这是因为
            # 这个新建立的链接还没有发数据过来，如果现在就接收，程序就会报错（因为这是非阻塞IO)，所以要想实现这个客户端发数据来时server端能知道
            # 就需要让内核select来监测这个conn链接，如果有数据则进行接收。即如果select活动了，就代表有数据进来了
            inputs.append(conn) # 下一次while循环的时候监测链接
            # 这时候的inputs = [server,conn],在select的封装中，会直接返回活动的IO，这些返回数据会存在readable中
            # 如果server活动则表示有新链接，如果conn活动则表示有数据
            msg_dic[conn] = queue.Queue()# 初始化一个队列，后面存要返回给客户端的数据
            print('msg_dic:',msg_dic)
            print('msg_dic[conn]:',msg_dic[conn])
        else:# 不是新链接，表示之前的conn发数据过来了
            try:
                print('r:', r)
                data = r.recv(1024)  # 只能是r 不能是conn，因为这时候的conn是托管给select了，而select给的返回的数据是给readable
                                     # 此时的r取的是for 循环里面的readable，而readable里面存的就是此次带数据的socket的conn
                print('收到数据：',data)
                msg_dic[r].put(data)
                print('msg_dic:', msg_dic)
                print('msg_dic[r]:',msg_dic[r])
                outputs.append(r) # 放入返回链接的队列里 # 不第一时间send，等需要的时候send
            except Exception as e:
                print('客户端%s断开连接。。。'%r)
                inputs.remove(r)


    for w in writeable: # 要返回给客户端的链接列表
        print(w)
        print('msg_dic:', msg_dic)
        print('msg_dic[w]:',msg_dic[w])
        data_to_client = msg_dic[w].get()
        w.send(data_to_client) #返回给客户端的源数据
        outputs.remove(w)# 确保下一次循环的时候，writeable不返回已经处理完的链接

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)# e肯定在inputs里面
        del msg_dic[e]
