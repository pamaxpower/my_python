from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_method_1(self):
        pass

    @abstractmethod
    def my_method_2(self):
        pass


class MyClass(MyAbstractClass):
    pass

mc = MyClass()

"""
TypeError: Can't instantiate abstract class MyClass with abstract methods my_method_1, my_method_2
"""
