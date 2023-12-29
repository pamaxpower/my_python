'''
Задание №1

Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.

'''
from math import factorial

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
    
if __name__ == '__main__':
    fact = Factorial(5)
    for i in range(1,10):
        fact(i)
        # print(f'{i}! = {fact(i)}')
    print(fact.get_history())
    




