#!/usr/bin/python3
"""
Run
  Python Project Euler Solution Runner

Usage:
  run [<index>]
"""

from os.path import isdir, isfile, join
from re import match, search

from docopt import docopt


def main():
    args = docopt(__doc__)
    if args['<index>'] is None:
        exit(__doc__.strip())
    else:
        index = args['<index>']
        if match(r'^\d+$', index):
            index = int(index)
        else:
            exit(f'Invalid index: {index}')
        full_path = join('src', f'{index}.py')

        if isfile(full_path):
            with open(full_path) as file:
                code = file.read()

            while result := search(
                r'([A-Za-z_]\w*) = None  # ([a-z\-]+\.txt)', code
            ):
                variable = result.group(1)
                path = result.group(2)

                with open(join('src', f'{index}', path)) as file:
                    content = f'{file.read()!r}'[1:-1]

                code = (
                    code[:result.span()[0]] +
                    f'{variable} = """{content}"""  # {path}' +
                    code[result.span()[1]:]
                )

            exec(code, {})

        else:
            exit(f'Solution index not found: {index}')


if __name__ == '__main__':
    main()
