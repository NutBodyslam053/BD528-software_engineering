import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from src.mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig) -> None:
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        X_train = train_data.drop([self.config.target_column], axis=1)
        X_test = test_data.drop([self.config.target_column], axis=1)
        y_train = train_data[self.config.target_column].ravel()
        y_test = test_data[self.config.target_column].ravel()

        rf = RandomForestClassifier(
            n_estimators=self.config.n_estimators,
            max_depth=self.config.max_depth,
            min_samples_leaf=self.config.min_samples_leaf,
            min_samples_split=self.config.min_samples_split,
            n_jobs=self.config.n_jobs,
            random_state=42
        )
        
        rf.fit(X_train, y_train)

        joblib.dump(rf, os.path.join(
            self.config.root_dir, self.config.model_name))