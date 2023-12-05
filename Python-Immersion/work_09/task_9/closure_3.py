# Используем код функции из предыдущего примера

from typing import Callable

def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    return add_two_str

# присваиваем переменным значение функции:
# в первом случае замыкаем строку "Hello", во втором - 'Good bye'
hello = add_one_str('Hello')
bye = add_one_str('Good bye')

# как итог, при вызове функции получаем склейку двух строк
print(hello('world!'))              # Hello world!
print(hello('friend!'))             # Hello friend!
print(bye('wonderful world!'))      # Good bye wonderful world!

# следующие строки кода показывают:
# 1) тип переменной (все функции)
# 2) имя функции: первая является сама собой, а две другие разными экземплярами первой функции
# 3) адреса в оперативной памяти - у всех функций разные
print(f'{type(add_one_str) = }, {add_one_str.__name__ = }, {id(add_one_str) = }')
print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')
