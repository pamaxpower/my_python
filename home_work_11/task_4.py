"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
s = ['разработка', 'администрирование', 'protocol', 'standard']
for el in s:
    print(f'{el} \t {type(el)}')
    enc = el.encode('utf-8')
    print(f"{enc} \t {type(enc)}")
    dec = enc.decode('utf-8')
    print(f"{dec} \t {type(dec)}\n")