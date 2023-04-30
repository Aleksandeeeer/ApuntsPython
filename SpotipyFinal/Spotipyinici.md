

```python
import time
import pandas as pd
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials


SPOTIPY_CLIENT_ID='89f634cbfb22458fbd2b396dd25496ee'
SPOTIPY_CLIENT_SECRET='f266a68c3f5f4fc6901091f6f7fb553e'

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist_id = "37i9dQZEVXbNFJfN1Vw8d9"

query = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None)

songs = []

for i in query['items']:
    song_id = i["track"]["id"]
    songs.append(song_id)

audio_ft = sp.audio_features(songs)

with open("output_features.json", 'w', encoding='utf-8') as f:
    json.dump(audio_ft, f, ensure_ascii=False, indent=4)
```

```python
import time  
import pandas as pd  
import spotipy  
import json  
from spotipy.oauth2 import SpotifyClientCredentials  
  
  
SPOTIPY_CLIENT_ID='89f634cbfb22458fbd2b396dd25496ee'  
SPOTIPY_CLIENT_SECRET='f266a68c3f5f4fc6901091f6f7fb553e'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlist_id = "37i9dQZEVXbNFJfN1Vw8d9"  
  
query = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None)  
  
songs = []  
  
for i in query['items']:  
    song_id = i["track"]["id"]  
    songs.append(song_id)  
  
print(songs)
```

Conseguir el JSON de les audio_features
```python
query = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None)  
  
songs = []  
  
for i in query['items']:  
    song_id = i["track"]["id"]  
    songs.append(song_id)  
  
audio_ft = sp.audio_features(songs)  
  
with open("output_features.json", 'w', encoding='utf-8') as f:  
    json.dump(audio_ft, f, ensure_ascii=False, indent=4)
```

Feina classe

```python
import pandas as pd  
import spotipy  
import json  
from spotipy.oauth2 import SpotifyClientCredentials  
import time  
  
SPOTIPY_CLIENT_ID='89f634cbfb22458fbd2b396dd25496ee'  
SPOTIPY_CLIENT_SECRET='f266a68c3f5f4fc6901091f6f7fb553e'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlist_id = "37i9dQZEVXbNFJfN1Vw8d9"  
  
query = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None)  
  
with open("q.json", 'w', encoding='utf-8') as f:  
    json.dump(query, f, ensure_ascii=False, indent=4)  
  
songs = []  
  
for i in query['items']:  
    song_id = i["track"]["id"]  
    features = sp.audio_features(song_id)  
    artists_name = i["track"]["album"]["artists"]  
    cantants = []  
    for artist in artists_name:  
        a = artist["name"]  
        cantants.append(a)  
    tupla = (song_id, cantants)  
    songs.append(tupla)  
for song in songs:  
    print(song[0],song[1])  
  
llista_final = []  
  
for song in songs:  
    song_ig = song[0]  
    audio_ft = sp.audio_features(song_ig)  
    for element in audio_ft:  
        dance = element["danceability"]  
  
    df = pd.DataFrame({  
        "danceability": dance,  
        "artist_name":   
    })  
  
  
  
  
    canco = (song_ig, song[1], audio_ft)  
    
    
    
    
    
    print(canco)  
    llista_final.append(canco)  
    time.sleep(1)  
  
print(llista_final)  
  
for e in llista_final:  
    track_id = e[0]  
    for ert in e[1]:  
        first_artist = ert[0]  
    features = e[2]  
    for feature in features:  
        dance =   
    df = pd.DataFrame({  
        "track_id": track_id,  
        "artist": first_artist,  
        })  
  
  
""""  
artists = []  
  
for i in query['items']:  
    artists_name = i["track"]["artists"]    for artist in artists_name:        artist_names= artist["name"]        artists.append(artist_names)print(len(artists))  
print(artists)  
  
with open("output_features.json", 'w', encoding='utf-8') as f:  
    json.dump(audio_ft, f, ensure_ascii=False, indent=4)"""
```

asdas

```python
import pandas as pd  
import spotipy  
import json  
from spotipy.oauth2 import SpotifyClientCredentials  
import time  
  
SPOTIPY_CLIENT_ID='89f634cbfb22458fbd2b396dd25496ee'  
SPOTIPY_CLIENT_SECRET='f266a68c3f5f4fc6901091f6f7fb553e'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlist_id = "37i9dQZEVXbNFJfN1Vw8d9"  
  
query = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None)  
  
with open("q.json", 'w', encoding='utf-8') as f:  
    json.dump(query, f, ensure_ascii=False, indent=4)  
  
songs = []  
  
for i in query['items']:  
    song_id = i["track"]["id"]  
    features = sp.audio_features(song_id)  
    artists_name = i["track"]["album"]["artists"]  
    cantants = []  
    for artist in artists_name:  
        a = artist["name"]  
        cantants.append(a)  
    for element in features:  
        dance = element["danceability"]  
        energy = element["energy"]  
        key = element["key"]  
        df = pd.DataFrame({  
        "danceability": dance,  
        "artist_name": cantants[0],  
        "song_id": song_id  
        })  
    time.sleep(1)  
print(df)
```

intentos

```python
import spotipy  
import json  
from spotipy.oauth2 import SpotifyClientCredentials  
import time  
  
SPOTIPY_CLIENT_ID='89f634cbfb22458fbd2b396dd25496ee'  
SPOTIPY_CLIENT_SECRET='f266a68c3f5f4fc6901091f6f7fb553e'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlist_id = "37i9dQZEVXbNFJfN1Vw8d9"  
  
query = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None)  
458  
with open("q.json", 'w', encoding='utf-8') as f:  
    json.dump(query, f, ensure_ascii=False, indent=4)  
  
songs = []  
  
for i in query['items']:  
    song_id = i["track"]["id"]  
    features = sp.audio_features(song_id)  
    artists_name = i["track"]["album"]["artists"]  
    cantants = []  
    for artist in artists_name:  
        a = artist["name"]  
        cantants.append(a)  
    for element in features:  
        dance = element["danceability"]  
        energy = element["energy"]  
        key = element["key"]  
        df = pd.DataFrame({  
        "danceability": dance,  
        "artist_name": cantants[0],  
        "song_id": song_id  
        })  
    time.sleep(1)  
print(df)
```
