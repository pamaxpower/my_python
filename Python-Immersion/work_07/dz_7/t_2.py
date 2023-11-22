'''
Задача 2

Из созданных на уроке и в рамках домашнего задания 
функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него функцию 
rename_files
'''
code="""
import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    folder_path = "test_folder"
    files = os.listdir(folder_path)
    for i, file_name in enumerate(files):
        if file_name.endswith(source_ext):
            new_name = desired_name
            if name_range is not None:
                start = name_range[0] - 1
                end = name_range[1]
                original_name = file_name[start:end]
                new_name += original_name
            num = str(i).zfill(num_digits)
            new_name += '.' + target_ext
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
"""


with open('__init__.py', 'w') as f:
        f.write(f'{code}')