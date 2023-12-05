'''
Работа с файлами

Копирование файлов
'''
import shutil

shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir')

shutil.copytree('dir', 'one_more_dir')
