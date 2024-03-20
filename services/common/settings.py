import os
import json


# REDIS settings
# Queue name
REDIS_QUEUE = "hozpitalization_predictor_queue"
# Port
REDIS_PORT = 6379
# DB Id
REDIS_DB_ID = 0
# Host IP
REDIS_IP = os.getenv("REDIS_IP", "redis")
# Sleep parameters which manages the
# interval between requests to our redis queue
API_SLEEP = 0.05

USED_VARIABLES = [
    'hltc', 'agey', 'height', 'decsib', 'henum', 'doctor1y', 'bmi', 'weight', 'cagem', 'outpt1y', 'fallinj',
    'mstat', 'livsib', 'shlt', 'imrc8', 'sight', 'mrct', 'drink', 'hearing', 'vscan', 'smokev', 'rxdiabi',
    'tr16', 'swell', 'hrtatte', 'fallnum', 'mstath', 'dentim1y', 'rxhibp', 'respe', 'rxarthr', 'painlv',
    'cancre', 'ftired', 'glasses', 'diabe', 'joga', 'shop', 'fatigue', 'vigact', 'rxhrtat', 'cesd_m', 'dlrc8',
    'fall', 'rxresp', 'push', 'nagi10', 'hearaid', 'breath_m', 'sleepr'
]

with open(
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "model_variables.json")
) as model_variables_file:
    JSON_MODEL_VARIABLES = json.load(model_variables_file)
    MODEL_VARIABLES = {
        variable: JSON_MODEL_VARIABLES[variable]
        for variable in USED_VARIABLES
    }
