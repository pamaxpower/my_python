'''
Если дополнить класс A, добавив туда метод say(),
мы получим вызов этого метода (даже если класс не был инициализирован), 
однако если обратиться напрямую к методу класса A, мы получим ошибку

Пояснение: работая из класса Z мы собираем в себя аргументы и методы 
наследуемых классов, а у класса A нет родительского класса и ему неоткуда 
взять атрибут data_b, который используется в его классе
'''
class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'

    def say(self):
        print('Текст')
        print(self.data_b)
    
class B:
    def __init__(self):
        print('Init class B')
        self.data_b = 'B'

class C:
    def __init__(self):
        print('Init class C')
        self.data_c = 'C'

class D:
    def __init__(self):
        print('Init class D')
        self.data_d = 'D'

class X1(A, C):
    def __init__(self):
        print('Init class X1')
        super().__init__()

class X2(B, D):
    def __init__(self):
        print('Init class X2')
        super().__init__()

class X3(A, D):
    def __init__(self):
        print('Init class X3')
        super().__init__()

class Z(X1, X2, X3):
    def __init__(self):
        print('Init class Z')
        super().__init__()

z = Z()
z.say()

a = A()
a.say()