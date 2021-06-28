# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/28 15:17
"""

import socket

hostaddress = ("127.0.0.1", 7777)

#使用ipv4 使用TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(hostaddress)
sk.listen(5)
print("启动socket服务，等待客户端连接……")

conn, clientaddress = sk.accept()

while True:

    data = conn.recv(1024).decode()
    if data == 'exit':
        print('客户端发送完成，断开连接……')
        break
    print("接收到客户端 %s 发送来的信息： %s" % (clientaddress, data))
    res = data.upper()
    conn.sendall(res.encode())

conn.close()