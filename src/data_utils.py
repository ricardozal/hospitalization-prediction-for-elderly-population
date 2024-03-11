import os
from typing import List, Tuple

import gdown
import pandas as pd
import numpy as np

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

    list_of_dataframes = [
        df for df in pd.read_sas(file_path, chunksize=chunksize)
    ]

    h_mas_c2 = pd.concat(list_of_dataframes)

    return h_mas_c2


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
        
    list_of_dataframes = [
        df for df in pd.read_csv(config.DATASET_TRAIN, chunksize=chunksize)
    ]

    app_train = pd.concat(list_of_dataframes)
    
    return app_train


def outline_dataframe(
        app_all: pd.DataFrame,
        elimins: List[list]
) -> pd.DataFrame:
    """
    Constructs dataframe with the most relevant dataset features.

    :param app_all: Raw dataset dataframe with all features.
    :param elimins: List of irrelevant features.
    :return: Dataframe with relevant features.
    """
    sections = [section_A, section_B, section_C, section_D, section_E, section_F,
                section_G, section_H, section_I, section_J, section_K, section_L,
                section_M, section_O, section_Q]
    
    working_app_all = app_all.copy()

    # Define old and new column names
    old_dfnames = ['hh1ctot1m', 'hh1cftot1m', 'hh2cftot1m', 'hh2ctot1m', 'hh3cftot1m',
                   'hh3ctot1m', 'hh4cftot1m', 'hh4ctot1m', 'hh5cftot1m', 'hh5ctot1m']
    # 'h1ctot1m', 'h1cftot1m', 'h2cftot1m', 'h2ctot1m', 'h3cftot1m'
    # 'h3ctot1m', 'h4cftot1m', 'h4ctot1m', 'h5cftot1m', 'h5ctot1m'
    new_dfnames = [column_name.replace("hh", "h") for column_name in old_dfnames]

    # Rename columns
    working_app_all.rename(columns=dict(zip(old_dfnames, new_dfnames)), inplace=True)

    waves_columns = filter_dataset(sections, elimins)

    waves = []

    for wave_columns in waves_columns:
        wave = pd.DataFrame({
            column: working_app_all[column]
            if column in working_app_all.columns else np.nan
            for column in wave_columns
        })
        wave.rename(columns={
            column: column[0] + 'X' + column[2:]
            for column in wave.columns if column[1].isdigit()
        }, inplace=True)
        waves.append(wave)
        
    app_all_data = pd.concat(waves)

    return app_all_data


def filter_dataset(
        sections: List[dict],
        elimins: List[list]
) -> Tuple[List[str]]:
    """
    Splits dataframe columns into five different interview columns.

    :param sections: List of feature sections.
    :param elimns: List of features to be eliminated.
    :return: Tuple object of features list divided in waves (interviews cycle).
    """
    total_sections = []

    # Iterate over each dictionary and its values
    for section, elimin in zip(sections, elimins):
        for key, values_list in section.items():
            if key not in elimin:
                # Extend the total_sections list with the values
                # from the current list
                total_sections.extend(values_list)

    unique_values_array = np.unique([
        section[0] + "X" + section[2:] if section[1].isdigit() else section
        for section in total_sections
    ])

    # Five different lists were created to store the five interviews
    # cycle information.
    return (
        [s.replace('X', str(i)) for s in unique_values_array]
        for i in range(1, 6)
    )


def unify_spousandref(
        app_train: pd.DataFrame
)-> pd.DataFrame:
    """
    Constructs unified dataframe.

    :param app_train: Raw not unified dataset dataframe.
    :return: Unified dataset dataframe.
    """
    # Extract all column names from the dataframe into a names_data_app list.
    names_data_app = app_train.columns.tolist()

    # Divide the list into three different lists: names_starting_s, names_starting_r, names_starting_other
    names_starting_s = [name for name in names_data_app if name.startswith('s')]
    names_starting_r = [name for name in names_data_app if name.startswith('r')]
    names_starting_other = [name for name in names_data_app if not name.startswith('s') and not name.startswith('r')]

    # Make 2 new DataFrames
    app_train_r = app_train[names_starting_other + names_starting_r]
    app_train_s = app_train[names_starting_other + names_starting_s]

    # Check if the column name starts with 's' before replacing the first letter
    app_train_s.columns = [name.replace('s', 'r', 1) if name.startswith('s') else name for name in app_train_s.columns]

    vars_in_s = ['rXbmonth', 'rXbyear', 'rXdmonth', 'rXdyear', 'rXedisced', 'rXeducl',
                 'rXedyrs', 'rXevbrn', 'rXfeduc_m', 'rXgender', 'rXindlang', 'rXliterate',
                 'rXmeduc_m', 'rXnumerate']
    # New variable names
    vars_to_repl = [column_name.replace("rX", "ra") for column_name in vars_in_s]
    
    # Create a mapping between the old variable names and the new ones
    variable_mapping = {old_var: new_var for old_var, new_var in zip(vars_in_s, vars_to_repl)}
    
    # Replace the variable names in vars_in_s with the new ones
    app_train_s.columns = [variable_mapping.get(var, var) for var in app_train_s.columns]
    
    # Concatenate the 2 new DataFrames into one DataFrame app_train_sr
    app_train_sr = pd.concat([app_train_r, app_train_s], axis=0)
    
    # Identify the variable named 'rXhosp1y' and rename it to 'Target'
    app_train_sr.rename(columns={'rXhosp1y': 'TARGET'}, inplace=True)

    # Delete all rows where the variable 'Target' is equal to null
    app_train_sr.dropna(subset=['TARGET'], inplace=True)

    # Rename the DataFrame as app_train
    app_train = app_train_sr.copy()

    # reset the index after dropping the rows with null 'TARGET'
    app_train.reset_index(drop=True, inplace=True)
       
    return app_train
