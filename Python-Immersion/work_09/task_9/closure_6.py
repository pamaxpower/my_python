'''
Проверка
'''

from typing import Callable


def main(x: int) -> Callable[[int], dict[int, int]]:
    d = {}
    def loc(y: int) -> dict[int, int]:
        for i in range(y):
            d[i] = x ** i
        return d
    return loc

small = main(42)    # замыкаем число 42
big = main(73)      # замыкаем число 73

print(small(7))     # получаем словарь с ключами от 0 до 6 (вкл) и значением: степень 42
print(big(7))       # такой же словарь, но значение это степени числа 73

print(small(3))     # словарь как из первого вывода: т.к. значения не поменяются


# Ответы:
# 1) Верно
# 2) Верно
# 3) Верно
