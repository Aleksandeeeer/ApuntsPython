

#EXERCICI 1




import pandas as pd

#creem el dataset de pandas agadant només les columnes que ens interessen, fent servir com a separador el tabulador
df= pd.read_csv("feb_23.csv", sep='\t', usecols=["captured_at", "viewer_count"])

#Agrupem les dades del dataset df en base als valor de la columna "captured_at" i a continuació sumem els valors de "viewer_count" per cada grup de captured_at.
viewers=df.groupby("captured_at")["viewer_count"].sum().tolist()
#aqui creem una llista anomenada hora que conté valors unics de "captured_at" amb els valors de "viewer_count" sumats per totes les dates iguals.
hora=df["captured_at"].unique().tolist()

#Creem un diccionari anomenat "data" con dos claus: "captura" que conté la llista de valores únics en la columna "captured_at" i "viewers" que conté la llista de sumas de la columna "viewer_count"
data = {'captura': hora, 'viewers': viewers}

#Creem una lista anomenada "ex" que conté tuplas creadas a partir dels elements de "viewers" y "captura" emparellats un a un utilizant la funció zip().
junto = zip(data["viewers"],data["captura"])
ex = []
for i in junto:
    ex.append(i)

#creem un dataset anomenat df1 on inserim les columnes emparellades anteriorment.
df1 = pd.DataFrame(ex, columns=['viewers','captura'])

#Finalment guardem aquest dataset en un arxiu CSV
df1.to_csv('exercici1.csv')



#EXERCICI 2




import pandas as pd

#Mida del fragment per llegir l'arxiu CSV en parts
chunksize = 20000

# Carreguem un fitxer CSV anomenat "feb_23.csv" en parts seguint el chunksize ja marcat. Agafem les dues columnes que ens interessen i ho guardem tot en un dataframe
df = pd.read_csv("feb_23.csv", sep='\t', usecols=["game_name", "viewer_count"], chunksize=chunksize)

#aqui creem dues llistes buides on emmagatzarem dades
result = []
result_count = []

#creem un loop per accadir a cada part del dataframe
for chunk in df:
    viewers = chunk.groupby("game_name")["viewer_count"].sum().reset_index() #agrupem les dades correpsonents als valors de la columna "game_name", i després sumem els valors de la columna "viewer_count" per a cada un d'aquests grups.
    counts = (chunk["game_name"].value_counts() / 4).reset_index() #Comptem la freqüència dels valors a la columna "game_name" en el fragment i divideix el resultat per 4. Així obtenim el numero d'hores, ja que hi ha 4 captures cada hora.
    result.append(viewers) #afegim els valors obtinguts a les dues llistes
    result_count.append(counts)

#Concatenem verticalment els DataFrames de la llista "result_count" en un nou DataFrame anomenat "result_count2", ignorant els índexs originals.
result_count2 = pd.concat(result_count, axis=0, ignore_index=True)
df = pd.concat(result, axis=0, ignore_index=True) #el mateix per la llista "result"

df_sorted = df.sort_values('game_name') #ordenem la llista de forma alfabetica tenint en compte la columna "game_name"

df_grouped = df_sorted.groupby('game_name').sum().reset_index() #sumem els valors dels espectadors per cada valor únic de "game_name"

df_grouped = df_grouped.rename(columns={'viewer_count': 'suma_viewers'}) #canviem el nom de la columna per reflexar el canvi

result_count2_grouped = result_count2.groupby('game_name')['count'].sum().reset_index() #fem el mateix pero amb les hores i l'altre dataframe

result_count2_grouped = result_count2_grouped.rename(columns={'count': 'hores'})

#treiem la columna dels espectadors del primer dataframe i l'afegim al segon datagrame
column_to_add = df_grouped['suma_viewers']
result_count2_grouped['viewers'] = column_to_add


#guardem el dataframe unificat a un CSV
result_count2_grouped.to_csv("exercici2.csv")



#EXERCICI 3



import pandas as pd

#Mida del fragment per llegir l'arxiu CSV en parts
chunksize=20000

# Carreguem un fitxer CSV anomenat "feb_23.csv" en parts seguint el chunksize ja marcat. Agafem les tres columnes que ens interessen i ho guardem tot en un dataframe
df= pd.read_csv("feb_23.csv", sep='\t', usecols=["captured_at", "game_name", "viewer_count"], chunksize=chunksize)

#creem una llista buida
game_counts=[]

#creem un loop per accadir a cada part del dataframe. Per a cada fragment, fem un loop pels valors únics de la columna "captured_at". Per a cada valor únic de "captured_at", creem un nou DataFrame amb els "value_counts" de la columna "game_name", que conté la freqüència de cada valor de "game_name" per a aquesta data de "captured_at".
for chunk in df:
    for captured_at_value in chunk["captured_at"].unique():
        game_name_counts = chunk[chunk["captured_at"] == captured_at_value]["game_name"].value_counts().reset_index()
        game_name_counts.columns = ["game_name", "count"]

        #Calculem la suma dels valors de la columna "viewer_count" agrupats per "game_name" per a aquesta data de "captured_at".
        viewer_count_sum = chunk[chunk["captured_at"] == captured_at_value].groupby("game_name")["viewer_count"].sum().reset_index()

        #Finalment, combinem aquests dos DataFrames en un de sol, afegint una columna amb la data de "captured_at".
        combined_counts = pd.merge(game_name_counts, viewer_count_sum, on="game_name", how="outer")
        combined_counts["capture_date"] = captured_at_value
        game_counts.append(combined_counts)#guardem els valors a la llista de "game_counts"

#concatenem els valors de la llista dins del dataframe
df = pd.concat(game_counts)

#ho exportem a dataset.
df.to_csv("exercici3_bo.csv", index=False)



#EXERCICI 4



import pandas as pd


"""Aquest codi es el mateix que a l'exercici 2 però canviant la columna de "game_name" per "streamer_name"""

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

result_count2_grouped['viewers'] = column_to_add

print(result_count2_grouped)

result_count2_grouped.to_csv("exercici4.csv")



#EXERCICI 5



import pandas as pd

"""igual que l'exercici 1 pero creant una columna per calcular la desviació estandard mitjançant una funció"""

df= pd.read_csv("feb_23.csv", sep='\t', usecols=["captured_at", "viewer_count"])

viewers=df.groupby("captured_at")["viewer_count"].sum().tolist()
hora=df["captured_at"].unique().tolist()


data = {'captura': hora, 'viewers': viewers}

junto = zip(data["viewers"],data["captura"])
ex = []

for i in junto:
    ex.append(i)


df1 = pd.DataFrame(ex, columns=['viewers','captura'])

#afegim una columna anomenada "std_viewers" , on afegim el calcul de la desviació mitjana de la columna de "viewer_count", a més afegim que ho posi en dos decimals.
df1['std_viewers'] = df.groupby("captured_at")["viewer_count"].std().round(2).tolist()

print(df1)

df1.to_csv('exercici5.csv')




