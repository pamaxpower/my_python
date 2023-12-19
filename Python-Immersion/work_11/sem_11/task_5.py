'''
Задание №5

Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.

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
    
    # вычитаем периметры
    def __sub__(self, other):
        new_perimeter = self.perimeter() - other.perimeter()
        if new_perimeter > 0:
            return f'Периметр {self} на {new_perimeter} больше чем {other}'
        elif new_perimeter < 0:
            return f'Периметр {other} на {new_perimeter} больше чем {self}'
        else:
            return 'Периметры равны'
        
    # складываем стороны    
    def __add__(self, other):
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)
    
    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'

if __name__ == '__main__':  
    r1 = Rectangle(2,5)
    r2 = Rectangle(3)

    r3 = r1 + r2
    r4 = r2 - r1
    print(f'{r1 = }\t{r2 = }\t{r3 = }\t{r4 = }')