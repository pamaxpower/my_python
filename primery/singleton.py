"""
Создать метакласс для паттерна Синглтон (см. конец вебинара)
"""

"""
    _instances = None
    print(type(_instances))

    def __new__(self, name, bases, dict):
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__new__(name, bases, dict)
        return self._instances[self]
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
"""


class Singleton(type):
    a = None

    def __new__(cls, clsname, superclasses, attributedi):
        if cls == None:
            cls = type.__new__(cls, clsname, superclasses, attributedict)
        return cls


class Cell(metaclass=Singleton):
    pass


cell = Cell()
cell2 = Cell()
print(cell)
print(cell2)
print(cell is cell2)

"""
class NewClass(type):
    def __new__(cls, name, bases, dict):
        a = super(NewClass, cls).__new__(cls, name, bases, dict)
        print(name)
        print(bases)
        print(dict)
        return a


class MyClass(metaclass=NewClass):
    pass


obj = MyClass()
obj2 = MyClass()
"""