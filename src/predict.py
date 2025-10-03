import pandas as pd
import mlflow
import json

def load_model():
    return mlflow.sklearn.load_model(f"models:/logreg_loan_approval/latest")

def predict(model, input_data: dict):
    X = pd.DataFrame([input_data])

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0, 1]

    return {
        "loan_status": "Approved" if pred == 1 else "Rejected",
        "probability": round(prob, 2)
    }

if __name__ == "__main__":
    model = load_model()

    example_input = {
        "person_age": 33,
        "person_gender": "female",
        "person_education": "Bachelor",
        "person_income": 42000,
        "person_emp_exp": 15,
        "person_home_ownership": "RENT",
        "loan_amnt": 11000,
        "loan_intent": "EDUCATION",
        "loan_int_rate": 11.76,
        "loan_percent_income": 0.26,
        "cb_person_cred_hist_length": 10,
        "credit_score": 627,
        "previous_loan_defaults_on_file": "No"
    }

    result = predict(model, example_input)
    print(json.dumps(result, indent=2))