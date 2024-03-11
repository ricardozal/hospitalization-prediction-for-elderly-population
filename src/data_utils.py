import os
from typing import List

import gdown
import pandas as pd
import numpy as np
import re

from src import config
from src.section_dict import (
    section_A, # A: DEMOGRAPHICS, IDENTIFIERS, AND WEIGHTS
    section_B, # B: HEALTH
    section_C, # C: HEALTH CARE UTILIZATION AND INSURANCE
    section_D, # D: COGNITION
    section_E, # E: FINANCIAL AND HOUSING WEALTH
    section_F, # F: INCOME
    section_G, # G: FAMILY STRUCTURE
    section_H, # H: EMPLOYMENT HISTORY
    section_I, # I: RETIREMENT
    section_J, # J: PENSION
    section_K, # K: PHYSICAL MEASURES
    section_L, # L: ASSISTANCE AND CAREGIVING
    section_M, # M: STRESS
    section_O, # O: END OF LIFE PLANNING
    section_Q  # Q: PSYCHOSOCIAL
)

sections = [section_A, section_B, section_C, section_D, section_E, section_F,
            section_G, section_H, section_I, section_J, section_K, section_L,
            section_M, section_O, section_Q]

def get_datasets() -> pd.DataFrame:
    """
    Download from GDrive all the needed datasets for the project.

    Returns:
        h_mas_c2 : pd.DataFrame
            Raw file with information from interviews with elderly people. 
            
    """
    # Download H_MHAS_c2.sas7bdat
    if not os.path.exists(config.DATASET_MHAS_C2):
        gdown.download(
            config.DATASET_MHAS_URL, config.DATASET_MHAS_C2, quiet=False
        )

    # read the dataset H_MHAS_c2 from the file (470 MB)
    file_path = './dataset/H_MHAS_c2.sas7bdat'
    h_mas_c2 = pd.read_sas(file_path)

    return h_mas_c2


def get_datatrain() -> pd.DataFrame:
    
    # Download application_train_aai.csv
    if not os.path.exists(config.DATASET_TRAIN):
        gdown.download(config.DATASET_TRAIN_URL, config.DATASET_TRAIN, quiet=False)
        
    app_train = pd.read_csv(config.DATASET_TRAIN)
    
    return app_train


def remove_unnecessary_columns(df: pd.DataFrame, subsections_to_remove: List):
    features_to_remove = []
    for section in sections:
        for subsection, features in section.items():
            if subsection in subsections_to_remove:
                features_to_remove += features

    df = df.drop(columns=features_to_remove)

    return df


def concat_waves(df: pd.DataFrame):
    column_names_new = set([re.sub(r'^(r|s|h|hh)\d', '', x) for x in df.columns])
    print(column_names_new)
    print(f'TAMAÑO = {len(column_names_new)}')
    dfs = {key: list() for key in column_names_new}

    # Dictionary to hold each column as a separate DataFrame
    column_dfs = {}

    # Split each column into a separate DataFrame
    for column in df:
        column_dfs[column] = df[[column]]

    for key, value in column_dfs.items():
        for col_new in column_names_new:
            pattern = re.compile(r'\d' + col_new + '$')
            if bool(pattern.search(key)):
                print(f'from {value.columns[0]} to {col_new}')
                value = value.rename(columns={value.columns[0]: col_new})
                dfs[col_new].append(value)
            elif key == col_new:
                print(f'from {value.columns[0]} to {col_new}')
                dfs[col_new].append(value)


    for key, value in dfs.items():
        print(f'{key} was resized to 1 from {len(value)}')


    # Adjusted step to concatenate DataFrames within each list and reset index
    concat_dfs = {key: pd.concat(df_list, ignore_index=True, axis=0) if df_list else pd.DataFrame() for key, df_list in dfs.items()}

    # Merge all concatenated DataFrames side by side
    final_df = pd.concat(concat_dfs.values(), axis=1)

    for col_new in column_names_new:
        if len(dfs[col_new]) == 1:
            print(f'{col_new} was filled')
            unique_values = final_df.loc[final_df[col_new].notna(), col_new].unique()

            # Calculate the number of NaNs to fill
            nan_count = final_df[col_new].isna().sum()

            sequence_to_fill = np.resize(unique_values, nan_count)

            # Assign this sequence to the NaN positions in each column
            final_df.loc[final_df[col_new].isna(), col_new] = sequence_to_fill

    return final_df
