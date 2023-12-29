from math import factorial


class Factorial:

    def __init__(self, count):
        self.history = []
        self.count = count

    def __call__(self, n):
        res = factorial(n)
        self.history.append({n: res})
        self.history = self.history[-self.count:]
        return res

    def get_history(self):
        return self.history


if __name__ == '__main__':
    f = Factorial(3)
    for i in range(1, 11):
        print(f'{i}! = {f(i)}')

    print(f.get_history())