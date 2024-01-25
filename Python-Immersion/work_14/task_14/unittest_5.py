'''
Подготовка тестов и сворачивание работ
- развертывание тестируемой стреды и уборка лишнего после ее завершения
используются фикстуры:

*** метод setUp - выполняется перед запуском каждого теста

*** метод tearDown - выполняется, если был выполнен setUp, 
независимо от того пройдет тест или провален
'''

import unittest

class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [2, 3, 5, 7]
        print('Выполнил setUp') # Только для демонстрации работы метода
    
    def test_append(self):
        self.data.append(11)
        """Добавляем число 11"""
        self.assertEqual(self.data, [2, 3, 5, 7, 11])

    def test_remove(self):
        """Удаляем число 5"""
        # каждый тест работает с исходным списокм!!!
        self.data.remove(5)
        self.assertEqual(self.data, [2, 3, 7])
    
    def test_pop(self):
        """Удаляем последнее число"""
        self.data.pop()
        self.assertEqual(self.data, [2, 3, 5])

if __name__ == '__main__':
    unittest.main()
