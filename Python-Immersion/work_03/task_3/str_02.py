txt = 'Hello world!'

print(txt.count('l'))       # кол-во вхождений
print(txt.index('l'))       # первое вхождение
print(txt.find('l'))        # тоже самое что и index()
print(txt.find('z'))        # в отличие от index() вернет -1, 
                            # если значение отсутствует

print(txt[::-1])            # реверс строки