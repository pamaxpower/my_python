'''
Задание №2

Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
'''

from math import factorial
from json import dump


class Factorial:
    def __init__(self, count):
        self.count = count
        self.history = []

    def __call__(self, n):
        result = factorial(n)
        self.history.append({n: result})
        self.history = self.history[-self.count:]
        return result
    
    def get_history(self):
        return self.history
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('factorial_history.json', 'w', encoding='utf-8') as f:
            dump(self.history, f, ensure_ascii=False, separators=(', ', ':'))

if __name__ == '__main__':
    fact = Factorial(5)
    with fact as js:
        for i in range(1,10):
            fact(i)
    