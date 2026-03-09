import os
import mlflow
import mlflow.pyfunc
import pandas as pd

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "https://pradelf-getaround-mlflow.hf.space")
MODEL_URI = os.getenv("MODEL_URI", "models:/getaround-price-prediction-model@certification")

BOOL_COLS = [
    "private_parking_available",
    "has_gps",
    "has_air_conditioning",
    "automatic_car",
    "has_getaround_connect",
    "has_speed_regulator",
    "winter_tires",
]

def load_predictor():
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.pyfunc.get_model_dependencies(MODEL_URI)
    return mlflow.pyfunc.load_model(MODEL_URI)

def predict_targets(model, input_rows):
    X = pd.DataFrame(input_rows)
    # Conversion explicite des colonnes booléennes
    for col in BOOL_COLS:
        X[col] = X[col].astype(bool)

    preds = model.predict(X)
    return preds

if __name__ == "__main__":
    model = load_predictor()
    peugeot_208 = {
      "model_key": "Peugeot",
      "mileage": 100000,
      "engine_power": 100,
      "fuel": "petrol",
      "paint_color": "black",
      "car_type": "convertible",
      "private_parking_available": False,
      "has_gps": False,
      "has_air_conditioning": False,
      "automatic_car": False,
      "has_getaround_connect": False,
      "has_speed_regulator": False,
      "winter_tires": False
    }
    citron={
      "model_key": "Citroën",
      "mileage": 100000,
      "engine_power": 150,
      "fuel": "petrol",
      "paint_color": "blue",
      "car_type": "sedan",
      "private_parking_available": False,
      "has_gps": False,
      "has_air_conditioning": False,
      "automatic_car": False,
      "has_getaround_connect": False,
      "has_speed_regulator": False,
      "winter_tires": False
    }
    data = [
        peugeot_208,
        citron,
    ]
    data= [citron]
    print(data)
    y_pred = predict_targets(model, data)
    print(y_pred)
    data = [
        peugeot_208,
        citron,
    ]
    print(data)
    y_pred = predict_targets(model, data)
    print(y_pred)