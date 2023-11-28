'''
Pickle - модуль Python для сериализации и десериализации 
структур в потом байт

- возможно преобразовать в любом месте и в любое время
- подходит только для языка Python
 модуль не занимается проверкой потока байт на безопасность 
 перед распаковкой, поэтому использовать его надо с осторожностью

Типы данных, допустимые для преобразования pickle:

● None, True и False;
● Числа: int, float, complex;
● Строки: str, bytes, bytearrays;
● Коллекции: tuple, list, set, dict 
если они содержат объекты, обрабатываемые pickle;

● встроенные функции и функции созданные разработчиком 
и доступные из верхнего уровня модуля, кроме 
lambda функций;

● классы доступные из верхнего уровня модуля;

● экземпляры классов, если pickle смог обработать их 
дандер __dict__ или результат вызова метода __getstate__().

'''

import pickle
import os

res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")

print(res)

os.system('echo Hello world!')