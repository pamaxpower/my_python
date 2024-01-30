'''
Массив array поддерживает методы типа list
'''

from array import array

long_array = array('l', [-6000, 800, 100500])
long_array.append(42)

print(long_array)
print(long_array[2])
print(long_array.pop())


# Однако нельзя добавить значение ,если оно выходит за 
# пределы диапазона, заданного кодом типа при создании

# long_array.append(2**32) # OverflowError: Python int too large to convert to C long
# long_array.append(3.14) # TypeError: 'float' object cannot be interpreted as an integer
