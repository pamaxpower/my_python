'''
Проверка
'''

data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items())
print(x)        # объект итератора и место в оперативной памяти
y = next(x)
print(y)        # ('один', 1)
z = next(iter(y))
print(z)        # 'один'
