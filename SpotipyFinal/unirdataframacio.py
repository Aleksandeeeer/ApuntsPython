import glob
import pandas as pd

file_list = glob.glob("grapho*.csv")

df_concatenated = pd.DataFrame()

for file in file_list:
    df = pd.read_csv(file)
    df_concatenated = pd.concat([df_concatenated, df])

df_concatenated.to_csv("concatenated_file_totjunt.csv", index=False)