import os
import json
import pprint
import subprocess

if not os.path.exists('BgUtils/package.json'):
    print('pull BgUtils submodule using:\n$ git submodule update --init --recursive')
    exit(1)
if not os.path.exists('BgUtils/dist/index.js'):
    print('build BgUtils using npm:')
    print('$ cd BgUtils')
    print('$ npm install -y')
    print('$ npm run build')
    exit(1)

try:
    version = subprocess.check_output(['deno', '--version'], text=True)
except FileNotFoundError:
    print('deno is not installed or added to PATH')
    exit(1)

is_deno2 = version.split()[1].startswith('2')
is_linux = os.name == 'posix'
import_perm = ['--allow-import'] if is_deno2 else []
read_perm = ['--allow-read=/etc/alpine-release'] if is_linux else []


subprocess.check_output(['deno', 'run', '--no-prompt', *import_perm, *read_perm, 'load-jsdom.js'])
output = subprocess.check_output(['deno', 'run', '--cached-only', '--no-prompt', '--no-check', *read_perm,
                                  '--allow-net=jnn-pa.googleapis.com', 'run.js'], text=True)
print('Session Info:')
pprint.pp(json.loads(output))
