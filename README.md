# SahelSound Records avec 
> Extension choisie : Journalisation des modifications.

## Membres du groupe

1. ATIKE Isatou    **(Consulter le catalogue)**
2. GBENOU Ezéchias **(Ajouter un artiste, Logs artiste)**
3. VIANOU Houéfa   **(Ajouter un album à un artiste existant, Logs album)**
4. ZANNOU Charbel  **(main.py, Statistiques et rapport)**

---

## Description du projet

Ce projet consiste à développer une application console permettant de gérer le catalogue d’un label musical africain fictif appelé **SahelSound Records**.

L’application permet de gérer les artistes, leurs albums, ainsi que de produire quelques statistiques.

Les données sont enregistrées dans un fichier `catalogue.json`.

---

## Fonctionnalités

### 1. Consulter le catalogue

* Afficher tous les artistes (nom, genre, pays, nombre d’albums)
* Rechercher un artiste par nom
* Rechercher un artiste par genre
* Afficher le détail d’un artiste (liste des albums avec le nombre de streams)

---

### 2. Ajouter un artiste

* Saisir les informations de l’artiste au clavier
* Vérifier que l’identifiant n’existe pas déjà
* Enregistrer les données dans `catalogue.json`

---

### 3. Ajouter un album à un artiste existant

* Rechercher l’artiste par son identifiant
* Saisir les informations de l’album (titre, année, streams)
* Mettre à jour le fichier `catalogue.json`

---

### 4. Statistiques et rapport

* Top 5 des artistes selon le nombre total de streams
* Moyenne des streams par genre musical
* Nombre d’albums sortis par année
* Export du rapport dans un fichier `rapport.csv`

---
