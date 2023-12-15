'''
Проверка
'''

class MyClass:
    A = 42
    """About class"""

    def __init__(self, a, b):
        """self.__doc__ = None"""
        self.a = a
        self.b = b

    def method(self):
        """Documentation"""
        self.__doc__ = None

help(MyClass)

# код выведет информацию о классу
# строка """About class""" показана не будет, тк записана не после определения
# строка """self.__doc__ = None""" будет показана как строка
# строка  """Documentation""" тоже будет показана
# еще добавятся дандер методы __dict__ и __weakref__ 