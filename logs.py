#!/usr/bin/env python

import socket

TCP_IP = '192.168.1.7'
TCP_PORT = 23
BUFFER_SIZE = 1024
#array = bytearray([28, 5, 100, 0, 0, 0, 255, 124])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
# s.send(array)
with open("logs.txt","a")as out:
    while True:
        for data in s.recv(BUFFER_SIZE):
            out.write("Received: {data}\n")
    s.close()

out.write("-"*20)
