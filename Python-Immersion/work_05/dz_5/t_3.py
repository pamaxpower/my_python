'''
Задача 3.

Создайте функцию генератор чисел Фибоначчи fibonacci.
'''

def fibonacci():
    f1 = 0
    f2 = 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2
        
        

res = fibonacci()
for i in range(10):
    print(next(res))