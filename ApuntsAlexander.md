# ApuntsPython
### Sessió 2 (21/02/2023)

Per escriure variables en prints sense haber d'estar escrivint comes:
```python
hola= "soc Alexander the Great"
print(f L'últim missatge del mort va ser {hola})
```

Exemple de codi de com interactuar amb llistes de forma bàsiques per buscar elements concrets

```python
Llista_noms = ["miquel","alex"]

for noms in Llista_noms:
	if nom == "alex":
		print(nom)
	else:
		print(nom+"no es l'alex")
	
```

Si volem treballar de forma similar però aquest cop amb valors numèrics farem servir la sintaxis seguent:
```python
llista=[1,2,3,5,7,8,12,15]
for n in llista:
	if n < 6:
		print(f"el numero {n} és inferior a 6")
	else:
		print(f"el numero {n} no és inferior a 6")
```

Això ens servirà sempre que volguem comprobar només una condició, bàsicament una comprovació booleana, en cas de que hi hagi més condicions podem seguir amb un "elif"
```python
llista=[1,2,3,5,7,8,12,15]
for n in llista:
	if n < 6:
		print(f"el numero {n} és inferior a 6")
	elif n < 2:
		print(f"el numero es inferior a 6 y superior a 2")
	else:
		print(f"el numero {n} no és inferior a 6 ni superior a 2")
	
```

Per comprovar la llargada d'una llista ho podem fer amb la funció "len"

```python
llista =["hola","caca"]
llargada= len(llista)
print(llargada)
```

Exercici 1 (treballar amb prints amb f)
```python
var="esto no es un ejercicio"  
print(var)  
nota=9.25  
assign="escenarios y arquitectura 3D"  
print(f"En la asignatura {assign} he obtenido un {nota}")  
nota=nota+2  
frase= f"En la asignatura {assign} he obtenido un {nota}"  
print(frase)
```

Exercici2 (aprendre la funció "zip", que permet aparellar elements de dues llistes)
```python
notas =["5","7","6","4","8","2"]  
alumnos =["jaume","carla","pere","adrià","rafael","agnès"]  
  
for n in notas:  
    nota_num = int(n)+1  
for nota,nom in zip(notas,alumnos):  
    nota_final= int(nota)+1  
    print(f"{nom} ha obtenido un {nota_final}")
```

A continuació veurem una funció per trobar la posició que ocupa en una llista una variable determinada 

```python
llista = ["alex", "miki","marpei","david"]
nom="alex"

if nom in llista:
	print("si")
	posicio = llista.index(nom)
	print(posicio)
else:
	print("no")
```

Hi ha una altre funció nativa per eliminar valors duplicats 

```python
llista=["hola","caca","davidllopfortuny","hola"]
valors_unics = set(llista)
```

Si volem comprovar la llargada de la llista sense duplicats:

```python
print(len(set(llista)))
```

Exercici 3:

```python
llista =["david","dani","marta","jaume","adria","carla","joan","pere","carla","pere","adria","quico","pere","joan","agustí","adria","joan","adria","siscu","carles","dani","carla"]  
var=len(set(llista))  
llista2 =[]  
print(f"el numero de personas que han asistido a las puertas abiertas es de {var}")  
for nom in llista:  
    if llista.count(nom) > 2:  
        if nom not in llista2:  
            llista2.append(nom)  
for i in llista2:  
    print(i)  
recurrentes = len(llista2)  
percentatge = recurrentes/var*100  
print(percentatge)
```

Hi ha una altre manera més eficient en quan a recursos:

```python
contador=0
for nom in llista:
	var=llista.count(nom)
	if var > 2:
		contador = contador + 1
print(contador)
```

Exercici 4:

```python
notes = ["5","3","7","8","9.5","4","6,2"]  
alumnes = ["adria","agnès","josep","rafa","cristina","Gemma","Eduard"]  
mitja = 0  
for nota,alum in zip(notes,alumnes):  
    nota = float(nota.replace(",","."))  
    mitja = mitja+nota  
    print(f"El alumno/a {alum} ha obtenido un {nota}")  
print(f"la nota media de la clase es {round(mitja/len(notes),2)}")  
alta = 0  
for nota,alum in zip(notes,alumnes):  
    nota = float(nota.replace(",","."))  
    if nota > alta:  
        alta = nota  
pos= notes.index(str(alta))  
alumni=alumnes[pos]  
print(f"El alumno con la nota mas alta es {alumni} con un {alta}")  
baixa = 10  
for nota,alum in zip(notes,alumnes):  
    nota = float(nota.replace(",","."))  
    if nota < baixa:  
        baixa = nota  
baixa=int(baixa)  
pos= notes.index(str(baixa))  
alumni=alumnes[pos]  
print(f"El alumno con la nota mas baja es {alumni} con un {baixa}")
```

També podem trobar la nota i màxima amb les funcions max() i min(), de fet es molt més eficient.

## SESSIÓ 3 28/02/2023

Introduim les tuples per agrupar 2 valors relacionats dins d'una mateixa variable

```python
llista_1 = [6,9]  
llista_2 = ["josep","cristina"]  
llista_final = []  
for nota,nom in zip(llista_1,llista_2):  
    conjunt = (nota,nom)  
    llista_final.append(conjunt)  
for t in llista_final:  
    nota = t[0]  
    nom = t[1]  
    print(nota,nom)
```

### Pandas

Exercici de com linkar dos valors de dues llistes diferents per a tenir només un valor string amb nom i cognom junt. Convertir 2 llistes en 1
```python
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
noms =[]  
for nom,cog in zip(alumnes,cognoms):  
    junt =nom+ " " +cog  
    noms.append(junt)  
print(noms)
```

juntant una tercera llista

```python
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
noms =[]  
llista_de_tuples = []  
for nom,cog,nota in zip(alumnes,cognoms,notes):  
    junt = f"{nom} {cog}"  
    tot = (junt, nota)  
    llista_de_tuples.append(tot)  
print(llista_de_tuples)
```

Ara treballarem amb operacions matemàtiques i un if

```python
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
noms =[]  
llista_de_tuples = []  
for nom,cog,nota in zip(alumnes,cognoms,notes):  
    junt = f"{nom} {cog}"  
    tot = (junt, nota)  
    llista_de_tuples.append(tot)  
print(llista_de_tuples)  
  
for persona in llista_de_tuples:  
    nota = persona[1]  
    if nota < 10:  
        nota=nota+1  
    nova_persona = (persona[0], nota)  
    print(nova_persona)
```

Exercici seguent: **Tarea 4:** Añadir un tercer elemento a la tupla siguiendo este criterio:  
  
- Si la nota final es inferior a 5, añadir el texto "suspendido".  
- Si la nota se encuentra entre 5 y 6 (ambos incluídos), añadir el texto "aprobado".  
- Si la nota es superior a 6, e inferior a 7, añadir el texto "bien".  
- Si la nota es igual o superior a 7, añadir el texto "notable".  
- Si la nota supera el 9, añadir el texto "Excelente".  
- Si la nota equivale a un 10, añadir el texto "matrícula de honor".

```python
    llista_nova.append(nova_persona)  
llista_definitiva = []  
for rating in llista_nova:  
    nota = rating[1]  
    quali = "hola"  
    if nota < 5:  
        quali="suspès"  
    elif nota >=5 and nota <=6:  
        quali="aprobado"  
    elif nota >6 and nota <7:  
        quali="bien"  
    elif nota >=7 and nota <9:  
        quali="notable"  
    elif nota >=9 and nota <10:  
        quali="excelente"  
    elif nota == 10:  
        quali="matricula de honor"  
    tupla_nova =(rating[0],nota,quali)  
    llista_definitiva.append(tupla_nova)  
print(llista_definitiva)
```

### Treballar amb arxius JSON

```python
import pandas as pd

df = pd.DataFrame({
	"data":"hola",
},index)
```

```python
import json  
  
f = open('medidas.json') #carregar l'arxiu  
data=json.load(f) #transformar en diccionaris  
  
for d in data: #iterem sobre les dades  
    print(f'{d["fecha"]} {d["temperatura"]}')

print(len(data))
```

Arreglos i creació d'arxiu csv amb correcció de decimal

```python
import json  
  
import pandas as pd  
  
f = open('medidas.json') #carregar l'arxiu  
data=json.load(f) #transformar en diccionaris  
  
llista_dades = []  
  
for d in data:  
    temp = d["temperatura"]  
    pres = d["presion"]  
    date = d["fecha"]  
    tupla=(temp,pres,date)  
    llista_dades.append(tupla)  
  
df = pd.DataFrame(llista_dades, columns=["temp","pres","data"])  
print(df)  
df.to_csv("temperatures.csv",index=False, decimal=",")
```
## Exercici 2 Pandas


1)
```python
import pandas as pd  
  
df = pd.read_csv(r'C:\Users\Aleksander\Desktop\dataset_youtube.csv')  
print(df)
```

2)
El numero de files és 19128 i el numero de columnes és 25

```python
import pandas as pd  
  
df = pd.read_csv(r'C:\Users\Aleksander\Desktop\dataset_youtube.csv')  
  
files_total = len(df.axes[0])  
columnes_total = len(df.axes[1])  
  
print(f"Numero de files {files_total}")  
print(f"Numero de columnes {columnes_total}")
```

3)
Fem servir el recurs utilitzat en el apartat anterior.

```python
import pandas as pd  
  
df = pd.read_csv(r'C:\Users\Aleksander\Desktop\dataset_youtube.csv')  
  
files_total = len(df.axes[0])  
columnes_total = len(df.axes[1])  
  
Columnes = []  
  
for columnes in df.axes[1]:  
    Columnes.append(columnes)  
  
print(Columnes)
```

4)
Amb el seguent codi podem veure quines columnes contenen valors nuls i quants
```python
import pandas as pd  
  
df = pd.read_csv(r'C:\Users\Aleksander\Desktop\dataset_youtube.csv')  
  
nuls = df.isnull().sum()  
  
print(nuls)
```

Amb això podem observar com la columna "defaultlenguage" i "dislikecount" tenen tots els valors nuls, per tant aquestes dues columnes les hem d'eliminar. La columna "defaultAudioLenguage" té més de 16.000 valors nuls, per tant tampoc ens serveix. Thumbnailres té més de 1500 valors nuls pero aquesta es una columna que no ens interessa igualment. En canvi la columna de licensed content té més de 3000 nuls però si ens interessa. A la vegada també hi ha altres columnes amb un nombre de columnes molt reduit. Pero abans de netejar aquestes columnes decidirem quins columnes ens interessa mantenir. Així no fem esforços en va.

Tot i això mirant la totalitat de l'exercici s'ha vist que les seguentes columnes no interessen, i per tant es procedeix a eliminar-les:

position  
publishedAt  
publishedAtSQL  
VideoDescription  
tags  
videocategoryLabel  
duration  
definition  
caption  
defaultLanguage  
defaultAudioLanguage  
thumbnail_maxres  
licensedContent  
dislikecount  
favoritecount

i alguns més

```python
import pandas as pd  
  
df = pd.read_csv(r'C:\Users\Aleksander\Desktop\dataset_youtube.csv')  
  
df.drop('position', inplace=True, axis=1)  
df.drop('publishedAt', inplace=True, axis=1)  
df.drop('publishedAtSQL', inplace=True, axis=1)  
df.drop('videoDescription', inplace=True, axis=1)  
df.drop('tags', inplace=True, axis=1)  
df.drop('videoCategoryId', inplace=True, axis=1)  
df.drop('videoCategoryLabel', inplace=True, axis=1)  
df.drop('duration', inplace=True, axis=1)  
df.drop('durationSec', inplace=True, axis=1)  
df.drop('dimension', inplace=True, axis=1)  
df.drop('definition', inplace=True, axis=1)  
df.drop('caption', inplace=True, axis=1)  
df.drop('defaultLanguage', inplace=True, axis=1)  
df.drop('thumbnail_maxres', inplace=True, axis=1)  
df.drop('licensedContent', inplace=True, axis=1)  
df.drop('dislikeCount', inplace=True, axis=1)  
df.drop('favoriteCount', inplace=True, axis=1)  
df.drop('defaultLAudioLanguage', inplace=True, axis=1)  
  
hola = df.isnull().sum()  
print(hola)
```

d'aquesta neteja ens queda el seguent:

channelId        0
channelTitle     0
videoId          0
videoTitle       0
viewCount        0
likeCount        5
commentCount    14

Habent de netejar el "likeCount" i el "commentCount". Al ser tant poques columnes s'ha optat per borrar directament les files on es troben els nuls.

Afegint això al final ja tenim tota la taula neta

```python
df_net = df.dropna(how= 'any')  
  
hola = df_net.isnull().sum()  
print(hola)
```

channelId       0
channelTitle    0
videoId         0
videoTitle      0
viewCount       0
likeCount       0
commentCount    0

6)

```python
num_videos = df['channelId'].value_counts().rename('TotalVideos')  
df_net = df_net.join(num_videos, on="channelId")  
for i in df_net['channelTitle']:  
    if i == i:  
        break  
for s in df_net['channelTitle']:  
    if s != i:  
        if s == s:  
            break  
  
p = df_net.loc[df_net["channelTitle"] == i, "TotalVideos"].values[-1]  
o = df_net.loc[df_net["channelTitle"] == s, "TotalVideos"].values[-1]  
  
print(f'El numero de videos del canal {i} és {p}')  
print(f'El numero de videos del canal {s} és {o}')
```

7)
mitjana de les visites, comentaris i likes

```python
sumavisitas1 = 0  
iteracion = 0  
for j in df_net['channelTitle']:  
    if j == i:  
        sumavisitas1 = sumavisitas1 + df_net['viewCount'][iteracion]  
averagevisitas1= sumavisitas1/p  
sumavisitas2 = 0  
for y in df_net['channelTitle']:  
    if y == s:  
        sumavisitas2 = sumavisitas2 + df_net['viewCount'][iteracion]  
averagevisitas2= sumavisitas2/o  
  
sumacomentaris1 = 0  
for j in df_net['channelTitle']:  
    if j == i:  
        sumacomentaris1 = sumacomentaris1 + df_net['commentCount'][iteracion]  
averagecomentaris1= sumacomentaris1/p  
sumacomentaris2 = 0  
for y in df_net['channelTitle']:  
    if y == s:  
        sumacomentaris2 = sumacomentaris2 + df_net['commentCount'][iteracion]  
averagecomentaris2= sumacomentaris2/o  
  
sumalikes1 = 0  
for j in df_net['channelTitle']:  
    if j == i:  
        sumalikes1 = sumalikes1 + df_net['likeCount'][iteracion]  
averagelikes1= sumalikes1/p  
sumalikes2 = 0  
for y in df_net['channelTitle']:  
    if y == s:  
        sumalikes2 = sumalikes2 + df_net['likeCount'][iteracion]  
averagelikes2= sumalikes2/o  
  
print(f"El canal {i} té de mitjana {round(averagevisitas1,2)} visites, {round(averagecomentaris1,2)} comentaris i {round(averagelikes1,2)} likes")  
print(f"El canal {s} té de mitjana {round(averagevisitas2,2)} visites, {round(averagecomentaris2,2)} comentaris i {round(averagelikes2,2)} likes")
```

RESULTAT :
El canal NPR Music té de mitjana 2004.13 visites, 11.0 comentaris i 147.94 likes
El canal KEXP té de mitjana 2003.21 visites, 10.99 comentaris i 147.87 likes

8)
Desviació de cada video respecte la seva mitjana:
```python
for m in df_net['channelTitle']:  
    ite = ite +1  
    if m == i:  
        desviacio = llist[ite]-averagevisitas1  
        print(desviacio)  
    else:  
        desviacio = llist[ite]-averagevisitas2  
        print(desviacio)
```

9)
Video amb màximes visites del canal 1:
```python
canal_lista = list(df_net['channelTitle'])  
title_lista = list(df_net['videoTitle'])  
video_lista = list(df_net['viewCount'])  
max1 = max(video_lista)  
index = video_lista.index(max1)  
titol = title_lista[index]  
canal = canal_lista[index]  
print(titol)  
print(canal)
```
resultat:
Dua Lipa: Tiny Desk (Home) Concert
NPR Music

Video amb màximes comentaris del canal:
```python
max2 = max(coment_lista)  
index2 = coment_lista.index(max2)  
titol2= title_lista[index2]  
canal2= canal_lista[index2]  
print(titol2)  
print(canal2)
```

resultat:
BTS: Tiny Desk (Home) Concert
NPR Music

# Exercici Classe Dataset Twitch
```python
import pandas as pd
import time

#Columnes en el dataset

inici = time.time()

df = pd.read_csv("feb-full-2023.csv", sep'\t',nrows=25, usecols=["captured_at","streamer_name","viewer_count","game_name","stream_title"])
#posant el nrows=2 fem que només es llegeixin les dues primers files del document. També hem posat que només llegeixi les seguents columnes. fent servir el usecols
stream_mes_vist = df["viewer_count"].idmax()
print(df["captured_at"].iloc[posicio],df["streamer_name"].iloc[posicio],df["stream_title"].iloc[posicio], df["viewer_count"].iloc[posicio])

final = time.time()

print(final-inici)
```

Que passa si volem crear un dataframe amb totes les dades d'un canal concret
```python
import pandas as pd
import time

#Columnes en el dataset

inici = time.time()

df = pd.read_csv("feb-full-2023.csv", sep'\t', usecols=["captured_at","streamer_name","viewer_count","game_name","stream_title"],)
#posant el nrows=2 fem que només es llegeixin les dues primers files del document. També hem posat que només llegeixi les seguents columnes. fent servir el usecols
stream_mes_vist = df["viewer_count"].idmax()
print(df["captured_at"].iloc[posicio],df["streamer_name"].iloc[posicio],df["stream_title"].iloc[posicio], df["viewer_count"].iloc[posicio])

dades_kings_league = df[df["streamer_name"] == "kingsleague"]
dades_kings_league.to_csv("kingsleague.csv",index=False)

final = time.time()

print(final-inici)
```
Introduim els chunks
```python
```python
import pandas as pd
import time

#Columnes en el dataset

inici = time.time()

df = pd.read_csv("feb-full-2023.csv", sep'\t', usecols=["captured_at","streamer_name","viewer_count","game_name","stream_title"],chunksize=1000000)
llista_kings_league = []
for chunk i df:
	dades_kings_league = chunk[chunk["streamer_name"] == "kingsleague"]
	llista_kings_league.append(dades_kings_league)

final_frame = pd_concat(llista_kings_league)

dades_kings_league.to_csv("kingsleague_v2.csv",index=False)
```

#Exercici Exemple API Spotipy

## Configuració inicial

```python
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials  
  
SPOTIPY_CLIENT_ID='e69a700cb0704a578b2df0a2c884e7a8'  
SPOTIPY_CLIENT_SECRET='da2ad366ad7b4b3c99b9b1d864f07744'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlists = sp.user_playlists('spotify')  
while playlists:  
    for i, playlist in enumerate(playlists['items']):  
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))  
    if playlists['next']:  
        playlists = sp.next(playlists)  
    else:  
        playlists = None
```

Codi per printar en pantalla tots els artistes dins una playlist

Hem de guardar primer el json per veure el que conté:
```python
playlist_id = "2BBr6zeDlnvGwTvEHME6IC"

query = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None)

with open("output_file.json", 'w', encoding='utf-8') as f:  
    json.dump(query, f, ensure_ascii=False, indent=4)
```

```python
playlist_id = "2BBr6zeDlnvGwTvEHME6IC"  
  
query = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None)  
  
for i in query['items']:  
    artists = i["track"]["artists"]  
    for artist in artists:  
        artist_name= artist["name"]  
        artist_id = artist["id"]  
        print(artist_name,artist_id)
```

Creació de dataset:

```python
import time  
import pandas as pd  
import spotipy  
import json  
from spotipy.oauth2 import SpotifyClientCredentials  
  
  
SPOTIPY_CLIENT_ID='e69a700cb0704a578b2df0a2c884e7a8'  
SPOTIPY_CLIENT_SECRET='da2ad366ad7b4b3c99b9b1d864f07744'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlist_id = "2BBr6zeDlnvGwTvEHME6IC"  
  
query = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None)  
  
relacions = []  
  
for i in query['items']:  
    artists = i["track"]["artists"]  
    for artist in artists:  
        source_artist_name= artist["name"]  
        source_artist_id = artist["id"]  
  
        related_artists = sp.artist_related_artists(source_artist_id)  
        time.sleep(0.2)  
        relacionats = related_artists['artists']  
        for l in relacionats:  
            related_artists_name = l["name"]  
            tupla = (source_artist_name, related_artists_name)  
            relacions.append(tupla)  
        print("estic dormint")  
        time.sleep(0.2)  
  
df = pd.DataFrame.from_records(relacions, columns=['source', 'target'])  
df.to_csv("dataset_spoti.csv", index=False)
```

# Exercici 2 entregable

```python
import json  
import pandas as pd  
import glob  
  
files = glob.glob('api_responses/*.json')  
  
llista_dfs = []  
  
for file in files:  
    with open(file,encoding="utf-8") as jsonfile:  
        dades = json.load(jsonfile)  
        tweets = dades["data"]  
  
        for tweet in tweets:  
            author_id = tweet["author_id"]  
            text = tweet["text"]  
  
            users = dades["includes"]["users"]  
            for user in users:  
                if user["id"] == author_id:  
                    user_name = user["username"]  
                    followers = user["public_metric"]["followers_count"]  
                    tweet_count = user["public_metric"]["tweet_count"]  
  
  
            df = df.DataFrame({  
                "user_id": author_id,  
                "user_name": user_name,  
                "followers": followers,  
                "text": text,  
            }, index=[0])  
            print(df)  
            llista_dfs.append(df)  
df_final = pd.concat(llista_dfs)  
df_final.to_csv("final.csv", index=False)
```
# Sessió 18/04

Fem servir el mòdul "glob" per concatenar la lectura de diferents datasets:

```python
import pandas as pd  
import glob  
  
datasets = glob.glob("datasets/twitch_*")  
  
  
llista_streamers = ['auronplay', 'illojuan']  
llista = []  
  
for data in datasets:  
    df = pd.read_csv(data, sep="\t")  
    for streamer in llista_streamers:  
        df.loc[df['streamer_name'] == streamer]  
        llista.append(df)  
  
df_final = pd.concat(llista)  
df_final.to_csv(f"{streamer}-dataset.csv", index=False)
```
#Exercici 15/04

```python
import pandas as pd  
  
"""Amb el seguent codi fem una lectura preliminar del csv per saber els noms de les columnes i quines hi ha"""  
df = pd.read_csv(r'feb_23.csv', nrows=25)  
  
Columnes=[]  
  
for columnes in df.axes[1]:  
Columnes.append(columnes)  
  
print(Columnes[0])
```

captured_at	 
streamer_name	
streamer_id,	  position	
viewer_count
game_name
game_id

```python
import pandas as pd  
  
df= pd.read_csv("feb_23.csv", sep='\t', usecols=["captured_at", "viewer_count"])  
  
viewers=df.groupby("captured_at")["viewer_count"].sum().tolist()  
hora=df["captured_at"].unique().tolist()  
  
  
data = {'captura': hora, 'viewers': viewers}  
  
junto = zip(data["viewers"],data["captura"])  
ex = []  
  
for i in junto:  
ex.append(i)  
  
  
df1 = pd.DataFrame(ex, columns=['viewers','captura'])  
print(df1)  
  
df1.to_csv('exercici1.csv')  
  
  
# Print the result DataFrame
```

```python
import pandas as pd  
  
  
chunksize = 20000  
df = pd.read_csv("feb_23.csv", sep='\t', usecols=["game_name", "viewer_count"], chunksize=chunksize)  
result = []  
result_count = []  
  
for chunk in df:  
viewers = chunk.groupby("game_name")["viewer_count"].sum().reset_index()  
counts = (chunk["game_name"].value_counts() / 4).reset_index()  
result.append(viewers)  
result_count.append(counts)  
  
result_count2 = pd.concat(result_count, axis=0, ignore_index=True)  
df = pd.concat(result, axis=0, ignore_index=True)  
  
result_unique = result_count2.drop_duplicates(subset='game_name').copy() # Make a copy of the subset of data  
  
# Groupby 'Name' and sum the values in the column 'Age', then merge with 'df_unique' on 'Name'  
result_unique = pd.merge(result_unique, df.groupby('game_name')['viewer_count'].sum().reset_index(), on='game_name')  
  
# Rename the summed column to 'Sum_Age'  
result_unique = result_unique.rename(columns={'hores_x': 'viewer_count', 'hores_y': 'viewer_count'})  
  
# Drop the original 'Age' column  
result_unique = result_unique.drop('viewer_count', axis=1)  
  
result_sorted = result_unique.sort_values('game_name')  
  
print(result_sorted)  
  
  
  
  
"""  
  
df_unique = df.drop_duplicates(subset='game_name').copy() # Make a copy of the subset of data  
  
# Groupby 'Name' and sum the values in the column 'Age', then merge with 'df_unique' on 'Name'  
df_unique = pd.merge(df_unique, df.groupby('game_name')['viewer_count'].sum().reset_index(), on='game_name')  
  
# Rename the summed column to 'Sum_Age'  
df_unique = df_unique.rename(columns={'viewer_count_x': 'viewer_count', 'viewer_count_y': 'viewer_count'})  
  
# Drop the original 'Age' column  
df_unique = df_unique.drop('viewer_count', axis=1)  
  
df_sorted = df_unique.sort_values('game_name')  
  
print(df_sorted)  
  
  
  
# Extraer la columna "viewer_count" como una lista  
viewer_count_list = df["viewer_count"].tolist()  
result_count2['viewers'] = viewer_count_list  
  
print(result_count2)  
result_count2.to_csv('exercici2.csv')"""
```

BUENO
```python
import pandas as pd  
  
  
chunksize = 20000  
df = pd.read_csv("feb_23.csv", sep='\t', usecols=["game_name", "viewer_count"], chunksize=chunksize)  
result = []  
result_count = []  
  
for chunk in df:  
viewers = chunk.groupby("game_name")["viewer_count"].sum().reset_index()  
counts = (chunk["game_name"].value_counts() / 4).reset_index()  
result.append(viewers)  
result_count.append(counts)  
  
result_count2 = pd.concat(result_count, axis=0, ignore_index=True)  
df = pd.concat(result, axis=0, ignore_index=True)  
  
df_sorted = df.sort_values('game_name')  
print(df_sorted)  
  
df_grouped = df_sorted.groupby('game_name').sum().reset_index()  
  
df_grouped = df_grouped.rename(columns={'viewer_count': 'suma_viewers'})  
print(df_grouped)  
  
print(result_count2)
```

EXERCICI 2 FINAL
```python
import pandas as pd  
  
  
chunksize = 20000  
df = pd.read_csv("feb_23.csv", sep='\t', usecols=["game_name", "viewer_count"], chunksize=chunksize)  
result = []  
result_count = []  
  
for chunk in df:  
viewers = chunk.groupby("game_name")["viewer_count"].sum().reset_index()  
counts = (chunk["game_name"].value_counts() / 4).reset_index()  
result.append(viewers)  
result_count.append(counts)  
  
result_count2 = pd.concat(result_count, axis=0, ignore_index=True)  
df = pd.concat(result, axis=0, ignore_index=True)  
  
df_sorted = df.sort_values('game_name')  
  
df_grouped = df_sorted.groupby('game_name').sum().reset_index()  
  
df_grouped = df_grouped.rename(columns={'viewer_count': 'suma_viewers'})  
  
result_count2_grouped = result_count2.groupby('game_name')['count'].sum().reset_index()  
  
result_count2_grouped = result_count2_grouped.rename(columns={'count': 'hores'})  
  
  
column_to_add = df_grouped['suma_viewers']  
  
  
# Add the extracted column to df2  
result_count2_grouped['viewers'] = column_to_add  
  
print(result_count2_grouped)  
  
result_count2_grouped.to_csv("exercici2.csv")
```

Exercici 4 FINAL

```python
import pandas as pd  
  
  
chunksize = 20000  
df = pd.read_csv("feb_23.csv", sep='\t', usecols=["streamer_name", "viewer_count"], chunksize=chunksize)  
result = []  
result_count = []  
  
for chunk in df:  
viewers = chunk.groupby("streamer_name")["viewer_count"].sum().reset_index()  
counts = (chunk["streamer_name"].value_counts() / 4).reset_index()  
result.append(viewers)  
result_count.append(counts)  
  
result_count2 = pd.concat(result_count, axis=0, ignore_index=True)  
df = pd.concat(result, axis=0, ignore_index=True)  
  
df_sorted = df.sort_values('streamer_name')  
  
df_grouped = df_sorted.groupby('streamer_name').sum().reset_index()  
  
df_grouped = df_grouped.rename(columns={'viewer_count': 'suma_viewers'})  
  
result_count2_grouped = result_count2.groupby('streamer_name')['count'].sum().reset_index()  
  
result_count2_grouped = result_count2_grouped.rename(columns={'count': 'hores'})  
  
column_to_add = df_grouped['suma_viewers']  
  
# Add the extracted column to df2  
result_count2_grouped['viewers'] = column_to_add  
  
print(result_count2_grouped)  
  
result_count2_grouped.to_csv("exercici4.csv")
```

Exercici 5
```python
import pandas as pd  
  
df= pd.read_csv("feb_23.csv", sep='\t', usecols=["captured_at", "viewer_count"])  
  
viewers=df.groupby("captured_at")["viewer_count"].sum().tolist()  
hora=df["captured_at"].unique().tolist()  
  
  
data = {'captura': hora, 'viewers': viewers}  
  
junto = zip(data["viewers"],data["captura"])  
ex = []  
  
for i in junto:  
ex.append(i)  
  
  
df1 = pd.DataFrame(ex, columns=['viewers','captura'])  
df1['std_viewers'] = df.groupby("captured_at")["viewer_count"].std().round(2).tolist()  
  
print(df1)  
  
df1.to_csv('exercici5.csv')

# Treball Final

El procés d'obtenció de dades sha realitzat mitjançant l'accés a l'api de desenvolupador de Spotify a través d'un codi de python. El primer pas realitzat per aquesta recolecció de dades es crear una aplicació d'Spotify Dev per poder accedir a l'api. Aquesta aplicació genera un Client ID i un Client Secret, dos claus que introduirem al python y mitjançant diferents mòduls utilitzarem per extreure informació de l'api d'Spotify.

# FOTO RECORTES

## Mòduls

Un cop tenim aquestes credencials ja podem començar amb el arxiu de python. Comencem instalant i important els mòduls que necessitarem per l'extracció.

```python
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import time
import pandas as pd
```

El primer de tots es la biblioteca de "spotipy", biblioteca de lliure accés creada per Paul Lamere pensada per manipular la api d'Spotify. També farem servir la biblioteca de "json", bàsicament per tenir accés i visualitzar arxius json, que serà el tipo d'arxiu que extraurem de la api. El tercer as preparatori es importar l'intèrpret de les credencials d'Spotify desde el propi mòdul d'Spotipy.
Importem també el mòdul "time" per afegir un temps de pausa a les peticions, en motiu d'evitar el bloqueig per sobresaturació de la api. I per acabar importem el mòdul "pandas" que emprarem per traballar amb datasets i dataframes.

## Preparació

Comencem assignant les dues credencials a dues variables internes. I amb aquestes dues variables i l'ajuda del "SpotifyClientCredentials" aconseguim el "auth_manager".  I mitjançant aquest objecte auth_manager per l'autentificació aconseguim accés a Spotify amb el modul d'Spotipy assignant aquest modul com a "sp".

```python
SPOTIPY_CLIENT_ID = '89f634cbfb22458fbd2b396dd25496ee'
SPOTIPY_CLIENT_SECRET = 'f266a68c3f5f4fc6901091f6f7fb553e'

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist_ids = ["37i9dQZEVXbO839WGRmpu1", "37i9dQZEVXbKPTKrnFPD0G", "37i9dQZEVXbK4fwx2r07XW", "37i9dQZEVXbKzoK95AbRy9", "37i9dQZEVXbMda2apknTqH", "37i9dQZEVXbLJ0paT1JkgZ", "37i9dQZEVXbL1Fl8vdBUba", "37i9dQZEVXbJZGli0rRP3r", "37i9dQZEVXbIZQf3WEYSut", "37i9dQZEVXbJPVQvqZqpcM", "37i9dQZEVXbMy2EcFg5F9m", "37i9dQZEVXbLp5XoPON0wI", "37i9dQZEVXbJVKdmjH0pON", "37i9dQZEVXbJHSzlHx2ZJU", "37i9dQZEVXbMdvweCgpBAe", "37i9dQZEVXbMWDif5SCBJq", "37i9dQZEVXbIZK8aUquyx8", "37i9dQZEVXbJ5J1TrbkAF9", "37i9dQZEVXbKqiTGXuCOsB", "37i9dQZEVXbLeBcWrdps2V", "37i9dQZEVXbMPoK06pe7d6", "37i9dQZEVXbKcS4rq3mEhp", "37i9dQZEVXbNM8vS9cIqAG", "37i9dQZEVXbKUoIkUXteF6", "37i9dQZEVXbLw80jjcctV1", "37i9dQZEVXbIWlLQoMVEFp", "37i9dQZEVXbNy9tB5elXf1", "37i9dQZEVXbNSiWnkYnziz", "37i9dQZEVXbMGcjiWgg253", "37i9dQZEVXbN66FupT0MuX", "37i9dQZEVXbJV3H3OfCN1z", "37i9dQZEVXbJ7qiJCES5cj", "37i9dQZEVXbMVY2FDHm6NN", "37i9dQZEVXbNvXzC8A6ysJ", "37i9dQZEVXbKZyn1mKjmIl"]
paises = ["SAU", "ARG", "AUS", "BRA", "CAN", "CHI", "COL", "KOR", "EAU", "ECU", "EGY", "USA", "PHI", "GUA", "HKG", "IND", "IDN", "ISR", "JAP", "KAZ", "DOM", "MAL", "MAR", "MEX", "NIG", "NZE", "PAK", "PAN", "PER", "SGP", "SAF", "THA", "TWN", "VEN", "VNM"]
```

Un cop tenim accés a l'Api procedim a manualment agafar els id de les playlist que ens interessen. En aquest cas totes les playlists del TOP 50 cançons de cada païs. En aquest codi d'exemple hi ha 35 països fora d'Europa, ja que els països europeus s'han extret amb un codi idèntic però generant un dataset només europeu. Al mateix temps que recolectem les id de les playlist en un altre llista i en el mateix ordre afegim el codi de tres lletres per a cada païs. Hem decidit fer servir aquest codi ja que d'aquesta manera Tableau reconeix els països i pots fer infografies de mapas.

## Iteració i recolecció

Gràcies a la documentació d'spotipy així com a l'analisi d'un json de prova vam poder arribar a veure com accedir a les dades que ens interessaven així com quina era la nomenclatura adequada per accedir-hi. Un cop fet aquests passos previs es moment d'aconseguir les dades definitives. 

Comencem iterant sobre les llistes d'identificadors de playlists i països simultaneament. Aconseguim una llista on cada element de la llista està comprès per l'identificador de la playlist i el codi del seu païs.

```python
for list, pais in zip(playlist_ids, paises):
    query = sp.playlist_items(list, fields=None, limit=100, offset=0, market=None)

    with open(f"{pais}-{list}.json", 'w', encoding='utf-8') as f:
        json.dump(query, f, ensure_ascii=False, indent=4)
```

I a la variable query li assignem tots els items de la playlist fent servir la playlist ID de cada païs. Per tant per a cada iteració "query" conté tots els items de cada un dels països. Per tant ens interessa generar un json per a cada païs. Per tant creem un json de nom el païs més la playlist ID. I en aques json aboquem tota la query pertanyent a aquell païs.

Ja hem establert que la query conté els elements d'una playlist. Així que és moment d'extreure aquells elements d'items que ens interessin. Primer creem una llista per volcar les mesures de cada cançó i iterem sobre "items" de "query". Que bàsicament es iterar sobre cada cançó de la playlist, per tant "i" és cada cançó.

```python
for i in query['items']:
        song_id = i["track"]["id"]
        track_name = i["track"]["name"]
        features = sp.audio_features(song_id)
        artists_name = i["track"]["album"]["artists"]
        cantants = []
```

En aquesta primera iteració obtenim uns paràmetres claus. Aconseguim el "ID" de la cançó, el nom de la cançó, el nom de l'artista d'aquesta canço i introduim en una llista tots els "audio_features". Finalment creem una llista buida per als cantants, ja que a la variable d'artists_name i ha més d'un artista en molts casos, i només ens interessa assignar un artista a cada cançó.

```python
for artist in artists_name:
            a = artist["name"]
            cantants.append(a)
```

És per això que tornem a iterar sobre la llista "artists_name" i afegim en una llista tots els cantants per separats. Fet que farà que més endavant poguem escollir quin d'aquests cantants volem assignar a cada cançó.

```python
for element in features:
            dance = element["danceability"]
            energy = element["energy"]
            key = element["key"]
            acousticness = element["acousticness"]
            duration_ms = element["duration_ms"]
            loudness = element["loudness"]
            speechiness = element["speechiness"]
            tempo = element["tempo"]
```

## Generar Dataset

A continuació iterem sobre la llista de les "audiofeatures" i a cada element d'aquesta llista li assignem la variable corresponent al seu nom. Les audio_features preseleccionades per aquest estudi son: "danceability", "energy", "key", "acousticness", "duration_ms", "loudness", "speechiness" i "tempo". A les quals les assignem a variables homònimes, que farem servir per introduir totes aquestes mesures i les anteriors en un dataframe.

```python
 df = pd.DataFrame({
                "danceability": [dance],
                "artist_name": [cantants[0]],
                "song_id": [song_id],
                "track_name": [track_name],
                "key": [key],
                "energy": [energy],
                "acousticness": [acousticness],
                "duration_ms": [duration_ms],
                "loudness": [loudness],
                "speechiness": [speechiness],
                "tempo": [tempo]
            })
```

Finalment creem el daframe fent servir totes les "audio_features" esmentades més el "song_id", "track_name" i el primer artista de la llista d'artistes de la cançó.

```python
		llista.append(df)
    time.sleep(0.2)
```

Un cop tenim el dataframe l'afegim a la llista, on s'aniràn afegint els dataframes de cada cançó a mesura que avançi la iteració. La iteració de "query""items" la tanquem amb un time sleep de 0.2 segons per no saturar la api.

Tenim tots els dataframes en una llista, però ara ens fa falta concatenar aquesta llista per aconseguir un dataset utilitzable.

```python
 dataset = pd.concat(llista)
    print(dataset)
    dataset.to_csv(f"dataset-{pais}-{list}.csv", index=False)
```

Concatenem aquesta llista en la variable dataset i exportem aquest dataset en un csv de nom igual al json previament generat, amb el nom del païs i el id de la playlist. Això ens dona 35 csvs individuals per cada païs, els quals el seguent pas serà ajuntar tots aquests csvs en un csv global. 

## Merging CSVS

Per concatenar tots aquests datasets generats necessitarem un nou mòdul, la biblioteca anomenada "glob". I la ja coneguda "pandas"

```python
import glob
import pandas as pd
```

És important tenir tots els arxius csv en la mateixa carpeta, ja que mitjançant la nomenclatura podrem accedir a tots aquests arxius sense haver d'anomenar-los individualment.

```python
file_list = glob.glob("*.csv")

df_concatenated = pd.DataFrame()

for file in file_list:
    df = pd.read_csv(file)
    df_concatenated = pd.concat([df_concatenated, df])
```

Fent servir el la funció del glob.glob llegim i emmagatzamem en una llista tots els datasets amb format csv del directori. A continuació creem un Dataframe buit on emmagatzarem els datasets concatenats i iterem sobre cada arxiu de la llista de datasets creada anteriorment.

Bàsicament llegim el csv, l'assignem a una variable i anem concatenant cada arxiu al dataframe buit previament creat. I finalmente creem un nou csv on tenim tot merged.

```python
df_concatenated.to_csv("concatenated_file_totjunt.csv", index=False)
```

Tot aquest codi es pot consultar en el seguent arxiu python: https://github.com/Aleksandeeeer/ApuntsPython/blob/main/SpotipyFinal/main.py 

## Europa i mundial

Tots aquests passos es van realitzar primerament amb uns 20 països europeus, generant un dataset idèntic al dataset concatenat mundial pero amb europa. I aquest procés de merging es va emprar entre aquests dos datasets generals generant un dataset total Europa+Mundial. Per tant podem dir que tenim un dataset Europeu, un dataset fora d'europa i un dataset Mundial. On el dataset mundial comprèn un total de 57 països.

## Grapho amb Gephi

Un cop generat tot això ja esmentat vam decidir generar un dataset especial per poder tractar amb gephi i generar un grapho de relacions entre països i artistes.

```python
import pandas as pd

df = pd.read_csv("concatenated_file_mundial.csv")

graph = []

for item, row in df.iterrows():
    source = row["artist_name"]
    target = row["pais"]
    tupla = (source, target)
    graph.append(tupla)
```

Agafem el csv general i el convertim en un dataframe, creem una llista buida per emmagatzemar les tuples resultants i iterem sobre les files del dataframe.

Agafem les dues variables de "artist_name" i "pais" i les assignem a les variables de "source" i "target" respectivament. Seguidament creem una tupla amb aquestes dues variables i les anem afegint a la llista de tuples.

```python
final = pd.DataFrame(graph, columns= ["source", "target"])
final.to_csv("grapho_mundial.csv", index= False)
```

El pas final serà convertir en un dataset aquesta llista de tuples i exportar-ho en un csv. Igual que hem fet amb els anteriors datasets generem un dataset per Europa, un per fora d'Europa i un mundial.

Tot aquest codi es accessible aqui: https://github.com/Aleksandeeeer/ApuntsPython/blob/main/SpotipyFinal/graphgephi.py

## Datasets

Tots els datasets son accessibles en el seguent repositori de github: https://github.com/Aleksandeeeer/ApuntsPython/tree/main/SpotipyFinal
