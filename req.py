import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re
import time 
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
def getting_artist_link():
    query = "" #keyword on gooogle
    links = []
    for j in search(query, tld="co.in", num=1, stop=1, pause=3): 
        links.append(j)
    url_result = links
    time.sleep(2)
    #print(url_result)
    #print (re.findall(r'(?<=/)\w+$',url_result)[-1])
    code_crack = re.findall(r'(?<=/)\w+$',url_result[-1])
    code = code_crack[0]

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="22d4b6997d4b4d6faf63ab9d78278fd5",
                                                            client_secret="8074223b87354205b8c5946589d9aa73"))
    urn = 'spotify:album:' + code
    print(urn)

    artist = sp.album(urn)
    print(artist["external_urls"]["spotify"])



getting_artist_link()
