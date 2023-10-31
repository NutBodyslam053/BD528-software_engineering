import pandas as pd
import numpy as np
import joblib
from pathlib import Path


class PredictionPipeline:
    def __init__(self) -> None:
        self.scaler = joblib.load(Path('artifacts/03_data_transformation/scaler.joblib'))
        self.model = joblib.load(Path('artifacts/04_model_trainer/model.joblib'))
        
    def predict(self, data):
        scaled_data = self.scaler.transform(data)
        prediction = self.model.predict(scaled_data)

        return prediction