"""
Задача 5

Вам предоставлен код на Python из предыдущих задач, 
который содержит два класса: Rectangle и NegativeValueError.

Ваша задача - написать набор тестов для класса Rectangle, 
чтобы убедиться, что он работает правильно и обрабатывает некорректные значения.

Тесты должны быть написаны с использованием модуля pytest.

*Тесты необходимо написать именно в этом порядке!

Тесты:

test_width: Тестирование инициализации ширины. 
    Создайте объект Rectangle с шириной 5 и 
    убедитесь, что ширина установлена правильно.

test_height: Тестирование инициализации ширины и высоты. 
    Создайте объект Rectangle с шириной 3 и 
    высотой 4 и убедитесь, что высота установлена правильно.

test_perimeter: Тестирование вычисления периметра. 
    Создайте объект Rectangle с шириной 5 и 
    вычислите его периметр (должен быть равен 20).

test_area: Тестирование вычисления площади. 
    Создайте объект Rectangle с шириной 3 и высотой 4 
    и вычислите его площадь (должна быть равна 12).

test_addition: Тестирование операции сложения двух прямоугольников. 
    Создайте два объекта Rectangle с ширинами 5 и 3, и высотами 1 и 4 соответственно. 
    Произведите операцию сложения и убедитесь, что полученный 
    прямоугольник имеет правильные значения ширины и высоты.

test_negative_width: Тестирование инициализации отрицательной ширины. 
    Попробуйте создать объект Rectangle с отрицательной шириной (-5) и 
    убедитесь, что это вызывает исключение NegativeValueError.

test_negative_height: Тестирование инициализации отрицательной высоты. 
    Попробуйте создать объект Rectangle с шириной 5 и отрицательной высотой (-4) и 
    убедитесь, что это вызывает исключение NegativeValueError.

test_set_width: Тестирование изменения ширины. 
    Создайте объект Rectangle с шириной 5 и измените его ширину на 10. 
    Убедитесь, что ширина изменена правильно.

test_set_negative_width: Тестирование изменения отрицательной ширины. 
    Создайте объект Rectangle с шириной 5 и попробуйте изменить его ширину 
    на отрицательное значение (-10). Убедитесь, что это вызывает исключение NegativeValueError.

test_set_height: Тестирование изменения высоты. 
    Создайте объект Rectangle с шириной 3 и высотой 4 и измените его высоту на 6. 
    Убедитесь, что высота изменена правильно.

test_set_negative_height: Тестирование изменения отрицательной высоты. 
    Создайте объект Rectangle с шириной 3 и высотой 4 и попробуйте изменить его высоту на отрицательное значение (-6). 
    Убедитесь, что это вызывает исключение NegativeValueError.

test_subtraction: Тестирование операции вычитания двух прямоугольников. 
    Создайте два объекта Rectangle с ширинами 10 и 3, и высотами 1 и 4 соответственно. 
    Произведите операцию вычитания и убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты.

test_subtraction_negative_result: Тестирование операции вычитания с отрицательным результатом. 
    Создайте два объекта Rectangle с ширинами 3 и 10, и высотами 4 и 1 соответственно. 
    Попробуйте выполнить операцию вычитания и убедитесь, что это вызывает исключение NegativeValueError.

test_subtraction_same_perimeter: Тестирование операции вычитания с одинаковым периметром. 
    Создайте два объекта Rectangle с ширинами 5 и 4, и высотами 1 и 3 соответственно. 
    Произведите операцию вычитания и убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты.
"""

import pytest


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(
                f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(
                    f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(
                f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(
                f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


def test_width():
    """Тестирование инициализации ширины"""
    assert Rectangle(5).width, 5


def test_height():
    """Тестирование инициализации ширины и высоты"""
    assert Rectangle(3, 4).height, 4


def test_perimeter():
    """Тестирование вычисления периметра"""
    assert Rectangle(5).perimeter(), 20


def test_area():
    """Тестирование вычисления площади"""
    assert Rectangle(3, 4).area(), 12


def test_addition():
    """Тестирование операции сложения двух прямоугольников"""
    rect1 = Rectangle(5, 1)
    rect2 = Rectangle(3, 4)
    result = rect1 + rect2
    assert result.width == 6
    assert result.height == 7.0


def test_negative_width():
    """Тестирование инициализации отрицательной ширины"""
    with pytest.raises(NegativeValueError):
        Rectangle(-5)


def test_negative_height():
    """Тестирование инициализации отрицательной высоты"""
    with pytest.raises(NegativeValueError):
        Rectangle(5, -4)


def test_set_width():
    """Тестирование изменения ширины"""
    r1 = Rectangle(5)
    r1.width = 10
    assert r1.width, 10


def test_set_negative_width():
    """Тестирование изменения отрицательной ширины"""
    r1 = Rectangle(5)
    with pytest.raises(NegativeValueError):
        r1.width = -10


def test_set_height():
    """Тестирование изменения высоты"""
    r1 = Rectangle(3, 4)
    r1.height = 6
    assert r1.height, 10


def test_set_negative_height():
    """Тестирование изменения отрицательной высоты"""
    r1 = Rectangle(3, 4)
    with pytest.raises(NegativeValueError):
        r1.height = -6


def test_subtraction_negative_result():
    """Тестирование операции вычитания с отрицательным результатом"""
    rect1 = Rectangle(3, 4)
    rect2 = Rectangle(10, 1)
    with pytest.raises(NegativeValueError):
        rect1 - rect2


def test_subtraction():
    """Тестирование операции вычитания двух прямоугольников"""
    r1 = Rectangle(10, 1)
    r2 = Rectangle(3, 4)
    r3 = r1 - r2
    assert r3.width, 7
    assert r3.height, -3


def test_subtraction_same_perimeter():
    """Тестирование операции вычитания с одинаковым периметром"""
    r1 = Rectangle(5, 1)
    r2 = Rectangle(4, 3)
    r3 = r1 - r2
    assert r3.width, 1
    assert r3.height, -2



if __name__ == '__main__':
    import os
    import sys

    # Текущее имя файла
    current_filename = __file__

    # Новое имя файла с добавлением "test_" в начале
    new_filename = "test_1.py"
                    #+ os.path.basename(current_filename))

    # Откройте текущий файл для чтения
    with open(current_filename, 'r') as source_file:
        source_code = source_file.read()
        source_file.close()

    # Запишите код в новый файл
    with open(new_filename, 'w') as new_file:
        new_file.write(source_code)
        new_file.close()

    with open(new_filename, 'r') as new_file:
        file_contents = new_file.read()
        # Выводим содержимое файла на экран
        #print(file_contents)

    # Открываем файл для записи
    with open('pytest_output.txt', 'w') as file:
        # Перенаправляем stdout в файл
        sys.stdout = file

        # Запускаем pytest.main() с нужными параметрами
        pytest.main(["--no-header", '-q', "--durations=0", new_filename])

    # Возвращаем stdout в исходное состояние
    sys.stdout = sys.__stdout__
    # Считываем содержимое файла
    with open('pytest_output.txt', 'r') as file:
        lines = file.readlines()
        first_line = file.readline()
        first_five_lines = lines[:1]

    # Выводим первые 5 строк
    for line in first_five_lines:
        print(line)
