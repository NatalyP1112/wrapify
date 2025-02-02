"""
main.py

Main orchestrator file. Authenticates user, fetches data, processes it,
and exports it (e.g., to CSV or prints to console).
"""

import csv
# import pandas as pd  # If you decide to use pandas for CSV or Excel export

from authentication import get_spotipy_client
from spotify_data import get_top_tracks, get_top_artists
from data_processing import process_top_tracks, process_top_artists


def export_to_csv(data: list, filename: str, fieldnames: list) -> None:
    """
    Exports a list of dictionaries to a CSV file.

    Args:
        data (list): The data to be written, a list of dicts.
        filename (str): The name of the output CSV file.
        fieldnames (list): The column headers for the CSV.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    """
    Main function to authenticate with Spotify, retrieve top tracks and artists,
    process the data, and export it to CSV.
    """
    # 1. Authenticate with Spotify
    sp = get_spotipy_client()

    # 2. Fetch top tracks and artists
    raw_tracks = get_top_tracks(sp, time_range="medium_term", limit=10)
    raw_artists = get_top_artists(sp, time_range="medium_term", limit=10)

    # 3. Process / transform the data
    processed_tracks = process_top_tracks(raw_tracks)
    processed_artists = process_top_artists(raw_artists)

    # 4. Export to CSV (or any other format you like)
    # Example: top_tracks.csv with columns track_name, artist_name, album_name, track_url, popularity
    track_fieldnames = ["track_name", "artist_name", "album_name", "track_url", "popularity"]
    export_to_csv(processed_tracks, "top_tracks.csv", track_fieldnames)

    # Example: top_artists.csv with columns artist_name, genres, artist_url, followers, popularity
    artist_fieldnames = ["artist_name", "genres", "artist_url", "followers", "popularity"]
    export_to_csv(processed_artists, "top_artists.csv", artist_fieldnames)

    print("Export complete! Check the CSV files in your project directory.")


if __name__ == "__main__":
    main()
