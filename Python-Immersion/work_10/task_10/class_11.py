'''
ПроверОчка
'''

class User:
    count = []
    def __init__(self, name, phone):
        # self.count = []       # такая бы запись кода соответствовала моему ответу
        self.name = name
        self.phone = phone

u1 = User('One', '123-45-67')       # name='One', phone='123-45-67'
u2 = User('NoOne', '76-54-321')     # name='Two', phone='76-54-321'
u1.count.append(42)                 # p1.count -> [42]
u1.count.append(73)                 # p1.count -> [42, 73]

u2.counter = 256                    # p2.counter = 256
u2.count.append(u2.counter)         # u2.counter = [256]
u2.count.append(u1.count[-1])       # p1.count -> [256, 73]

print(f'{u1.name = }, {u1.phone = }, {u1.count = }')
# name='One', phone='123-45-67', count = [42]

print(f'{u2.name = }, {u2.phone = }, {u2.count = }')
# name='Two', phone='76-54-321', count = [256, 73]




# Праивльный ответ:
# в обоих экземплярах список будет одинаковый, тк атрибут
# count принаджеит всему классу, а значит и всем его 
# экземплярам. И имеет значение [42,73,256,256]
