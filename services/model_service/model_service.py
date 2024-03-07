import json
import time

import numpy as np
import redis
from common import settings
import random

db = redis.StrictRedis(host=settings.REDIS_IP, port=settings.REDIS_PORT, db=settings.REDIS_DB_ID)

model = ...


def predict(data):

    print(data)

    prediction = np.random.choice([True, False], size=len(data)).tolist()
    pred_probability = random.random()

    return prediction, pred_probability



def handle_queue_messages():
    while True:
        _, job = db.brpop(settings.REDIS_QUEUE)

        data = json.loads(job.decode("utf-8"))
        id = data.pop('id', None)

        class_name, pred_probability = predict(data)

        result = {
                "prediction": class_name,
                "score": str(pred_probability),
            }
        
        db.set(id, json.dumps(result))

        time.sleep(settings.SERVER_SLEEP)


if __name__ == "__main__":
    print("Launching ML service...")
    handle_queue_messages()
