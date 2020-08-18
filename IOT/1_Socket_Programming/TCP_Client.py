# -*- coding: utf-8 -*-
"""
TCP Client
Client communication with the server
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 12345))

# Include the size of the message that the client wants to receive in bytes
# print(s.recv(2048))

# Decode the byte string into proper string
msg = s.recv(2048)
print(msg.decode())

s.close()