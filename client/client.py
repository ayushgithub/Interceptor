import random

import requests


def main():
    proxy_server_port = 8080
    url = "http://localhost:{}/".format(proxy_server_port)
    while True:
        start_time = random.randint(1, 101)
        duration = random.randint(100, 10001)
        querystring = {"service": "database_server", "start_time": str(start_time), "duration": str(duration)}
        response = requests.request("GET", url, params=querystring)
        print(response.text)

if __name__ == "__main__":
    main()
