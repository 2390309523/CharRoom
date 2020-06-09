import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

service_addr = ("0.0.0.0",5555)

sock.bind(service_addr)

while True:
    data,addr = sock.recvfrom(1024)
    print("the addr is :",addr)




