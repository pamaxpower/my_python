"""__getitem__"""


class Class1:
    def __init__(self, param):
        self.param = param

    def __str__(self):
       return str(self.param)


class Class2:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(Class1(el))

    def __getitem__(self, index):
        return self.my_list[index]


my_obj = Class2(10, True, "text")
#print(my_obj.my_list[0])
print(my_obj[1])
print(my_obj.my_list[2])

"""
10
True
text
"""
