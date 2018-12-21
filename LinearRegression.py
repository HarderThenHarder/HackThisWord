"""
@author: P_k_y
"""
import numpy as np
from DataBase import DataBase


class LinearRegression:

    def __init__(self):
        self.theta = np.array([])
        self.coefficients = np.array([])
        self.intercept = 0

    def fit(self, X_train, y_train):
        X_b = np.hstack([np.ones((X_train.shape[0], 1)), X_train])
        self.theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
        self.coefficients = self.theta[1:]
        self.intercept = self.theta[0]


if __name__ == '__main__':
    data_base = DataBase([0], [0])
    data_base.add_data([1, 1])
    data_base.add_data([2, 1])

    lr = LinearRegression()
    lr.fit(data_base.get_X_train(), data_base.get_y_train())
    print(lr.intercept)
    print(lr.coefficients)
