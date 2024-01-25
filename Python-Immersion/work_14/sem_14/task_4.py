'''
Задание №4

Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
'''

import pytest
from task_1 import func


def test_method_1():
    assert func('hello'), 'hello'


def test_method_2():
    assert func('YoU mY bRoTHer'), 'you my brother'


def test_method_3():
    assert func('hello world!!!'), 'hello world'


def test_method_4():
    assert func('Валера cool'), ' cool'


def test_method_5():
    assert func('100 раз YoU говорю!'), '  you '



# def test_1():
#     assert func('hello world') == 'hello world', 'ошибка тест 1'
# def test_2():
#     assert func('HelLO WorlD') == 'hello world', 'ошибка тест 2'
# def test_3():
#     assert func('Hello, world!') == 'hello world', 'ошибка тест 3'
# def test_4():
#     assert func('hello мой world') == 'hello  world', 'ошибка тест 4'
# def test_5():
#     assert func('HelLO# мой$ WorlD!!') == 'hello  world', 'ошибка тест 5'

if __name__ == '__main__':
    pytest.main(['-v'])