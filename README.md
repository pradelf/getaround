# getaround

**Bloc 5 - Industrialisation d'un algorithme d'apprentissage automatique et automatisation des processus de décision.**

Ce projet est à réaliser pour valider partiellement la certification Data Science - Fullstack : Certification RNCP35288 CDSD avec le bloc 5.

Ce projet est également déposé sur github :  [https://github.com/pradelf/getaround](https://github.com/pradelf/getaround)
___

![MLflow](https://img.shields.io/badge/MLflow-Tracking-red?logo=mlflow)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-orange?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Live](https://img.shields.io/badge/Status-Live%20Demo-success)
![CCDS](https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter)

___

![snap](https://fr.getaround.com/packs/images/app/assets/images/shared/getaround-logo.245e368962541c3c.svg)

- [getaround](#getaround)
  - [Description et contexte du projet](#description-et-contexte-du-projet)
    - [Contexte](#contexte)
    - [Projet 🚧](#projet-🚧)
    - [Objectifs 🎯](#objectifs-🎯)
      - [Tableau de bord web](#tableau-de-bord-web)
      - [Machine Learning – endpoint `/predict`](#machine-learning-–-endpoint-predict)
      - [Page de documentation](#page-de-documentation)
      - [Mise en production en ligne](#mise-en-production-en-ligne)
    - [Aides 🦮](#aides-🦮)
      - [Partage du code](#partage-du-code)
    - [Livrables 📬](#livrables-📬)
    - [Données](#données)
  - [Organisation du projet](#organisation-du-projet)
    - [Structure du projet](#structure-du-projet)
    - [Données](#données-1)
    - [Point d'entrée](#point-dentrée)

___
Projet d'évaluation des impacts de retard sur les locations de getaround.

## Description et contexte du projet

[GetAround](https://www.getaround.com/?wpsrc=Google+Organic+Search) est l’équivalent d’Airbnb pour les voitures. Il est possible de louer des véhicules appartenant à des particuliers pour quelques heures ou plusieurs jours. Fondée en 2009, cette entreprise a connu une croissance rapide. En 2019, elle comptait plus de 5 millions d’utilisateurs et environ 20 000 véhicules disponibles dans le monde.

En tant que partenaire de Jedha, GetAround a proposé le challenge suivant :

### Contexte

Lors de la location d’un véhicule, les utilisateurs doivent réaliser :

- un **check-in** au début de la location,
- un **check-out** à la fin de la location,

afin de :

- évaluer l’état du véhicule et signaler aux autres parties les dommages préexistants ou survenus pendant la location ;
- comparer les niveaux de carburant ;
- mesurer le nombre de kilomètres parcourus.

Le check-in et le check-out peuvent être réalisés selon trois modalités distinctes :

- **📱 Mobile** : contrat de location signé via l’application mobile, le conducteur et le propriétaire se rencontrent et signent tous deux sur le smartphone du propriétaire ;
- **Connect** : le conducteur ne rencontre pas le propriétaire et ouvre le véhicule à l’aide de son smartphone ;
- **📝 Papier** : contrat papier (cas négligeable).

### Projet 🚧

Pour cette étude de cas, nous vous proposons de vous placer dans notre situation et de reproduire une analyse que nous avons menée en 2017 🔮🪄

Sur GetAround, les conducteurs réservent des véhicules pour une période donnée, allant d’une heure à plusieurs jours. Ils sont censés restituer le véhicule à l’heure prévue, mais il arrive que certains conducteurs soient en retard lors du check-out.

Ces retards peuvent générer une forte friction pour le conducteur suivant lorsque le véhicule est reloué le même jour. Le service client rapporte fréquemment des utilisateurs mécontents ayant dû attendre le retour du véhicule depuis la location précédente, voire contraints d’annuler leur réservation parce que le véhicule n’avait pas été restitué à temps.

### Objectifs 🎯

Afin de limiter ces problèmes, nous avons décidé d’implémenter un **délai minimum entre deux locations**. Un véhicule ne sera pas affiché dans les résultats de recherche si les heures de check-in ou de check-out demandées sont trop proches d’une location déjà existante.

Cette solution permet de réduire les problèmes de retard au check-out, mais elle peut également impacter négativement les revenus de GetAround et des propriétaires : il est donc nécessaire de trouver le bon compromis.

**Notre Product Manager doit encore trancher sur les points suivants :**

- **seuil** : quelle doit être la durée minimale du délai entre deux locations ?
- **périmètre** : faut-il activer cette fonctionnalité pour tous les véhicules ou uniquement pour les véhicules Connect ?

Afin de l’aider à prendre la bonne décision, il vous est demandé de produire des analyses de données pertinentes. Voici quelques premières pistes de réflexion pour lancer la discussion (n’hésitez pas à approfondir avec des analyses supplémentaires) :

- Quelle part des revenus des propriétaires serait potentiellement affectée par cette fonctionnalité ?
- Combien de locations seraient impactées en fonction du seuil et du périmètre choisis ?
- À quelle fréquence les conducteurs sont-ils en retard pour le check-in suivant ? Quel est l’impact pour le conducteur suivant ?
- Combien de situations problématiques seraient résolues selon le seuil et le périmètre retenus ?

#### Tableau de bord web

Commencez par construire un **dashboard** destiné à aider l’équipe Produit à répondre aux questions ci-dessus. Vous pouvez utiliser `streamlit` ou toute autre technologie que vous jugerez appropriée.

#### Machine Learning – endpoint `/predict`

En complément des analyses précédentes, l’équipe Data Science travaille sur un sujet d’**optimisation de la tarification**. Des données ont été collectées afin de proposer des prix optimaux aux propriétaires à l’aide de modèles de Machine Learning.

Vous devez fournir au minimum **un endpoint** `/predict`. L’URL complète est : `https://pradelf-getaround-api.hf.space/predict`.

Cet endpoint doit accepter des requêtes **POST** avec des données d’entrée au format JSON et retourner les prédictions correspondantes. On suppose que **les données d’entrée sont toujours correctement formatées** ; la gestion des erreurs est donc optionnelle.

Exemple d’entrée :

```
{
  "model_key": "Peugeot",
  "mileage": 10000,
  "engine_power": 130,
  "fuel": "petrol",
  "paint_color": "black",
  "car_type": "convertible",
  "private_parking_available": true,
  "has_gps": true,
  "has_air_conditioning": true,
  "automatic_car": true,
  "has_getaround_connect": true,
  "has_speed_regulator": true,
  "winter_tires": true
}
```

La réponse attendue est un JSON contenant une clé `prediction` correspondant aux valeurs prédites.

Exemple de réponse :

```
{
  "prediction": 145.66041029414708,
  "detail": "Prédiction du tarif journalier (nul si aucun modèle)."
}
```

#### Page de documentation

Vous devez fournir aux utilisateurs une **documentation** décrivant votre API.

Cette documentation est accessible à l’URL `/docs` de mon site sur hugging face <https://pradelf-getaround-api.hf.space/docs>.

Cette documentation contient :

- un titre de niveau h1 (le titre est libre) ;
- une description de chaque endpoint disponible, précisant le nom de l’endpoint, la méthode HTTP, les entrées requises et les sorties attendues (des exemples peuvent être fournis).

#### Mise en production en ligne

Le déploiement est **hébergé avec son API en ligne** chez [Hugging Face](https://huggingface.co/spaces),

#### Partage du code

Pour permettre l’évaluation, le code est versionné dans un dépôt [GitHub](https://github.com/pradelf/getaround)avec ce fichier `README.md` décrivant brièvement le projet, la procédure d’installation locale et l’URL de la version en ligne.

### Livrables 📬

Pour valider ce projet, vous devrez fournir :

- un **dashboard** déployé en production (accessible via une page web) ;
- l’**ensemble du code source** dans un **dépôt GitHub**, dont vous fournirez l’URL ;
- une **API documentée et accessible en ligne** (Hugging Face ou autre) contenant au moins **un endpoint `/predict`** conforme aux spécifications ci-dessus. Il doit être possible d’interroger l’endpoint `/predict` via `curl` :

```shell
curl -X 'POST' \
  "https://pradelf-getaround-api.hf.space/predict" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "model_key": "Peugeot",
  "mileage": 10000,
  "engine_power": 130,
  "fuel": "petrol",
  "paint_color": "black",
  "car_type": "convertible",
  "private_parking_available": true,
  "has_gps": true,
  "has_air_conditioning": true,
  "automatic_car": true,
  "has_getaround_connect": true,
  "has_speed_regulator": true,
  "winter_tires": true
}'
```

Ou en Python :

```python
import requests

response = requests.post( "https://pradelf-getaround-api.hf.space/predict",
  {
  "model_key": "Peugeot",
  "mileage": 10000,
  "engine_power": 130,
  "fuel": "petrol",
  "paint_color": "black",
  "car_type": "convertible",
  "private_parking_available": true,
  "has_gps": true,
  "has_air_conditioning": true,
  "automatic_car": true,
  "has_getaround_connect": true,
  "has_speed_regulator": true,
  "winter_tires": true
})
print(response.json())
```

### Données

Pour les données, deux fichiers de données sont nécessaires et son placer dans le repertoire /data/raw:

- [Delay Analysis](https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_delay_analysis.xlsx) 👈 Analyse de données
- [Pricing Optimization](https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_pricing_project.csv) 👈 Machine Learning

Bon courage et bon code 👩‍💻
___

## Organisation du projet

### Structure du projet

Le projet est inclus dans ce dépôt et il a la structure de fichier suivante :

```
├── LICENSE            <- Licence open source ici MIT
├── Makefile           <- Makefile avec des commandes pratiques comme `make data` ou `make train`
├── README.md          <- README principal du projet à destination des développeurs
├── data
│   ├── external       <- Données provenant de sources tierces
│   ├── interim        <- Données intermédiaires ayant déjà subi des transformations
│   ├── processed      <- Jeux de données finaux et canoniques utilisés pour la modélisation
│   └── raw            <- Données brutes d’origine, immuables
│
├── docs               <- Projet mkdocs par défaut ; voir www.mkdocs.org pour plus de détails
│
├── models             <- Modèles entraînés et sérialisés, prédictions des modèles ou résumés
│
├── notebooks          <- Notebooks Jupyter. Convention de nommage : un numéro (pour l’ordre),
│                         les initiales de l’auteur, et une courte description séparée par des `-`,
│                         par exemple : `1.0-jqp-exploration-initiale-des-donnees`
│
├── pyproject.toml     <- Fichier de configuration du projet avec les métadonnées du package
│                         getaround et la configuration d’outils comme black
│
├── references         <- Dictionnaires de données, manuels et autres documents explicatifs
│
├── reports            <- Analyses générées (HTML, PDF, LaTeX, etc.)
│   └── figures        <- Graphiques et figures générés pour les rapports
│
├── requirements.txt   <- Fichier des dépendances pour reproduire l’environnement d’analyse,
│                         par exemple généré avec `pip freeze > requirements.txt`
│
├── setup.cfg          <- Fichier de configuration pour flake8
│
└── getaround          <- Code source utilisé dans ce projet pour la web app et l'api
```

--------

### Données

Les données du projet sont rangées dans le repertoire data/raw :

- [data/raw/get_around_delay_analysis.xlsx](./data/raw/get_around_delay_analysis.xlsx) : Données pour l'analyse des retards au format excel
- [data/raw/get_around_delay_analysis.csv](./data/raw/get_around_delay_analysis.csv) : Données pour l'analyse des retards au format csv
- [data/raw/get_around_pricing_project.csv](./data/raw/get_around_pricing_project.csv) : Données pour l'optimisation des retards

Comme les données sont de faible volume, je les ai placé dans le reprtoire data/raw du projet. Mais pour l'exercice, elles sont également rangées comme un dataset de Hugging Face dans un dépôt [Git Xet](https://huggingface.co/docs/hub/xet/index) : [getaround-dataset](https://huggingface.co/datasets/pradelf/getaround-dataset)

### Point d'entrée

Le point d'entrée pour l'analyse du projet est le notebook : [01-Getaround_analysis_FR.ipynb](./notebooks/01-Getaround_analysis_FR.ipynb).
Le point d'entrée pour l'EDA du projet est le notebook : [02_Getaround_eda.ipynb](./notebooks/02_Getaround_eda.ipynb).
Le point d'entrée pour l'entraînement des modèles est le script : [03_Getaround_model_training.ipynb](./getaround/notebooks/03_Getaround_model_training.ipynb).
Le point d'entrée pour la prédiction des prix de location est le projet Docker dans le repertoire : [getaround/api](./getaround/api).
La documentation de l'API est en ligne sur hugging face sous l'url : [https://pradelf-getaround-api.hf.space/docs](https://pradelf-getaround-api.hf.space/docs)
Le point d'entrée pour l'Application wede calcul de prix est : [https://pradelf-getaround-web.hf.space](https://pradelf-getaround-web.hf.space)
