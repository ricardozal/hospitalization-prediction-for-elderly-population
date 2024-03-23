from .settings import MODEL_VARIABLES
import re
import numpy as np


def get_description_value(key, value):
    try:
        return MODEL_VARIABLES[key]["values"][
            re.sub(r'^\d+.','', value)]
    except:
        return value


def encode_data(data: dict):
    encoded_data = {}
    for key, value in data.items():
        if value is None:
            encoded_data[key] = None
        else:
            if MODEL_VARIABLES[key]["is_categorical"]:
                if isinstance(value, dict):
                    encoded_data[key] = [
                        get_description_value(key, v)
                        for v in value.values()
                    ]
                else:
                    encoded_data[key] = get_description_value(key, value)
            else:
                if isinstance(value, dict):
                    encoded_data[key] = list(value.values())
                else:
                    encoded_data[key] = value
    return encoded_data


def decode_data(data: dict):
    decoded_data_dict = {}
    for key, value in data.items():
        if value is None:
            decoded_data_dict[key] = None
        else:
            if MODEL_VARIABLES[key]["is_categorical"]:
                decoded_data_dict[key] = [k for k, v in MODEL_VARIABLES[key]["values"].items()
                                     if v == value]
                if len(decoded_data_dict[key]) == 1:
                    decoded_data_dict[key] = decoded_data_dict[key][0]
                else:
                    decoded_data_dict[key] = None
            else:
                decoded_data_dict[key] = data[key]
    return decoded_data_dict
