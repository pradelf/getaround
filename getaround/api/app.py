from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd
import config
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# 1) URL du Space HF qui héberge MLflow (tracking server)
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


description = """
Bienvenue sur l'API de Getaround pour prédire le prix journalier de location d'une voiture en fonction de son année d'expérience!
## Point de terminaison d'introduction
Pour tester le fonctionnement de l'API, vous pouvez utiliser le point de terminaison d'introduction suivant:
* `/`: **GET** retourne la version de l'API et un message de bienvenue.
## Point de terminaison de ligne de vie
Cette web fonction permet de vérifier que le serveur de l'API est opérationnel et de surveiller son statut.
* `/health`: **GET** retourne juste OK pour valider que le serveur de l'API est en cours d'exécution sans problèmes.
## Machine Learning : Point de terminaison du prix de location
Cette terminaison de l'API permet de prédire le prix journalier de location d'une voiture en fonction de ses caractéristiques..
* `/predict` accepte une requête POST avec un JSON contenant un objet JSON donnant les caractéristiques d'une voiture 
et retourne une prédiction du prix journalier de location de celle-ci.
La documentation est ci-dessous 👇 pour chaque point de terminaison (endpoints). 
"""

tags_metadata = [
    {
        "name": "Point de terminaison d'introduction",
        "description": "Terminaison simple de présentation de l'API et de sa version pour vérifier que tout fonctionne correctement.",
    },
    {
        "name": "Point de terminaison de ligne de vie",
        "description": "Point de terminaison de ligne de vie pour surveiller le statut du serveur de l'API. Retourne 'ok' si le serveur fonctionne sans problèmes.",
    },
    {
        "name": "Point de terminaison du prix de location",
        "description": "Point de terminaison permettant de prédire le prix journalier de location d'une voiture en fonction de ses caractéristiques.",
    },
    {
        "name": "Machine Learning",
        "description": "Point de terminaison de prediction du prix de location journalier d'un véhicule en fonction de ses caractéristiques.",
    },
]


model= None

app = FastAPI(
    title="Getaround API pour le prix journalier de location d'une voiture.",
    description=description,
    version=config.__version__,
    contact={
        "name": "Francis Pradel",
        "url": "https://promotion.francispradel.fr",
    },
    openapi_tags=tags_metadata,
)

@app.on_event("startup")
def load_model_on_startup():
    global model
    try:
        logger.info(f"Chargement du modèle depuis {MLFLOW_TRACKING_URI}")
        logger.info(f"Model  : {MODEL_URI}")
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)  # ou via env MLFLOW_TRACKING_URI
        model = mlflow.pyfunc.load_model(MODEL_URI)
        logger.info("Modèle chargé avec succès")
    except Exception:
        logger.exception("Impossible de charger le modèle au démarrage")
        model = None

class RentalFeatures(BaseModel):
    model_key: str
    mileage: int
    engine_power: int
    fuel: str
    paint_color: str
    car_type: str
    private_parking_available: int
    has_gps: int
    has_air_conditioning: int
    automatic_car: int
    has_getaround_connect: int
    has_speed_regulator: int
    winter_tires: int


@app.get("/", tags=["Introduction Endpoints"])
def greet_json():
    """
    Bonjour
    """
    return {"Hello": "World!", "version": config.__version__}


@app.get("/health")
def health():
    """
    Health line to monitor the server status of the API. Returns "ok" if the server is running without issues.
    """
    return {"status": "ok"}


@app.post("/predict", tags=["Machine Learning"])
async def predict(predictionFeatures: RentalFeatures):
    """
    Prediction of car daily rental cost for a given properties of a car !
    """
    # Read data
    # pf = [
    #     predictionFeatures.model_key or "Peugeot",   
    #     predictionFeatures.mileage or 0,
    #     predictionFeatures.engine_power or 0,
    #     predictionFeatures.fuel or "petrol",
    #     predictionFeatures.car_type or "sedan",
    #     predictionFeatures.private_parking_available or 1,
    #     predictionFeatures.has_gps or 0,
    #     predictionFeatures.has_air_conditioning or 0,
    #     predictionFeatures.automatic_car or 0,
    #     predictionFeatures.has_getaround_connect or 0,
    #     predictionFeatures.has_speed_regulator or 0,
    #     predictionFeatures.winter_tires or 0,
    # ]
    try:
        car_caracteristic = pd.DataFrame([predictionFeatures.model_dump()])
        #car_caracteristic = pd.DataFrame({"Car": pf})
        # Log model from mlflow
   
        BOOL_COLS = [
            "private_parking_available",
            "has_gps",
            "has_air_conditioning",
            "automatic_car",
            "has_getaround_connect",
            "has_speed_regulator",
            "winter_tires",
        ]
        # Conversion explicite des colonnes booléennes
        for col in BOOL_COLS:
            car_caracteristic[col] = car_caracteristic[col].astype(bool)
        # Prediction from previously loaded model as a PyFuncModel.
        prediction = model.predict(car_caracteristic)

        # Format response
        response = {
            "prediction": prediction.tolist()[0],
            "detail": "Prédiction du tarif journalier (nul si aucun modèle : model.pkl).",
        }
        return response
    except Exception as e:
        logger.exception("Erreur dans /predict")
        raise Exception(status_code=500, detail=str(e))
