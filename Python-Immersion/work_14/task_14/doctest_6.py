'''Проверка

Что должна делать программа, чтобы пройти следующие тесты:
'''

def say(text, count=2, separator=' '):
    """
    >>> say('Hello')
    Hello Hello
    >>> say('Hi', 5)
    Hi Hi Hi Hi Hi
    >>> say('cat', 3, '(=^.^=)')
    cat(=^.^=)cat(=^.^=)cat
    """
    result = ''
    i = 0
    while i < count:
        result += text + separator
        i += 1

    print(result)

# - функция say, принимает 1 обязательный параметр (text -> str)
# и два необязательных (число повторений и символ)
# - принимая один аргумент - функция возвращает слова два раза через пробел
# - принимая два аргумента - функция вовзращает слово, количество раз через пробел
# - принимая три аргумента - функция возвращает слово, количество раз через заданный символ
    
say('Hello')
say('Hi', 5)
say('cat', 3, '(=^.^=)')