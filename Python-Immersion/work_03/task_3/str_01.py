'''
Строки (str)
'''

txt = 'Hello world'

print(txt[6])           # индексация
print(txt[3:7])         # срез

# .replace(старое значение, новой значение, {кол-во замен})

new_txt = txt.replace('l', 'L', 2)
print(txt, new_txt, sep='   ')
