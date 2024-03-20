import json
import time

import redis
import common.settings as settings
import pandas as pd

db = redis.StrictRedis(host=settings.REDIS_IP, port=settings.REDIS_PORT, db=settings.REDIS_DB_ID)


def predict_hospitalization(data):
    prediction = None
    score = None
    id = data['id']

    db.lpush(settings.REDIS_QUEUE, json.dumps(data))

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


def predict_hospitalization_bunch(data):
    pass
