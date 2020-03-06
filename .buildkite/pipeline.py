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
    agents:
      docker: true
''')

def prepare():
    print(f'''  - label: ":rocket: Prepare agents"
    command: "buildkite-agent start --spawn 3 --tags="docker=true""
    agents:
      docker: true
''')


if __name__ == '__main__':
    prepare()
    setup()
