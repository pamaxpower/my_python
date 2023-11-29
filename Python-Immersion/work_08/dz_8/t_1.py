'''
Ваша задача - написать программу, которая принимает на вход директорию и 
рекурсивно обходит эту директорию и все вложенные директории. 
Результаты обхода должны быть сохранены в нескольких форматах: 
JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:

Путь к файлу или директории: Абсолютный путь к файлу или директории. 

Тип объекта: Это файл или директория. 

Размер: Для файлов - размер в байтах, для директорий - размер, 
учитывая все вложенные файлы и директории в байтах. 

Важные детали:
* Для дочерних объектов (как файлов, так и директорий) укажите родительскую 
директорию.

* Для файлов сохраните их размер в байтах.

* Для директорий, помимо их размера, учтите размер всех файлов и директорий, 
находящихся внутри данной директории, и вложенных директорий.

* Программа должна использовать рекурсивный обход директорий, чтобы учесть все 
вложенные объекты.

Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. 
Форматы файлов должны быть выбираемыми.

Для обхода файловой системы вы можете использовать модуль os.

Вам необходимо написать функцию traverse_directory(directory), 
которая будет выполнять обход директории и возвращать результаты в 
виде списка словарей. После этого результаты должны быть сохранены в трех 
различных файлах (JSON, CSV и Pickle) с помощью функций save_results_to_json, 
save_results_to_csv и save_results_to_pickle.
'''

import os
import json
import csv
import pickle

def get_dir_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

def traverse_directory(directory):
    results = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            filepath = os.path.join(dirpath, f)
            file_type = 'file'
            file_size = get_dir_size(filepath)
            result = {'Path': filepath, 'Type': file_type, 'Size': file_size}
            results.append(result)
        for d in dirnames:
            dirpath = os.path.join(dirpath, d)
            file_type = 'directory'
            file_size = get_dir_size(dirpath)
            result = {'Path': dirpath, 'Type': file_type, 'Size': file_size}
            results.append(result)
    return results

def save_results_to_json(results, filename):
    with open(filename, 'w') as file:
        json.dump(results, file)

def save_results_to_csv(results, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)

def save_results_to_pickle(results, filename):
    with open(filename, 'wb') as file:
        pickle.dump(results, file)

