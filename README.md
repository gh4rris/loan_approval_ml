# Loan Approval Predictor

A supervised machine learning application that predicts loan approval likelihood. Includes full MLOps tracking and deployment pipeline using MLflow, Docker, and AWS EC2 Instance.

The notebooks include an exploratory data analysis of the training data: [01_eda.ipynb](/notebooks/01_eda.ipynb) & an interpretability analysis of the final XGBClassifier, using partial dependece plots to visualize how features affect the target: [04_interpretability.ipynb](/notebooks/04_interpretability.ipynb)

Live app: [http://ec2-35-179-103-165.eu-west-2.compute.amazonaws.com:8000](http://ec2-35-179-103-165.eu-west-2.compute.amazonaws.com:8000)

![loan-app](/images/loan-approval.jpg)

## Features

- Machine Learning model to predict loan approval likelihood
- MLflow tracking and experiment logging
- Live API & Frontend UI
- Automated Docker compose for local build
- AWS EC2 Instance deployment
- CI/CD via Github Actions
- Notebooks with data EDA & model interpretability analysis

![mlflow-server](/images/mlflow.jpg)

## Tech Stack

- **Backend:** Python, FastAPI
- **ML:** scikit-learn, pandas, numpy, mlflow
- **Frontend:** Javascript, HTML, CSS
- **Deployment:** Docker, AWS EC2

## Run locally

Local run can either be done with, or without containers

- Clone the repo:

```bash
git clone https://github.com/gh4rris/loan_approval_ml.git
cd loan_approval_ml
```

- Create a .env file:

```env
APP_PORT="8000"
MLFLOW_PORT="5000"
MLFLOW_BASE_URI="http://mlflow_server:"
HOST="0.0.0.0"
PLATFORM="docker"
```

### With containers (Recommended)

- Build docker containers:

```bash
docker compose -f docker-compose.local.yml up -d
```

### Without containers

- Update PLATFORM variable to "dev" in .env

- Install dependencies and run python:

```bash
pip install -r requirements.txt
python main.py
```

- Run mlflow in another terminal:

```bash
mlflow ui --port 5000
```

### View App & MLflow Server

App: http://localhost:8000<br>
MLflow Server: http://localhost:5000

## Relationship between features and target [04_interpretability.ipynb](/notebooks/04_interpretability.ipynb)

![numerical](/images/pdp_numerical.png)

![categorical](/images/pdp_categorical.png)
