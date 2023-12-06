code='''
import json
import csv


def save_to_json():
    print('1')

def find_roots():
    print('2')

def generate_csv_file():
    print('3')
'''

with open('__init__.py', 'w') as f:
        f.write(f'{code}') 


with open("__init__.py", "r") as init_file:
    code = init_file.read()

function_names = [
    "def save_to_json",
    "def find_roots",
    "def generate_csv_file"
]

for func_name in function_names:
    if func_name not in code:
        print(f"Функция {func_name} не найдена в файле __init__.py")
    else:
        print(f"Функция {func_name} найдена в файле __init__.py")