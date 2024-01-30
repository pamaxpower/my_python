'''
Отдельно добавим параметры a, b, c,
но теперь они станут не позиционными, а не обязательными опциональными параметрами
вещественного типа и задали значения по умолчанию

'''


import argparse

def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    
    parser.add_argument('-a', metavar='a', type=float,
                        help='enter a for ax^2+bx+c=0', default=1)

    parser.add_argument('-b', metavar='b', type=float,
                        help='enter b for ax^2+bx+c=0', default=0)
    
    parser.add_argument('-c', metavar='c', type=float,
                        help='enter c for ax^2+bx+c=0', default=0)
    
    args = parser.parse_args()
    
    print(quadratic_equations(args.a, args.b, args.c))


# Для запуска кода через консоль

# python argparse_6.py -a 2 -b -12 -c 10