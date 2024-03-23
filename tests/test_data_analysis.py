from model_engineering.src import (
    constants,
    data_utils
)


def test_get_datasets():
    h_mhas_c2 = data_utils.get_datasets(chunksize=10000)
    assert h_mhas_c2.shape[0] == 26839
    assert h_mhas_c2.shape[1] == 5241


def test_remove_unnecessary_columns():
    h_mhas_c2 = data_utils.get_datasets(chunksize=10000)
    h_mhas_c2 = data_utils.remove_unnecessary_columns(
        h_mhas_c2, constants.UNNECESARY_SECTION_COLUMNS)
    assert h_mhas_c2.shape[0] == 26839
    assert h_mhas_c2.shape[1] == 3706


def test_concatenate_waves():
    h_mhas_c2 = data_utils.get_datasets(chunksize=10000)
    h_mhas_c2 = data_utils.remove_unnecessary_columns(
        h_mhas_c2, constants.UNNECESARY_SECTION_COLUMNS)
    h_mhas_c2 = data_utils.concat_waves(h_mhas_c2)
    assert h_mhas_c2.shape[0] == 268390
    assert h_mhas_c2.shape[1] == 451
