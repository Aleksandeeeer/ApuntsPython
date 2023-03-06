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
