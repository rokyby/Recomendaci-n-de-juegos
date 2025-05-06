import opendatasets as od

dataset_link="https://www.kaggle.com/datasets/joebeachcapital/top-1000-steam-games"
od.download(dataset_link)

import os
os.chdir("top-1000-steam-games")
os.listdir()

import pandas as pd
archivo="steam_app_data.csv"
pd.read_csv(archivo)

import json

# Cargar el archivo CSV
archivo = "steam_app_data.csv"
df = pd.read_csv(archivo)

# Seleccionar las columnas relevantes
columnas = ["name"],["detailed_description"],["short_description"],["categories"],["genres"]
df = df[columnas]

# Convertir a JSON y guardar
json_data = df.to_json(orient="records", indent=4)
with open("steam_data.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

print("Archivo JSON creado exitosamente: steam_data.json")
