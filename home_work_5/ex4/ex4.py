"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные.При этом английские числительные должны заменяться на русские.
 Новый блок строк должен записываться в новый текстовый файл.
"""


num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_text = []

with open('text4.txt', 'r+', encoding="utf-8") as text4:
    with open('file.txt', 'w', encoding="utf-8") as file:
        mylist = text4.readlines()
        for el in mylist:
            el = el.split(' ', 1)
            new_text.append(num[el[0]] + ' ' + el[1])
            print(new_text)
        file.writelines(new_text)
        
        
with open('file.txt', 'r', encoding="utf-8") as file:        
    print(file.read())



