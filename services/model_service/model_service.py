import json
import time

import redis
from common import settings
import joblib

import pandas as pd

from common.utils import encode_data

db = redis.StrictRedis(host=settings.REDIS_IP, port=settings.REDIS_PORT, db=settings.REDIS_DB_ID)

model = joblib.load("trained_model/final_model.pkl")
preprocessing_pipeline = joblib.load('trained_model/preprocessing_pipeline.pkl')


def predict(data):

    data = encode_data(data)

    df = pd.DataFrame(data, index=[0])
    df = df[sorted(df.columns)]
    df = pd.DataFrame(preprocessing_pipeline.transform(df), columns=df.columns)

    prediction = model.predict(df)
    pred_probability = model.predict_proba(df)[:, 1]

    return prediction, pred_probability


def handle_queue_messages():
    while True:
        _, job = db.brpop(settings.REDIS_QUEUE)

        data = json.loads(job.decode("utf-8"))
        id = data.pop('id', None)

        class_name, pred_probability = predict(data)

        result = {
                "prediction": class_name.tolist()[0],
                "score": str(pred_probability[0]),
            }

        db.set(id, json.dumps(result))

        time.sleep(settings.SERVER_SLEEP)


if __name__ == "__main__":
    print("Launching ML service...")
    handle_queue_messages()
