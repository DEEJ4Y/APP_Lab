import socket


s = socket.socket()
host = socket.gethostname()
port = 3000
s.connect((host, port))

print(s.recv(2048).decode("utf-8"))

s.close()
quit()
