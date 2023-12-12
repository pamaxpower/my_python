'''
ПроверОчка
'''
class A:
    name = 'A'
    def call(self):
        print(f'I am {self.name}')

class B:
    name = 'B'
    def call(self):
        print(f'I am {self.name}')

class C:
    name = 'C'
    def call(self):
        print(f'I am {self.name}')

class D(C, A):
    pass

class E(D, B):
    pass

e = E()
# print(*E.mro(), sep='\n')
e.call()

# Ответ:
# порядок вызова классов: E, D, C, A, B, object
# метод call() вызовет первый метод call() -> а именно C 

