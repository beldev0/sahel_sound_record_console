import pandas as pd

def load_dataframe() :

    df = pd.read_json("catalogue.json")

    df_albums = df.explode("albums")
    df_albums["titre"] = df_albums["albums"].apply(lambda x: x["titre"])
    df_albums["annee"] = df_albums["albums"].apply(lambda x: x["annee"])
    df_albums["streams"] = df_albums["albums"].apply(lambda x: x["streams"])

    df_albums = df_albums.drop(columns=["albums"])
    return df_albums


def get_top5() :
    df_albums = load_dataframe()
    resultat = (df_albums
    .groupby("nom")["streams"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
    .head(5))
    resultat.columns = ['Artiste', 'Stream']
    return resultat

def stream_mean() :
    df_albums = load_dataframe()
    resultat  = (df_albums
    .groupby("genre")["streams"]
    .mean()
    .sort_values(ascending=False)
    .reset_index())
    resultat.columns = ['Genre', 'Stream']
    return resultat

def album_per_year() :
    df_albums = load_dataframe()
    resultat =  (
    df_albums
    .groupby("annee")
    .size()
    .sort_index()
    .reset_index()
    )

    resultat.columns = ['Annee', "Nombre d'album"]
    return resultat

def export_csv_rapport() :
    # Convertir en DataFrame pour export
    top5_df = get_top5().reset_index()
    # top5_df.columns = ["Artiste", "Total_Streams"]

    moyenne_genre_df = stream_mean().reset_index()
    # moyenne_genre_df.columns = ["Genre", "Moyenne_Streams"]

    albums_par_annee_df = album_per_year().reset_index()
    # albums_par_annee_df.columns = ["Annee", "Nombre_Albums"]

    # Sauvegarde dans un seul fichier CSV (sections séparées)
    with open("rapport.csv", "w") as f:
        f.write("TOP 5 ARTISTES\n")
        top5_df.to_csv(f, index=False)
        
        f.write("\n\nMOYENNE STREAMS PAR GENRE\n")
        moyenne_genre_df.to_csv(f, index=False)
        
        f.write("\n\nNOMBRE D'ALBUMS PAR ANNEE\n")
        albums_par_annee_df.to_csv(f, index=False)

        print("Rapport exporté dans rapport.csv")