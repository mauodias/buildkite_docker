#!/usr/bin/env python
import requests
from time import sleep
import json

def call():
    base = 'https://httpbin.org'
    urls = [
            f'/delay/4',
            '/stream/5',
            '/status/418',
            '/bytes/40',
            '/uuid'
    ]

    for u in urls:
        response = requests.get(f'{base}{u}')
        print(response.content)
        sleep(3)

if __name__ == '__main__':
    call()
