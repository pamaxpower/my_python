'''
Плохой пример импорта:
- вы создали файл random.py и написали там функцию randint
- потом пытаетесь сгенерировать случайное число, используя модуль random
'''

import random_

print(random_.randint(1, 6))

# На выходе получим не искомое число, 
# а результат выполнения функции randint из файла random_.py