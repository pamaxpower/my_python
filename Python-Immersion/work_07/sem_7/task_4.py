"""
Задача 4.

Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:

✔ расширение
✔ минимальная длина случайно сгенерированного имени, 
по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, 
по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, 
по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, 
по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного 
диапазона
"""
from random import randint, choices, randbytes
from os import chdir, mkdir, getcwd

# создаем новую директорию
# Path('dir_4').mkdir()
# print(Path.cwd())

try:
    mkdir('dir_4')
    chdir('dir_4')
except FileExistsError:
    chdir('dir_4')

# # переходим в эту директорию
# chdir('dir_4')
# print(Path.cwd())

# при выполнении кода в новой папке создаются
eng_alphabet = ''.join([chr(char) for char in range(ord('a'), ord('z') + 1)])

def create_files(ext, files=42, min_len=6, max_len=30, min_bytes=256, max_bytes=4096):
    
    for _ in range(files):
        name = ''.join(choices(eng_alphabet, k=randint(min_len, max_len))) + ext
        size = randint(min_bytes, max_bytes)
        with open(name, 'wb') as f:
            f.write(randbytes(size))

create_files('.txt', files=10) 
