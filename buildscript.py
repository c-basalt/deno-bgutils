import os
import ast


# this part should be completed in prev workflow steps
if not os.path.exists('BgUtils/package.json'):
    print('pull BgUtils submodule using:\n$ git submodule update --init --recursive')
    exit(1)
if not os.path.exists('BgUtils/dist/index.js'):
    print('build BgUtils using npm:')
    print('$ cd BgUtils')
    print('$ npm install -y')
    print('$ npm run build')
    exit(1)


with open('BgUtils/bundle/index.cjs', 'r') as f:
    bgutils_lib = f.read()

with open('main.js', 'r') as f:
    main_script = f.read()


script = f'var module = {{}};\n{bgutils_lib}\nconst BG = module.exports.BG;\n{main_script}'


assign = ast.Assign([ast.Name('SCRIPT', ast.Store())], ast.Constant(script), lineno=1)

with open('script.py', 'wt') as f:
    f.write(ast.unparse(assign))


# validate generated python file
with open('script.py', 'r') as f:
    exec(f.read())
assert SCRIPT == script
