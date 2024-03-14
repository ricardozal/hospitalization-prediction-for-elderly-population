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


def get_new_columns_names(
    df_columns: pd.core.indexes.range.RangeIndex
) -> pd.DataFrame:
    """
    Get new columns names from dataframe.

    :param df: Dataset dataframe.
    :return: _description_
    """
    # New columns names dataframe
    columns_names_df = pd.DataFrame({
        "old_column_name": df_columns})
    columns_names_df["new_column_name"] = \
        columns_names_df["old_column_name"].apply(
            lambda old_column_name: re.sub(
                r"(r|s|h|hh)\d", "", old_column_name))
    return columns_names_df


def fill_ds(
    ds: pd.Series
):
    """
    Fill concatenated pandas series nan values.

    :param ds: Pandas series.
    :return: Filled pandas series.
    """
    unique_values = ds.loc[pd.notna].unique()
    fillna_values = np.resize(unique_values, ds.isna().sum())
    return ds.fillna(pd.Series(fillna_values))


def concat_waves(
        df: pd.DataFrame
) -> pd.DataFrame:
    """
    Constructs a unified dataframe from dataset dataframe.

    :param df: Not unified dataset dataframe.
    :return: Unified dataset dataframe.
    """
    # New columns names dataframe
    columns_names = get_new_columns_names(df.columns)

    concat_dc: dict = {}
    # Iterate over each column in the DataFrame
    grouped_columns_by_names = columns_names.groupby("new_column_name")
    for new_column_name, old_column_name_list in grouped_columns_by_names:
        concat_dc[new_column_name] = pd.concat(
            map(
                lambda column_name: df[column_name].rename(
                    new_column_name),
                old_column_name_list["old_column_name"]
            ), ignore_index=True, axis=0)
        if old_column_name_list.shape[0] == 1:
            concat_dc[new_column_name] = fill_ds(concat_dc[new_column_name])

    return pd.concat(
        map(lambda key: concat_dc[key], concat_dc),
        axis=1
    )
