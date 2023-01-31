
#!/usr/bin/env python

import socket
import time
import json
import binascii

TCP_IP = '192.168.1.7'
TCP_PORT = 23
BUFFER_SIZE = 1024
array = bytearray([28, 4, 100, 0, 0, 0, 255, 125])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

for a in range(0,3):
    for b in range(122,125):
        array[1] = a
        array[3] = a
        array[7] = b
        s.send(array)
        time.sleep(0.1)
        print(array)
        print(", ".join(hex(b) for b in array))

while True:
     array = b''
     while len(array) < 8:
         array += s.recv(1)
         print(array[len(array)-1])
         if array[len(array)-1] == 0x1c:
             array = bytearray([28])

     data_str = str(binascii.hexlify(array).decode('utf-8'))
     with open(data_str, 'w') as f:
         json.dump(data_str, f)
s.close()

