''''
Строгая динамическая типизация:

type(object) - возвращает класс объекта и его тип
id(object) - возвращает адрес объекта в оперативной памяти
isinstance(object, classinfo) - принимает объект и класс и возвращает истину, если объект является экземпляром данного класса
is - сравнивает пару объектов на идентичность

'''

a = 5
print(type(a), id(a))

a = 'hello world'
print(type(a), id(a))

a = 42.0 * 3.141592 / 2.71828
print(type(a), id(a))


