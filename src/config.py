import os
ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = f"{ROOT_PATH}/data/loan_data.csv"
LATEST_RUN_PATH = f"{ROOT_PATH}/latest_run.txt"
SEED = 666