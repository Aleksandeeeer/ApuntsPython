import pandas as pd

df = pd.read_csv("concatenated_file_mundial.csv")

graph = []

for item, row in df.iterrows():
    source = row["artist_name"]
    target = row["pais"]
    tupla = (source, target)
    graph.append(tupla)

final = pd.DataFrame(graph, columns= ["source", "target"])
final.to_csv("grapho_mundial.csv", index= False)