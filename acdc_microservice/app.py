import mysql.connector
from flask import Flask, request, jsonify
import requests
from bing_image_urls import bing_image_urls
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

# Configuração da conexão com o banco de dados MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'recomendacoes'
}



def search_album(album_name, artist_name):
    # Chaves da API do Spotify
    client_id = '22d4b6997d4b4d6faf63ab9d78278fd5'
    client_secret = '8074223b87354205b8c5946589d9aa73'

    # Configuração da autenticação com a API do Spotify
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Pesquisa do álbum
    results = sp.search(q=f"album:{album_name} artist:{artist_name}", type='album', limit=1)

    # Verificação se o álbum foi encontrado e retornar o Link

    if results['albums']['items']:
        album = results['albums']['items'][0]
        spotify_link = album['external_urls']['spotify']
        return spotify_link
    else:
        return None




@app.route('/search_album', methods=['POST'])
def search_album_api():
    try:
        data = request.json
        title = data.get('nome')

        # Extrair nome do artista e nome do álbum do título
        artist_name, album_name = title.split(' - ')

        # Pesquisar o álbum
        spotify_link = search_album(album_name, artist_name)
        print(spotify_link)
        

        if spotify_link:
            # Conectar ao banco de dados MySQL
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Atualizar o registro no banco de dados com o link do Spotify
            update_query = "UPDATE recomendacoes SET reclink_spotify = %s WHERE titulo = %s"
            print(update_query)
            cursor.execute(update_query, (spotify_link, title))
            connection.commit()

            # Fechar a conexão com o banco de dados
            cursor.close()
            connection.close()

            return jsonify({'message': 'Link do Spotify salvo com sucesso.'}), 200
        else:
            return jsonify({'message': 'Álbum não encontrado.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500



# Rota para atualizar uma recomendação
@app.route('/update_recommendation', methods=['POST'])
def update_recommendation():
    try:
        # Obtém os dados do POST
        data = request.json
        nome = data.get('nome')
        id_recomendacao = data.get('id')

        print(data)
        print(id_recomendacao)
        print(nome)

        # Faz uma requisição para o Deezer para buscar o link
        artist_name, album_name = nome.split(' - ')

        # Formata a URL da API do Deezer com o nome do artista e do álbum
        deezer_url = f"https://api.deezer.com/search/album/?q={album_name} {artist_name}&limit=1"
        deezer_response = requests.get(deezer_url)
        # Verifica se a requisição ao Deezer foi bem-sucedida
        if deezer_response.status_code == 200:
            # Extrai os dados da resposta em formato JSON
            deezer_data = deezer_response.json()

            # Verifica se há dados retornados
            if 'data' in deezer_data and deezer_data['data']:
                # Extrai o primeiro item da lista de resultados
                primeiro_resultado = deezer_data['data'][0]

                # Obtém o link do primeiro resultado
                link_rec = primeiro_resultado.get('link')
                

                # Conecta ao banco de dados MySQL
                connection = mysql.connector.connect(**db_config)
               
                cursor = connection.cursor()

                # Atualiza o registro no banco de dados com o link encontrado
                update_query = "UPDATE recomendacoes SET reclink = %s WHERE id = %s"
                print(update_query)
                cursor.execute(update_query, (link_rec, id_recomendacao))
                
                connection.commit()

                # Fecha a conexão com o banco de dados
                cursor.close()
                connection.close()

                return jsonify({'message': f'Registro atualizado com sucesso. Novo link: {link_rec}'}), 200
            else:
                return jsonify({'message': 'Nenhum resultado encontrado no Deezer.'}), 404
        else:
            return jsonify({'message': 'Falha ao acessar a API do Deezer.'}), 500
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    

# Rota para pesquisa da imagem
@app.route('/update_image', methods=['POST'])
def update_image():
        try:
            # Obtém os dados do POST
            data = request.json
            nome = data.get('nome')
            id_recomendacao = data.get('id')

            # Faz uma busca por uma imagem com base no nome do álbum e do artista
            image_urls = bing_image_urls(nome, limit=1)

            # Verifica se foram encontradas URLs de imagens
            if image_urls:
                image_url = image_urls[0]

                # Conecta ao banco de dados MySQL
                connection = mysql.connector.connect(**db_config)
                cursor = connection.cursor()

                # Atualiza o registro no banco de dados com o link da imagem encontrada
                update_query = "UPDATE recomendacoes SET img = %s WHERE id = %s"
                cursor.execute(update_query, (image_url, id_recomendacao))
                connection.commit()

                # Fecha a conexão com o banco de dados
                cursor.close()
                connection.close()

                return jsonify({'message': f'Imagem atualizada com sucesso. Nova URL da imagem: {image_url}'}), 200
            else:
                return jsonify({'message': 'Nenhuma URL de imagem encontrada.'}), 404
        except Exception as e:
            return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)