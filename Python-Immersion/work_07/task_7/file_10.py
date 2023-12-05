'''
Файловая система.

Удаление каталога
'''

import os
from pathlib import Path

# нельзя удалить каталог, если в нем чтото есть

# os.rmdir('dir') # OSError
# Path('some_dir').rmdir() # OSError


# os.rmdir('dir/other_dir/new_os_dir')          # удаляется только new_os_dir
# Path('some_dir/dir/new_path_dir').rmdir()     # удаляется только new_path_dir


import shutil

shutil.rmtree('dir/other_dir')  # удаляем все, кроме dir
shutil.rmtree('some_dir')       # удаляем все
