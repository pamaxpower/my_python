'''
Обращение к несуществующему атрибуту, __getattr__
Если в классе свойство отсутствует, то вызывается метод __getattribute__.
В случае, если он возвращает ошибку AttributeError вызывается метод __getattr__

Общий вид:
class Name():
    ...
    def __getattr__(self, item):
        ...
        return ...
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

a = Vector(2, 4)

# Метод __getattr__ вызывает None для любого свойства, которого не удалось найти
print(a.z)          # None
print(a.W)          # None

print(f'{a = }')
