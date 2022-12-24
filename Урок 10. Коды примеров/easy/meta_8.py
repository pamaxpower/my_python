"""Пример метакласса, переопределяющего поведение методов __new__ и __init__ своих классов"""


class MyMetaClass(type):
    # Должен вернуть словарь для атрибутов класса
    @classmethod
    def __prepare__(metacls, name, bases):
        print('Перегружаю prepare')
        return type.__prepare__(metacls, name, bases)

    # Должен создать и вернуть новый класс
    def __new__(cls, name, bases, dct):
        print(f'Выделение памяти для класса {name}, '
              f'имеющего кортеж базовых классов {bases}, '
              f'и словарь атрибутов {dct}')
        return type.__new__(cls, name, bases, dct)
    # Должен инициализировать созданный класс
    def __init__(cls, name, bases, dct):
        print(f'Инициализация класса {name}')
        super(MyMetaClass, cls).__init__(name, bases, dct)
    # Должен создать и вернуть экземпляр нового класса
    def __call__(self, *args, **kwargs):
        print('Перегружаю call')
        return type.__call__(self, *args, **kwargs)


# родитель 1
class Parent_1():
    pass

# родитель 2
class Parent_2():
    pass

# пользовательский класс
class MyClass(Parent_1, Parent_2, metaclass=MyMetaClass):

    my_attr = 10

    def __call__(self):
        return 'Кто вперед!'


MC = MyClass()
print(MC())

