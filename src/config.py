import os
from pathlib import Path

DATASET_ROOT_PATH = str(Path(__file__).parent.parent / "dataset")
os.makedirs(DATASET_ROOT_PATH, exist_ok=True)

DATASET_MHAS_C2 = str(Path(DATASET_ROOT_PATH) / "H_MHAS_c2.sas7bdat")
DATASET_MHAS_URL = (
    "https://drive.google.com/uc?id=1PZRLL7cq6UAVLG3DFeuPuhrS1LJTsNvY&confirm=t"
)
DATASET_MHAS_EOL = str(Path(DATASET_ROOT_PATH) / "H_MHAS_EOL_b.sas7bdat")
DATASET_MHAS_EOL_URL = (
    "https://drive.google.com/uc?id=1bH9hNW0FoN_1q-rovnB8_59ovi3jXs3j&confirm=t"
)
DATASET_MEX_COG = str(
    Path(DATASET_ROOT_PATH) / "H_MEX_COG_A2_2016.dta"
)
DATASET_MEX_COG_URL = (
    "https://drive.google.com/uc?id=1MnDC30Jo5Jztmb99z5PLJQA47vj-iDdA&confirm=t"
)
