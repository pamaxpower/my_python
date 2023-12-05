'''
Множественно декорирование

Функция может быть декорирована одновременно несколькими декораторами

@deco_c
@deco_b
@deco_a
def my_func(data):
    ...
    return wrapper

'''
from typing import Callable

# декоратор A
def deco_a(func: Callable):
    def wrapper_a(*args, **kwargs):
        print('Старт декоратора A')
        print(f'Запускаю {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Завершение декоратора A')
        return res
    
    print('Возвращаем декоратор A')
    return wrapper_a

# декоратор B
def deco_b(func: Callable):
    def wrapper_b(*args, **kwargs):
        print('Старт декоратора B')
        print(f'Запускаю {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Завершение декоратора B')
        return res

    print('Возвращаем декоратор B')
    return wrapper_b

# декоратор С
def deco_c(func: Callable):
    def wrapper_c(*args, **kwargs):
        print('Старт декоратора C')
        print(f'Запускаю {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Завершение декоратора C')
        return res
    
    print('Возвращаем декоратор C')
    return wrapper_c


@deco_c
@deco_b
@deco_a
def main():
    print('Старт основной функции')


if __name__ == '__main__':
    print('>>> Запуск main()')
    main()
    print('>>> Завершение main()')

# Выводы:
# 1) Возврат декораторов выводится первым (до запуска функции main())
# 2) Процесс декорирования начинается снизу вверх (сначала deco_a, потом deco_b, затем deco_c)
# 3) Запускается код декоратора (в порядке следования сверху вниз, как записаны перед main())
# 4) Потом запускается код основной функции
# 5) Функция завершает работу, декортаторы завершают работу в обратном порядке (порядок обратный 3 пункту)



