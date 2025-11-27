from config import SEED

import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.metrics import precision_score, recall_score, f1_score


def test_load_data():
    X, y = make_classification(n_samples=45000, n_features=13, random_state=SEED)

    assert X.shape == (45000, 13), "The data should have 45,000 samples of 13 features"
    assert y.shape == (45000,), "The data should have 45,000 samples of 1 target"

def test_train_model():
    X_train, y_train = make_classification(n_samples=36000, n_features=13, random_state=SEED)
    X_test, y_test = make_classification(n_samples=14000, n_features=13, random_state=SEED)

    model = xgb.XGBClassifier().fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = model.score(X_test, y_test)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    assert accuracy >= 0 and accuracy <= 1, "Accuracy should be between 0 and 1"
    assert precision >= 0 and precision <= 1, "Precision should be between 0 and 1"
    assert recall >= 0 and recall <= 1, "Recall should be between 0 and 1"
    assert f1 >= 0 and f1 <= 1, "F1 should be between 0 and 1"