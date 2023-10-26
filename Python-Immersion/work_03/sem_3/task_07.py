'''
Задание №7

✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях
'''

text = input('Введите текст: ')
mydict1 = {}
mydict2 = {}
for el in text:
    count = 0
    for el2 in text:
        if el2 == el:
            count += 1

    mydict1[el] = count
    mydict2[el] = text.count(el)


print(mydict1, mydict2, sep='\n')

my_dict3 = {el: text.count(el) for el in text if el.isalpha()}
print(my_dict3)
