from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import load_model, predict
import uvicorn

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

app = FastAPI(title="Loan Approval Prediction API")

@app.get("/")
def root():
    return {"message": "Loan Approval Prediction API is running!"}

@app.post("/predict")
def get_prediction(application: LoanApplication):
    input_data = application.model_dump()
    model = load_model()
    return predict(model, input_data)

if __name__ == "__main__":
    uvicorn.run("api.app:app", reload=True)