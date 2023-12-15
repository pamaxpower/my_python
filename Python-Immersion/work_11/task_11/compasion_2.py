'''
Сравнение экземпляров по содержанию

На примере треугольников, которые  можно переворачивать
'''

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
    
    # до сравнения мы сортируем списки по возрастанию
    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second

one = Triangle(3, 4, 5)
two = one
three = Triangle(3, 4, 5)
four = Triangle(4, 3, 5)

# в результате предварительной сортировки все треугольники имеют вид 3,4,5, и соответственно равны
print(f'{one == two = }')       # -> True
print(f'{one == three = }')     # -> True
print(f'{one == four = }')      # -> True

# проверка на неравно: питон не нашел нужный метод  __ne__, поэтому к результату 
# метода __eq__ применил not, те вернул противоположный результат
print(f'{one != one = }')       
