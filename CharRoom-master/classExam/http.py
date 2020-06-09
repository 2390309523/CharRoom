import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定
sock.bind(("0.0.0.0",5566))
#监听
sock.listen(20)
#接收
conn,addr = sock.accept();

print("address is :",addr)

data = conn.recv(1024)

print(data)
msg = """HTTP/1.1 200 OK
Content-Type:text/html

<meta charset='utf-8'>
<h1>人生苦短，我用python</h1>
"""
# 发送数据
conn.sendto(msg.encode("utf-8"),addr)

conn.close()
sock.close()
