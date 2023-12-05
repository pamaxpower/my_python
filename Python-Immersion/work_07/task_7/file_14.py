'''
Чтение данных в каталогах.

Обход папок через os.walk()

Функция возвращает кортеж из трёх значений:
dir_path — абсолютный путь до каталога
dir_names — список с названиями всех каталогов, 
находящихся в dir_path
dir_names — список с названиями всех файлов, 
находящихся в dir_path

'''

import os
for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')