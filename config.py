import os
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()

APP_PORT = os.getenv("APP_PORT")
MLFLOW_PORT = os.getenv("MLFLOW_PORT")
MLFLOW_BASE_URI = os.getenv("MLFLOW_BASE_URI")
HOST = os.getenv("HOST")
PLATFORM = os.getenv("PLATFORM")

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(ROOT_PATH, "data", "loan_data.csv")
FRONTEND = os.path.join(ROOT_PATH, "frontend")
STATIC = os.path.join(FRONTEND, "static")
TEMPLATES = os.path.join(FRONTEND, "templates")
RUN_IDS = os.path.join(ROOT_PATH, "run_ids")
LATEST_RUN = os.path.join(RUN_IDS, "app_latest_run.txt")
MLFLOW_TRACKING_URI = MLFLOW_BASE_URI + MLFLOW_PORT if PLATFORM == "docker" else f"file://{ROOT_PATH}/mlruns"
RELOAD = False if PLATFORM == "prod" else True
SEED = 666

class ApplicationValues(BaseModel):
    person_age: tuple[int, int]
    person_gender: tuple[str, ...]
    person_education: tuple[str, ...]
    person_income: tuple[int, int]
    person_emp_exp: tuple[int, int]
    person_home_ownership: tuple[str, ...]
    loan_amnt: tuple[int, int]
    loan_intent: tuple[str, ...]
    loan_int_rate: tuple[float, ...]
    loan_percent_income: tuple[float, ...]
    cb_person_cred_hist_length: tuple[int, int]
    credit_score: tuple[int, int]
    previous_loan_defaults_on_file: tuple[str, ...]

RANDOM_VALUES = ApplicationValues(
    person_age=(20, 120),
    person_gender=("male", "female"),
    person_education=("High School", "Associate", "Bachelor", "Master", "Doctorate"),
    person_income=(8000, 200_000),
    person_emp_exp=(0, 40),
    person_home_ownership=("RENT", "MORTGAGE", "OWN", "OTHER"),
    loan_amnt=(500, 35000),
    loan_intent=("PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"),
    loan_int_rate=(5.5, 20),
    loan_percent_income=(0, 0.66),
    cb_person_cred_hist_length=(2, 25),
    credit_score=(200, 800),
    previous_loan_defaults_on_file=("Yes", "No")
)