import os
from typing import List, Tuple
from sas7bdat import SAS7BDAT
from collections import OrderedDict

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

    # Download H_MHAS_EOL_b.sas7bdat
    if not os.path.exists(config.DATASET_MHAS_EOL):
        gdown.download(config.DATASET_MHAS_EOL_URL, config.DATASET_MHAS_EOL, quiet=False)

    # Download H_MEX_COG_A2_2016.dta
    if not os.path.exists(config.DATASET_MEX_COG):
        gdown.download(config.DATASET_MEX_COG_URL, config.DATASET_MEX_COG, quiet=False)

    # read the dataset H_MHAS_c2 from the file (470 MB)
    with SAS7BDAT('./dataset/H_MHAS_c2.sas7bdat') as file:
        h_mas_c2 = file.to_data_frame()

    return h_mas_c2


def get_datatrain() -> pd.DataFrame:
    
    # Download application_train_aai.csv
    if not os.path.exists(config.DATASET_TRAIN):
        gdown.download(config.DATASET_TRAIN_URL, config.DATASET_TRAIN, quiet=False)
        
    app_train = pd.read_csv(config.DATASET_TRAIN)
    
    return app_train

def outline_dataframe(app_all: pd.DataFrame, elimins: List[list]) -> pd.DataFrame:
    sections = [section_A, section_B, section_C, section_D, section_E, section_F,
                section_G, section_H, section_I, section_J, section_K, section_L,
                section_M, section_O, section_Q]
    
    working_app_all = app_all.copy()

    # Define old and new column names
    old_dfnames = ['hh1ctot1m', 'hh1cftot1m', 'hh2cftot1m', 'hh2ctot1m', 'hh3cftot1m', 'hh3ctot1m', 'hh4cftot1m', 'hh4ctot1m', 'hh5cftot1m', 'hh5ctot1m']
    new_dfnames = ['h1ctot1m', 'h1cftot1m', 'h2cftot1m', 'h2ctot1m', 'h3cftot1m', 'h3ctot1m', 'h4cftot1m', 'h4ctot1m', 'h5cftot1m', 'h5ctot1m']
    # Rename columns
    working_app_all.rename(columns=dict(zip(old_dfnames, new_dfnames)), inplace=True)

    waves_col = filter_dataset(sections, elimins)

    waves = []

    for i in range(5):  
        data = {col: working_app_all[col] if col in working_app_all.columns else np.nan for col in waves_col[i]}
        wave = pd.DataFrame(data)
        wave.columns = [item[0] + 'X' + item[2:] if item[1].isdigit() else item for item in wave.columns.tolist()]
        waves.append(wave)
        
    app_all_data = pd.concat(waves)

    return app_all_data

def filter_dataset(sections: List[dict], elimins: List[list]) -> Tuple[List[str]]:
    """
    Splits the entire column list of the DataFrame into five different interview columns.

    Returns:
        waves : List[list]
                  
    """
    
    Total_sections = []

    # Iterate over each dictionary and its values
    for section, elimin in zip(sections, elimins):
        filtered_section = {k: v for k, v in section.items() if k not in elimin}
        # Extend the Total_sections list with the values from the current list
        for values_list in filtered_section.values():
            Total_sections.extend(values_list)

    new_list = [item[0] + 'X' + item[2:] if item[1].isdigit() else item for item in Total_sections]

    unique_values_array = np.unique(new_list)
    # No need to convert to list
    # Five different lists were created to store the information from the five interviews.
    waves = [[s.replace('X', str(i)) for s in unique_values_array] for i in range(1, 6)]

    return tuple(waves)

def unify_spousandref(app_train: pd.DataFrame)-> pd.DataFrame:
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

    vars_in_s = ['rXbmonth', 'rXbyear', 'rXdmonth', 'rXdyear', 'rXedisced', 'rXeducl', 'rXedyrs', 'rXevbrn', 'rXfeduc_m', 'rXgender', 'rXindlang', 'rXliterate', 'rXmeduc_m', 'rXnumerate']
    # New variable names
    vars_to_repl = ['rabmonth', 'rabyear', 'radmonth', 'radyear', 'raedisced', 'raeducl', 'raedyrs', 'raevbrn', 'rafeduc_m', 'ragender', 'raindlang', 'raliterate', 'rameduc_m', 'ranumerate']
    
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