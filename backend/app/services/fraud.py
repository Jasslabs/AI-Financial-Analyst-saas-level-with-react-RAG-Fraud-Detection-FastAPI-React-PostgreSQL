# backend/app/services/fraud.py
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

def train_fraud_model(df: pd.DataFrame):
    features = df[["amount"]]
    model = IsolationForest(contamination=0.02, random_state=42)
    model.fit(features)
    joblib.dump(model, "models/fraud.pkl")

def predict_fraud(amount: float):
    model = joblib.load("models/fraud.pkl")
    pred = model.predict([[amount]])
    score = model.decision_function([[amount]])[0]
    return {
        "is_fraud": bool(pred[0] == -1),
        "fraud_score": float(score)
    }