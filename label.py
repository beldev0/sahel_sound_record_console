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
    data = []
    for element in catalogue :
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

# Part Houéfa

def ajouter_log(titre_album):
    """
    Ajoute une ligne dans historique.log a chaque modifications du catalogue
    """
    date_heure = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    ligne = f"{date_heure} - INFOS : L'album {titre_album} a été enregistré.\n"
    
    with open("historique.log", "a", encoding="utf-8") as f:
        f.write(ligne)


def ajouter_album(album, artiste_id, chemin="catalogue.json"):
    """
    Ajoute un album à un artiste
    """

    # 1. Charger le catalogue
    catalogue = charger_catalogue(chemin)

    # 2. Trouver l'artiste avec filter()
    artistes_trouves = list(filter(lambda a: a["id"] == artiste_id, catalogue))

    artiste = artistes_trouves[0]

    # 3. Ajouter l'album
    artiste["albums"].append(album)

    # 4. Ajouter log
    ajouter_log(album["titre"])

    # 5. Sauvegarder
    sauvegarder_catalogue(catalogue, chemin)

    # 6. Message
    print(f"{album['titre']} a été enregistré")

# Part Ola

def afficher_resume_artiste(data) : 
    if len(data) == 0:
        print('Aucun artiste a affiché')
    for element in data :
        print("="*40)
        print(f"🎤 Artiste : {element.get('nom')}")
        print(f"-"*40)
        print(f"ID     : {element.get('id')}")
        print(f"GENRE  : {element.get('genre')}")
        print(f"PAYS   : {element.get('pays')}")
        print(f"ALBUMS : {element.get('nbre_albums')}\n")
    
    print()
        


def rechercher_artiste(catalogue, critere, valeur) :
    """Recherche des artistes par nom ou par genre."""
    resultats = []
    valeur = valeur.strip().lower()
    for artiste in catalogue:
        if critere == 'nom' and valeur in artiste.get('nom').lower():
            resultats.append(artiste)
        elif critere == 'genre' and valeur in artiste.get('genre').lower():
            resultats.append(artiste)
    return resultats


def rechercher_artiste_par_id(catalogue, id) :
    found = list(filter(lambda element:element['id']==id, catalogue))
    if found :
        return found[0]
    return None

def artiste_en_detail(artiste) :
    print("="*40)
    print(f"🎤 Artiste : {artiste.get('nom')}")
    print(f"-"*40)
    print(f"ID     : {artiste.get('id')}")
    print(f"GENRE  : {artiste.get('genre')}")
    print(f"PAYS   : {artiste.get('pays')}")
    print(f"ALBUMS : {len(artiste.get('albums'))}\n")
    print(f"-"*40)
    print()
    albums = artiste.get('albums')
    print("📀 Albums : \n")
    for i, album in enumerate(albums) :
        print(f"    {i+1}) {album.get('titre')}")
        print(f"       Année   : {album.get('annee')} ")
        print(f"       Streams : {album.get('streams')}")
        print()

    print()