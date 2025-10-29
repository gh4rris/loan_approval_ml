from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from src.predict import load_model, predict
from src.train import load_data, train_model
from src.config import DATA
import uvicorn
import mlflow
from dotenv import load_dotenv
import os

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
mlflow_server = FastAPI(title="Mlflow server")

def main():
    load_dotenv()
    tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
    if tracking_uri:
        mlflow.set_tracking_uri(tracking_uri)
        
    model = load_model()
    if model:
        print("Model loaded successfully")
    else:
        print("No existing model. Training new model:")
        df = load_data(DATA)
        train_model(df)
    

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
    

if __name__ == "__main__":
    main()
    uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=True)
    uvicorn.run("api.app:mlflow_server", host="0.0.0.0", port=5000)