'''
Задание №4

Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств
'''
from sys import getsizeof

class Rectangle:
    # __slots__ = ('_width', '_length')

    def __init__(self, length, width=0):
        self._length = length
        self._width = width
        if width == 0:
            self._width = self._length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        if new_width < 0:
            raise ValueError('Ширина должна быть больше 0')
        self._width = new_width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_length):
        if new_length < 0:
            raise ValueError('Длина должна быть больше 0')
        self._length = new_length

    def area(self):
        if not self._width:
            return round(self._length**2, 2)
        else:
            return round(self._length * self._width, 4)
    
    def perimeter(self):
        if not self._width:
            return round(self._length * 4, 2)
        else:
            return round(self._length * 2 + self._width * 2, 4)
    
    def __sub__(self, other):
        new_perimeter = self.perimeter() - other.perimeter()
        if new_perimeter > 0:
            return f'Периметр {self} на {new_perimeter} больше чем {other}'
        elif new_perimeter < 0:
            return f'Периметр {other} на {new_perimeter} больше чем {self}'
        else:
            return 'Периметры равны'
        
    def __add__(self, other):
        new_length = self._length + other._length
        new_width = self._width + other._width
        return Rectangle(new_length, new_width)
    
    def __repr__(self):
        return f'Rectangle({self._length}, {self._width})'

if __name__ == '__main__':
    rectangle1 = Rectangle(7, 11)
    print(rectangle1)

    rectangle1.width = 9
    print(rectangle1)

    rectangle1.length = 1
    print(rectangle1)

    # rectangle1.width = -9     # ValueError: Ширина должна быть больше 0
    # print(rectangle1)

    # print(getsizeof(rectangle1.__slots__))      # -> 56
    print(getsizeof(rectangle1.__dict__))       # -> 104