import pandas as pd
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import re

# Leer archivo JSON
juegos = pd.read_json('steam_data.json')

# Renombrar 'name' a 'title' por compatibilidad
juegos['title'] = juegos['name']
juegos = juegos.drop('name', axis=1)

# Si no hay años, lo dejamos vacío o como NaN
juegos['year'] = None

# Limpiar géneros en formato HTML
juegos['genres'] = juegos['genres'].apply(lambda x: re.findall(r">([^<]+)<", x))

# Copiar para codificación
juegos_co = juegos.copy()

# One Hot Encoding de géneros
for index, row in juegos.iterrows():
    for genre in row['genres']:
        juegos_co.at[index, genre] = 1

juegos_co = juegos_co.fillna(0)

# Procesamiento de ratings
rating = rating.drop('timestamp', axis=1, errors='ignore')  # timestamp puede no existir

# Ejemplo de entrada del usuario
usuario_en = [
    {'title': 'The Legend of Zelda', 'rating': 5},
    {'title': 'Minecraft', 'rating': 4.5},
    {'title': 'Call of Duty', 'rating': 3},
    {'title': 'Animal Crossing', 'rating': 4},
    {'title': 'Fortnite', 'rating': 2}
]

entrada_juegos = pd.DataFrame(usuario_en)

# Fusión con el dataset principal
id_juegos = juegos[juegos['title'].isin(entrada_juegos['title'].tolist())]
entrada_juegos = pd.merge(id_juegos, entrada_juegos)

# Limpieza de columnas innecesarias
entrada_juegos = entrada_juegos.drop(['genres', 'year'], axis=1)

# Codificación de géneros para los juegos del usuario
juegos_usuario = juegos_co[juegos_co['gameId'].isin(entrada_juegos['gameId'].tolist())]

# Preparación de tabla de géneros
juegos_usuario = juegos_usuario.reset_index(drop=True)
tabla_generos = juegos_usuario.drop(['gameId', 'title', 'genres', 'year'], axis=1)

# Perfil del usuario
perfil_usu = tabla_generos.transpose().dot(entrada_juegos['rating'])

# Preparación de géneros del dataset completo
generos = juegos_co.set_index('gameId')
generos = generos.drop(['title', 'genres', 'year'], axis=1)

# Cálculo de puntuaciones ponderadas
recom = (generos * perfil_usu).sum(axis=1) / perfil_usu.sum()

# Ordenar y filtrar recomendaciones
recom = recom.sort_values(ascending=False)

# Mostrar top 20 juegos recomendados
final = juegos.loc[juegos['gameId'].isin(recom.head(20).index)]
nfinal = final[['title']]
print("Juegos recomendados:\n", nfinal)
