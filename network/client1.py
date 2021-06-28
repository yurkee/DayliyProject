# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/28 16:00
"""

import socket

serveraddress = ('127.0.0.1', 7777)

sk = socket.socket()

sk.connect(serveraddress)

while True:

    sss = input('发送内容：').strip()
    sk.sendall(sss.encode())
    if sss == 'exit':
        print('客户端退出连接。')
        break

    answer = sk.recv(1024).decode()
    print("收到服务器应答：%s" % answer)

sk.close()