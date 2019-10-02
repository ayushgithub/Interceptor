#!/usr/bin/env python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse


class myHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    # GET sends back a Hello world message
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        start_time = int(query_components["start_time"][0])
        duration = int(query_components["duration"][0])
        self._set_headers()
        response = []
        for i in range(duration):
            response.append({start_time+i: 'garbage'})
        self.wfile.write(json.dumps(response).encode())


def run():
    try:
        server_address = ('', 9000)
        httpd = HTTPServer(server_address, myHandler)
        print('Started httpserver on port ', 9000)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        httpd.socket.close()

if __name__ == '__main__':
    run()
