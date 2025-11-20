from config import DATA, SEED, LATEST_RUN

import pandas as pd
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import precision_score, recall_score, f1_score
from xgboost import XGBClassifier

def load_data(path: str):
    return pd.read_csv(path)

def build_processor(df: pd.DataFrame):
    categorical_features = df.select_dtypes(include="object").columns
    
    return ColumnTransformer(
        transformers=[("ohe", OneHotEncoder(drop="first"), categorical_features)],
        remainder="passthrough"
    )

def train_model(df: pd.DataFrame):
    numerical_features = df.select_dtypes(exclude="object").columns
    df[numerical_features] = df[numerical_features].astype(float)

    X = df.drop(columns="loan_status")
    y = df["loan_status"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEED)

    processor = build_processor(df)
    pipeline = Pipeline(
        steps=[("preprocessor", processor),
               ("scaler", StandardScaler()),
               ("classifier", XGBClassifier(colsample_bytree=0.5244063969, learning_rate=0.03997856839636343, max_depth=83, n_estimators=600))]
    )
    
    mlflow.set_experiment("Loan Approval")
    with mlflow.start_run() as run:
        pipeline.fit(X_train, y_train)

        y_pred = pipeline.predict(X_test)

        accuracy = round(pipeline.score(X_test, y_test), 2)
        precision = round(precision_score(y_test, y_pred), 2)
        recall = round(recall_score(y_test, y_pred), 2)
        f1 = round(f1_score(y_test, y_pred), 2)
    
        mlflow.log_param("model_type", "XGBoostClassifier")
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1", f1)
        mlflow.set_tag("Training Info", "XGBoost for predicting loan approval")
        
        mlflow.sklearn.log_model(
            sk_model=pipeline,
            name="app_model",
            input_example=X_train,
            signature=infer_signature(X_train.head(), pipeline.predict(X_train.head()))
        )
        run_id = run.info.run_id
    with open(LATEST_RUN, "w") as f:
        f.write(run_id)

    print(f"Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1: {f1}")

if __name__ == "__main__":
    df = load_data(DATA)
    train_model(df)