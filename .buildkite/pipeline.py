#!/usr/bin/env python
import glob
import ntpath

def setup():
    scripts = glob.glob('scripts/*')
    print('steps:')
    for script in scripts:
        step(script)

def step(script):
    print(f'''  - label: ":rocket: {ntpath.basename(script)}"
    command: "./{script}"
''')


if __name__ == '__main__':
    setup()
