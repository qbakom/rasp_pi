#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

        # Check for the presence of a "cmd" parameter in the URL
        params = urlparse.parse_qs(urlparse.urlparse(self.path).query)
        if 'cmd' in params:
            # Send the command to the light device
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            s.send(bytearray(binascii.unhexlify(params['cmd'][0])))
            s.close()

        # Generate the HTML page
        self.wfile.write("""
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Light Control</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      background-color: #f2f2f2;
    }
    h1 {
      text-align: center;
    }
    .container {
      margin: 50px auto;
      max-width: 800px;
      padding: 20px;
      background-color: white;
      border-radius: 10px;
      box-shadow: 0px 0px 10px #888888;
    }
    .button {
      background-color: #4CAF50;
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      margin: 10px;
      cursor: pointer;
      border-radius: 5px;
      transition: background-color 0.3s ease;
    }
    .button:hover {
      background-color: #000000;
    }
    .button1 {
      background-color: #4CAF50;
    }
    .button2 {
      background-color: #f44336;
    }
    .fade {
      transition: none;
    }
    .center {
      text-align: center;
    }
    @media screen and (max-width: 600px) {
      .container {
        max-width: 400px;
      }
      .button {
        display: block;
        width: 100%;
        margin: 10px 0;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Light Control</h1>
    <form class="center">
      <button class="button button1" name="cmd" value="1c0264000000ff7f">Hall On</button>
      <button class="button button2" name="cmd" value="1c0264030000ff7c">Hall Off</button>
      <br>
      <button class="button button1" name="cmd" value="1c0364000000ff7e">Salon On</button>
      <button class="button button2" name="cmd" value="1c0364030000ff7b">Salon Off</button>
      <br>
      <button class="button button1" name="cmd" value="1c0464000000ff7d">Kuchnia On</button>
      <button class="button button2" name="cmd" value="1c0464030000ff7a">Kuchnia Off</button>
      <br>
      <button class="button button1" name="cmd" value="1c0564000000ff7c">Korytarz On</button>
      <button class="button button2" name="cmd" value="1c0564030000ff79">Korytarz Off</button>
      <br>
    </form>
  </div>
</body>
</html>
        """)


# Create the HTTP server
server = BaseHTTPServer.HTTPServer(('192.168.1.11', 8000), RequestHandler)

# Start the server
server.serve_forever()
