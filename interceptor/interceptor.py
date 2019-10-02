#!/usr/bin/env python3

import json
import time
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlopen, urlparse

from kubernetes import client, config
from kubernetes.client.rest import ApiException

config.load_incluster_config()
API_INSTANCE = client.CoreV1Api()
TOLERANCE = 10

class myHandler(BaseHTTPRequestHandler):
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

        try:
            label_selector = 'app={}'.format(service_label)
            api_response = API_INSTANCE.list_service_for_all_namespaces(label_selector=label_selector)
            for service in api_response.items:
                service_name = service.metadata.name
        except ApiException as e:
            err = "Exception when calling CoreV1Api->list_service_for_all_namespaces: {}".format(e)
            print(err)

        params_list = []
        for key, val in query:
            params_list.append('{}={}'.format(key, val))
        params = '&'.join(params_list)

        url = 'http://{}:80/?{}'.fomat(service_name, params)

        start_time = datetime.now()
        response = urllib.urlopen(url)
        end_time = datetime.now()
        delta = (end_time-start_time).total_seconds()*1000
        print('{} --- Received response in {}'.format(url, delta))
        if delta > TOLERANCE:
            print('ERROR')
        self.copyfile(response, self.wfile)


def run():
    try:
        server_address = ('', 8080)
        httpd = HTTPServer(server_address, myHandler)
        print('Started proxyserver on port ', 8080)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        httpd.socket.close()

if __name__ == '__main__':
    run()
