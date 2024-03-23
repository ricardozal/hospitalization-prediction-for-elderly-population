import json
import time
from uuid import uuid4

import redis
import common.settings as settings
from common.utils import decode_data
import pandas as pd

db = redis.StrictRedis(host=settings.REDIS_IP, port=settings.REDIS_PORT, db=settings.REDIS_DB_ID)


def predict_hospitalization(data: pd.DataFrame):
    prediction = None
    score = None
    data['id'] = str(uuid4())
    id = data['id'].iloc[0]  # Access the first element since data is a DataFrame

    db.lpush(settings.REDIS_QUEUE, json.dumps(data.to_dict(orient="records")[0]))

    while True:
        output = db.get(id)

        if output is not None:
            output = json.loads(output.decode("utf-8"))
            prediction = output["prediction"]
            score = output["score"]

            db.delete(id)
            break

        time.sleep(settings.API_SLEEP)

    return prediction, score


def predict_hospitalization_bunch(data: pd.DataFrame) -> pd.DataFrame:
    # Initialize lists to store the predictions and scores
    predictions = []
    scores = []

    # Iterate through each row in the DataFrame
    for _, row in data.iterrows():
        # Convert the single row to a DataFrame
        single_row_df = pd.DataFrame([row])

        # Call the predict_hospitalization function
        prediction, score = predict_hospitalization(single_row_df)

        # Append the results to the lists
        predictions.append("YES" if prediction else "NO")
        scores.append(f"{(float(score) * 100):.3f} %")

    data_dict = data.to_dict(orient="records")
    decoded_data = []

    for to_decode in data_dict:
        decoded = decode_data(to_decode)
        decoded_data.append(decoded)

    data = pd.DataFrame(decoded_data)

    # Add the predictions and scores as new columns to the original DataFrame
    data['will be hospitalized'] = predictions
    data['probability'] = scores

    return data
