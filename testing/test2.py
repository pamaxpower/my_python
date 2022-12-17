'''Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и подготовить аналитику, что вы сделали
и чего удалось добиться'''

from memory_profiler import profile

# first competition
rating_list = [7, 5, 3, 3, 2]
rating_lst = [7, 5, 3, 3, 2]
rating = 6


@profile()
def update_rating(r_list, number):
    for i in range(len(r_list)):
        if r_list[i] == number:
            r_list.insert(i + 1, number)
            break
        if r_list[0] < number:
            r_list.insert(0, number)
        elif r_list[-1] > number:
            r_list.append(number)
        elif r_list[i + 1] < number < r_list[i]:
            r_list.insert(i + 1, number)
            break
    return r_list


print(update_rating(rating_list, rating))


@profile()
def update_rating_2(r_list, number):
    r_list.append(number)
    r_list.sort(reverse=True)
    return r_list


print(update_rating_2(rating_lst, rating))

# second competition
number_1, number_2 = 5, -3


@profile()
def my_func_1(x, y):
    '''
    First way
    :param x: real positive number
    :param y: integer negative number
    :return: pow
    '''
    try:
        if int(y) < 0 < float(x):
            print(f'({x})^({y}) = {float(x) ** float(y)}')
        else:
            print('Please enter numbers according to the task')
    except ValueError:
        print('Second number should be integer negative')


my_func_1(number_1, number_2)


@profile()
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
            print(f'({x})^({y}) = {1 / result}')
        else:
            print('Please enter numbers according to the task')
    except ValueError:
        print('Second number should be integer negative')


my_func_2(number_1, number_2)


@profile()
def my_func_3(x, y):
    '''
    Third way
    :param x: real positive number
    :param y: integer negative number
    :return: pow
    '''
    return pow(x, y)


my_func_3(number_1, number_2)