import unittest

class TestSample(unittest.TestCase):

    def setUp(self) -> None:
        """Перед каждым тестом создается файл top_secret.txt для записи,
        и заполняет его числами от 0 до 10 с нулями в начале, 
        так чтобы общая длина не превышала 5 знаков"""
        with open('top_secret.txt', 'w', encoding='utf-8') as f:
            for i in range(10):
                f.write(f'{i:05}\n')

    def test_line(self):
        """Открывает файл для чтения и проверяет что там 10 строчек"""
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                pass
        self.assertEqual(i, 10)

    def test_first(self):
        """Роверяем, что первая запись в файле '00000' """
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            first = f.read(5)
            self.assertEqual(first, '00000')

    def tearDown(self) -> None:
        """Удалякм файл top_secret.txt после каждого теста"""
        from pathlib import Path
        Path('top_secret.txt').unlink()

if __name__ == '__main__':
    unittest.main()
