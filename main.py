from label import *

menu_items = {
    1 : {
        "a" : "Afficher tous les artistes (nom, genre, pays, nombre d'albums)",
        "b" : "Rechercher un artiste par nom ou par genre",
        "c" : "Afficher le détail d'un artiste (liste de ses albums avec streams)"
    },

    2 : {
        "a" : "Saisir les informations de l'artiste au clavier",
        "b" : "Vérifier que l'identifiant n'existe pas déjà",
        "c" : "Sauvegarder immédiatement dans catalogue.json"
    },

    3 : {
        "a" : "Rechercher l'artiste par son identifiant",
        "b" : "Saisir les informations de l'album (titre, annee, streams)",
        "c" : "Mettre à jour catalogue.json"
    },

    4 : {
        "a" : "Top 5 des artistes par nombre total de streams",
        "b" : "Moyenne des streams par genre musical",
        "c" : "Nombre d'albums sortis par annee (agregation)",
        "d" : "Exporter le rapport complet dans rapport.csv"
    }
}

items = [
    "Consulter le catalogue",
    "Ajouter un artiste",
    "Ajouter un album à un artiste existant",
    "Statistiques et rapport",
    "Quitter le programme"
]

CATALOGUE = 'catalogue.json'

new_album = None
artist_id = None
new_artist = None

def loop_over_options(elements):
    for key, value in elements.items() :
        print(f"{key}. {value}")
    choice = ""
    while not choice.lower() in elements.keys():
        choice = input("\nQue souhaitez vous faire ?\n")

    print()
    return choice.lower()

def get_string_value(entree, field):
    text = ''
    while not len(text) != 0 :
        print(f"{entree}")
        text = input("")
        if len(text) == 0 :
            print(f"{field} ne peut pas être vide")

    return text

while True :
    for index, value in enumerate(items) :
        print(f"{index + 1}. {value}")

    choice = ''

    while not choice.isnumeric() or int(choice) < 1 or int(choice) > len(items) :
        choice = input("\nQue voulez vous faire ?\n")
    
    choice = int(choice)
    print()

    if choice != 5 :
        elements = menu_items[choice]
        if choice == 1 :
            choice = loop_over_options(elements)
            print(f"=== {elements[choice]} ===")

            if choice == "a":
                catalogue = charger_catalogue(CATALOGUE)
                catalogue_resume = lister_artistes(catalogue)
                afficher_resume_artiste(catalogue_resume)
            elif choice == "b":
                critere = ''
                valeur = ''
                catalogue = charger_catalogue(CATALOGUE)

                while critere.lower() not in ['nom', 'genre'] :
                    critere = input("Quelle est le critère de recherche (nom/genre) ? ")
                    if critere not in ['nom', 'genre'] :
                        print("Vous devre choisir entre (nom/genre)")
                
                while not len(valeur) != 0 :
                    valeur = input("Entrer la valeur du critère de recherche :")
                    if len(value) == 0 :
                        print("La valeur ne peut pas être vide")

                
                artiste_trouve = rechercher_artiste(catalogue, critere, valeur)
                artiste_resume = lister_artistes(artiste_trouve)
                afficher_resume_artiste(artiste_resume)
                
            else :
                id = ''
                while not len(id) != 0 :
                    id = input("Entrer l'ID de l'artiste : ")
                    if len(id) == 0 :
                        print("L'ID ne peut pas être vide")
                
                catalogue = charger_catalogue(CATALOGUE)
                artiste_trouve = rechercher_artiste_par_id(catalogue, id)
                if artiste_trouve :
                    artiste_en_detail(artiste_trouve)
                else :
                    print(f'Artiste {id} non trouvé')

        elif choice == 2 :
            choice = loop_over_options(elements)
            print(f"=== {elements[choice]} ===")

            if choice == 'a':
                id = get_string_value("Entrer l'ID de l'artiste", 'ID')
                nom = get_string_value("Entrer le nom de l'artiste", 'Nom')
                pays = get_string_value("Entrer le pays de l'artiste", "Pays")
                genre = get_string_value("Entrer le genre musical", "Genre")
                new_artist = {
                    'id':     id,
                    'nom':    nom,
                    'pays':   pays,
                    'genre':  genre,
                    'albums': []
                }
                print("Nouveau artiste crée")

            elif choice == 'b':
                id = get_string_value("Entrer l'ID de l'artiste", 'ID')
                # artiste = rechercher_artiste_par_id(id)
                # if artiste:
                #     print("L'ID existe déjà")
                # print("ID pas encore existant")
            
            else :
                if new_artist :
                    # ajouter_artiste(new_artist) 
                    new_artist = None
                else :
                    print("Il n'y a pas d'artiste en instance")

        elif choice == 3 :
            choice = loop_over_options(elements)
            print(f"=== {elements[choice]} ===")
            
            if choice == 'a' :
                catalogue = charger_catalogue(CATALOGUE)
                id = get_string_value("Entrer l'ID de l'artiste", 'ID')
                artiste = rechercher_artiste_par_id(catalogue,id)
                if artiste:
                    artiste_en_detail(artiste)
                    artist_id = id
                else :
                    print("Ce artiste n'existe pas.")

            elif choice == 'b' :
                titre = get_string_value("Entrer le titre de l'album",'Titre')
                annee = ''
                streams = ''
                while not annee.isnumeric() or int(annee) < 0 or int(annee) > 2026 :
                    annee = input("Entrer l'année de l'album : ")
                    if not annee.isnumeric() or int(annee) < 0 or int(annee) > 2026 :
                        print(f"{annee} n'est pas une année valide")
                annee = int(annee)

                while not streams.isnumeric() or int(streams) < 0 :
                    streams = input("Entrer le nombre de stream : ")
                    if not streams.isnumeric() or int(streams) < 0:
                        print(f"{streams} n'est pas un nombre valide")
                streams = int(streams)

                new_album = {
                    'titre'   : titre,
                    'annee'   : annee,
                    'streams' : streams
                }
                print('Nouveau album crée en mémoire')
            else :
                if new_album and artist_id:
                    ajouter_album(new_album, artist_id, chemin=CATALOGUE)
                    new_album = None
                    artist_id = None
                else :
                    if not artist_id :
                        print('Aucun artiste selectionné')
                    if not new_album :
                        print("Aucun album en instance.")

        else :     
            choice = loop_over_options(elements)
            print(f"=== {elements[choice]} ===")
            if choice == 'a' :
                pass
            elif choice == 'b' :
                pass
            elif choice == 'c' :
                pass
            else :
                pass
    else :
        break
   

print("FIN DU PROGRAMME")