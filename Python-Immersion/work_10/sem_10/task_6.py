'''
Задание №6

Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
'''

class Animal():
    def __init__(self, kind, name, areal):
        self._kind = kind
        self._name = name
        self._areal = areal

    def get_kind(self):
        return self._kind
    
    def get_name(self):
        return self._name
    
    def get_areal(self):
        return self._areal


class Fish(Animal):
    def __init__(self, kind, name, areal, size: int):
        self._size = size
        super().__init__(kind, name, areal)

    def get_spec(self):
        return f'Длина тела - {self._size}'


class Bird(Animal):
    def __init__(self, kind, name, areal, wingspan: int):
        self._wingspan = wingspan
        super().__init__(kind, name, areal)
    
    def get_spec(self):
        return f'Размах крыльев - {self._wingspan}'


class Amphibian(Animal):
    def __init__(self, kind, name, areal, color: str):
        self._color = color
        super().__init__(kind, name, areal)
    
    def get_spec(self):
        return f'Цвет - {self._color}'


class Insect(Animal):
    def __init__(self, kind, name, areal, venomous: bool):
        self._venomous = venomous
        super().__init__(kind, name, areal)

    def get_spec(self):
        return f'Ядовитый - {self._venomous}'
    

f1 = Fish('Дельфин', 'Иннокентий', 'Черное море', 3)
print(f'Особенность класса: {f1.get_spec()} м') 
print(f'Вид персонажа: {f1.get_kind()}')

n1 = Insect('Шершень', 'Жужик', 'Цветочная поляна', True)
print(f'Особенность класса: {n1.get_spec()}')
print(f'Место обитания: {n1.get_areal()}')