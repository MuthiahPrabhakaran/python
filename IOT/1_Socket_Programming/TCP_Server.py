"""
Socket programming - networking in python
TCP Server
    - Associates the IP address with server socket
    - Accept the client request and prints the message
"""

import socket

# we define the IPV4 and UDP connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345

# Bind the host and port with socket. We have to pass host and port as one parameter
s.bind((host,port))

# Start to listen
s.listen(5)

# Have a infinite loop to listen continously
while True:
    msg,addr = s.accept() # Accept the message and address when the client tries to connect
    msg.send(b"Hello from server") # Once acception the connection request, server sends message in byte format. Default is raw
    msg.close()

