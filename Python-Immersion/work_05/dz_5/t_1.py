'''
Задача 1.

Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


На входе:
file_path = "C:/Users/User/Documents/example.txt"

На выходе:
('C:/Users/User/Documents/', 'example', '.txt')
'''


def get_file_info(path):
    file = path.split("/")[-1]
    *file_name, file_extension = file.split(".")

    return (path.replace(file, '').strip(), '.'.join(file_name), "." + file_extension)


# file_path = "C:/Users/User/Documents/example.txt"
file_path = '/home/user/data/file'
# file_path = 'D:/myfile.txt'
# file_path = 'C:/Projects/project1/code/script.py'
# file_path = '/home/user/docs/my.file.with.dots.txt'
# file_path = 'file_in_current_directory.txt'

print(get_file_info(file_path))


