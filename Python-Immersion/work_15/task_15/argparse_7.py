'''
параметр action 

'''

import argparse

parser = argparse.ArgumentParser(description='Sample')

parser.add_argument('-x', action='store_const', const=42)
parser.add_argument('-y', action='store_true')
parser.add_argument('-z', action='append')
parser.add_argument('-i', action='append_const', const=int, dest='types')
parser.add_argument('-f', action='append_const', const=float, dest='types')
parser.add_argument('-s', action='append_const', const=str, dest='types')
args = parser.parse_args()
print(args)


# python argparse_7.py -h

"""
usage: argparse_7.py [-h] [-x] [-y] [-z Z] [-i] [-f] [-s]

Sample

options:
  -h,   --help  show this help message and exit
  -x
  -y
  -z    Z
  -i
  -f
  -s
"""

# python argparse_7.py -x -y -z 42 -z 73 -i -f -s
