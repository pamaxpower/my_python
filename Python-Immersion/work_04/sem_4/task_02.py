'''
Задание №2

✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
'''

text = 'mngakjh asdgjh aren newbq mweow euof nbdgkj awej rqkj fhlyt'

def uni_list(txt: str):
    res = []
    for i in range(len(txt)):
        res.append(ord(txt[i]))
    return sorted(set(res), reverse=True)


print(uni_list(text))


def uniq_simbol(txt: str):
    return sorted(list(set([ord(el) for el in txt])), reverse=True)

print(uniq_simbol(text))
