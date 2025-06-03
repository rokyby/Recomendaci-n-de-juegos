import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Importar los datos procesados desde tu motor de búsqueda
import motorDeBusqueda

# Acceder a los datos del sistema de recomendación
top_20 = motorDeBusqueda.top_20
juegos_filtrados = motorDeBusqueda.juegos_filtrados
juegos_usuario = motorDeBusqueda.juegos_usuario
generos_cols = motorDeBusqueda.generos_cols

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")



# --- Gráfico 1: Top 20 recomendaciones ---
plt.figure(figsize=(10, 6))
plt.barh(top_20['title'], top_20['similitud'], color='skyblue')
plt.xlabel('Similitud con el perfil del usuario')
plt.title('Top 20 juegos recomendados')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# --- Gráfico 2: Similitud vs cantidad de géneros ---
juegos_filtrados['num_generos'] = juegos_filtrados[generos_cols].sum(axis=1)
plt.figure(figsize=(8, 6))
plt.scatter(juegos_filtrados['num_generos'], juegos_filtrados['similitud'], alpha=0.5)
plt.xlabel('Número de géneros del juego')
plt.ylabel('Similitud con el perfil del usuario')
plt.title('Similitud vs. cantidad de géneros')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Gráfico 3: Heatmap de géneros en favoritos ---
generos_usuario = juegos_usuario[generos_cols]
plt.figure(figsize=(10, 4))
sns.heatmap(generos_usuario.T, cmap="YlGnBu", cbar=False, annot=True)
plt.title('Presencia de géneros en los juegos favoritos del usuario')
plt.ylabel('Géneros')
plt.xlabel('Juegos favoritos')
plt.tight_layout()
plt.show()

# --- Gráfico 4: Géneros más frecuentes en el top 20 recomendado ---
generos_top = top_20[generos_cols].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
generos_top.plot(kind='bar', color='lightcoral')
plt.ylabel('Cantidad de juegos con ese género')
plt.title('Frecuencia de géneros en el Top 20 recomendado')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Gráfico 5: Histograma de distribución de similitudes ---
plt.figure(figsize=(8, 4))
plt.hist(juegos_filtrados['similitud'], bins=30, color='purple', edgecolor='black')
plt.xlabel('Similitud')
plt.ylabel('Cantidad de juegos')
plt.title('Distribución de similitud de juegos con el perfil del usuario')
plt.tight_layout()
plt.show()
