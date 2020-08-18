# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:55:38 2020

@author: Dallps
"""

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
    data,addr = sock.recvfrom(2048)
    print("Received Message: %s" % data.decode())