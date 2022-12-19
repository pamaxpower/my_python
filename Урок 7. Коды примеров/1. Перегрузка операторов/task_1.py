"""__init__"""


class MyClass:
    def __init__(self, param):
        self.param = param


mc = MyClass("text")
print(mc.param)  # -> text
