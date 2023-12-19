'''
Задание №3

Добавьте к задачам 1 и 2 строки документации для классов.
'''
from datetime import datetime


class MyStr(str):
    """
    Тут будет описание класса MyStr
    """
    def __new__(cls, value, author_name):
        my_str = super().__new__(cls, value)
        my_str.author_name = author_name
        my_str.time = datetime.now()
        return my_str
    

class Archive:
    """
    Любое описание класса Archive
    """
    nums_archive = []
    strs_archive = []
    last_num = None
    last_str = None

    def __init__(self, num, new_str):
        """
        Любое описание метода
        :param num: любое число
        :param new_str: любая строка
        """

        self.num = num
        self.str = new_str

        if Archive.last_num is not None:
            Archive.nums_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.strs_archive.append(Archive.last_str)  

        Archive.last_num = num
        Archive.last_str = new_str

if __name__ == '__main__':
    str1 = MyStr('Новая строка текста','Alex')
    arc_1 = Archive(5, 'Hello')
    print(arc_1.num, arc_1.str, arc_1.nums_archive, arc_1.strs_archive)
    arc_2 = Archive(3, 'World')
    print(arc_2.num, arc_2.str, arc_2.nums_archive, arc_2.strs_archive)
    arc_3 = Archive(42, 'Universal')
    print(str1.__doc__)
    print(arc_1.__doc__)
    print(arc_1.__init__.__doc__)