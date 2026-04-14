import json
import sys
from datetime import datetime

def charger_catalogue(chemin) :
    """ Charge et retourne le JSON depuis le fichier """

    try :
        with open(chemin, 'r') as file :
            data = json.load(file)
            return data
    except FileNotFoundError:
        sys.exit("Le fichier catalogue n'existe pas.")


def sauvegarder_catalogue(data, chemin) :
    """ Écrit les données dans le fichier JSON """

    try :
        with open(chemin, 'w') as file:
            json.dump(data, file, indent=4)
            print('Catalogue mise à jour !')
    except FileNotFoundError:
        sys.exit("Le fichier catalogue n'existe pas.")

def lister_artistes(catalogue) :
    """ Retourne la liste des artistes avec infos résumés """
    
    catalogue_data  = charger_catalogue(catalogue)
    data = []
    for element in catalogue_data :
        data.append(
            {
                "id" :          element['id'],
                "nom" :         element['nom'],
                "genre" :       element['genre'], 
                "pays" :        element['pays'],
                "nbre_albums" : len(element['albums'])
            }
        )
    
    return data

def ajouter_artiste(new_artist):

    # Ecris les données d'un nouveau artiste dans le fihier json
    try:
        with open("catalogue.json", "r") as f:
            donnees = json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        donnees= []

    donnees.append(new_artist)


    with open("catalogue.json", "w") as f:
        json.dump(donnees,f,indent=4)

    print(f"L'artiste {new_artist['id']} a été ajouté")
    ajouter_log(new_artist)


def ajouter_log(new_artist):
    #Mise à jour du fichier historique.log avec l'heure et date d'ajout d'un nouveau artiste
    with open("historique.log", "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Infos: L'artiste {new_artist['id']} a été ajouté\n")
