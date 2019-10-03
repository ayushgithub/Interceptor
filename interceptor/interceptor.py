#!/usr/bin/env python3

import json
import socketserver
import time
from datetime import datetime
from http.server import SimpleHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

import requests
from kubernetes import client, config
from kubernetes.client.rest import ApiException

config.load_incluster_config()
API_INSTANCE = client.CoreV1Api()
TOLERANCE = 0.004


class myHandler(SimpleHTTPRequestHandler):
    # GET sends back a Hello world message
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        query = {}
        service_label = ''
        for key, val in query_components.items():
            if key == 'service':
                service_label = val[0]
            else:
                query[key] = val[0]
        service_name = ''
        try:
            label_selector = 'app={}'.format(service_label)
            api_response = API_INSTANCE.list_service_for_all_namespaces(label_selector=label_selector)
            for service in api_response.items:
                service_name = service.metadata.name
        except ApiException as e:
            err = "Exception when calling CoreV1Api->list_service_for_all_namespaces: {}".format(e)
            print(err)
        params_list = []
        for key, val in query.items():
            params_list.append('{}={}'.format(key, val))
        params = '&'.join(params_list)
        url = 'http://{}:80/?{}'.format(service_name, params)   

        resp = requests.request("GET", url)
        delta = resp.elapsed.total_seconds()
        print('{} --- Received response in {}'.format(url, delta))
        if delta > TOLERANCE:
            print('ERROR')
        self.wfile.write(json.dumps(resp.json()).encode())


def run():
    try:
        server_address = ('', 8080)
        httpd = socketserver.ForkingTCPServer(server_address, myHandler)
        print('Started proxyserver on port ', 8080)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        httpd.socket.close()

if __name__ == '__main__':
    run()
