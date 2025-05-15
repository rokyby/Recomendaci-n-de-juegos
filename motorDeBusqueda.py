from flask import Flask, jsonify, request, render_template
import pandas as pd
import re

app = Flask(__name__)

# Cargar y preparar los datos una sola vez al iniciar el servidor
df = pd.read_json('static/steam_data.json')
df['title'] = df['name']
df['gameId'] = df.index
df['year'] = None
df['genres'] = df['genres'].apply(lambda x: re.findall(r">([^<]+)<", x))
df = df.drop('name', axis=1)
df['title_norm'] = df['title'].str.lower().str.strip()

# One-hot encoding
df_co = df.copy()
for index, row in df.iterrows():
    for genre in row['genres']:
        df_co.at[index, genre] = 1
df_co = df_co.fillna(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/juegos')
def juegos():
    top = df[['title', 'short_description', 'categories']].rename(columns={
        'title': 'name'
    }).head(1000)
    return jsonify(top.to_dict(orient='records'))

@app.route('/api/recomendar', methods=['POST'])
def recomendar():
    entrada = request.get_json()

    entrada_df = pd.DataFrame(entrada)
    entrada_df['title_norm'] = entrada_df['title'].str.lower().str.strip()

    id_juegos = df[df['title_norm'].isin(entrada_df['title_norm'].tolist())]
    entrada_df = pd.merge(id_juegos, entrada_df, on='title_norm')
    entrada_df = entrada_df.drop(['genres', 'year', 'title_norm'], axis=1)

    juegos_usuario = df_co[df_co['gameId'].isin(entrada_df['gameId'].tolist())]
    tabla_generos = juegos_usuario.drop(['gameId', 'title', 'genres', 'year'], axis=1).reset_index(drop=True)
    perfil_usu = tabla_generos.transpose().dot(entrada_df['rating'])

    generos = df_co.set_index('gameId').drop(['title', 'genres', 'year'], axis=1)
    recom = (generos * perfil_usu).sum(axis=1) / perfil_usu.sum()
    recom = recom.sort_values(ascending=False)

    final = df[df['gameId'].isin(recom.head(20).index)]
    resultado = final[['title', 'short_description', 'categories']]
    resultado = resultado.rename(columns={'title': 'name'})
    return jsonify(resultado.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
