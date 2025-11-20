from src.predict import load_model
from src.train import load_data, train_model
from config import DATA, HOST, APP_PORT, RELOAD, MLFLOW_TRACKING_URI

import mlflow
import uvicorn
import os


def main():
    if MLFLOW_TRACKING_URI:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    if not os.path.exists("run_ids"):
        os.mkdir("run_ids")
    
    model = load_model()
    if model:
        print("Model loaded successfully")
    else:
        print("No existing model. Training new model:")
        df = load_data(DATA)
        train_model(df)


if __name__ == "__main__":
    main()
    uvicorn.run("api.app:app", host=HOST, port=int(APP_PORT), reload=RELOAD)