# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/10 17:36

# 需求：
# 利用socket建立服务器，并且能够利用浏览器进行访问
# 要求多个浏览器可以同时访问

from socket import *
import threading
import re
import time
import mini_frame

class WSGISever(object):
    def __init__(self):
        # 创建socket
        self.tcp_server_socket = socket(AF_INET, SOCK_STREAM)
        # 设置当服务器先close 即服务器端4次握手之后资源能够立即释放，这样就保证了，下次运行程序时，可以立即使用该端口
        self.tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 本地信息
        address = ('', 7788)

        # 绑定
        self.tcp_server_socket.bind(address)

        # 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
        self.tcp_server_socket.listen(128)  # 允许很多客户端连接

    def work(self, client_socket, client_addr):
        # 接收对方发送过来的数据
        recv_data = client_socket.recv(1024).decode("gbk")  # 接收1024个字节
        # 解析请求的页面名字
        ret = r"^GET (/.*?) HTTP"
        page_name = re.findall(ret, recv_data)
        print('请求的页面为:', page_name)

        if page_name:
            page_name = page_name[0]
            if page_name == '/':
                page_name = "/index.html"   # 如果返回的是/，则让网址访问index.html
        # 2. 返回http格式的数据,给浏览器
        # 2.1 如果请求的资源不是以.py结尾，那么就认为是静态资源（html，css，js，png，jpg等等）
        if not page_name.endswith('.py'):
            # 打开文件操作及其危险，因此在此尝试打开文件
            try:
                # 拼接地址
                root_path = r'../html'   # 根目录
                complete_page_path = root_path + page_name    # 拼接
                # 打开页面，并读取内容
                f = open(complete_page_path, 'rb')   # 打开文件
            except:   # 如果打开文件失败，则返回404
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "------file not found-----"
                client_socket.send(response.encode("utf-8"))
            else:
                body = f.read()
                f.close()
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                # body = "<h1>你好!</h1>\r\n"
                # return_data = response + body
                # 发送一些数据到客户端
                client_socket.send(response.encode('utf-8'))
                client_socket.send(body)
        else:
            # 如果是以.py结尾，那么就认为是动态请求
            header = 'HTTP/1.1 200 OK\r\n'
            header += "\r\n"
            # body = 'hahaha %s' % time.localtime()
            body = mini_frame.login()
            response = header + body
            client_socket.send(response.encode('utf-8'))

        client_socket.close()
        print('---- 客户%s服务完毕 ----' % str(client_addr))
        # 关闭为这个客户端服务的套接字,只要关闭了，就意味着不能再为这个客户端服务了，如果还需要服务，只能再次访问


    def run_forever(self):
        while True:
            # 监听套接字 负责 等待有新的客户端进行连接
            # accept产生的新的套接字用来 为客户端服务
            client_socket, client_addr = self.tcp_server_socket.accept()
            t = threading.Thread(target=self.work, args=(client_socket, client_addr))
            t.start()
        self.tcp_server_socket.close()


def main():
    wsgisever = WSGISever()
    wsgisever.run_forever()


if __name__ == '__main__':
    main()

