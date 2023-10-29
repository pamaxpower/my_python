'''
Позиционные и ключевые параметры

def func(только позицонные, /, позиционные или ключевые, *, только ключевые):
    pass
    
Символы / и * разделяют позиционные и ключевые параметры

Ключевые параметры принимают значения только при явном 
указании ключа, т.е. название_параметра=значение
'''

def standard_arg(arg):
    """Пример обычной функции."""
    print(arg)

standard_arg(42)
standard_arg(arg=42)


def pos_only_arg(arg, /):
    """Пример только позиционной функции."""
    print(arg)

pos_only_arg(42)
# pos_only_arg(arg=42)    # TypeError


def kwd_only_arg(*, arg):
    """Пример только ключевой функции."""
    print(arg)

# kwd_only_arg(42)    # TypeError
kwd_only_arg(arg=42)


def combined_example(pos_only, /, standard, *, kwd_only):
    """Пример функции со всеми вариантами параметров."""
    print(pos_only, standard, kwd_only)

# combined_example(1, 2, 3) # TypeError
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # TypeError


