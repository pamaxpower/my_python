"""
Задача 5.

Доработаем предыдущую задачу.

Создайте новую функцию которая генерирует файлы с разными 
расширениями.

Расширения и количество файлов функция принимает в качестве 
параметров.

Количество переданных расширений может быть любым.

Количество файлов для каждого расширения различно.

Внутри используйте вызов функции из прошлой задачи.

"""
from random import choices, randint
from task_4 import create_files
from os import getcwd

# from pathlib import Path
# from os import chdir

# chdir('dir_4')
# print(Path.cwd())

def new_func(count=5, **kwargs):
    val = []
    for k, v in kwargs.items():
        val.append(v)
    print(val)
    for _ in range(count):
        ext = str(*choices(val))
        num = randint(1,3)
        create_files(ext, files=num)
        

new_func(a='.txt', b='.py', c='.bin', d='.doc', e='.exe')

print(getcwd())