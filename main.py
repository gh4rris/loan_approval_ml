from src.train import load_data, train_model
from src.predict import load_model, predict
from config import APP_PORT, HOST, DATA, STATIC, TEMPLATES, RUN_IDS, RANDOM_VALUES, MLFLOW_TRACKING_URI, RELOAD

import os
import mlflow
import uvicorn
from typing import Any, AsyncGenerator
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
from pydantic import BaseModel
from numpy.random import choice, uniform


class LoanApplication(BaseModel):
    person_age: float
    person_gender: str
    person_education: str
    person_income: float
    person_emp_exp: float
    person_home_ownership: str
    loan_amnt: float
    loan_intent: str
    loan_int_rate: float
    loan_percent_income: float
    cb_person_cred_hist_length: float
    credit_score: float
    previous_loan_defaults_on_file: str


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    if MLFLOW_TRACKING_URI:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    os.makedirs(RUN_IDS, exist_ok=True)

    try:
        app.model = load_model()
        print("Model loaded successfully")
    except:
        print("No existing model. Training new model:")
        df = load_data(DATA)
        train_model(df)
        app.model = load_model()
    yield

app = FastAPI(title="Loan Approval Prediction App", lifespan=lifespan)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    app.mount("/static", StaticFiles(directory=STATIC), name="static")
    templates = Jinja2Templates(directory=TEMPLATES)
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=JSONResponse)
def get_prediction(application: LoanApplication) -> dict[str, Any]:
    input_data = application.model_dump()
    return predict(app.model, input_data)

@app.get("/random", response_class=JSONResponse)
def random_input() -> dict[str, Any]:
    return LoanApplication(
        person_age=round(uniform(RANDOM_VALUES.person_age[0], RANDOM_VALUES.person_age[1])),
        person_gender=choice(RANDOM_VALUES.person_gender),
        person_education=choice(RANDOM_VALUES.person_education),
        person_income=round(uniform(RANDOM_VALUES.person_income[0], RANDOM_VALUES.person_income[1])),
        person_emp_exp=round(uniform(RANDOM_VALUES.person_emp_exp[0], RANDOM_VALUES.person_emp_exp[1])),
        person_home_ownership=choice(RANDOM_VALUES.person_home_ownership),
        loan_amnt=round(uniform(RANDOM_VALUES.loan_amnt[0], RANDOM_VALUES.loan_amnt[1])),
        loan_intent=choice(RANDOM_VALUES.loan_intent),
        loan_int_rate=round(uniform(RANDOM_VALUES.loan_int_rate[0], RANDOM_VALUES.loan_int_rate[1]), 2),
        loan_percent_income=round(uniform(RANDOM_VALUES.loan_percent_income[0], RANDOM_VALUES.loan_percent_income[1]), 2),
        cb_person_cred_hist_length=round(uniform(RANDOM_VALUES.cb_person_cred_hist_length[0], RANDOM_VALUES.cb_person_cred_hist_length[1])),
        credit_score=round(uniform(RANDOM_VALUES.credit_score[0], RANDOM_VALUES.credit_score[1])),
        previous_loan_defaults_on_file=choice(RANDOM_VALUES.previous_loan_defaults_on_file)
        ).model_dump()
    

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=int(APP_PORT), reload=RELOAD)