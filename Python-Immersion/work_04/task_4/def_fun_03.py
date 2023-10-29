'''
Встроенные функции. Часть 3.

all(iterable) - возвращает истину, 
если все элементы являются истной

any(iterable) - вохвращает истину, 
если хотя бы один элемент истина
'''


def all_(iterable):
    for element in iterable:
        if not element:
            return False
    return True


def any_(iterable):
    for element in iterable:
        if element:
            return True
    return False


numbers = [42, -73, 1024]

if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('В последовательности есть отрицательные и/или нулевые элементы')

if any(map(lambda x: x > 0, numbers)):
    print('Хотя бы один элемент положительный')
else:
    print('Все элементы не больше нуля')

