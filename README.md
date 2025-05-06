top-1000-steam-games/
│
├── steam_app_data.csv       # Dataset original descargado desde Kaggle
├── steam_data.json          # Archivo JSON generado con los datos relevantes
├── recomendador.py          # Código principal del sistema de recomendación
├── README.md                # Este archivo


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
