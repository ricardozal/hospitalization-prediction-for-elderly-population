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


def get_datasets(
        chunksize: int = 10000
) -> pd.DataFrame:
    """
    Downloads and loads SAS dataset from GDrive.

    :param chunksize: Dataset chunk size (avoids memory overload).
    :return: Raw dataframe with information of elderly people interviews.
    """
    # Download H_MHAS_c2.sas7bdat
    if not os.path.exists(config.DATASET_MHAS_C2):
        gdown.download(
            config.DATASET_MHAS_URL, config.DATASET_MHAS_C2, quiet=False
        )

    # read the dataset H_MHAS_c2 from the file (470 MB)
    file_path = os.path.join(config.DATASET_ROOT_PATH, config.DATASET_MHAS_C2)

    return pd.concat([
        df for df in pd.read_sas(file_path, chunksize=chunksize)
    ])


def get_datatrain(
        chunksize: int = 10000
) -> pd.DataFrame:
    """
    Gets preliminary unified spouse dataset.

    :param chunksize: Dataset chunk size (avoids memory overload).
    :return: Raw unified spouse dataframe.
    """    
    # Download application_train_aai.csv
    if not os.path.exists(config.DATASET_TRAIN):
        gdown.download(config.DATASET_TRAIN_URL, config.DATASET_TRAIN, quiet=False)
        
    return pd.concat([
        df for df in pd.read_csv(config.DATASET_TRAIN, chunksize=chunksize)
    ])


def remove_unnecessary_columns(
        df: pd.DataFrame,
        subsections_to_remove: List
) -> pd.DataFrame:
    """
    Removes unnecessary columns.

    :param df: Working dataframe.
    :param subsections_to_remove: List of subsections to remove.
    :return: Dataframe without the given subsections.
    """
    features_to_remove = []
    for section in sections:
        for subsection, features in section.items():
            if subsection in subsections_to_remove:
                features_to_remove += features

    df.drop(columns=features_to_remove, inplace=True)

    return df


def extract_column_names(df):
    """Extract new column names by removing specific prefixes."""
    return set([re.sub(r'^(r|s|h|hh)\d', '', x) for x in df.columns])


def split_df_by_columns(df):
    """Split each column into a separate DataFrame."""
    return {column: df[[column]] for column in df}


def group_dfs_by_new_names(df, column_names_new):
    """Group DataFrames by new column names based on patterns."""
    dfs_grouped = {column_name: [] for column_name in column_names_new}
    column_dfs = split_df_by_columns(df)

    for column_name, column_df in column_dfs.items():
        for col_new in column_names_new:
            pattern = re.compile(r'\d' + col_new + '$')
            if bool(pattern.search(column_name)):
                column_df = column_df.rename(columns={column_df.columns[0]: col_new})
                dfs_grouped[col_new].append(column_df)
            elif column_name == col_new:
                dfs_grouped[col_new].append(column_df)

    return dfs_grouped


def concatenate_grouped_dfs(dfs_grouped):
    """Concatenate DataFrames within each group."""
    return {column_name: pd.concat(df_list, ignore_index=True, axis=0) if df_list else pd.DataFrame()
            for column_name, df_list in dfs_grouped.items()}


def concat_waves(df):
    """Main function to orchestrate the refactoring process."""
    column_names_new = extract_column_names(df)
    dfs_grouped = group_dfs_by_new_names(df, column_names_new)
    concat_dfs = concatenate_grouped_dfs(dfs_grouped)
    final_df = pd.concat(concat_dfs.values(), axis=1)
    return final_df
