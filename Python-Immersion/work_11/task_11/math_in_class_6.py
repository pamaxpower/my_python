'''
Проверка
'''

class MyClass:
    def __init__(self, data):
        self.data = data

    def __and__(self, other):
        return MyClass(self.data + other.data)
    
    def __str__(self):
        return str(self.data)

a = MyClass((1, 2, 3, 4, 5))
b = MyClass((2, 4, 6, 8, 10))
print(a & b)

# код вернет кортеж из 10 значений: 5 от первого экземпляра, 5 от второго
