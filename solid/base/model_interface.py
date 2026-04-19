from abc import ABC, abstractmethod
import numpy as np

class BaseModel(ABC):
    """
    ISP: Only methods relevant to all classifiers.
    DIP: High-level modules depend on this abstraction, not concrete models.
    """

    @abstractmethod
    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> None:
        pass

    @abstractmethod
    def predict(self, X: np.ndarray) -> np.ndarray:
        pass