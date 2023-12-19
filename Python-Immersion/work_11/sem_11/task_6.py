'''
Задание №6

Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
'''

class Rectangle:

    def __init__(self, length, width=0):
        self.length = length
        self.width = width
        if width == 0:
            self.width = self.length

    def area(self):
        if not self.width:
            return round(self.length**2, 2)
        else:
            return round(self.length * self.width, 4)
    
    def perimeter(self):
        if not self.width:
            return round(self.length * 4, 2)
        else:
            return round(self.length * 2 + self.width * 2, 4)
        
    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()
    
    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    # def __repr__(self):
    #     return f'Rectangle({self.length}, {self.width})'

if __name__ == '__main__':  
    r1 = Rectangle(2,5)
    r2 = Rectangle(3)
    print(f'{r1.area()}, {r2.area()}')

    print(f'{r1 == r2 = }')
    # print(r1.__eq__(r2))

    print(f'{r1 != r2 = }')
    # print(r1.__ne__(r2))

    print(f'{r1 > r2 = }')
    # print(r1.__gt__(r2))

    print(f'{r1 >= r2 = }')
    # print(r1.__ge__(r2))

    print(f'{r1 < r2 = }')
    # print(r1.__lt__(r2))

    print(f'{r1 <= r2 = }')
    # print(r1.__le__(r2))
