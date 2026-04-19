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
    return (df_albums
    .groupby("nom")["streams"]
    .sum()
    .sort_values(ascending=False)
    .head(5))

def stream_mean() :
    df_albums = load_dataframe()
    return (df_albums
    .groupby("genre")["streams"]
    .mean()
    .sort_values(ascending=False)
)