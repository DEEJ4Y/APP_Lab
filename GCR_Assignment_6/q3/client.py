import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

s.send(b"ping")
res1 = s.recv(1024)
print(res1)
s.close()
