"""
Задача 6.

Дорабатываем функции из предыдущих задач.

Генерируйте файлы в указанную директорию — отдельный параметр 
функции.
Отсутствие/наличие директории не должно вызывать ошибок 
в работе функции (добавьте проверки).

Существующие файлы не должны удаляться/изменяться в 
случае совпадения имён.
"""

from os import chdir, getcwd, mkdir
from task_5 import new_func

# после запуска файлов task_4 и task_5 выходим из папки dir_4
chdir('..') 

def func_dir(dir):
    my_path = getcwd() + dir
    print(getcwd())
    try:
        mkdir(my_path)
        chdir(my_path)
    except FileExistsError:
        chdir(my_path)
    print(getcwd())

    new_func(5, a='.bin', b='.py', c='.doc')
    

func_dir('\\task')
