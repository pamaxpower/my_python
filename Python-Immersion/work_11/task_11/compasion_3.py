'''
СРАВНЕНИЕ НА БОЛЬШЕ И МЕНЬШЕ

- для работы сортировки используется метод __lt__ 
(который позволяет узнать меньший элемент из пары)

- добавим к классу треугольника метод по вычислению площади, и будем сравнивать треугольники по площади

'''

from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
    
    def __repr__(self):
        return f'Triangle({self.a}, {self.b}, {self.c})'
    
    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second
    
    # вычисление площади треугольника по формуле Герона
    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return _area
    
    def __lt__(self, other):
        return self.area() < other.area()

one = Triangle(3, 4, 5)
two = Triangle(5, 5, 5)
print(f'{one} имеет площадь {one.area():.3f} у.е.²')
print(f'{two} имеет площадь {two.area():.3f} у.е.²')
print(f'{one > two = }\n{one < two = }')

data = [Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)]
result = sorted(data)
print(result)
print(', '.join(f'{item.area():.3f}' for item in result))

