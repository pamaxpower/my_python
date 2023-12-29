'''
Возврат итератора __iter__
- используется для возврата объекта-итератора
- если объект есть, то он вернет сам себя
'''

class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

    # возвращаем объект-итератор
    def __iter__(self):
        return self

fib = Fibonacci(20, 100)
# но итерировать еще не можем, тк вернулся не итерируемый объект
for num in fib: # TypeError: iter() returned non-iterator of type 'Fibonacci'
    print(num)
