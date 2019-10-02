import random
import time

import requests


def main():
    proxy_server_port = 8080
    url = "http://localhost:{}/".format(proxy_server_port)
    while True:
        try:
            start_time = random.randint(1, 101)
            duration = random.randint(100, 10001)
            querystring = {"service": "database_server", "start_time": str(start_time), "duration": str(duration)}
            response = requests.request("GET", url, params=querystring)
            print(response.text)
        except requests.exceptions.RequestException:
            print('connection error, retrying after 5 seconds')
            time.sleep(5)

if __name__ == "__main__":
    main()
