'''
Классы bytes (неизменяемые) и bytearray(изменяемые)
'''

text_en = 'Hello world!'
res1 = text_en.encode('utf-8')
print(res1, type(res1))

text_ru = 'Привет, мир!'
res2 = text_ru.encode('utf-8')
print(res2, type(res2))
print()

x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(f'{x = }\n{y = }')
