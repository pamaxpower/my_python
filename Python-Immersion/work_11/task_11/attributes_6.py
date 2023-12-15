'''
Функции setattr(), getattr() и delattr()


В Python есть функции, которые позволяют делать тоже самое, что и 
рассмотренные выше дандер методы. 

Разница лишь в том, что метод реагирует на событие в коде, а функцию мы 
вызываем в тот момент, когда это нужно.

● setattr(object, name, value) — аналог object.name = value

● getattr(object, name[, default]) — аналог object.name or default

● delattr(object, name) — аналог del object.name

'''