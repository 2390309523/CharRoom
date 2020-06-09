from socket import *

# 发送广播的目标地址
dest = ("localhost",7788);

sock = socket(AF_INET,SOCK_DGRAM);
sock.bind(("localhost",5566))

# 设置可以接收和发送广播
sock.setsockopt(SOL_SOCKET,SO_BROADCAST,1);

data = """ this is broadcast """;

sock.sendto(data.encode("utf-8"),dest);

sock.close()