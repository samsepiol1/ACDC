import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="22d4b6997d4b4d6faf63ab9d78278fd5",
                                                           client_secret="8074223b87354205b8c5946589d9aa73"))

results = sp.search(q='Grimes', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
