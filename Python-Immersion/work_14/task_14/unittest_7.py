''' Проверка
Что делает программа
'''

import unittest
from main import func

class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
    
    def test_step_1(self):
        self.assertEqual(func(self.data), 4)
    
    def test_step_2(self):
        self.assertEqual(func(self.data, first=False), 2)

if __name__ == '__main__':
    unittest.main()


# Метод setUp пере каждым тестом создает словарь, где ключ это слово, 
# а значение его значение
    
# 1 тест - проверка на равенство. На вход функции принимает словарь, 
# а на выходе должны получить 4. Могу предположить, что это кол-во ключей 
# в словаре
# Правильно: значение ключа, если бы ключи были отсортированы в алфавитном порядке

# 2 тест - проверяет тот же словарь, что и первый - ...
# Правильно: значение ключа, если бы они были отсортированы в обратном порядке
