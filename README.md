## AC/DC

AC/DC é módulo proposto para que o usuário possa descobrir em quais plataformas famosas um determinado álbum está disponível.

### Spotify

```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

# Carregas as variáveis de ambiente
load_dotenv()


def search_album(album_name, artist_name):
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

    # Configuração da autenticação com a API do Spotify
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Pesquisa do álbum
    results = sp.search(q=f"album:{album_name} artist:{artist_name}", type='album', limit=1)

    # Verificação se o álbum foi encontrado e apresentação do Link
    if results['albums']['items']:
        album = results['albums']['items'][0]
        print(f"Nome do álbum: {album['name']}")
        print(f"Artista: {album['artists'][0]['name']}")
        print(f"Link do álbum no Spotify: {album['external_urls']['spotify']}")
    else:
        print("Álbum não encontrado.")

if __name__ == "__main__":

    # Exemplo de pesquisa de álbum com input
    album_name = input("Digite o nome do álbum: ")
    artist_name = input("Digite o nome do artista: ")

    search_album(album_name, artist_name)

```

### Deezer

```python
mport requests

# URL da sua API
api_url = 'http://localhost:3000/recommendations/2'

# Faz uma requisição GET para a sua API
response = requests.get(api_url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Extrai os dados da resposta em formato JSON
    data = response.json()

    # Verifica se há dados retornados
    if data:
        # Assume que o primeiro item na lista de recomendações contém as informações desejadas
        recommendation = data[0]

        # Extrai a string no formato 'nome_artista - album'
        recommendation_info = recommendation.get('titulo')

        # Divide a string no hífen para obter o nome do artista e o nome do álbum
        artist_name, album_name = recommendation_info.split(' - ')

        # Exibe as informações
        print(f'Nome do Artista: {artist_name}')
        print(f'Título do Álbum: {album_name}')

        # Faz uma requisição para a API do Deezer com base nas informações obtidas
        deezer_url = f"https://api.deezer.com/search/album/?q={album_name} {artist_name}&limit=1"
        deezer_response = requests.get(deezer_url)

        # Verifica se a requisição ao Deezer foi bem-sucedida
        if deezer_response.status_code == 200:
            # Extrai os dados da resposta em formato JSON
            deezer_data = deezer_response.json()

            # Verifica se há álbuns retornados
            if 'data' in deezer_data and deezer_data['data']:
                # Extrai o primeiro álbum da lista
                deezer_album = deezer_data['data'][0]

                # Exibe o título do álbum e a URL do álbum no Deezer
                deezer_album_title = deezer_album.get('title')
                deezer_album_url = deezer_album.get('link')

                print(f'Título do Álbum no Deezer: {deezer_album_title}')
                print(f'URL do Álbum no Deezer: {deezer_album_url}')
            else:
                print('Nenhum álbum encontrado no Deezer com essas informações.')
        else:
            print('Falha ao acessar a API do Deezer.')
    else:
        print('Nenhuma recomendação encontrada.')
else:
    print('Falha ao acessar a sua API.')
```
