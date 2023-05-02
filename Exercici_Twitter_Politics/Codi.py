import json
import pandas as pd
import glob
from tqdm import tqdm


#fent servir el mòdul glob llegim els noms de tots els arxius json de la carpeta api_responses i posem tots aquests noms en una llista anomenada files
files = glob.glob('api_responses/*.json')

#Aqui creem 3 llistes que farem servir més tard
llista_temes = []
llista_dfs = []
llista_tuples = []

#Creem un loop per llegir tots els elements de la llista de noms de Json, fem servir el mòdul tqdm per saber quan trigarà el procés
for file in tqdm(files):
    with open(file, encoding="utf-8") as jsonfile:
        dades = json.load(jsonfile)

        #Un cop llegit el json assignem a la llista tweets tots els elements dins de dades on cada element d'aquesta llista es un tuit individual
        tweets = dades["data"]

        #en aquest seguent loop accedim a cada un dels tuits i extraiem les variables de author_id, text, i la data de captura
        for tweet in tweets:
            author_id = tweet["author_id"]
            text = tweet["text"]
            captured = tweet["created_at"]

            #per la variable de hashtag emprem un try degut a que no tots els tuits tenen hashtags, per tant volem que només extregui el tag en cas de que existeixi
            try:
                tema = tweet["entities"]["hashtags"]
                for hashtag in tema:
                    h = hashtag["tag"]
                    llista_temes.append(h)
            except KeyError:
                pass

            #dins de cada tuit entrem a users per agafar les dades dels usuaris de cada tuit, per saber que estem en el tuit corresponent fem un if per igualar el author_id i el username
            users = dades["includes"]["users"]
            for user in users:
                if user["id"] == author_id:
                    #i extraiem el user_name, numero de followers i el numero de tuits
                    user_name = user["username"]
                    followers = user["public_metrics"]["followers_count"]
                    tweet_count = user["public_metrics"]["tweet_count"]

            #creem el dataframe amb les columnes corresponents de les dades extretes.
            df = pd.DataFrame({
                "user_id": author_id,
                "user_name": user_name,
                "followers": followers,
                "text": text,
                "data": captured,
            }, index=[0])
            #afegim aquest dataframe a la llista anteriorment creada
            llista_dfs.append(df)
            #al igual que hem fet amb els hashtags extraiem les mencions i els mencionats posant els dos valors en una tupla, que afegirem a una llista.
            try:
                llista_mencions = tweet["entities"]["mentions"]
                for u in llista_mencions:
                    mencionat = u["username"]
                    tup = (user_name, mencionat)
                    llista_tuples.append(tup)
            except KeyError:
                pass

#creem el csv de les mencions 
df = pd.DataFrame(llista_tuples, columns=["source","target"])
df.to_csv("mencions.csv", index=False)

#creem el csv dels valors extrets
df_final = pd.concat(llista_dfs)
df_final.to_csv("finalbo.csv", index=False)

#en el cas dels hashtags primer contem quans cops es repeteixen cada hashtag
unics = set(llista_temes)
llista_neta = []
for u in unics:
    q = llista_temes.count(u)
    t = (u, q)
    llista_neta.append(t)

#i finalment creem el csv dels temes amb els hashtags
df_2 = pd.DataFrame(llista_neta, columns=["hashtag","repetitions"])
df_2.to_csv("hasahtags_repetits.csv", index=False)
