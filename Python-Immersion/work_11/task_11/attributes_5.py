'''
Удаление атрибута, __delattr__
- срабатывает при попытки удалить свойство класса (del name.attribute)

Общий вид:

class Name():
    ...
    def __delattr__(self, item):
        ...
        object.__delattr__(self, item)
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)
    
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)
    
    def __getattr__(self, item):
        return None
    
    def __delattr__(self, item):
        if item in ('x', 'y'):
            setattr(self, item, 0)
        else:
            object.__delattr__(self, item)


a = Vector(2, 4)

# благодаря методу __setattr__ присваиваем значение свойству s
a.s = 73
print(f'{a = }, {a.s = }')

# удаляем свойства
del a.x     # -> 0  - контролирем значения, в методе __delattr__ код идет по ветке if
del a.s     # -> None - работает ветка else, свойство полностью удаляется
print(f'{a = }, {a.s = }')
