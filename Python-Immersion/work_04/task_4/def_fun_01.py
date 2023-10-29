'''
Встроенные функции:

abs(), aiter(), all(), any(), anext(), ascii(), bin(), bool(), 
breakpoint(), bytearray(), bytes(), callable(), chr(), 
classmethod(), compile(), complex(), delattr(), dict(), dir(), 
divmod(), enumerate(), eval(), exec(), filter(), float(), 
format(), frozenset(), getattr(), globals(), hasattr(), hash(), 
help(), hex(), id(), input(), int(), isinstance(), issubclass(), 
iter(), len(), list(), locals(), map(), max(), memoryview(), 
min(), next(), object(), oct(), open(), ord(), pow(), print(), 
property(), range(), repr(), reversed(), round(), set(), 
setattr(), slice(), sorted(), staticmethod(), str(), sum(), 
super(), tuple(), type(), vars(), zip().

Часть 1. 

map(функция, последовательность) - принимает на вход функцию и последовательность,
функция применяется к каждому элементу последовательности и возвращает map-итератор

filter(функция, последовательность) - принимает на вход функцию и последовательность,
если функция возвращает истину, элемент остается в последовательности,
возвращает объект итератор

zip(*последовательности, strict=False) - принимает на вход несколько последовательностей
и итерируется по ним параллельно.
Если strict=True, а число элементов в последовательностях разное, 
то функция вызовет ошибку ValueError

'''

texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res1 = map(lambda x: x.lower(), texts)
print(*res1)


numbers = [42, -73, 1024]
res2 = tuple(filter(lambda x: x > 0, numbers))
print(res2)


names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')

