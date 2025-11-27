from config import SEED

import xgboost as xgb
from sklearn.datasets import make_classification


def test_predict():
    X_train, y_train = make_classification(n_samples=36000, n_features=13, random_state=SEED)
    X, _ = make_classification(n_samples=1, n_features=13, random_state=SEED)

    model = xgb.XGBClassifier().fit(X_train, y_train)

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0, 1]

    assert set([pred]) <= {0, 1}, "Prediction should be 0 or 1"
    assert prob >= 0 and prob <= 1, "Probability should be between 0 and 1"
