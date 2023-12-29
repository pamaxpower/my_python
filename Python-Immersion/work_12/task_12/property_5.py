'''
Антипаттерны сеттера, геттера и делейтера
'''

class BadPattern:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

# На самом деле, код работает и ошибку не вызывает, но он ничего не делает.
# В идеале он должен выглядеть так:
# class GoodPattern:
#     def __init__(self, x):
#         self.x = x
# потому что без защиты свойство переменной x можно изменять и удалять
        
        