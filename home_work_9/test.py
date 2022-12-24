import unittest
from scripts import *


class TestScripts(unittest.TestCase):
    def setUp(self):
        # тут будут необходимые данные для проведения тестов
        self.lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
        self.res_unique = [23, 1, 3, 10, 4, 11]
        self.lst2 = [5, 4, 3, 2, 1, 0]
        self.res_large = [7, 23, 44, 10]
        self.cell1 = 10
        self.cell2 = 7
        pass

    def tearDown(self):
        pass

    def test_my_func(self):
        self.assertEqual(my_func(2, -3), 0.125)

    def test_unique_items(self):
        self.assertEqual(unique_items(self.lst), self.res_unique)

    def test_unique_items_2(self):
        # тест будет пройдет, если будет не пустой список
        self.assertTrue(unique_items(self.lst2))

    def test_larger_item(self):
        self.assertEqual(larger_item(self.lst), self.res_large)

    def test_larger_item_2(self):
        # тест будет пройден, если список будет пустой
        self.assertFalse(larger_item(self.lst2))

    def test_class_car(self):
        # тест будет пройдет, если A экземпляр класса B
        self.assertIsInstance(Car(60, 'Red', 'Mazda'), Car)

    def test_cell(self):
        # тест будет пройдет, если ссылаются на разные объекты
        self.assertIsNot(Cell(20), Cell(20))

    def test_cell_2(self):
        self.assertNotEqual(Cell(self.cell1)/Cell(self.cell2), 1)

    def test_cell_3(self):
        self.assertLess(self.cell1 - self.cell2, 5)

    def test_error(self):
        self.assertRaises(ZeroDivision, divizion, 5, 0)




    
