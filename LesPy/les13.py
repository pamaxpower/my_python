"""
Функция zip()
- применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных

zip ([1, 2, 3], ['a', 'b'. 'c'], ['й', 'ц', 'у'])   ->  [(1, 'a', 'й'), (2, 'b', 'ц'), (3, 'c', 'у')]

"""

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids))
data1 = list(zip(users, ids, salary))           # функция zip пробегается по минимальному входящему набору
print(data)
print(data1)    # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

