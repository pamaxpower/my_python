'''
Сравнение экземпляров классов

● __eq__ - равно, ==
● __ne__ - не равно, !=
● __gt__ - больше, >
● __ge__ - не больше, меньше или равно, <=
● __lt__ - меньше, <
● __le__ - не меньше, больше или равно, >=

Сравнение на идентичность __eq__

'''

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c 

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'

    # по умолчанию питон добавляет метод __eq__
    # def __eq__(self, other):
    #     return self is other



one = Triangle(3, 4, 5)
two = one

three = Triangle(3, 4, 5)

# если у экземпляров одинаковые id, то вернется True
print(one == two)       # -> True, тк это один и тот же объект
print(one == three)     # -> False, хоть значения и одинаковые, объекты разные
