'''
Задание №6

Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
'''

class Validator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше или равно {self.max_value}')
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        print('!!!')

class Rectangle:
    length = Validator(10, 20)
    width = Validator(10, 40)
    
    def __init__(self, length, width=0):
        self._length = length
        if width == 0:
            width = length
        self._width = width
        

    def area(self):
        return round(self._length * self._width, 4)
    
    def perimeter(self):
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
    
    def __str__(self):
        res = f'Прямоугольник со сторонами {self._length} и {self._width}'
        return res

if __name__ == '__main__':
    rectangle1 = Rectangle(17, 135)
    # del rectangle1.width
    # print(rectangle1.width)

    # rectangle1.width = 12
    # rectangle1.length = 19
    print(rectangle1)