'''
Возврат очередного значения __next__
- создает цикл, пока значение не превысит значение stop
- получаем пару значений чисел Фибоначчи
- если значение оказывается в нужно диапазоне [start, stop], то возвращаем его
- проверяем на вызов ошибки StopIteration
'''

class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.first < self.stop:
            self.first, self.second = self.second, self.first + self.second
            if self.start <= self.first < self.stop:
                return self.first
        raise StopIteration


fib = Fibonacci(20, 100)
for num in fib:
    print(num)