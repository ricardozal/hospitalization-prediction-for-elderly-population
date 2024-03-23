import pandas as pd
import numpy as np

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

def elim_bycorr(app_train : pd.DataFrame, corr_threshold : float) -> pd.DataFrame:
    sections = [section_A, section_B, section_C, section_D, section_E, section_F,
                section_G, section_H, section_I, section_J, section_K, section_L,
                section_M, section_O, section_Q] 

    df = app_train.copy()
    
    vars_to_elimin = ['rXbmonth', 'rXbyear', 'rXdmonth', 'rXdyear', 'rXedisced', 'rXeducl', 'rXedyrs', 'rXevbrn', 'rXfeduc_m', 'rXgender', 'rXindlang', 'rXliterate', 'rXmeduc_m', 'rXnumerate']

    all_to_drop = []

    for section in sections:
        Total_section = []
        for values_list in section.values():
                Total_section.extend(values_list)
        new_list = [item[0] + 'X' + item[2:] if item[1].isdigit() else item for item in Total_section]
        new_list = [name.replace('s', 'r', 1) if name.startswith('s') else name for name in new_list]
        modified_list = [name for name in new_list if name not in vars_to_elimin]
        names_starting_other = [name for name in df.columns.tolist() if name in modified_list]
        corr = df[names_starting_other].corr(numeric_only=True).abs()
        upper_tri = corr.where(np.triu(np.ones(corr.shape), k=1).astype(np.bool_)) 
        to_drop = [col for col in upper_tri.columns if any(upper_tri[col] > corr_threshold)]
        all_to_drop.extend(to_drop)

    all_to_drop = np.unique(all_to_drop)
    df_dropped = df.drop(all_to_drop.tolist(), axis=1)
    return df_dropped

def remove_highly_correlated(df: pd.DataFrame, target: str, threshold: float):
    # Make a copy of df
    temp_df = df.copy()

    # Check if target is datetime, if so, convert it to numeric timestamps
    if temp_df[target].dtypes.kind == 'M':
        temp_df[target] = temp_df[target].values.astype(float)

    # Calculate correlations
    correlations = temp_df.corr(numeric_only=True)[target].abs()

    # Identify columns to drop (those with correlation to target greater than threshold)
    to_drop = [column for column in temp_df.columns
               if column != target and column in correlations and correlations[column] >= threshold]

    # Drop highly correlated columns
    df_dropped = df.drop(to_drop, axis=1)

    return df_dropped