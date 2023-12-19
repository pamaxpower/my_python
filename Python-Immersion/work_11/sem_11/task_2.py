'''
Задание №2

Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра

'''

class Archive():
    nums_archive = []
    strs_archive = []
    last_num = None
    last_str = None

    def __init__(self, num, new_str):
        self.num = num
        self.str = new_str

        # проверяем прошлые значения, если они не пустые, то добавляем в список
        # для 1 экземпляра класса этот кусок кода не работает
        if Archive.last_num is not None:
            Archive.nums_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.strs_archive.append(Archive.last_str)  

        # текущие значения num и new_str присваиваются в прошлые значения,
        # чтобы при дальнейшем создании экземпляров они записывались в список
        Archive.last_num = num
        Archive.last_str = new_str


if __name__ == '__main__':
    arc_1 = Archive(5, 'Hello')
    print(arc_1.num, arc_1.str, arc_1.nums_archive, arc_1.strs_archive)
    arc_2 = Archive(3, 'World')
    print(arc_2.num, arc_2.str, arc_2.nums_archive, arc_2.strs_archive)
    arc_3 = Archive(42, 'Universal')
    print(arc_3.num, arc_3.str, arc_3.nums_archive, arc_3.strs_archive)
