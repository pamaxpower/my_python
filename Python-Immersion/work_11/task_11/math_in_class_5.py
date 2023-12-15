'''
IN PLACE МЕТОДЫ
- используются при короткой записи математического символа слитно 
со знаком равенства ( +=, -=)

- такая запись подразумевает внесение изменений в исходный объект, а не возврат нового экземпляра
и возвращать в методе надо самого себя - self

Вычисление процента вместо нахождения остатка от деления, метод __imod__

'''

from decimal import Decimal

class Money:
    def __init__(self, value: int | float):
        self.value = Decimal(value)

    def __repr__(self):
        return f'Money({self.value:.2f})'
    
    def __imod__(self, other):
        self.value = self.value * Decimal(1 + other / 100)
        return self

m = Money(100)
print(m)
m %= 50
print(m)
m %= 100
print(m)

