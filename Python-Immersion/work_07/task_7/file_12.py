'''
Чтение данных в каталогах

Содержание каталога
'''

import os
from pathlib import Path

print(os.listdir())     # СПИСОК всего, что есть в текущей папке

# получает путь ко всем файлам в текущем каталоге
p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)
