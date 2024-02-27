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


def outline_dataframe(app_all: pd.DataFrame, elimins: List[list]) -> pd.DataFrame:
    sections = [section_A, section_B, section_C, section_D, section_E, section_F,
                section_G, section_H, section_I, section_J, section_K, section_L,
                section_M, section_O, section_Q]

    waves_col = filter_dataset(sections, elimins)

    waves = []

    for i in range(5):  
        data = {col: app_all[col] if col in app_all.columns else np.nan for col in waves_col[i]}
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
    waves = [[s.replace('X', str(i)) for s in unique_values_array] for i in range(1, 6)]

    return tuple(waves)

