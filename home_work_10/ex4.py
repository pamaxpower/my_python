"""
Создать метакласс для паттерна Синглтон (см. конец вебинара)
"""


class Singleton(type):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = None

    def __call__(self, *args, **kwargs):
        if self.value is None:
            # Если еще не создан ни один экземпляр класса, создаем его
            self.value = super().__call__(*args, **kwargs)
            return self.value
        else:
            # Если уже есть экземпляр класса, возвращаем его
            return self.value


class Cell(metaclass=Singleton):
    pass


cell1 = Cell()
cell2 = Cell()
print(cell1)
print(cell2)
print(cell1 is cell2)

