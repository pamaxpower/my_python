'''
Задание №5

Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
'''

class Fish():
    def __init__(self, kind, name, areal, size: int):
        self._kind = kind
        self._name = name
        self._areal = areal
        self._size = size

    def get_spec(self):
        return f'Длина тела - {self._size}'

class Bird():
    def __init__(self, kind, name, areal, wingspan: int):
        self._kind = kind
        self._name = name
        self._areal = areal
        self._wingspan = wingspan
    
    def get_spec(self):
        return f'Размах крыльев - {self._wingspan}'

class Amphibians():
    def __init__(self, kind, name, areal, color: str):
        self._kind = kind
        self._name = name
        self._areal = areal
        self._color = color
    
    def get_spec(self):
        return f'Цвет - {self._color}'

class Insect():
    def __init__(self, kind, name, areal, venomous: bool):
        self._kind = kind
        self._name = name
        self._areal = areal
        self._venomous = venomous

    def get_spec(self):
        return f'Ядовитый - {self._venomous}'
    
f1 = Fish('Дельфин', 'Иннокентий', 'Черное море', 3)
print(f'Особенность класса: {f1.get_spec()}')

n1 = Insect('Шершень', 'Жужик', 'Цветочная поляна', True)
print(f'Особенность класса: {n1.get_spec()}')