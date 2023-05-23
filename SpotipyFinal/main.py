import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import time
import pandas as pd

SPOTIPY_CLIENT_ID = '89f634cbfb22458fbd2b396dd25496ee'
SPOTIPY_CLIENT_SECRET = 'f266a68c3f5f4fc6901091f6f7fb553e'

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist_ids = ["37i9dQZEVXbO839WGRmpu1", "37i9dQZEVXbKPTKrnFPD0G", "37i9dQZEVXbK4fwx2r07XW", "37i9dQZEVXbKzoK95AbRy9", "37i9dQZEVXbMda2apknTqH", "37i9dQZEVXbLJ0paT1JkgZ", "37i9dQZEVXbL1Fl8vdBUba", "37i9dQZEVXbJZGli0rRP3r", "37i9dQZEVXbIZQf3WEYSut", "37i9dQZEVXbJPVQvqZqpcM", "37i9dQZEVXbMy2EcFg5F9m", "37i9dQZEVXbLp5XoPON0wI", "37i9dQZEVXbJVKdmjH0pON", "37i9dQZEVXbJHSzlHx2ZJU", "37i9dQZEVXbMdvweCgpBAe", "37i9dQZEVXbMWDif5SCBJq", "37i9dQZEVXbIZK8aUquyx8", "37i9dQZEVXbJ5J1TrbkAF9", "37i9dQZEVXbKqiTGXuCOsB", "37i9dQZEVXbLeBcWrdps2V", "37i9dQZEVXbMPoK06pe7d6",
"37i9dQZEVXbKcS4rq3mEhp", "37i9dQZEVXbNM8vS9cIqAG", "37i9dQZEVXbKUoIkUXteF6", "37i9dQZEVXbLw80jjcctV1", "37i9dQZEVXbIWlLQoMVEFp", "37i9dQZEVXbNy9tB5elXf1", "37i9dQZEVXbNSiWnkYnziz", "37i9dQZEVXbMGcjiWgg253", "37i9dQZEVXbN66FupT0MuX", "37i9dQZEVXbJV3H3OfCN1z", "37i9dQZEVXbJ7qiJCES5cj", "37i9dQZEVXbMVY2FDHm6NN", "37i9dQZEVXbNvXzC8A6ysJ", "37i9dQZEVXbKZyn1mKjmIl"]
paises = ["SAU", "ARG", "AUS", "BRA", "CAN", "CHI", "COL", "KOR", "EAU", "ECU", "EGY", "USA", "PHI", "GUA", "HKG", "IND", "IDN", "ISR", "JAP", "KAZ", "DOM", "MAL", "MAR", "MEX", "NIG", "NZE", "PAK", "PAN", "PER", "SGP", "SAF", "THA", "TWN", "VEN", "VNM"]

for list, pais in zip(playlist_ids, paises):
    query = sp.playlist_items(list, fields=None, limit=100, offset=0, market=None)

    with open(f"{pais}-{list}.json", 'w', encoding='utf-8') as f:
        json.dump(query, f, ensure_ascii=False, indent=4)

    songs = []
    llista= []
    for i in query['items']:
        song_id = i["track"]["id"]
        track_name = i["track"]["name"]
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
            acousticness = element["acousticness"]
            duration_ms = element["duration_ms"]
            loudness = element["loudness"]
            speechiness = element["speechiness"]
            tempo = element["tempo"]
            df = pd.DataFrame({
                "danceability": [dance],
                "artist_name": [cantants[0]],
                "song_id": [song_id],
                "track_name": [track_name],
                "key": [key],
                "energy": [energy],
                "acousticness": [acousticness],
                "duration_ms": [duration_ms],
                "loudness": [loudness],
                "speechiness": [speechiness],
                "tempo": [tempo]
            })
            llista.append(df)
        time.sleep(0.2)

    dataset = pd.concat(llista)
    print(dataset)
    dataset.to_csv(f"dataset-{pais}-{list}.csv", index=False)
