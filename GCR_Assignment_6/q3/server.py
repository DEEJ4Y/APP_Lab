import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host, port))
print(f'Server started at {host}:{port}')
s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    req1 = c.recv(1024)
    req1 = str(req1, 'utf-8')
    if(req1 == "ping"):
        c.send(b'pong')
        # print(str1)
        c.close()
