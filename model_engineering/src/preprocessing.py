from sklearn.pipeline import Pipeline
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
import joblib
import os

pipeline_path = './trained_model/preprocessing_pipeline.pkl'


def preprocess_dataframe(df: pd.DataFrame, pipeline) -> pd.DataFrame:
    df = df[sorted(df.columns)]

    transformed_df = pd.DataFrame(pipeline.transform(df), columns=df.columns)

    return transformed_df


def get_transform_pipeline(df: pd.DataFrame = None, save = False) -> Pipeline:
    if os.path.exists(pipeline_path):
        pipeline = joblib.load(pipeline_path)
    elif df is not None:
        df = df[sorted(df.columns)]

        pipeline_steps = [
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', MinMaxScaler())
        ]

        pipeline = Pipeline(steps=pipeline_steps)

        pipeline.fit(df)

        if save:
            joblib.dump(pipeline, pipeline_path)
    else:
        raise Exception("Not be able to get the preprocessing pipeline, fit the pipeline")

    return pipeline
