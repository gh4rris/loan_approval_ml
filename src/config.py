import os
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = f"{ROOT_PATH}/data/loan_data.csv"
REGISTERED_MODEL="logreg_loan_approval"
SEED = 666