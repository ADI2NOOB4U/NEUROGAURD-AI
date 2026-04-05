from sklearn.ensemble import IsolationForest
import joblib
import os
import numpy as np

MODEL_PATH = "model.pkl"
model = None


def train_model():
    global model

    data = np.array([
        [5, 10, 2],
        [10, 20, 4],
        [15, 30, 6],
        [20, 40, 8],
        [25, 35, 5],
        [30, 50, 10],
        [2, 5, 1],
        [8, 15, 3]
    ])

    model = IsolationForest(contamination=0.2, random_state=42)
    model.fit(data)

    joblib.dump(model, MODEL_PATH)


def load_model():
    global model

    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
    else:
        train_model()


def predict(process_data):
    global model

    if model is None:
        load_model()

    try:
        data = np.array([[
            process_data["cpu"],
            process_data["memory"],
            process_data["threads"]
        ]])

        prediction = model.predict(data)[0]

        # ✅ Confidence score (NOW CORRECT)
        score = model.decision_function(data)[0]
        confidence = round(abs(score) * 100, 2)

        label = "SAFE" if prediction == 1 else "SUSPICIOUS"

        return {
            "prediction": label,
            "confidence": confidence
        }

    except Exception as e:
        print("Prediction Error:", e)
        return {
            "prediction": "SAFE",
            "confidence": 0
        }