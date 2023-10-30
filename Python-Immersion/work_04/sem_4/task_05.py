'''
Задание №5

✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии. 
'''

name = ['Bob', 'Alex', 'Tom']
rate = [120, 150, 100]
bonus = ['5.0%', '3.4%', '7.8%']

def find_tax(lst1: str, lst2: int, lst3: str) -> dict:
    "Функция для подсчета зарплаты"
    res = {}

    # if len(lst1) != len(lst2) != len(lst3):
    #     print('Вы ввели списки разной длины')
    # else:

    for i in range(len(lst1)):
        res[lst1[i]] = lst2[i] * float(lst3[i][:-1])
    return res

    # return {el1: el2 * float(el3.rstrip('%')) for el1, el2, el3 in zip(lst1, lst2, lst3)}

print(find_tax(name, rate, bonus))


