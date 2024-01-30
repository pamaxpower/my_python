'''
Замена значений

- создается новый объект, не меняя старый
'''

from collections import namedtuple

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
a = Point(2, 3, 4)
print(a)
b = a._replace(z=0, x=a.x + 4)
print(b)
