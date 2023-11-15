'''
Import
пишется в самом начале файла, после него 1-2 пустые строки кода

import module_name

Если нужно импортировать больше 1 модуля, 
то каждый импорт стоит писать на отдельной строке:

import sys, random - неправильная запись!!!
'''

import sys

print(sys)
print(sys.builtin_module_names)
print(*sys.path, sep='\n')

# PYTHONPATH - переменная с путями до мест расположения модулей