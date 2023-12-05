'''
Файловая система

Текущий каталог

cwd - текущая рабочая директория
'''

import os
from pathlib import Path

print(os.getcwd())
print(Path.cwd())


os.chdir('../..')   # смена директории на 2 папки выше
print(os.getcwd())
print(Path.cwd())