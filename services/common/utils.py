from .settings import MODEL_VARIABLES


def encode_data(data: dict):
    encoded_data = {}
    for key, value in data.items():
        if value is None:
            encoded_data[key] = None
        else:
            if MODEL_VARIABLES[key]["is_categorical"]:
                encoded_data[key] = MODEL_VARIABLES[key]["values"][value]
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
