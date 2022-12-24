class Singleton(type):
    # Должен вернуть словарь для атрибутов класса
    a = None

    def __new__(mcs, name, bases, dct):
        if mcs.a is None:
            mcs.a = type.__new__(mcs, name, bases, dct)
        else:
            return mcs.a


class Test(metaclass=Singleton):
    pass


T_OBJ = Test()
T_OBJ_1 = Test()
print(T_OBJ is T_OBJ_1)

"""
__new__() вызывается для создания класса;
__init__() для инициализации класса;
__call__() вызывается при создании объектов класса;
"""
