'''
Доступ к значению словаря
'''

# dict[key]
TEN = 'ten'
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}

print(my_dict['two'])   
print(my_dict[TEN])     
# print(my_dict[1])       # KeyError: 1
print()

# dict.get(key[,default])
print(my_dict.get('two'))       # ключ есть, знаечние 2
print(my_dict.get('five'))      # ключа нет, значения нет -> None
print(my_dict.get('five', 5))   # ключа нет, но значение по умолчанию 5
print(my_dict.get('ten', 5))    # ключ есть, поэтому значение по умолчанию игнорируется

