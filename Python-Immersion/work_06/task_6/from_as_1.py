'''
Зарезервированные слова from и as

- используя слово from, можно импортировать не весь модуль, а только определенные объекты:
from sys import builtin_module_names, path

- с помощью ключевого слова as можно присвоить псевдоним:
import random as rnd
'''

import random as rnd
from sys import builtin_module_names as bmn, path as p

print(bmn)
print(*p, sep='\n')
print(rnd.randint(1, 6))
print(path)             # NameError: name 'path' is not defined
print(sys.path)         # NameError: name 'sys' is not defined
