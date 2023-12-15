'''
ОБЫЧНЫЕ МЕТОДЫ

Сдвиг вправо, __rshift__

'''

from random import choices

class Closet:
    CLOTHES = ('брюки', 'рубашка', 'костюм', 'футболка', 'перчатки', 'носки', 'туфли')
    def __init__(self, count: int, storerom=None):
        self.count = count
        if storerom is None:
            self.storerom = choices(self.CLOTHES, k=count)
        else:
            self.storerom = storerom
    
    def __str__(self):
        names = ', '.join(self.storerom)
        return f'Осталось вещей в шкафу {self.count}:\n{names}'
    
    def __rshift__(self, other):
        shift = self.count if other > self.count else other
        self.count -= shift
        return Closet(self.count, choices(self.storerom, k=self.count))


storeroom = Closet(10)
print(storeroom)

for _ in range(4):
    storeroom = storeroom >> 3
    print(storeroom)
