"""
Задание №9
Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
"""

for i in range(2, 10):
    for j in range(2, 10):
        print(f'{i} * {j} = {i * j}')
    print()


'''
for i in range(2, 10):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end='\n')
    print()
'''