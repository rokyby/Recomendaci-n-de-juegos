🎮 Recomendación de Juegos de Steam
Este proyecto es un sistema de recomendación de juegos basado en los datos de los 1000 juegos más populares de la plataforma Steam. Su objetivo es ofrecer a los usuarios recomendaciones personalizadas según sus gustos y preferencias.


📌 Descripción General
El sistema utiliza un modelo basado en similitudes para identificar y sugerir juegos que se alineen con los intereses del usuario. A través de una interfaz web interactiva, los usuarios pueden explorar juegos sugeridos en función de sus selecciones previas.


🚀 Funcionalidades Principales
📥 Carga y procesamiento de datos:
Se utiliza un conjunto de datos que contiene información de los 1000 juegos más populares de Steam, incluyendo nombre, etiquetas, desarrolladores, precios, calificaciones y número de reseñas.


🧠 Sistema de recomendación:
El sistema implementa un modelo de filtrado basado en contenido para encontrar juegos similares a los seleccionados por el usuario, usando métricas de similitud (como el coseno) entre vectores de características.


🌐 Interfaz web:
Los usuarios pueden interactuar fácilmente a través de una página web para seleccionar sus juegos favoritos y recibir recomendaciones al instante.


🧰 Pila Tecnológica
Python – lenguaje principal para el procesamiento y lógica del sistema.

Pandas – manipulación y análisis de los datos.

NumPy – soporte para cálculos numéricos.

Matplotlib – generación de gráficos opcionales para análisis.

Flask – desarrollo de la API y de la interfaz web.


top-1000-steam-games/
│
├── steam_app_data.csv       # Dataset original descargado desde Kaggle
├── steam_data.json          # Archivo JSON generado con los datos relevantes
├── recomendador.py          # Código principal del sistema de recomendación
├── README.md                # Este archivo
├──top-1000-steam-games/

Requisitos
Python 3.7+

Pandas

NumPy

Matplotlib

OpenDatasets (para descargar desde Kaggle)




Descargar los datos de Kaggle

pip install pandas numpy matplotlib opendatasets

import opendatasets as od
od.download("https://www.kaggle.com/datasets/joebeachcapital/top-1000-steam-games")

instalar(ejecutar los siguientes comandos)

pip install flask

python app.py


 Notas
Asegúrate de que los nombres de los juegos coincidan exactamente con los del dataset.

Se recomienda limpiar y normalizar descripciones o categorías si se desea extender el sistema más allá de los géneros.

📖 Créditos
Dataset original de Kaggle: Top 1000 Steam Games

Autor: edwin torres
