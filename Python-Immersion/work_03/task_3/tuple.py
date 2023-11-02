'''
Кортежи - неизменяемая коллекция (список)
 
Аналогичны со списками, только ставятся не [], а ()
Методы, которые изменяют список к кортежам не применимы (будет ошибка)

Применяются:
* индексация и срезы
* методы count() и index()
* функция len() 

'''

mtup = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)

print(mtup[2:6:2])          # (6,8)
print(mtup[-3])             # 14
print(mtup.count(2))        # 2
print(f'{mtup = }')         # mtup = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
print(mtup.index(2, 2))     # 3
print(type('text',))        # str