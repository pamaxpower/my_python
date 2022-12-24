# Все, что вы видите в Python – объекты.
# В том числе и строки, числа, классы и функции.
# ЭТО ВЕДЬ КЛАССЫ! ОКАЗЫВАЕТСЯ У КАЖДОГО ИЗ ЭТИХ КЛАССОВ ТОЖЕ ЕСТЬ КЛАСС - СВЕРХКЛАСС

# начнем
AGE = 35
print(AGE.__class__.__class__)

NAME = 'Иван'
print(NAME.__class__)


def my_func():
    pass


print(my_func.__class__)


class MyClass:
    pass


MC = MyClass()
print(MC.__class__)


# Получается каждый из этих объектов относится к классу
# это мы знаем
# а теперь самое интересное

print(AGE.__class__.__class__)

print(NAME.__class__.__class__)

print(my_func.__class__.__class__)

print(MC.__class__.__class__.__class__)

# запускаем. вот это да!
"""
<class 'int'>
<class 'str'>
<class 'function'>
<class '__main__.MyClass'>

<class 'type'>
<class 'type'>
<class 'type'>
<class 'type'>
"""


# Получается у каждого из стандартных классов тоже есть класс-метакласс type
class NewClass(type):
    def __new__(cls, name, bases, dict):
        new_class = super(NewClass, cls).__new__(cls, name, bases, dict)
        print(name)
        print(bases)
        print(dict)
        return new_class


class Parent_1:
    pass


class MyClass(Parent_1, metaclass=NewClass):
    pass


obj = MyClass()
