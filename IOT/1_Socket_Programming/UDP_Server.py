# -*- coding: utf-8 -*-
"""
UDP Server
We don't build connections.
Steps:
    1. Form a socket
    2. Bind the address
    3. Send the data
"""

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = b"Hello from UDP Server"

print("UDP Target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("Message: %s" % MESSAGE)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE,(UDP_IP,UDP_PORT))




