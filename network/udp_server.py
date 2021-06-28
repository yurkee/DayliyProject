# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/28 17:26
"""

import socket

hostaddress = ('127.0.0.1', 8888)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sk.bind(hostaddress)
print('启动socket服务，等待客户端连接……')

while True:
    data = sk.recv(1024).decode()
    print('udp服务器接收到客户端的数据：%s' % data)
    if data == 'exit':
        print('客户端请求退出')
        break

sk.close()