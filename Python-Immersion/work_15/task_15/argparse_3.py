'''
Создание парсера, ArgumentParser
- может принять 13 аргументов (большинство из них имеет 
оптимальные настройки по умолчанию)

prog - заменяет название файла в первой строки справки на заданное имя
description - описание в начале справки
epilog - описание в конце справки
'''

import argparse
parser = argparse.ArgumentParser(prog='average',
                                description='My first argument parser',
                                epilog='Returns the arithmetic mean')

parser.add_argument('numbers', metavar='N', type=float,
                    nargs='*', help='press some numbers')

args = parser.parse_args()

print(f'В скрипт передано: {args}')

# python argparse_3.py 42 --help