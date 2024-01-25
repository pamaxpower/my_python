"""
Задача 1

Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError, 
которое выбрасывается при некорректных значениях ширины и высоты, как при создании 
объекта, так и при установке их через сеттеры.
"""

class NegativeValueError(Exception):
    pass


class Rectangle:

    def __init__(self, width, height=0):
        self._width = width
        self._height = height
        if width < 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {self._width}')
        if height < 0:
            raise NegativeValueError(f'Высота должна быть положительной, а не {self._height}')
        
        if height == 0:
            self.height = self.width

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value < 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')
        self.height = value
    
# r = Rectangle(-2)
# __main__.NegativeValueError: Ширина должна быть положительной, а не -2

# r = Rectangle(5, -3)
# # __main__.NegativeValueError: Высота должна быть положительной, а не -3

# r = Rectangle(4, 4)
# r.width = -3
# # __main__.NegativeValueError: Ширина должна быть положительной, а не -3

r = Rectangle(4, 4)
r.height = -3
# # __main__.NegativeValueError: Высота должна быть положительной, а не -3