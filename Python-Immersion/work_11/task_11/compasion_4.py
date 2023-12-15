'''
Неизменяемые экземпляры, хэширование дандер __hash__

- для проверки на неизменяемость используется функция hash()

Общее правило:

● нет __eq__,   нет __hash__ - неизменяемый объект. 
Python сам реализует оба дандера

● есть __eq__,  нет __hash__ - изменяемый объект.
Python устанавливает __hash__ = None

● есть __eq__,  есть __hash__ - неизменяемый объект.
Реализуется разработчиком

● нет __eq__,   есть __hash__ - запрещённая комбинация!
Разработчик допустил ошибку

Чтобы явно отключить поддержку хеширования, в определение класса 
добавляется строка __hash__ = None

'''

from compasion_3 import Triangle


trangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)}
print(trangle_set)

# вызывает ошибку, потому что не реальзован дандер __hash__
print(', '.join(f'{hash(item)}' for item in trangle_set)) # TypeError: unhashable type: 'Triangle'

# но если закомментировать метод __eq__, то экземпляры станут хешируемыми