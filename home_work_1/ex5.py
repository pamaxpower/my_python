"""Запросите у пользователя значения выручки и издержек фирмы. Определите,
с каким финансовым результатом работает фирма (прибыль — выручка больше
издержек, или убыток — издержки больше выручки). Выведите соответствующее
сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue = int(input('Введите сумму выручки: '))
cost = int(input('Введите сумму расходов: '))
if revenue < cost:
    print('\tУвы, вы работаете в убыток!')
else:
    print('\tВаш бизнесс приносит прибыль!!!')
    cost_effectiveness = round((revenue-cost) / revenue * 100, 1)
    print(f'\tРентабельность составляет {cost_effectiveness}%')
    staff = int(input('Введите число сотрудников: '))
    profit_staff = (revenue-cost) // staff
    print(f'\tПрибыль на одного сотрудника равна: {profit_staff}')
    