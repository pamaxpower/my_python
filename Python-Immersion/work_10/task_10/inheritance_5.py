'''
MRO - method resolution order (порядок разрешения методов”)
- в основе лежит алгоритм C3-линеаризации 
(представление иерархической структуры - графов - в линейную)

Пример:
1. Классы A, B, C, D не имеют родительского класса. Точнее они
наследуются от прародителя object. 
У каждого из классов есть по параметру.

2. Три класса X имеют по два родительских класса.

3. Класс Z наследуется от трёх классов X.

'''

class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'

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


print(*Z.mro(), sep='\n')


# Разберем MRO класса Z:
# 1) Отрабатывает инициализация класса Z
# 2) Далее X1 и X2 (по порядку следования родительских класса)
# 3) Далее B (!!!)
#             - по приоритету идут классы X, а потом его наследники (после X1 должны идти A и D)
#             - A и D идти не могут, потому что являются дочерними еще у двух классов (а дочерние не могут идти раньше родительских)
#             - у X2 два родителя B и D
# 4) Далее идет класс X3
# 5) Потом наследники классов X: A, C, D
# 6) и последним будет класс object

z = Z()
# Вызов метода __init__ остановился на классе B
print(f'{z.data_b = }')
# все дальнейшие действия не были произведены
print(f'{z.data_a = }') # AttributeError: 'Z' object has no attribute 'data_a'
