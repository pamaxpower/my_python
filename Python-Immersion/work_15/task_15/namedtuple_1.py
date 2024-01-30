'''
Модуль collections
- хранит много полезных и интересных структур данных

Функция namedtuple()
- принимает два обязательных значения:
имя класса - точно такое же имя как и переменная слева от знака равно
список строк или строка с пробелами в кач-ве разделителей

в итоге получаем класс, аналогичный созданному вручную классу class.

'''

from collections import namedtuple
from datetime import datetime

User = namedtuple('User', ['first_name', 'last_name',
'birthday'])
u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))

print(u_1)
print(f'{type(User)}, {type(u_1)}')

# можно получить доступ к свойствам используя точечную нотацию
print(u_1.first_name, u_1.birthday.year)


