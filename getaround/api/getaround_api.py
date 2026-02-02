from fastapi import FastAPI
from pydantic import BaseModel
import os, joblib
import numpy as np

app = FastAPI(title="GetAround Pricing API", version="0.1.0")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")


class RentalFeatures(BaseModel):
    car_age: float | None = None
    mileage: float | None = None
    rating: float | None = None
    delay_between_rentals: float | None = None
    price_per_day: float | None = None


def _load_model():
    if os.path.exists(MODEL_PATH):
        try:
            return joblib.load(MODEL_PATH)
        except Exception:
            pass

    # Fallback dummy linear model
    class FallbackModel:
        coef_ = np.array([2.0, -0.0005, 1.5, 0.1, 0.0], dtype=float)
        intercept_ = 20.0

        def predict(self, X):
            X = np.array(X, dtype=float)
            return X @ self.coef_ + self.intercept_

    return FallbackModel()


model = _load_model()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(features: RentalFeatures):
    x = [
        features.car_age or 0,
        features.mileage or 0,
        features.rating or 0,
        features.delay_between_rentals or 0,
        features.price_per_day or 0,
    ]
    y_pred = float(model.predict([x])[0])
    return {
        "prediction": y_pred,
        "detail": "Predicted daily demand score (dummy if no model.pkl).",
    }
