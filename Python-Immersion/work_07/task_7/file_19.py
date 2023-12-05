'''
Проверка
'''

import os
import shutil
from pathlib import Path

for i in range(10):
    with open(f'file_{i}.txt', 'w', encoding='utf-8') as f:
        f.write('Hello world!')

# 1) перебором цикла от 0 до 9 вкл, 
# создаются файлы с именем file_i и туда записывается 
# текст 'Hello world'


os.mkdir('new_dir')

# 2) создается папка new_dir

for i in range(2, 10, 2):
    f = Path(f'file_{i}.txt')
    f.replace('new_dir' / f)

# 3) перебором по циклу от 2 до 10 невкл с шагом 2 (2,4,6,8) 
# файлы с этими названиями перемещаются в папку new_dir. 
# В итоге ожидаем там 4 файла: file_2 (4,6,8)

shutil.copytree('new_dir', Path.cwd() / 'dir_new')

# 4) копируем все содержимое папки new_dir в папку dir_new