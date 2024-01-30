'''
Если все свойства являются объектами неизменяемого типа, то
экземпляр может быть ключом словаря, элементом множеств и тд

'''
from collections import namedtuple

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
d = {
    Point(2, 3, 4): 'first',
    Point(10, -100, -500): 'second',
    Point(3, 7, 11): 'last',
    }
print(d)

# создание точки, с координатой y в виде списка
mut_point = Point(2, [3, 4, 5], 6)
print(mut_point)

# создание экземпляра прошло успешно, но тип поменялся на изменяемый, 
# поэтому следующий код (добваление в словарь) вызывает ошибку

# d.update({mut_point: 'bad_point'}) # TypeError: unhashable type: 'list'
