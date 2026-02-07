# getaround

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-red?logo=mlflow)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-orange?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Live](https://img.shields.io/badge/Status-Live%20Demo-success)
![CCDS](https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter)

___

![snap](https://fr.getaround.com/packs/images/app/assets/images/shared/getaround-logo.245e368962541c3c.svg)

___

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

Vous devez fournir au minimum **un endpoint** `/predict`. L’URL complète pourrait par exemple être : `https://your-url.com/predict`.

Cet endpoint doit accepter des requêtes **POST** avec des données d’entrée au format JSON et retourner les prédictions correspondantes. On suppose que **les données d’entrée sont toujours correctement formatées** ; la gestion des erreurs est donc optionnelle.

Exemple d’entrée :

```
{
  "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8],
            [7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
}
```

La réponse attendue est un JSON contenant une clé `prediction` correspondant aux valeurs prédites.

Exemple de réponse :

```
{
  "prediction": [6, 6]
}
```

#### Page de documentation

Vous devez fournir aux utilisateurs une **documentation** décrivant votre API.

Cette documentation doit être accessible à l’URL `/docs` de votre site (par exemple : `https://your-url.com/docs`).

Cette documentation devra au minimum contenir :

- un titre de niveau h1 (le titre est libre) ;
- une description de chaque endpoint disponible, précisant le nom de l’endpoint, la méthode HTTP, les entrées requises et les sorties attendues (des exemples peuvent être fournis).

Vous êtes libre d’ajouter toute information pertinente et de styliser la page HTML comme vous le souhaitez.

#### Mise en production en ligne

Vous devez **héberger votre API en ligne**. Nous vous recommandons d’utiliser [Hugging Face](https://huggingface.co/spaces), qui est gratuit, mais vous pouvez choisir tout autre fournisseur d’hébergement.

### Aides 🦮

Pour vous aider à démarrer ce projet, voici quelques recommandations :

- prenez le temps de bien comprendre les données ;
- ne négligez pas la phase d’analyse de données, qui recèle de nombreux enseignements ;
- l’analyse de données devrait prendre entre 2 et 5 heures ;
- la partie Machine Learning devrait prendre entre 3 et 6 heures ;
- l’utilisation d’outils de gestion du cycle de vie des modèles (comme `mlflow`) n’est pas obligatoire mais fortement recommandée.

#### Partage du code

Afin de permettre l’évaluation, n’oubliez pas de partager votre code dans un dépôt [GitHub](https://github.com/). Vous pouvez y inclure un fichier `README.md` décrivant brièvement le projet, la procédure d’installation locale et l’URL de la version en ligne.

### Livrables 📬

Pour valider ce projet, vous devrez fournir :

- un **dashboard** déployé en production (accessible via une page web) ;
- l’**ensemble du code source** dans un **dépôt GitHub**, dont vous fournirez l’URL ;
- une **API documentée et accessible en ligne** (Hugging Face ou autre) contenant au moins **un endpoint `/predict`** conforme aux spécifications ci-dessus. Il doit être possible d’interroger l’endpoint `/predict` via `curl` :

```shell
curl -i -H "Content-Type: application/json" -X POST -d '{"input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]}' http://your-url/predict
```

Ou en Python :

```python
import requests

response = requests.post("https://your-url/predict", json={
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
})
print(response.json())
```

### Données

Deux fichiers de données sont nécessaires :

- [Delay Analysis](https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_delay_analysis.xlsx) 👈 Analyse de données
- [Pricing Optimization](https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_pricing_project.csv) 👈 Machine Learning

Bon courage et bon code 👩‍💻

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
└── getaround          <- Code source utilisé dans ce projet
    │
    ├── __init__.py             <- Déclare getaround comme un module Python
    │
    ├── config.py               <- Stockage des variables utiles et de la configuration
    │
    ├── dataset.py              <- Scripts pour télécharger ou générer les données
    │
    ├── features.py             <- Code de construction des features pour la modélisation
    │
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py          <- Code pour exécuter l’inférence avec des modèles entraînés
    │   └── train.py            <- Code d’entraînement des modèles
    │
    └── plots.py                <- Code pour créer des visualisations

```

--------

### Données

Les données du projet sont rangées dans le repertoire data/raw :

- [data/raw/get_around_delay_analysis.xlsx](./data/raw/get_around_delay_analysis.xlsx) : Données pour l'analyse des retards
- [data/raw/get_around_pricing_project.csv](./data/raw/get_around_pricing_project.csv) : Données pour l'optimisation des retards

### Point d'entrée

Le point d'entrée pour l'analyse du projet est le notebook : [01-Getaround_analysis_FR.ipynb](./notebooks/01-Getaround_analysis_FR.ipynb).
Le point d'entrée pour l'entraînement des modèles est le script : [train_model.py](./getaround/modeling/train.py).
Le point d'entrée pour les prédictions des modèles est le script : [predict_model.py](./getaround/modeling/predict.py).
Le point d'entrée pour l'API webservice des modèles est le script : [getaround_api.py](./getaround/api/getaround_api.py)
