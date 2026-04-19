from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy as np

class DataLoader:
    """
    SRP: This class has one job — load and split data.
    Nothing else.
    """

    def __init__(self, test_size=0.2, random_state=42):
        self.test_size = test_size
        self.random_state = random_state

    def load(self):
        data = load_breast_cancer()
        X, y = data.data, data.target
        return train_test_split(
            X, y,
            test_size=self.test_size,
            random_state=self.random_state
        )