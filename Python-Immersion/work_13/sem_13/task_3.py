'''
Задание №3

Создайте класс с базовым исключением и дочерние классы исключения:
○ ошибка уровня,
○ ошибка доступа.

'''

class BaseError(Exception):
    pass


class LevelError(BaseError):
    """Ошибка уровня"""
    pass


class AccessError(BaseError):
    """Ошибка доступа"""
    pass


if __name__ == "__main__":
    level = 7

    if not isinstance(level, int):
        raise LevelError('Ошибка уровня')
    elif level < 5:
        raise AccessError('Ваш уровень не соответствует нужному')
    else:
        print('Доступ разрешен')
