"""
@author: P_k_y
"""
import numpy as np


class DataBase:

    def __init__(self, X_train, y_train):
        self._X_train = np.array(X_train)
        self._y_train = np.array(y_train)

    def add_data(self, data):
        x_train = data[:-1]
        y_train = data[-1]
        self._X_train = np.vstack([self._X_train, np.array(x_train)])
        y_train_list = list(self._y_train)
        y_train_list.append(y_train)
        self._y_train = np.array(y_train_list)

    def get_X_train(self):
        return self._X_train[1:][:]

    def get_y_train(self):
        return self._y_train[1:]


if __name__ == "__main__":
    data_base = DataBase([0], [0])
    data_base.add_data([1, 1])
    data_base.add_data([2, 2])
    data_base.add_data([3, 3])

    print(data_base.get_X_train())
