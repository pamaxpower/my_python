''' Проверка '''
d = {'42': 73}
try:
    key, value = input('Ключ и значение: ').split()
    if d[key] == value:
        r = 'Совпадение'
except ValueError as e:
    print(e)
except KeyError as e:
    print(e)
else:
    print(r)
finally:
    print(d)

# Ключ и значение: 42 13 >>> ValueError {'42': 73}
# Ключ и значение: 42 73 3 >>> ValueError {'42': 73}
# Ключ и значение: 73 42 >>> "Совпадение" {'42': 73}
# Ключ и значение: 42 73 >>> KeyError {'42': 73}

# Разбор кода:
# 1) При введении чисел не происходит преобразование в int, поэтому 
# 2) условие if выполнено не будет и присваивание в переменную r тоже не будет
# 3) Ошибки ValueError и KeyError не сработают, выполнится блок кода else
# 4) при попытке вызвать r получим ошибку NameError
    
# Правильные ответы:
# {'42': 73} NameError: name 'r' is not defined
# {'42': 73} NameError: name 'r' is not defined
# Ловим ошибку KeyError: '73' {'42': 73}
# {'42': 73} NameError: name 'r' is not defined
