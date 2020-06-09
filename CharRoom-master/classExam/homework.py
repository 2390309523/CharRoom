import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("localhost",5566));


print("gethostname:",socket.gethostname())
print("gethostbyname:",socket.gethostbyname("www.baidu.com"))
print("getServByName:",socket.getservbyname("http","tcp"))
print("getServByport:",socket.getservbyport(53,"udp"))
print("getSockname:",sock.getsockname())
print("getfileno:",sock.fileno())
#print("getpeername:",sock.getpeername())
print("type:",sock.type)
print("family:",sock.family)