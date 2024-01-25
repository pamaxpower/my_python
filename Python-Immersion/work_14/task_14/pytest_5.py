import pytest


@pytest.fixture
def get_file(tmp_path):
    # tmp_file - создает путь для временных файлов
    f_name = tmp_path / 'test_file.txt'
    print(f'Создаю файл {f_name}') # принтим в учебных целях
    # создаемп файл и через yield возвращаем указатель на него
    with open(f_name, 'w+', encoding='utf-8') as f:
        yield f
    print(f'Закрываю файл {f_name}') # принтим в учебных целях


@pytest.fixture
def set_num(get_file):
    print(f'Заполняю файл {get_file.name} цифрами') # принтим в учебных целях
    # записываем в файл строку из цифр и возвращаем указатель в начало файла
    for i in range(10):
        get_file.write(f'{i:05}')
    get_file.seek(0)


@pytest.fixture
def set_char(get_file):
    print(f'Заполняю файл {get_file.name} буквами') # принтим в учебных целях
    # заполняем файл буквами (название файлов одинаковое, но директории разные)
    for i in range(65, 91):
        get_file.write(f'{chr(i)}')
    get_file.seek(0)
    return get_file


def test_first_num(get_file, set_num):
    first = get_file.read(5)
    assert first == '00000'


def test_first_char(set_char):
    first = set_char.read(5)
    assert first == 'ABCD'     # специально провалим тест
    # assert first == 'ABCDE'    # для успешного теста


if __name__ == '__main__':
    pytest.main(['-v'])
