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