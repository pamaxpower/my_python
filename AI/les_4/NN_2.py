'''
Собираем нейронную сеть из нейронов

Входной слой: x1, x2
Скрытые слой: h1, h2
Выходной слой: o1

'''

from NN_1 import Neuron
import numpy as np

# ... вставьте сюда код из предыдущего раздела


class OurNeuralNetwork:
    '''
    Нейронная сеть с:
      - 2 входами
      - скрытым слоем с 2 нейронами (h1, h2)
      - выходным слоем с 1 нейроном (o1)
    Все нейроны имеют одинаковые веса и пороги:
      - w = [0, 1]
      - b = 0
    '''

    def __init__(self):
        weights = np.array([0, 1])
        bias = 0
        # Используем класс Neuron из предыдущего раздела
        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)
        # Входы для o1 - это выходы h1 и h2
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))
        return out_o1


network = OurNeuralNetwork()
x = np.array([2, 3])
print(network.feedforward(x))  # 0.7216325609518421
