'''
Шаблон одиночка, Singleton

- паттерн, который позволяет создать лишь один экземпляр класса
- при второй и последующей попытке создания будет возвращать первый экземпляр

'''

class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name: str):
        self.name = name

a = Singleton('Первый')
print(f'{a.name = }')

b = Singleton('Второй')
print(f'{a is b = }')       # покажет что это один и тот же экземпляр

print(f'{a.name = }\n{b.name = }')      # показывает, что при создании второго и
                                        # последующих экземпляров меняется только название
