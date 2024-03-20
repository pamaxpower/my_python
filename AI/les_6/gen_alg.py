'''
Генетический алгоритм


найти такое x, при котором функция имеет 
максимум на определенном диапазоне от 0 до 255
'''


from random import randint


CHROMOSOME = 8
len_population = 8      # кол-во решений в одном прогоне

# целевая функция
def func(x):
    # return x**3 + 2*x**2 - 10*x + 87
    return x*x - 50*x + 87


def to_binary(number):
    res = []
    count = 0
    while number > 0:
        res.append(number % 2)
        number = number//2
        count += 1
    for _ in range(CHROMOSOME-count):
        res.append(0)
    return res


def to_number(binary):
    res = 0
    for i in range(CHROMOSOME):
        if binary[i]:
            res += 2**i
    return res


def start_population(len_pop):
    pop = []
    for _ in range(len_pop):
        osob = []
        for _ in range(CHROMOSOME):
            osob.append(randint(0, 1))
        pop.append(osob)
    return pop


def find_max(pop):
    """
    Находим максимальное значение функции
    :param pop: стартовая популяция
    :return: максимальное значение функции
    """
    maks = 0
    for i in pop:
        current = func(to_number(i))
        if current > maks:
            maks = current
    return maks


def find_champ(pop):
    """
    Находим чемпионов
    :param pop: стартовая популяция
    :return: 4 максимальных значения из словаря {[максимум]: чемпион}
    """
    fit = {}
    for item in pop:
        fit[func(to_number(item))] = item
    return dict(sorted(fit.items(), reverse=True)[:4])


def new_population(champs):
    """
    Скрещиваем чемпионов и получаем повую популяцию
    :param champs: список чемпионов
    :return: новая популяция
    """
    new_pop = champs[:]
    n = 2           # чемпионов 4, пар - 2
    for i in (0, n):
        child1 = champs[i][:4] + champs[i+1][4:]
        child2 = champs[i][4:] + champs[i+1][:4]
        new_pop.extend([child1, child2])
    for _ in range(4):
        osob = []
        for _ in range(CHROMOSOME):
            osob.append(randint(0, 1))
        new_pop.append(osob)
    return new_pop


st_pop = start_population(len_population)
print(*st_pop, sep='\n')
champ = list(find_champ(st_pop).values())

print(find_max(st_pop))
print(find_max(new_population(champ)))
