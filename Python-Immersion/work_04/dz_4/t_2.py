'''
Напишите функцию key_params, принимающую на вход только ключевые 
параметры и возвращающую словарь, где ключ - значение переданного аргумента, 
а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''
def key_params(**kwargs):
    res = {}
    for key, value in kwargs.items():
        # if type(value) in (int, float, bool):
        if isinstance(value, (int, str, float, bool, tuple)):
            res[value] = str(key)
        else:
            res[str(value)] = str(key)
    return res

params = key_params(a=False, b='hello', c=[1, 2, 3], d={})

print(params)