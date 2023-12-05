'''
Файловая система

Создание каталога
'''

import os
from pathlib import Path

# os.mkdir('new_os_dir')
# Path('new_path_dir').mkdir()

os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
Path('some_dir/dir/new_path_dir').mkdir(parents=True)
