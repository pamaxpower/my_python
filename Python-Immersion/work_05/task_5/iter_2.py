# функция next(iterator[, default])
# - принимает итератор, который вернула функция iter()
# - второй параметр нужен для возврата значения по умолчанию вместо исключения StopIterator

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
# print(next(list_iter)) # StopIteration
print()

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
