from src.predict import load_model
from src.train import load_data, train_model
from src.config import DATA

import mlflow
import uvicorn
import os
from dotenv import load_dotenv

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

if __name__ == "__main__":
    main()
    uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=True)