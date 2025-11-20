from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from src.predict import load_model, predict

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


app = FastAPI(title="Loan Approval Prediction App")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    app.mount("/static", StaticFiles(directory="api/static"), name="static")
    templates = Jinja2Templates(directory="api/templates")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=JSONResponse)
def get_prediction(application: LoanApplication):
    input_data = application.model_dump()
    model = load_model()
    return predict(model, input_data)