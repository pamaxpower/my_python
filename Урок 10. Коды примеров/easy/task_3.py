"""
Задание 3.

В этом задании мы применим и дескриптор, и метакласс.

1. Реализовать класс-дескриптор TypedProperty.
В нем нужно перегрузить метод __set__, в котором делаем валидацию,
в которой проверяем, что присваиваемое значение относится к переданному
также в __set__ типу данных. Если не относится даем исключение.
Если относится, нужно обратиться к слотам экземпляра подчиненного класса
и через append добавить нужное значение в атрибуты.

2. Реализовать метакласс TypedMeta
В нем сделать перегрузку метода __new__
В нем перебирать атрибуты подчиненного класса
и на предмет, является ли очередной атрибут экземпляром TypedProperty
isinstance(value, TypedProperty)
и если да, вносим атрибут в слоты.

3. Наконец, сделать подчиненный метаклассу класс MyClass
class MyClass(metaclass=TypedMeta):
    ''' Пользовательский класс с контролируемыми атрибутами
    '''
    name = TypedProperty(str)
    num = TypedProperty(int)
    zzz = 15
    xxx = 17

Потестить операции с атрибутами его экземпляра, увидеть разницу
"""


class TypedProperty:
    def __init__(self, type_name):
        self.type = type_name

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError(f"Значение должно быть типа {self.type}")

        instance.__slots__.append(value)


class TypedMeta(type):
    """Метакласс, создающий список __slots__,
    который будет содержать только атрибуты типа TypedProperty"""

    def __new__(cls, clsname, bases, clsdict):
        slots = []
        #print(clsdict)
        for key, value in clsdict.items():
            if isinstance(value, TypedProperty):

                value.name = "_" + key
                #print(value.name)
                slots.append(value.name)
        clsdict['__slots__'] = slots
        return type.__new__(cls, clsname, bases, clsdict)


class MyClass(metaclass=TypedMeta):
    """Пользовательский класс с контролируемыми атрибутами"""
    name = TypedProperty(str)
    num = TypedProperty(int)
    zzz = 15
    xxx = 17


mc = MyClass()
mc._name = 'Ivan'
# Попытка добавить новый атрибут объекту приведёт к исключению:
# foo.xxx = 13
print(mc._name)
