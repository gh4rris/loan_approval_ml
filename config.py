import os
from dotenv import load_dotenv


load_dotenv()

APP_PORT = os.getenv("APP_PORT")
MLFLOW_PORT = os.getenv("MLFLOW_PORT")
MLFLOW_BASE_URI = os.getenv("MLFLOW_BASE_URI")
HOST = os.getenv("HOST")
PLATFORM = os.getenv("PLATFORM")

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DATA = f"{ROOT_PATH}/data/loan_data.csv"
LATEST_RUN = f"{ROOT_PATH}/run_ids/app_latest_run.txt"
MLFLOW_TRACKING_URI = f"file://{ROOT_PATH}/mlruns" if PLATFORM == "dev" else MLFLOW_BASE_URI + MLFLOW_PORT
RELOAD = True if PLATFORM == "dev" else False
SEED = 666