"""
authentication.py

Handles the OAuth2 process via Spotipy to obtain a valid token.
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, SCOPES


def get_spotipy_client(cache_path: str = ".spotipyoauthcache") -> spotipy.Spotify:
    """
    Initializes and returns a Spotipy client with OAuth2 flow.

    Args:
        cache_path (str): Path to store the access token. Defaults to ".spotipyoauthcache".

    Returns:
        spotipy.Spotify: Authenticated client.
    """
    auth_manager = SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=" ".join(SCOPES),
        cache_path=cache_path,
        show_dialog=True # If it's set to 'True' then it will trigger the login and permission dialog everytime starting Wrapify
    )
    return spotipy.Spotify(auth_manager=auth_manager)
