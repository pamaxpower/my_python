'''
Проверка
'''
import random
from sys import argv

print(argv)
print(random.uniform(int(argv[1]), int(argv[2])))
print(random.randrange(int(argv[1]), int(argv[2]), int(argv[1])))
print(random.sample(range(int(argv[1]), int(argv[2]), int(argv[1])), 10))

# скрипт запущен командой python box_modules_4.py 10 1010

# в argv сохранится список ['name_file', 10', '1010']
# 1) вещественное число от 10 до 1010
# 2) число от 10 до 1010, кратное 10
# 3) вернет 10 элементов из последовательности от 10 до 1010 с шагом 10