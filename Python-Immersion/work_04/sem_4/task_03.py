'''
Задание №3

✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
'''


def uni_dict(txt: str) -> dict:
    res = {}
    for el in sorted(txt.split(' ')):
        res[chr(int(el))] = int(el)
    return res
    # return {chr(int(el)) = int(el) for el in sorted(txt.split(' '))}

print(uni_dict(input('Введите числа через пробел: ')))