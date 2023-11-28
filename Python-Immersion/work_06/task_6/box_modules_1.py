"""
Встроенные модули (модули "из коробоки")

1) устанавливаются вместе с интерпретатором
2) для использования модуля достаточно импортировать его в свой код
3) для решения большинства задач в стандартной библиотеке 
имеются свои средства (использовать справку, чтобы найти)
4) некоторые модули стандартной библиотеки могут быть 
не оптимальны для решения задач (слишком старые)
"""

# Модуль sys
# - обеспечивает доступ к некоторым переменным, используемым или
# поддерживаемым интерпретатором, а также к функциям, тесно
# взаимодействующим с интерпретатором

from sys import argv

print('start')
print(argv)
print('stop')

# в hезультате вывода (кроме уже известных start и stop)
# получаем список, в нулевой ячейке которого мы видим имя 
# запускаемого скрипта и переданные значения (в виде str), 
# где в качестве разделителя используется пробел