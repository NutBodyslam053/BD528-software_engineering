import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, RobustScaler
from mlProject.entity.config_entity import DataTransformationConfig
import joblib


class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    def train_test_spliting(self):
        # Data Importing
        df = pd.read_csv(self.config.data_path)

        # Missing Values Handling
        df.dropna(subset=["Diabetic"], inplace=True)
        df.reset_index(drop=True, inplace=True)
        df["Pdiabetes"].fillna("no", inplace=True)
        df["BMI"].fillna(df["BMI"].median(), inplace=True)
        df["Pregancies"].fillna(df["Pregancies"].mode()[0], inplace=True)
        df['RegularMedicine'].replace({"o": "no"}, inplace=True)
        df["BPLevel"] = df['BPLevel'].str.strip().str.lower()
        df["Pdiabetes"].replace({"0": "no"}, inplace=True)
        df["Diabetic"] = df["Diabetic"].str.strip()

        # Label Encoding
        object_columns = df.select_dtypes(include=['object']).columns.tolist()
        for c in object_columns:
            encoder = OrdinalEncoder(categories=[df[c].unique().tolist()])
            df[c] = encoder.fit_transform(df[[c]])

        df = df.astype('int')

        # Data Scaling
        scaler = RobustScaler()
        X_scaled = scaler.fit_transform(df.iloc[:, :-1])
        
        # Save fitted scaler
        joblib.dump(scaler, os.path.join(self.config.root_dir, self.config.scaler_name))

        X = pd.DataFrame(
            data=X_scaled,
            columns=['Age', 'Gender', 'Family_Diabetes', 'highBP', 'PhysicallyActive', 'BMI',
                     'Smoking', 'Alcohol', 'Sleep', 'SoundSleep', 'RegularMedicine',
                     'JunkFood', 'Stress', 'BPLevel', 'Pregancies', 'Pdiabetes',
                     'UriationFreq']
        )
        Y = df[["Diabetic"]]

        data_transformed = pd.concat([X, Y], axis=1)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data_transformed)

        train.to_csv(os.path.join(
            self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(
            self.config.root_dir, "test.csv"), index=False)

        logger.info("Splited data: Train set = {}, Test set = {}".format(
            train.shape, test.shape))