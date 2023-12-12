'''
Доступ к приватным переменным

Приватная переменная __max_up не исчезает за пределами класса. 
Срабатывает механизм модификации имени - он превращает переменную
__name в переменныю _classname__name.
'''

class Person:
    __max_up = 3
    ...

p1 = Person()
# print(p1.__max_up)        # ошибка AttributeError
print(f'{p1._Person__max_up = }')