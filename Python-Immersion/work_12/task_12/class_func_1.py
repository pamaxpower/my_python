'''
Класс как функция

- при желании можно заставить экземпляры класса вести себя как функции, 
указывая в круглых скобках параметры для вызова
'''

class Number:
    def __init__(self, num):
        self.num = num

n = Number(42)
print(f'{callable(Number) = }')
print(f'{callable(n) = }')
