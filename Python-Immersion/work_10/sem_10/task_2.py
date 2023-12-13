'''
Задание №2

Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.

'''

class Rectangle():
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
    
r1 = Rectangle(2,5)
print(f' Площадь: {r1.area()}, Периметр: {r1.perimeter()}')

r2 = Rectangle(2)
print(f' Площадь: {r2.area()}, Периметр: {r2.perimeter()}')