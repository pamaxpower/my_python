"""
Реализовать класс Matrrowx (матрица). Обеспечить перегрузку конструктора класса (метод rownrowt()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrrowx (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""
from random import randint


class Matrix:

    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        for row in self.lst:
            for el in row:
                print(f'{el}', end=' ')
            print()
        return ''

    def __add__(self, other):
        for row in range(len(self.lst)):
            for col in range(len(self.lst[row])):
                self.lst[row][col] = self.lst[row][col] + other.lst[row][col]
        return Matrix.__str__(self)


n = int(input('Введите число строк:\t'))
m = int(input('Введите число столбцов:\t'))


def rand_list(a, b):
    lst = [[randint(0, 9) for i in range(a)] for j in range(b)]
    return lst


m1 = Matrix(rand_list(n, m))
m2 = Matrix(rand_list(n, m))

print(m1)
print(m2)
print(m1 + m2)
