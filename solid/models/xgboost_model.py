import numpy as np
import xgboost as xgb
from base.model_interface import BaseModel

class XGBoostModel(BaseModel):
    """
    OCP: Pipeline is open for extension (swap XGBoost with LightGBM)
         without modifying orchestrator.
    LSP: XGBoostModel can replace any BaseModel without breaking the pipeline.
    """

    def __init__(self, n_estimators=100, max_depth=4, learning_rate=0.1):
        self.model = xgb.XGBClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            learning_rate=learning_rate,
            use_label_encoder=False,
            eval_metric="logloss"
        )

    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> None:
        self.model.fit(X_train, y_train)
        print("Model training complete.")

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.predict(X)