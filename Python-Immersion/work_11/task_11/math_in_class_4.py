'''
RIGTH МЕТОДЫ
- срабатывают, если у левого объекта в выражении метод не был найден
Например:
при сложении x + y вначале происходит поиск дандер метода x.__add__, 
если он не был найден, то вызывается метод y.__radd__

Умножение текста на "продвинутый текст" методом __rmul__

'''
class StrPro(str):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance
    
    # создаем метод, где self - справа от знака *, other - слева
    def __rmul__(self, other: str):
        # делим строку, стоящую слева от знака на отдельные слова
        words = other.split()
        # собираем строку с добавлением self-строки
        result = self.join(words)
        return StrPro(result)


text = 'Каждый охотник желает знать где сидит фазан'
s = StrPro(' (=^.^=) ')
print(f'{text = }\n{s = }')
print(text * s)
# print(s * text) # TypeError: 'str' object cannot be interpreted as an integer