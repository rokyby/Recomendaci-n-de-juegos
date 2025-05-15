import pandas as pd
import numpy as np
import re

# Cargar JSON
juegos = pd.read_json('steam_data.json')

# Preparar campos necesarios
juegos['title'] = juegos['name']
juegos['year'] = None
juegos['gameId'] = juegos.index  # si no existía un ID
juegos['genres'] = juegos['genres'].apply(lambda x: re.findall(r">([^<]+)<", x))
juegos = juegos.drop('name', axis=1)

# Crear copia para codificación
juegos_co = juegos.copy()

# One-hot encoding de géneros
for index, row in juegos.iterrows():
    for genre in row['genres']:
        juegos_co.at[index, genre] = 1

juegos_co = juegos_co.fillna(0)

# Entrada de usuario
usuario_en = [
    {'title': 'The Legend of Zelda', 'rating': 5},
    {'title': 'Minecraft', 'rating': 4.5},
    {'title': 'Call of Duty', 'rating': 3},
    {'title': 'Animal Crossing', 'rating': 4},
    {'title': 'Fortnite', 'rating': 2}
]

# Normalizar títulos
juegos['title_norm'] = juegos['title'].str.lower().str.strip()
entrada_juegos = pd.DataFrame(usuario_en)
entrada_juegos['title_norm'] = entrada_juegos['title'].str.lower().str.strip()

# Fusión
id_juegos = juegos[juegos['title_norm'].isin(entrada_juegos['title_norm'].tolist())]
entrada_juegos = pd.merge(id_juegos, entrada_juegos, on='title_norm')
entrada_juegos = entrada_juegos.drop(['genres', 'year', 'title_norm'], axis=1)

# Codificación de géneros para juegos del usuario
juegos_usuario = juegos_co[juegos_co['gameId'].isin(entrada_juegos['gameId'].tolist())]

# Preparar tabla de géneros
tabla_generos = juegos_usuario.drop(['gameId', 'title', 'genres', 'year'], axis=1).reset_index(drop=True)

# Perfil del usuario
perfil_usu = tabla_generos.transpose().dot(entrada_juegos['rating'])

# Puntuación para todos los juegos
generos = juegos_co.set_index('gameId')
generos = generos.drop(['title', 'genres', 'year'], axis=1)

# Recomendaciones
recom = (generos * perfil_usu).sum(axis=1) / perfil_usu.sum()
recom = recom.sort_values(ascending=False)

# Mostrar resultados
final = juegos[juegos['gameId'].isin(recom.head(20).index)]
nfinal = final[['title']]
print("Juegos recomendados:\n", nfinal)
