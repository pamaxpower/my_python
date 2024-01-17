'''
Исключение - любое состояние или непредвиденное поведение, 
возникающее при выполнении программы
'''

num = int(input('Введите целое число: '))
# введем 'сорок два' и получим ошибку:

# Traceback (most recent call last):
#   File "c:\Users\Lenovo\MyPython\Python-Immersion\work_13\task_13\except.py", line 6, in <module>     - где произошла ошибка (файл и номер строки)
#     num = int(input('Введите целое число: '))                         - строка кода с ошибкой
# ValueError: invalid literal for int() with base 10: 'сорок два'       - суть ошибки

