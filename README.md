## AC/DC

AC/DC é módulo proposto para que o usuário possa descobrir em quais plataformas famosas um determinado álbum está disponível.


### Deezer

```python
import requests

def search_album_deezer(album_name, artist_name):
    # Construir a URL da API do Deezer para pesquisa de álbuns
    url = f"https://api.deezer.com/search/album/?q={album_name} {artist_name}&limit=1"

    # Fazer a solicitação GET
    response = requests.get(url)

    # Verificar se a solicitação foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Converter a resposta para JSON
        data = response.json()

        # Verificar se há resultados
        if 'data' in data and data['data']:
            album = data['data'][0]
            print(f"Nome do álbum: {album['title']}")
            print(f"Artista: {album['artist']['name']}")
            print(f"Link do álbum no Deezer: {album['link']}")
        else:
            print("Álbum não encontrado no Deezer.")
    else:
        print(f"Falha na solicitação. Código de status: {response.status_code}")

if __name__ == "__main__":
    # Exemplo de pesquisa de álbum no Deezer
    album_name = input("Digite o nome do álbum: ")
    artist_name = input("Digite o nome do artista: ")
    search_album_deezer(album_name, artist_name)
```
