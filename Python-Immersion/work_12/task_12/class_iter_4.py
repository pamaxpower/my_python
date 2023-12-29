'''
Проверка
'''
class Iter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        for i in range(self.start, self.stop):
            # self.start += 1
            return chr(i)
        raise StopIteration

chars = Iter(65, 91)
for c in chars:
    print(c)

# Выведет построчно символы Unicode, соответствующие числам от 65 до 91, а именно латинский алфавит

# Правильный ответ: код будет бесконечно вызывать букву A, 
# потому что каждый раз функция вызывает параметры 65 и 91
# Чтобы код работал правильно и выводил латинский алфавит от A до Z, 
# нужно либо прибавлять 1 к параметру start, 
# либо вместо цикла for использовать цикл while