"""Профилировка затрат памяти"""

from copy import deepcopy
from memory_profiler import profile


@profile
def function_1():
    """Значительный инкремент"""
    x = list(range(100000))
    y = deepcopy(x)
    del x
    y = None
    return y


function_1()
