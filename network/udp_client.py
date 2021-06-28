# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/28 17:26
"""

import socket

serveraddress = ('127.0.0.1', 8888)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    sss = input('【udp】发送内容：').strip()
    sk.sendto(sss.encode(), serveraddress)
    if sss == 'exit':
        print('客户端退出。')
        break

sk.close()