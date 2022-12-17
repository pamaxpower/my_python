'''Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и подготовить аналитику, что вы сделали
и чего удалось добиться'''


from timeit import timeit


"""
"""




def my_func_1(x, y):
    '''
    First way
    :param x: real positive number
    :param y: integer negative number
    :return: pow
    '''
    try:
        if int(y) < 0 < float(x):
            return float(x) ** float(y)
        else:
            print('Please enter numbers according to the task')
    except ValueError:
        print('Second number should be integer negative')


def my_func_2(x, y):
    '''
    Second way
    :param x: real positive number
    :param y: integer negative number
    :return: pow
    '''
    try:
        if int(y) < 0 < float(x):
            result = 1
            i = 1
            while i <= abs(int(y)):
                result *= float(x)
                i += 1
            return 1 / result
        else:
            print('Please enter numbers according to the task')
    except ValueError:
        print('Second number should be integer negative')


def my_func_3(x, y):
    '''
    Third way
    :param x: real positive number
    :param y: integer negative number
    :return: pow
    '''
    return pow(x, y)


# first competition
rating_list = [7, 5, 3, 3, 2]
rating_lst = [7, 5, 3, 3, 2]
rating = 8

rating_1 = timeit("update_rating(rating_list, rating)", globals=globals(),
                  number=10000)
rating_2 = timeit("update_rating_2(rating_lst, rating)", globals=globals(),
                  number=10000)
print(f'Rating_1 - {rating_1} seconds')
print(f'Rating_2 - {rating_2} seconds')

# second competition
number_1, number_2 = 5, -3

pow_1 = timeit("my_func_1(number_1, number_2)", globals=globals(),
               number=100000)
pow_2 = timeit("my_func_2(number_1, number_2)", globals=globals(),
               number=100000)
pow_3 = timeit("my_func_3(number_1, number_2)", globals=globals(),
               number=100000)
print(f'Pow_1 - {pow_1} seconds')
print(f'Pow_2 - {pow_2} seconds')
print(f'Pow_3 - {pow_3} seconds')