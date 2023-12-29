'''
Итераторы
- если экземпляр класса должен итерироваться, то надо 
реализовать дандер методы __iter__, __next__
'''

class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

fib = Fibonacci(20, 100)
# попытка проитерировать экземпляр выдаст ошибку (тк в методах класса нет нужного функционала)
for num in fib: # TypeError: 'Fibonacci' object is not iterable
    print(num)
