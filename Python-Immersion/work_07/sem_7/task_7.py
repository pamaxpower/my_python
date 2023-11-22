"""
Задача 7.

✔ Создайте функцию для сортировки файлов по директориям: 
видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими 
расширениями.
✔ В исходной папке должны остаться только те файлы, 
которые не подошли для сортировки.

"""
# from os import chdir, getcwd, mkdir, listdir, isfile
import os

DICT_EXT = {
    'videos': ['mpeg', 'mkv', 'mp4', 'avi', 'mov', 'wmv', 'flv', 'vob'],
    'image': ['jpg', 'gif', 'png', 'jpeg', 'bmp', 'psd', 'ico', 'fitt',],
    'text': ['fb2', 'txt', 'doc', 'docx', 'mobi', 'ebup', 'pdf', 'rtf'],
    'data': ['sql', 'csv', 'dat', 'db', 'mdb'],
    'audio': ['mp3', 'wav', 'wma', 'cda', 'ogg', 'flac'],
}


def sort_files(dir, extension):

    file_list = [file.split('.') for dirs, folders,
                 files in os.walk(dir) for file in files]
    print(file_list)

    for (name, ext) in file_list:
        for k, v in extension.items():
            if ext in v:
                new_dir = os.path.join(os.getcwd(), dir, k)

                old_place = os.path.join(dir, f'{name}.{ext}')
                new_place = os.path.join(new_dir, f'{name}.{ext}')

                if os.path.isdir(new_dir):
                    os.replace(old_place, new_place)
                else:
                    os.makedirs(new_dir)
                    os.replace(old_place, new_place)


sort_files('sort', DICT_EXT)
