#!/usr/bin/env python3

import json
import math
import itertools
from http.server import HTTPServer, BaseHTTPRequestHandler

def encode(limit, data):
    matrix = [data[x:x+limit] for x in range(0, len(data), limit)]

    # fill incomplete rows
    for i in range(len(matrix)):
        if len(matrix[i]) < limit:
            matrix[i] += ' '*(limit-len(matrix[i]))
    
    transposed = zip(*matrix)
    return ''.join(itertools.chain(*transposed))

def decode(limit, data):
    rows = math.ceil(len(data)/limit)
    matrix = [data[x:x+rows] for x in range(0, len(data), rows)]
    transposed = zip(*matrix)
    return ''.join(itertools.chain(*transposed)).strip()

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path in ('/encode', '/decode'):
            self.handler()
        else:
            self.send_error(404)

    def handler(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        message = json.loads(body.decode('utf-8'))
        
        transform = globals().get(self.path[1:])
        data = transform(message['vueltas'], message['mensaje'])
        
        self.send_response(200)
        self.end_headers()        
        self.wfile.write(json.dumps({'message': data}).encode('utf-8'))

PORT = 8000
httpd = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
print ('Server Listening at: http://{}:{}'.format(httpd.server_name, httpd.server_port))
httpd.serve_forever()
