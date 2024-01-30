'''
Проверка

Что выведет программа
'''

from collections import namedtuple

# создаем класс Data
Data = namedtuple('Data', ['mathematics', 'chemistry', 'physics',
                'genetics'], defaults=[5, 5, 5, 5])

# создаем словарь из экземпляров класса
d = {
    'Ivanov': Data(4, 5, 3, 5),         # успешно Data(4, 5, 3, 5)
    'Petrov': Data(physics=4, genetics=3),  # успешно Data(5, 5, 4, 3)
    'Sidorov': Data(),                  # успешно Data(5, 5, 5, 5)
    }


print(d)

# Программа выведет словарь учеников с ключами (фамилиями) и 
# значениями (оценками), вида:
# 'Фамилия': Data(предмет=оценка, предмет=оценка, ...)