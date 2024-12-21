import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

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


sp.user_playlist_create(user_id, "test", public=True, collaborative=False, description='Testing the spotipy api')