'''
Чтение CSV в словарь

ключи словаря - названия столбцов,
значения - очередная строка файла CSV

для этого используем класс DictReader с использованием 
доп.параметров:
- fieldnames - список заголовков столбцов, ключей словаря
- restkey - значение ключа для столбцов, которых нет в списке
- restval - значение поля для ключей fildnames, которых нет в файле csv

'''

import csv
with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", \
        "age", "height", "weight", "office"], restkey="new", \
        restval="Main Office", quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')

# в получившимся файле данные запишутся как надо, а в ключе офис (которого у нас нет) мы получим переданный аргумент restval