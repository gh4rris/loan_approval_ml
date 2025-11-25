from config import LATEST_RUN

import pandas as pd
import mlflow
from typing import Any


def load_model() -> Any | None:
    with open(LATEST_RUN, "r") as f:
        run_id = f.read()
    return mlflow.sklearn.load_model(f"runs:/{run_id}/app_model")


def predict(model: Any, input_data: dict[str, Any]) -> dict[str, Any]:
    X = pd.DataFrame([input_data])

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0, 1]

    return {
        "loan_status": "Approved" if pred == 1 else "Rejected",
        "probability": round(float(prob), 2)
    }