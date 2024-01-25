'''
Задание №3

Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
* возврат строки без изменений
* возврат строки с преобразованием регистра без потери
символов
* возврат строки с удалением знаков пунктуации
* возврат строки с удалением букв других алфавитов
* возврат строки с учётом всех вышеперечисленных пунктов
'''

import unittest
from task_1 import func


class TestCaseName(unittest.TestCase):


    def test_method_1(self):
        self.assertEqual(func('hello'), 'hello')


    def test_method_2(self):
        self.assertEqual(func('YoU mY bRoTHer'), 'you my brother')


    def test_method_3(self):
        self.assertEqual(func('hello world!!!'), 'hello world')


    def test_method_4(self):
        self.assertEqual(func('Валера cool'), ' cool')


    def test_method_5(self):
        self.assertEqual(func('100 раз YoU говорю!'), '  you ')


if __name__ == '__main__':
    unittest.main(verbosity=2)        