import os
import pandas as pd
import numpy as np
from src import data_utils
from src.constants import ORIGINAL_TARGET_NAME, EXCLUDED_SUBSECTIONS
from services.common.utils import encode_data
from sklearn.model_selection import train_test_split
import joblib
from zipfile import ZipFile

path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(path, "data")
features_path = os.path.join(path, "top50_features.txt")
x_test_path = os.path.join(path, "x_test.csv")
y_test_path = os.path.join(path, "y_test.csv")
raw_df_path = os.path.join(path, "H_MHAS_c2.dta")
df_zip_path = os.path.join(path, "H_MHAS_c2.zip")
pipeline_path = os.path.join(path, "preprocessing_pipeline.pkl")
pipeline = joblib.load(pipeline_path)

if not os.path.exists(raw_df_path):
    with ZipFile(df_zip_path, 'r') as zip_file:
        zip_file.extractall(path=path)


def test_encoding_through_pipeline():
    with open(features_path, 'r') as file:
        USED_VARIABLES = [line.strip() for line in file]
        X_test = pd.read_csv(x_test_path)[sorted(USED_VARIABLES)]
        y_test = pd.read_csv(y_test_path)

        df = pd.read_stata(raw_df_path)
        df = data_utils.remove_unnecessary_columns(
            df, EXCLUDED_SUBSECTIONS)
        df = data_utils.concat_waves(df)

        # df.rename(columns={ORIGINAL_TARGET_NAME: 'TARGET'}, inplace=True)
        df.dropna(subset=[ORIGINAL_TARGET_NAME], inplace=True)

        X = df[sorted(USED_VARIABLES)]
        y = df[[ORIGINAL_TARGET_NAME]]

        _, X_test_raw, _, _ = train_test_split(
            X, y, test_size=0.2, random_state=42)
        
        X_test_ = encode_data(X_test_raw.to_dict())
        X_test_ = pd.DataFrame(
            np.transpose(list(X_test_.values())),
            columns=X_test_.keys())

        X_test_ = pipeline.transform(X_test_)

        error_x = np.abs(
            X_test_ - X_test.to_numpy())
        error_x = error_x.flatten().mean()

        assert error_x <= 0.001
