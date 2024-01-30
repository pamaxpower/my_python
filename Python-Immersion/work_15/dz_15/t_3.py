'''
Дополнтельная задача #2

Возьмите любые 1-3 задания из прошлых домашних заданий. 

Добавьте к ним логирование ошибок и полезной информации. 

Также реализуйте возможность запуска из командной строки с передачей параметров. 



За основу взял класс прямугольника с функцией поиска площади

'''


import argparse
import logging


class NegativeValueError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Rectangle:
    def __init__(self, width, height):
        self._width = None
        self._height = None
        self.set_width(width)
        self.set_height(height)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self.set_width(value)

    def set_width(self, value):
        if value < 0:
            raise NegativeValueError("Ширина не может быть отрицательной")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self.set_height(value)

    def set_height(self, value):
        if value < 0:
            raise NegativeValueError("Высота не может быть отрицательной")
        self._height = value

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'
    
    def area(self):
        return self._width * self._height


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Калькулятор площади прямоугольника")
    parser.add_argument('-a', type=int, help='Введите сторону a', default='1')
    parser.add_argument('-b', type=int, help='Введите сторону b', default='1')
    args = parser.parse_args()

    logging.basicConfig(filename="log/t_3.log",
                        filemode='a',
                        encoding='utf-8',
                        format='{asctime} {levelname} функция "{funcName}()" строка {lineno}: {msg}',
                        style='{',
                        level=logging.INFO
                        )

    logger = logging.getLogger(__name__)

    try:
        r1 = Rectangle(args.a, args.b)
        area = r1.area()
        logger = logging.getLogger(__name__)
        logger.info(f'Нашли площадь прямоугольника {r1}. Она равна {area}')
        print(f'Площадь прямоугольника {r1} равна {area}')
    except NegativeValueError as e:
        logger.error(str(e))
