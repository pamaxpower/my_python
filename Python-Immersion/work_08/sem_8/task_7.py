'''
Задание №7

Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.

Распечатайте его как pickle строку.
'''

from csv import reader
from pickle import dumps, loads, DEFAULT_PROTOCOL

with open('new_8.csv', 'r', encoding='utf-8') as cf:
    data = list(reader(cf))
    #data = list(cf.readlines())
    
    res = dumps(data, protocol=DEFAULT_PROTOCOL)
    print(f'{res = }')
    print(loads(res))