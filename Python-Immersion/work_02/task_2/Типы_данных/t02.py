data = 42
print(isinstance(data, int))

data = True                         # логические типы True/Flase являются подклассами целого числа int 
print(isinstance(data, int))

data = 3.14
print(isinstance(data, (int, float, complex)))
