"""
spotify_data.py

Functions to fetch data from the Spotify Web API.
"""

import spotipy


def get_top_tracks(sp: spotipy.Spotify, time_range: str = "medium_term", limit: int = 10):
    """
    Fetches a user's top tracks.

    Args:
        sp (spotipy.Spotify): Authenticated Spotipy client.
        time_range (str): short_term, medium_term, or long_term.
        limit (int): How many tracks to fetch.

    Returns:
        list: List of track objects (dicts).
    """
    results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
    return results.get("items", [])


def get_top_artists(sp: spotipy.Spotify, time_range: str = "medium_term", limit: int = 10):
    """
    Fetches a user's top artists.

    Args:
        sp (spotipy.Spotify): Authenticated Spotipy client.
        time_range (str): short_term, medium_term, or long_term.
        limit (int): How many artists to fetch.

    Returns:
        list: List of artist objects (dicts).
    """
    results = sp.current_user_top_artists(time_range=time_range, limit=limit)
    return results.get("items", [])
