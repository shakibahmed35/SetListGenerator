import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from scraper import get_songs

load_dotenv('.env')

CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URL = os.getenv('SPOTIPY_REDIRECT_URL')


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope="playlist-modify-public"))

user_profile = sp.current_user()
user_id = user_profile['id']  # This gives the user's Spotify ID

url = input("Please Give URL of the Setlist from Setlist.fm: ")

[songs, name] = get_songs(url)
uris = []

for song in songs:
    try:
        query = f"track:{song} artist:{name}"
        result = sp.search(q=query, type="track", limit=1)

        if result['tracks']['items']:
            uris.append(result['tracks']['items'][0]['uri'])
        else:
            raise IndexError
    except IndexError:
        print(f"Error: Could not find {song} by {name}")


new_playlist = sp.user_playlist_create(user_id, f'{name} setlist', public=True, collaborative=False, description=f'Creating Setlist for {name}')
playlist_id = new_playlist['id']

if uris:
    sp.playlist_add_items(playlist_id=playlist_id, items=uris)
else:
    print('No songs to add')