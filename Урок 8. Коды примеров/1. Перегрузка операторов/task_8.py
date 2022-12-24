"""__call__"""
def my_func():
    pass

my_func()

class MyClass:
    def __init__(self, param):
        self.param = param

    def __call__(self, newparam):
        self.param = newparam
        return self.param

    def __str__(self):
        return f"Значение параметра - {self.param};"


obj = MyClass("привет")
print(obj("новый привет"))