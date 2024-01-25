'''
Юниттесты для проверки кода функции is_prime()
'''

import io
import unittest
from unittest.mock import patch
from unittest_2 import is_prime


class TestPrime(unittest.TestCase):

    def test_is_prime(self):
        """Проверяем, является ли число простым"""
        self.assertFalse(is_prime(42))      # только ложь
        self.assertTrue(is_prime(73))       # только правда

    def test_type(self):
        """Проверка типа"""
        self.assertRaises(TypeError, is_prime, 3.14)    # проверка вызова ошибки

    def test_value(self):
        """проверка значения"""
        with self.assertRaises(ValueError): #проверка ошибки
            is_prime(-100)
            is_prime(1)

    @patch('sys.stdout', new_callable=io.StringIO)
    # декоратор patch принимает на вход 'sys.stdout' - стандартный поток вывода и 
    # new_callable=io.StringIO - перехват потока ввода-вывода
    def test_warning_false(self, mock_stdout):
        """Тест на предупреждение о большом числе, если не простое"""
        self.assertFalse(is_prime(100_000_001))     # проверяем на ложь 
        self.assertEqual(mock_stdout.getvalue(), 'If the number P is prime, the check may take a long time. Working...\n')
        # из переменной mock_stdout получаем значение, которое должно совпасть с текстом об ошибке строчкой выше

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_true(self, mock_stdout):
        """Тест на предупреждение о большом числе, если простое"""
        self.assertTrue(is_prime(100_000_007))
        self.assertEqual(mock_stdout.getvalue(), 'If the number P is prime, the check may take a long time. Working...\n')

if __name__ == '__main__':
    unittest.main(verbosity=2)
