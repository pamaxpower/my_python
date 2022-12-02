'''
Функции
'''


def new_string(symbol, count):
    return symbol * count
print(new_string('!', 5))   # !!!!!
# print(new_string('!'))      # TypeError: new_string() missing 1 required positional argument: 'count'


def new_string2(symbol, count = 3):
    return symbol * count
print(new_string2('!', 5))      # !!!!!
print(new_string2('!'))         # !!!   - параметр count задан по умолчанию
print(new_string2(4))           # 12    - 


def concatenatio(*params):      # позволяет вносить любое число агрументов в функцию
    res: str = ''
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'f'))     # asdf
print(concatenatio('a', '1', 's'))          # a1s
# print(concatenatio(1, 2, 3, 4))             # TypeError: can only concatenate str (not "int") to str


def fib(n):                         # Рекурсивная функция
    if n in [1, 2]:                 # услоыие выхода из рекурсии (можно указывать значения списком)
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)