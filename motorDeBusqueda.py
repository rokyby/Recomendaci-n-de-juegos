import pandas as pd
import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity

# Leer archivo JSON
juegos = pd.read_json('top-1000-steam-games/steam_data.json')

# Renombrar columna
juegos['title'] = juegos['name']
juegos = juegos.drop('name', axis=1)

# Extraer géneros desde HTML
juegos['genres'] = juegos['genres'].apply(lambda x: re.findall(r">([^<]+)<", x))

# One Hot Encoding de géneros
juegos_cod = juegos.copy()
for index, row in juegos.iterrows():
    for genre in row['genres']:
        juegos_cod.at[index, genre] = 1
juegos_cod = juegos_cod.fillna(0)

juegos_cod = juegos_cod.drop(['detailed_description', 'short_description', 'categories'], axis=1, errors='ignore')

# Añadir ID si no existe
juegos_cod['gameId'] = juegos_cod.index

# ✅ Entrada del usuario: títulos que le gustaron (sin rating)
favoritos_usuario = [
    'Streets of Rogue',
    'Evolvation',
    'Counter-Strike ',
    'My Summer Car ',
    'theHunter: Call of the Wild™ '
]

# Filtrar los juegos que el usuario indicó
juegos_usuario = juegos_cod[juegos_cod['title'].isin(favoritos_usuario)]

# Generar perfil de usuario como suma de vectores de géneros
perfil_usuario = juegos_usuario.drop(['title', 'genres'], axis=1, errors='ignore').sum().to_frame().T

# Quitar juegos del usuario para no recomendarlos
juegos_filtrados = juegos_cod[~juegos_cod['title'].isin(favoritos_usuario)]

# Extraer solo columnas de géneros para el resto de juegos
#generos_cols = perfil_usuario.columns
#juegos_generos = juegos_filtrados[generos_cols]
# Extraer solo las columnas numéricas de géneros
generos_cols = [col for col in perfil_usuario.columns if col not in ['title', 'genres', 'short_description', 'detailed_description']]
juegos_generos = juegos_filtrados[generos_cols]

# Calcular similitud del coseno entre perfil del usuario y cada juego
similitudes = cosine_similarity(juegos_generos, perfil_usuario)

# Agregar las similitudes al DataFrame
juegos_filtrados = juegos_filtrados.copy()
juegos_filtrados['similitud'] = similitudes

# Ordenar por similitud
recomendados = juegos_filtrados.sort_values(by='similitud', ascending=False)

# Mostrar top 20 recomendaciones
top_20 = recomendados.head(20)
print("🎮 Recomendaciones basadas en géneros similares:\n")
print(top_20[['title', 'similitud']])
