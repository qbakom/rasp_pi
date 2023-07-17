#!/usr/bin/env python

import os
import BaseHTTPServer
import urlparse
import socket
import time
import json
import binascii
import sys
import glob

TCP_IP = '192.168.1.7'
TCP_PORT = 23


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        # Send the HTTP headers
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        params = urlparse.parse_qs(urlparse.urlparse(self.path).query)

        if 'cmd' in params:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            s.send(bytearray(binascii.unhexlify(params['cmd'][0])))
            s.close()

        files = glob.glob('1c*')
        files.sort()
        for a in files:
            self.wfile.write('<a href="?cmd='+a+'">'+a+'</a><br>')

# Create the HTTP server
server = BaseHTTPServer.HTTPServer(('192.168.1.11', 8000), RequestHandler)

# Start the server
server.serve_forever()
