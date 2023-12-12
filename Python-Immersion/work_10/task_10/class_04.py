'''
Динамеческая структура класса
- добавлять атрибуты можно в процессе работы, а не только 
в момент создания класса

'''
class Person:
    max_up = 3

p1 = Person()
p2 = Person()

# если в процессе работы мы добавим атрибут классу, то 
# он появится у всех экземпляров этого класса
Person.level = 1
print(f'{Person.level = }, {p1.level = }, {p2.level = }')

# если мы добавим атрибут для экземляра, то увидим следующее: 
p1.health = 100
# получим ошибку, что у класса Person() отсутствует атрибут health
# print(f'{Person.health = }, {p1.health = }, {p2.healt
# у экземпляра класса Person (а именно p2) отсутствует атрибут health 
# print(f'{p1.health = }, {p2.health = }') # AttributeError: 'Person' object has no attribute 'health'
print(f'{p1.health = }')
