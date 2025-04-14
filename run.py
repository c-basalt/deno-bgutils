import os
import json
import pprint
import subprocess

try:
    from script import SCRIPT
except ImportError:
    print('run buildscript.py first')
    exit(1)


with open('script.js', 'wt') as f:
    f.write('const visitorData = ["dQw4w9WgXcQ"];\n')
    f.write(SCRIPT)


try:
    version = subprocess.check_output(['deno', '--version'], text=True)
except FileNotFoundError:
    print('deno is not installed or added to PATH')
    exit(1)

is_linux = os.name == 'posix'
read_perm = ['--allow-read=/etc/alpine-release'] if is_linux else []


subprocess.check_output(['deno', 'cache', 'https://esm.sh/v135/jsdom'])
output = subprocess.check_output(['deno', 'run', '--cached-only', '--no-prompt', '--no-check', *read_perm,
                                  '--allow-net=jnn-pa.googleapis.com', 'script.js'], text=True)
print('Session Info:')
pprint.pp(json.loads(output))
