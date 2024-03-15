from typing import List, Tuple, Dict
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler

def preprocess_dataframe(df : pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.astype(str)

    # Applying SimpleImputer
    median_imputer = SimpleImputer(strategy='median')
    median_imputer.fit(df)

    # Transform the data
    df = pd.DataFrame(median_imputer.transform(df), columns=df.columns)

    scaler = MinMaxScaler()
    scaler.fit(df)

    df_scaled = scaler.transform(df)
    working_train_df = pd.DataFrame(df_scaled, columns=df.columns)

    train = working_train_df

    return train
