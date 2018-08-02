# -*- coding:utf-8 -*-
#  Author:aling
import paramiko
privage_key = paramiko.RSAKey.from_private_key_file('id_ras31.txt')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddrPolicy())
# 连接服务器
ssh.conn(hostname = 'c1.salt.com',port=22,username = 'aling',pkey=privage_key)

#执行命令
stdin,stdout,stderr = ssh.exec_command('df;ifconfig')#df是一条命令,stdin标准输入，stdout标准输出,stderr标准错误
#获取命令结果
result = stdout.read()
res,err = stdout.read(),stderr.read()
result = res if res else err # 三元运算符
print(result.decode())

#关闭连接
ssh.close()