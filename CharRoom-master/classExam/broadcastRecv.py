from socket import *
# 创建UDP的套接字
sock = socket(AF_INET,SOCK_DGRAM)
# 设置发送接收广播
sock.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
# 选择接收广播的地址(类似接收广播，可以随意修改接收不同的信号)
sock.bind(("localhost",7788));
data,addr = sock.recvfrom(1024)
print("broadcast msg:",data.decode("utf-8"))
print("address:",addr)
sock.close()