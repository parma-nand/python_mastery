from data.data_loader import DataLoader
from preprocessing.preprocessor import Preprocessor
from models.xgboost_model import XGBoostModel
from evaluation.evaluator import Evaluator
from base.model_interface import BaseModel

def run_pipeline(model: BaseModel):
    """
    DIP: This function depends on BaseModel abstraction, not XGBoostModel directly.
    You can pass LightGBMModel or RandomForestModel here tomorrow — nothing changes.
    """

    # Load
    loader = DataLoader()
    X_train, X_test, y_train, y_test = loader.load()

    # Preprocess
    preprocessor = Preprocessor()
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)

    # Train
    model.train(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluate
    evaluator = Evaluator()
    evaluator.evaluate(y_test, y_pred)


if __name__ == "__main__":
    model = XGBoostModel(n_estimators=100, max_depth=4, learning_rate=0.1)
    run_pipeline(model)