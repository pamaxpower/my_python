'''
Файловая система.

Формирование пути
'''

import os
from pathlib import Path

file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')

file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')


print(type(file_1),     # возвращает строку
      type(file_2))     # возвращает путь к файлу