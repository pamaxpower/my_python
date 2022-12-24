# Простой метакласс
# Этот метакласс обеспечивает доступ своих классов к методу логгирования on_log


import sys
import logging

LOG = logging.getLogger('basic')
CRIT_HAND = logging.StreamHandler(sys.stderr)
FORMATTER = logging.Formatter("%(levelname)-7s %(asctime)s %(message)s")
CRIT_HAND.setFormatter(FORMATTER)
LOG.addHandler(CRIT_HAND)
LOG.setLevel(logging.DEBUG)


class Logging(type):
    # Метод on_log
    def on_log(cls):
        LOG.info(f'Данный метакласс фиксирует работу с классом {cls}')

    # Вызываем метакласс
    # Должен создать и вернуть экземпляр нового класса
    def __call__(self, *args, **kwargs):
        # создаём новый класс как обычно
        obj = type.__call__(self, *args)
        print(obj)  # -< <__main__.MyClass object at 0x000001AF90007148>

        # определяем новый метод on_log для каждого из этих классов
        setattr(obj, "on_log", self.on_log)
        print(obj)
        # возвращаем класс
        return obj


# Проверяем метакласс
class MyClass(metaclass=Logging):
    def fixing(self):
        self.on_log()

# Создаём экземпляр метакласса. Он должен автоматически содержать метод on_log
# хотя он не объявлен в классе вручную
# иными словами, он объявлен за нас метаклассом

MC = MyClass()
MC.fixing()

"""
Метаклассы дают нам возможность писать код, который изменяет 
не только данные, 
но и другой код, то есть изменяет класс во время его создания. 
В примере выше наш метакласс автоматически добавляет новый метод 
к новым классам, 
которые мы определяем, чтобы использовать метакласс.
"""
