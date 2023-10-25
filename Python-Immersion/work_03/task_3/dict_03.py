'''
Методы работы со словарями
'''

# setdefault()

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')               # ключа нет, значение None, но в словаре создалась пара 'five": None
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6)             # ключа нет, значение по умолчанию, в словаря добавляется пара 'six': 6
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')            # ключ есть, значение 2
print(f'{new_spam=}\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)     # ключ есть, значение по умолчанию игнорируется
print(f'{new_eggs=}\t{my_dict=}')

# keys() - возвращает список ключей словаря

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys())
for key in my_dict.keys():
    print(key)

# values() - возвращает список значений словаря

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.values())
for value in my_dict.values():
    print(value)

# items() - возвращает пару (ключ: значение)

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())

for key, value in my_dict.items():
    print(f'{key = } value before 100 - {100 - value}')
 
# popitems() - удаление последней добавленой пары (ключ: значение)

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')
print()

# pop() - удаление пары (ключ: значение) по ключу

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')
# err = my_dict.pop('six')        # KeyError: 'six'
# err = my_dict.pop()             # TypeError: pop expected at least 1 argument, got 0

# update() - расширяет исходный словарь
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)]))
print(my_dict, '\n')

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
print(new_dict)
