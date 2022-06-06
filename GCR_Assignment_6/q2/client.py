import socket  # Import socket module
import os

s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345  # Reserve a port for your service.
s.connect((host, port))
s.send(b"Sending request to UpperCase this line")
res1 = s.recv(1024)
print(res1)
s.close()
