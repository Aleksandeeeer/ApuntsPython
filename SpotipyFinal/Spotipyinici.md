

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


