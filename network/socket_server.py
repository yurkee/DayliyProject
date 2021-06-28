# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/28 16:56
"""

import socketserver

class MyHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024).decode()
            if data == 'exit':
                print('客户端发送完成，断开连接.')
                break
            print('接收到客户端 %s 发送来的信息：%s' % (self.client_address, data))
            res = data.upper()
            self.request.send(res.encode())
        self.request.close()

hostaddress = ("127.0.0.1", 7777)
server = socketserver.ThreadingTCPServer(hostaddress, MyHandler)
print("启动socket服务，等待客户端连接……")
server.serve_forever()