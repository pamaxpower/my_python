'''
Задание №1

Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
'''
from datetime import datetime

# Есть встроенный класс Str, нужно улучшенный (измененный) класс
# для этого мы используем перегрузку функции __new__


class MyStr(str):
    def __new__(cls, value, author_name):
        # перенимаем все свойства класса
        my_str = super().__new__(cls, value)
        # и дополняем их нужными нам значениями
        my_str.author_name = author_name
        my_str.time = datetime.now()
        return my_str

if __name__ == '__main__':
    str1 = MyStr('Новая строка текста','Alex')
    print(str1.author_name)
    print(str1.time)

    # help(MyStr)