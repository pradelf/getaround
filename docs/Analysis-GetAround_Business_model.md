# Business model de Get Around

Voici un **résumé clair du business model de Getaround**, basé sur les pages web du site de [Get Around](https://fr.getaround.com/help/articles/1453c295ca9b#owners).

---

## 1. Principe général du business model

Getaround est une **plateforme de location de voitures entre particuliers (P2P)**.
Elle met en relation trois acteurs :

1. **Le propriétaire du véhicule**
2. **Le locataire**
3. **Getaround (la plateforme)**

Le modèle économique repose sur une **commission prélevée par la plateforme** et sur certains services associés (assurance, abonnement au boîtier Connect).

Le prix payé par le locataire se décompose en deux parties principales :

* **Prix de base de la location** (lié au véhicule)
* **Frais additionnels** (services et options)

---

## 2. Comment est calculé le prix de location

### 2.1 Prix de base

Le prix de base est déterminé à partir du **prix journalier fixé par le propriétaire**.

#### Étapes de calcul

1. **Définition du prix journalier**

   * Le propriétaire fixe un prix par jour.
   * Il peut utiliser :

     * un **prix manuel**
     * un **prix variable selon la demande**
     * un **prix intelligent dynamique**

2. **Addition des prix journaliers**

   * On additionne les prix correspondant aux dates de réservation.

3. **Application de réductions selon la durée**

| Durée      | Calcul                                  |
| ---------- | --------------------------------------- |
| 1 à 8 h    | première heure = 55% du prix journalier |
| 8,5 à 24 h | prix journalier complet                 |
| > 2 jours  | réduction progressive                   |

Ces réductions permettent d’aligner les prix sur ceux des loueurs professionnels.

---

### 2.2 Tarification dynamique

La plateforme propose deux mécanismes :

#### Prix variable

Le propriétaire adapte les prix selon la demande :

* faible (semaine hors vacances)
* moyenne (week-end)
* forte (vacances)
* très forte (week-end vacances)

Les recommandations sont basées sur les prix des véhicules similaires dans la zone.

#### Prix intelligents

Algorithme de pricing automatique basé sur :

* nombre de recherches
* taux de réservation local
* caractéristiques du véhicule
* saisonnalité

Ces prix peuvent augmenter les revenus jusqu’à ~20%.

---

## 3. Frais additionnels payés par le locataire

En plus du prix de base, le locataire paie plusieurs frais :

#### 1️⃣ Assurance et assistance

Obligatoire pour toutes les locations.

#### 2️⃣ Frais de service locataire

Commission de la plateforme.

#### 3️⃣ Options possibles

* assurance supplémentaire (réduction de franchise)
* packs kilomètres supplémentaires
* supplément jeune conducteur (<26 ans)

#### 4️⃣ Ajustements après location

Facturés après la location si nécessaire :

* kilomètres supplémentaires
* carburant manquant
* retard
* pénalités diverses

---

## 4. Comment est réparti le prix entre les acteurs

Le flux financier est le suivant.

### Étape 1 — paiement du locataire

Le locataire paie :

```
Prix total =
prix de base
+ assurance
+ frais de service locataire
+ options
```

---

### Étape 2 — revenu du propriétaire

Le propriétaire reçoit :

```
Revenu propriétaire =
prix de base
– commission Getaround (frais de service propriétaire)
+ ajustements fin de location
```

La commission est **un pourcentage fixe du prix de base**.

---

### Étape 3 — revenus de Getaround

Getaround gagne de l’argent via :

1️⃣ **commission sur la location**
2️⃣ **frais de service locataire**
3️⃣ **abonnement Connect (25 €/mois)** pour les voitures équipées du système d’ouverture à distance
4️⃣ **commissions sur certains frais (km supplémentaires, etc.)**

---

## 5. Exemple simplifié

Supposons :

* prix journalier : 50 €
* location : 2 jours
* réduction : 10 %

#### Calcul

Prix de base :

```
50 + 50 = 100 €
réduction 10 %
= 90 €
```

Frais locataire :

```
assurance : 15 €
service locataire : 10 €
```

Total payé par le locataire :

```
90 + 15 + 10 = 115 €
```

Répartition :

| Acteur       | Montant            |
| ------------ | ------------------ |
| Propriétaire | ~70–80 €           |
| Getaround    | commission + frais |
| Assurance    | part du prix       |

*(ordre de grandeur, dépend du pays et du véhicule)*

---

## 6. Résumé du modèle économique

Le modèle Getaround combine trois logiques :

**Marketplace P2P**

* mise en relation propriétaires / locataires

**Pricing algorithmique**

* optimisation des prix via data et saisonnalité

**Monétisation multi-sources**

* commission sur la location
* frais locataire
* abonnement technologique (Connect)

Ce modèle maximise :

* le **taux d’occupation des véhicules**
* les **revenus propriétaires**
* la **commission de la plateforme**
