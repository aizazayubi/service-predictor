# app/model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "service_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "service_encoder.pkl")

# Load data
df = pd.read_csv(DATA_PATH)

# Preprocessing
X = df[["Make","Model","Year","Mileage"]]
y = df["LastServiceType"]
X = pd.get_dummies(X)
le = LabelEncoder()
y = le.fit_transform(y)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model and encoder
pickle.dump(model, open(MODEL_PATH, "wb"))
pickle.dump(le, open(ENCODER_PATH, "wb"))

def predict_service(data_dict):
    df_input = pd.DataFrame([data_dict])
    df_input = pd.get_dummies(df_input)
    # Align columns with training data
    for col in X.columns:
        if col not in df_input:
            df_input[col] = 0
    df_input = df_input[X.columns]
    
    model = pickle.load(open(MODEL_PATH, "rb"))
    le = pickle.load(open(ENCODER_PATH, "rb"))
    pred = model.predict(df_input)
    return le.inverse_transform(pred)[0]
