import json
import sys

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