#!/usr/bin/env python
from time import sleep
import sys

def factorial():
    i = 1
    for j in range(1, 21):
        sys.stdout.write(f'{i} * {j} = ')
        i = i*j
        sys.stdout.write(f'{i}\n')
        sys.stdout.flush()
        sleep(1)

if __name__ == '__main__':
    factorial()
