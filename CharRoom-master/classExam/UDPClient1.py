import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

service_addr = ("localhost",5555)


while True:
    data = input("您想向服务器发送什么消息：")
    sock.sendto(data.encode("utf-8"),service_addr)




