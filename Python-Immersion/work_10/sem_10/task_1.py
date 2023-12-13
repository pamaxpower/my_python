'''Задание №1

Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
'''
from math import pi

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return round(2 * pi * self.radius, 4)
    
    def area(self):
        return round(pi * self.radius**2, 4)
    
c1 = Circle(10)
print(f' Длина окружности: {c1.length()}, Площадь: {c1.area()}')

c2 = Circle(5)
print(f' Длина окружности: {c2.length()}, Площадь: {c2.area()}')