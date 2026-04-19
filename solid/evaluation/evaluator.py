import numpy as np
from sklearn.metrics import accuracy_score, classification_report

class Evaluator:
    """
    SRP: One job — evaluate model predictions.
    """

    def evaluate(self, y_true: np.ndarray, y_pred: np.ndarray) -> None:
        acc = accuracy_score(y_true, y_pred)
        print(f"\nAccuracy: {acc:.4f}")
        print("\nClassification Report:")
        print(classification_report(y_true, y_pred))