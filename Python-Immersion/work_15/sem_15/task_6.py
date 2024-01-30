'''
Задание №6

Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.

Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.

'''

import os
import argparse
import logging
from collections import namedtuple


FileObject = namedtuple('FileObject', ['name', 'extension', 'is_directory',
                                       'parent_directory'])

# делаем настройки логирования
logging.basicConfig(filename='file_objects.log',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='{asctime} - {levelname} - {message}',
                    style='{'
                    )


def get_file_objects(directory):
    """
    Функция для получения объектов из директории
    :param directory: Путь до директории
    :return: Список объектов, содержащихся в этой директории
    """
    
    files = []
    for entry in os.scandir(directory):
        # получаем имя объекта
        name = os.path.splitext(entry.name)[0] if entry.is_file() else entry.name
        # расширение (если это файл)
        extension = os.path.splitext(entry.name)[1] if entry.is_file() else None
        # True - если объект каталог
        is_directory = entry.is_dir()
        # родительский каталог
        parent_directory = os.path.basename(directory)

        file_object = FileObject(name, extension, is_directory,
                                 parent_directory)
        files.append(file_object)
    return files


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Принимаем пусть до директории")
    parser.add_argument('-d', help="Path to the directory")

    args = parser.parse_args()
    print(args)

    try:
        file_objects = get_file_objects(args.d)
        for f_obj in file_objects:
            logging.info(f_obj)
            print(f_obj)
    except Exception as e:
        logging.error(str(e))
        print("Error:", str(e))
