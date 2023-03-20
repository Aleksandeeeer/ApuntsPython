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

