
#!/usr/bin/env python

import socket
import time
import json
import binascii
import sys

TCP_IP = '192.168.1.7'
TCP_PORT = 23

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print(sys.argv[1])
print(bytearray(binascii.unhexlify(sys.argv[1])))
s.send(bytearray(binascii.unhexlify(sys.argv[1])))
s.close()
 
