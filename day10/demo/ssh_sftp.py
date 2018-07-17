# -*- coding:utf-8 -*-
#  Author:aling
import paramiko
transport = paramiko.Transport(('hostname',22))
transport.connect(username='aling',password='aling666')#建议连接
sftp = paramiko.SFTPClient.from_transport(transport)#定义怎么传
sftp.put('/tmp/abc.txt','local_path')# 上传
sftp.get('remove_path','local_path')# 下载
transport.close()