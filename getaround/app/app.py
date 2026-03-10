import streamlit as st
from pydantic import BaseModel
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import requests
import logging

logger = logging.getLogger(__name__)

# ======================================================
# 🌐 API Pricing HF
# ======================================================

API_URL = "https://pradelf-getaround-api.hf.space/predict"


class RentalFeatures(BaseModel):
    model_key: str = "Peugeot"
    mileage: int = 0
    engine_power: int = 100
    fuel: str = "petrol"
    paint_color: str = "black"
    car_type: str = "sedan"
    private_parking_available: int = 1
    has_gps: int = 0
    has_air_conditioning: int = 0
    automatic_car: int = 0
    has_getaround_connect: int = 0
    has_speed_regulator: int = 0
    winter_tires: int = 0



def call_pricing_api(featRentalFeatures: RentalFeatures):
    """
    Appelle l'API FastAPI déployée sur Hugging Face.
    Retourne le prix prédit (float) ou None en cas d'erreur.
    """
    #payload = {"input": [featRentalFeatures.model_dump()]}
    payload = featRentalFeatures.model_dump()
    try:
        resp = requests.post(API_URL, json=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        logger.info(data)
        if "prediction" in data:
            return float(data["prediction"])
        else:
            st.error("Réponse API inattendue : clé 'prediction' absente.")
            return None, payload, data
    except Exception as e:
        st.error(f"Erreur lors de l'appel à l'API : {e}")
        return None, payload, None


logger.info('Started')
### CONFIG
st.set_page_config(page_title="Location Voiture", page_icon="💸", layout="wide")

### TITLE AND TEXT
st.title("Tableau de bord de Get Around")

st.markdown("""
    Ce site représente le **dashboard** destiné à aider l’équipe Produit pour appréhender l'introduction 
    de la nouvelle fonctionnalité consistant en l'implémentation d'un **délai minimum entre deux locations**.<br/> 
    Un véhicule ne sera pas affiché dans les résultats de recherche si les heures de check-in 
    ou de check-out demandées sont trop proches d’une location déjà existante.<br/>
             
    Grâce à ce site, l'équipe produit pourra répondre aux questions suivantes :<br/>
    - quelle doit être la durée minimale du délai entre deux locations ?
    - faut-il activer cette fonctionnalité pour tous les véhicules ou uniquement pour les véhicules Connect ?
    - Quelle part des revenus des propriétaires serait potentiellement affectée par cette fonctionnalité ?
    - Combien de locations seraient impactées en fonction du seuil et du périmètre choisis ?
    - À quelle fréquence les conducteurs sont-ils en retard pour le check-in suivant ? Quel est l’impact pour le conducteur suivant ?
    - Combien de situations problématiques seraient résolues selon le seuil et le périmètre retenus ?
            
    La documentation du web serveur de fonctions est déploiée sur l'url : [https://pradelf-getaround-api.hf.space/docs](https://pradelf-getaround-api.hf.space/docs)        """)
### LOAD DATA
DATA_PRICING = "/app/Data/get_around_pricing_project.csv"
DATA_PRICING_HF = "https://huggingface.co/datasets/pradelf/getaround-dataset/blob/main/get_around_pricing_project.csv"

DATA_DELAY = "/app/Data/get_around_delay_analysis.csv"
DATA_DELAY_HF = "https://huggingface.co/datasets/pradelf/getaround-dataset/blob/main/get_around_delay_analysis.csv"

# usage d'un décorateur python pour ajouter des fonctionnalité
# : st.cache_data et st.cache_resource qui remplace st.cache qui va devenir obsolète.
# https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data
# https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource
@st.cache_data
def load_data(file, nrows, delimiter=","):
    data = pd.read_csv(file, nrows=nrows, delimiter=delimiter)
    # data["Date"] = data["Date"].apply(lambda x: pd.to_datetime(",".join(x.split(",")[-2:])))
    # data["currency"] = data["currency"].apply(lambda x: pd.to_numeric(x[1:]))
    return data


data_load_state = st.text("Chargement des données...")
data_pricing = load_data(DATA_PRICING, 1000)
data_analysis = load_data(DATA_DELAY, 1000, ";")
data_load_state.text(
    ""
)  # change text from "Loading data..." to "" once the the load_data function has run

## Run the below code if the check is checked ✅
if st.checkbox("Montrer les données brutes sur le prix de location."):
    st.subheader("Tarif de location")
    st.write(data_pricing)
## Run the below code if the check is checked ✅
if st.checkbox("Montrer les données brutes sur l'analyse des retards de check-in."):
    st.subheader("Retard de check-in")
    st.write(data_analysis)
### SHOW GRAPH STREAMLIT

# price_per_model = data_pricing["price"]
# st.bar_chart(price_per_model)


### SIDEBAR
st.sidebar.header("Tableau de bord GetAround")
st.sidebar.markdown("""
    * GetAround projet
""")
e = st.sidebar.empty()
e.write("")
st.sidebar.write("GetAround Projet")

### EXPANDER

with st.expander(
    "⏯️ Regardez cette vidéo d'une minute pour comprendre comment fonctionne Getaround."
):
    st.video("https://youtu.be/3LyzwpGSfzE")

st.markdown("---")

#### CREATE TWO COLUMNS
col1, col2 = st.columns(2)

with col1:
    # visu des widgets
    st.markdown("Première colonne")
    car_id = st.selectbox(
        "Select a country you want to see all time sales",
        data_analysis["car_id"].sort_values().unique(),
    )
    # intelligence et contrôle du widget
    rental_canceled = data_analysis[data_analysis["state"] == "canceled"]
    fig = px.histogram(
        rental_canceled,
        x="time_delta_with_previous_rental_in_minutes",
        y="delay_at_checkout_in_minutes",
    )
    fig.update_layout(bargap=0.2)
    st.plotly_chart(fig, width='stretch')

with col2:
    st.markdown("Seconde colonne")
    with st.form("average_sales_per_country"):
        model = st.selectbox(
            "Sélectionnez un modèle de voiture pour voir le prix de location moyen",
            data_pricing["model_key"].sort_values().unique(),
        )
        power = st.selectbox(
            "Sélectionnez la puissance du moteur",
            data_pricing["engine_power"].sort_values().unique(),
        )
        submit = st.form_submit_button("submit")
        if submit:
            
            car_select=RentalFeatures(model_key=model, engine_power=power)
            # avg_rental_price = data_pricing[model_select & power_select][
            #    "rental_price_per_day"
            # ].mean()
            # model_select = data_pricing[data_pricing["model_key"] == model]
            # power_select = data_pricing[data_pricing["engine_power"] == power]
            logger.info(car_select)
            rental_price = call_pricing_api(
                car_select
            )
            # avg_rental_price = 0.0
            logger.info("##############")
            logger.info(rental_price)
            st.metric(f"Prix de location moyen (en $) :",f"{float(rental_price):.2f}")
# exemple de véhicule du site avec les données : https://fr.getaround.com/location-voiture/paris/citroen-c3-1608526