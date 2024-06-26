'''
Нейронная сеть с обучением, используя функцию потерь

'''


import numpy as np
from NN_3 import mse_loss

def sigmoid(x):
    # Sigmoid activation function: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))


def deriv_sigmoid(x):
    # Derivative of sigmoid: f'(x) = f(x) * (1 - f(x))
    fx = sigmoid(x)
    return fx * (1 - fx)


class OurNeuralNetwork:
    '''
    Нейронная сеть:
      - 2 входных нейрона
      - 2 нейрона в скрытом слое (h1, h2)
      - 1 выходной нейрон (o1)
    '''

    def __init__(self):
        # Weights
        self.w1 = np.random.uniform(-1,1)
        self.w2 = np.random.uniform(-1,1)
        self.w3 = np.random.uniform(-1,1)
        self.w4 = np.random.uniform(-1,1)
        self.w5 = np.random.uniform(-1,1)
        self.w6 = np.random.uniform(-1,1)
        print(self.w1)

        # Biases
        self.b1 = np.random.uniform(-1,1)
        self.b2 = np.random.uniform(-1,1)
        self.b3 = np.random.uniform(-1,1)

    def feedforward(self, x):
        # x is a numpy array with 2 elements.
        h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1

    def train(self, data, all_y_trues):
        '''
        - data - массив numpy (n x 2) numpy, n = к-во наблюдений в наборе.
        - all_y_trues - массив numpy с n элементами.
        Элементы all_y_trues соответствуют наблюдениям в data.
        '''
        learn_rate = 0.1
        epochs = 3000  # сколько раз нужно пройти по всему датасету
        print('Начинаем обучение')
        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                # --- Прямой проход (feedforwards)
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = sigmoid(sum_h1)

                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_h2)

                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_o1)
                y_pred = o1

                # --- Считаем частные производные.
                # --- Имена: p_L_p_w1 = "частная производная L по w1"
                p_L_p_ypred = -2 * (y_true - y_pred)

                # Neuron o1
                p_ypred_p_w5 = h1 * deriv_sigmoid(sum_o1)
                p_ypred_p_w6 = h2 * deriv_sigmoid(sum_o1)
                p_ypred_p_b3 = deriv_sigmoid(sum_o1)

                p_ypred_p_h1 = self.w5 * deriv_sigmoid(sum_o1)
                p_ypred_p_h2 = self.w6 * deriv_sigmoid(sum_o1)

                # Neuron h1
                p_h1_p_w1 = x[0] * deriv_sigmoid(sum_h1)
                p_h1_p_w2 = x[1] * deriv_sigmoid(sum_h1)
                p_h1_p_b1 = deriv_sigmoid(sum_h1)

                # Neuron h2
                p_h2_p_w3 = x[0] * deriv_sigmoid(sum_h2)
                p_h2_p_w4 = x[1] * deriv_sigmoid(sum_h2)
                p_h2_p_b2 = deriv_sigmoid(sum_h2)

                # --- Обновляем веса и пороги
                # Neuron h1

                self.w1 -= learn_rate * p_L_p_ypred * p_ypred_p_h1 * p_h1_p_w1
                # p_L_p_ypred = -2 * (y_true - y_pred)
                # y_true -> распаковка из массива all_y_trues
                # y_pred -> конечный выход из нейрона o1
                # p_ypred_p_h1 = self.w5 * deriv_sigmoid(sum_o1) - вес w5 * производная от суммы весов в o1
                # p_h1_p_w1 = x[0] * deriv_sigmoid(sum_h1) - значение входного нейрона x0 * производная от суммы весов в нейроне o1
                
                self.w2 -= learn_rate * p_L_p_ypred * p_ypred_p_h1 * p_h1_p_w2
                self.b1 -= learn_rate * p_L_p_ypred * p_ypred_p_h1 * p_h1_p_b1

                # Neuron h2
                self.w3 -= learn_rate * p_L_p_ypred * p_ypred_p_h2 * p_h2_p_w3
                self.w4 -= learn_rate * p_L_p_ypred * p_ypred_p_h2 * p_h2_p_w4
                self.b2 -= learn_rate * p_L_p_ypred * p_ypred_p_h2 * p_h2_p_b2

                # Neuron o1
                self.w5 -= learn_rate * p_L_p_ypred * p_ypred_p_w5
                self.w6 -= learn_rate * p_L_p_ypred * p_ypred_p_w6
                self.b3 -= learn_rate * p_L_p_ypred * p_ypred_p_b3

            # --- Считаем полные потери в конце каждой эпохи
            if epoch % 100 == 0:
                y_preds = np.apply_along_axis(self.feedforward, 1, data)
                loss = mse_loss(all_y_trues, y_preds)
                print("Epoch %d loss: %.3f" % (epoch, loss))
        print('Заканчиваем обучение')


    def predict(self, x):
        return self.feedforward(x)

if __name__ == '__main__':
    # Определим набор данных
    dataset = np.array([
        [-2, -1],  # Алиса
        [25, 6],   # Боб
        [17, 4],   # Чарли
        [-15, -6], # Диана
        ])
    
    answer = np.array([
        1, # Алиса
        0, # Боб
        0, # Чарли
        1, # Диана
        ])

    network = OurNeuralNetwork()
    network.train(dataset, answer)
