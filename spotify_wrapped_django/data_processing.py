"""
data_processing.py

Process and transform the raw Spotify data.
"""

from typing import List, Dict


def process_top_tracks(top_tracks: List[Dict]) -> List[Dict]:
    """
    Processes Spotify track data into a simplified structure.

    Args:
        top_tracks (List[Dict]): Raw track data from Spotify API.

    Returns:
        List[Dict]: Cleaned list of track info.
    """
    processed = []
    for track in top_tracks:
        images = track["album"]["images"]
        album_image_url = images[0]["url"] if images else None
        track_info = {
            "track_name": track["name"],
            "artist_name": track["artists"][0]["name"] if track["artists"] else "",
            "album_name": track["album"]["name"] if track["album"] else "",
            "track_url": track["external_urls"]["spotify"],
            "album_image_url": album_image_url,
        }
        processed.append(track_info)
    return processed


def process_top_artists(top_artists: List[Dict]) -> List[Dict]:
    """
    Processes Spotify artist data into a simplified structure.

    Args:
        top_artists (List[Dict]): Raw artist data from Spotify API.

    Returns:
        List[Dict]: Cleaned list of artist info.
    """
    processed = []
    for artist in top_artists:
        images = artist["images"]
        artist_image_url = images[0]["url"] if images else None
        
        artist_info = {
            "artist_name": artist["name"],
            "genres": artist["genres"],
            "artist_url": artist["external_urls"]["spotify"],
            "followers": artist["followers"]["total"],
            "artist_image_url": artist_image_url,
        }
        processed.append(artist_info)
    return processed
