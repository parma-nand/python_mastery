import numpy as np
from sklearn.preprocessing import StandardScaler

class Preprocessor:
    """
    SRP: Only responsibility is to scale/transform features.
    """

    def __init__(self):
        self.scaler = StandardScaler()

    def fit_transform(self, X_train: np.ndarray) -> np.ndarray:
        return self.scaler.fit_transform(X_train)

    def transform(self, X_test: np.ndarray) -> np.ndarray:
        return self.scaler.transform(X_test)